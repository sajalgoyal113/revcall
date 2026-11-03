"""Pipeline Runner for US Guidance Accuracy & Delivery Forensics.

Executes the institutional evaluation pipeline:
1. Point-in-time Bayesian Beta-Binomial credibility scoring (Say-Do Score, 80% CI, Grades)
2. Stacking Machine Learning Model (Bayesian MAP Logistic + HistGBDT) for P(Guidance Held)
   with strict point-in-time featurization, out-of-sample cross-validation, and calibration.
3. Event Study & Market Impact (Beat/Miss vs Guidance Credibility Spread)
4. Forensic Credibility Memos with verified guidance ledger citations
Exports deterministic JSON pipeline artifacts to `data/out/`.
"""
import json
import os
import sys
from datetime import date
import numpy as np

# Ensure REPO_DIR is in python path for portable execution
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_DIR not in sys.path:
    sys.path.insert(0, REPO_DIR)

try:
    import config
    from engine import market, memo, predict, score
except ImportError:
    from us_earnings import config
    from us_earnings.engine import market, memo, predict, score


def run_pipeline():
    print("=" * 70)
    print("  RevCall · US Corporate Guidance Forensics & Delivery Predictor")
    print("=" * 70)

    # 1. Load data
    prom_file = os.path.join(config.DATA, "promises.json")
    with open(prom_file) as f:
        promises = json.load(f)

    comp_file = os.path.join(config.DATA, "companies.json")
    with open(comp_file) as f:
        companies = json.load(f)

    events_file = os.path.join(config.DATA, "market_events.json")
    with open(events_file) as f:
        market_events = json.load(f)

    print(f"Loaded {len(companies)} US companies and {len(promises)} resolved guidance commitments.")

    # 2. Score companies using Beta-Binomial Bayesian Engine
    base_rt = score.calculate_base_rate(promises)
    print(f"Universe-wide delivery base rate: {base_rt * 100:.1f}%")

    company_scores = []
    scores_dict = {}
    for comp in companies:
        t = comp["ticker"]
        sc = score.score_company(promises, t, prior=base_rt)
        sc["name"] = comp["name"]
        sc["sector"] = comp["sector"]
        sc["market_cap"] = comp["market_cap"]
        sc["ceo"] = comp["ceo"]
        sc["cfo"] = comp["cfo"]
        sc["theme"] = comp["theme"]
        company_scores.append(sc)
        scores_dict[t] = sc

    # Sort leaderboard by score descending
    company_scores.sort(key=lambda x: (x["score"], x["effective_n"]), reverse=True)

    # Add Rank
    for i, sc in enumerate(company_scores, 1):
        sc["rank"] = i

    # Point-in-time trajectory history
    hist = {}
    for comp in companies:
        t = comp["ticker"]
        c_proms = [p for p in promises if p["ticker"] == t]
        dates = sorted(list({p["call_date"] for p in c_proms if "call_date" in p}))
        hist[t] = []
        for d in dates:
            prior_proms = [p for p in c_proms if p["call_date"] <= d]
            sc_d = score.score_company(prior_proms, t, prior=base_rt)
            hist[t].append({
                "date": d,
                "score": round(float(sc_d["score"]), 1),
                "n": int(sc_d["n"]),
                "grade": sc_d["grade"],
            })

    # Save scores.json
    scores_out = {
        "asof": "2026-11-03",
        "base_rate": round(base_rt * 100, 1),
        "companies": company_scores,
        "history": hist,
    }
    with open(os.path.join(config.OUT, "scores.json"), "w") as f:
        json.dump(scores_out, f, indent=2)
    print(f"Exported scores and history for {len(company_scores)} companies to scores.json")

    # 3. Train & Evaluate Ensemble Predictive Model with Strict Point-in-Time History (No Leakage)
    X_list = []
    y_list = []
    weights_list = []
    tickers_list = []

    for p in promises:
        t = p["ticker"]
        call_dt = date.fromisoformat(p["call_date"])
        # Strictly knowable prior to call date (prevents target leakage)
        strictly_prior = [
            pr for pr in promises
            if pr["ticker"] == t and date.fromisoformat(pr["resolution"]["knowable_at"]) < call_dt
        ]
        sc_pit = score.score_company(strictly_prior, t, prior=base_rt)
        y_val = p["resolution"]["y"]
        if y_val is None:
            continue
        fv = predict.extract_features(p, sc_pit)
        w = score.weight_promise(p)
        X_list.append(fv)
        # binary target for ML classification (1 if fully delivered else 0)
        y_list.append(1.0 if y_val >= 1.0 else 0.0)
        weights_list.append(w)
        tickers_list.append(t)

    X = np.array(X_list)
    y = np.array(y_list)
    w = np.array(weights_list)
    tickers = np.array(tickers_list)

    # Out-of-Sample Cross-Validation by Company Groups (5-Fold Stratified)
    unique_tickers = np.unique(tickers)
    s_oos = np.zeros(len(y))

    np.random.seed(42)
    shuffled_cos = np.random.permutation(unique_tickers)
    folds = np.array_split(shuffled_cos, 5)

    for fold_cos in folds:
        test_mask = np.isin(tickers, fold_cos)
        train_mask = ~test_mask
        fold_model = predict.EnsemblePredictor()
        fold_model.fit(X[train_mask], y[train_mask], sample_weight=w[train_mask])
        for idx in np.where(test_mask)[0]:
            s_oos[idx] = fold_model.predict_proba(X[idx])

    # Fit final production model on full universe
    prod_model = predict.EnsemblePredictor()
    prod_model.fit(X, y, sample_weight=w)

    # Compute prediction probabilities on all promises using production model
    predictions = []
    for idx, p in enumerate(promises):
        t = p["ticker"]
        sc = scores_dict[t]
        pred_res = prod_model.predict_guidance(p, sc)
        pred_res["p_held_oos"] = round(float(s_oos[idx]), 3)
        pred_res["promise_id"] = p["id"]
        pred_res["ticker"] = t
        pred_res["summary"] = p["summary"]
        pred_res["quote"] = p["quote"]
        pred_res["call_date"] = p["call_date"]
        pred_res["actual_outcome"] = p["resolution"]["outcome"]
        pred_res["actual_y"] = p["resolution"]["y"]
        predictions.append(pred_res)

    # Out-of-Sample Cross-Validation Metrics
    roc_auc = round(predict.calc_auc(y, s_oos), 3)
    roc_auc_ci90 = predict.boot_auc_ci(y, s_oos)
    brier = round(float(np.mean((s_oos - y) ** 2)), 3)
    base_brier = round(float(np.mean((base_rt - y) ** 2)), 3)

    # Calibration buckets based on out-of-fold predictions
    bins = [
        ("0-40%", 0.0, 0.40),
        ("40-60%", 0.40, 0.60),
        ("60-80%", 0.60, 0.80),
        ("80-100%", 0.80, 1.01),
    ]
    calibration_data = []
    for label, lo, hi in bins:
        mask = (s_oos >= lo) & (s_oos < hi)
        n_in_bin = int(mask.sum())
        if n_in_bin > 0:
            pred_mean = round(float(s_oos[mask].mean() * 100), 1)
            act_held = round(float(y[mask].mean() * 100), 1)
        else:
            pred_mean = round((lo + hi) / 2 * 100, 1)
            act_held = pred_mean
        calibration_data.append({
            "bucket": label,
            "predicted_mean": pred_mean,
            "actual_held": act_held,
            "n": n_in_bin,
        })

    # Top features ranking (standardized log-odds)
    raw_weights = prod_model.weights / (prod_model.sd + 1e-6)
    feature_weights = []
    for fname, weight_val in zip(predict.FEATURE_NAMES, raw_weights):
        if fname == "bias":
            continue
        feature_weights.append({
            "feature": fname,
            "weight": round(float(weight_val), 3),
            "impact": "Higher Probability Kept" if weight_val > 0 else "Lower Probability Kept"
        })
    feature_weights.sort(key=lambda x: abs(x["weight"]), reverse=True)

    model_out = {
        "roc_auc": roc_auc,
        "roc_auc_ci90": roc_auc_ci90,
        "brier_score": brier,
        "base_brier": base_brier,
        "feature_weights": feature_weights,
        "sample_count": len(predictions),
        "base_rate": round(float(np.mean(y)), 3),
        "calibration": calibration_data,
    }
    with open(os.path.join(config.OUT, "model.json"), "w") as f:
        json.dump(model_out, f, indent=2)
    print(f"Exported predictive model metrics (Out-of-Sample ROC AUC {roc_auc}, Brier {brier:.3f}) to model.json")

    # Save resolved.json
    with open(os.path.join(config.OUT, "resolved.json"), "w") as f:
        json.dump(promises, f, indent=2)
    print(f"Exported resolved guidance ledger to resolved.json")

    # 4. Market Test & Event Study
    market_stats = market.compute_market_stats(company_scores, market_events)
    with open(os.path.join(config.OUT, "market.json"), "w") as f:
        json.dump(market_stats, f, indent=2)
    print(f"Exported market impact results (Spread: +{market_stats.get('spread_pct')}% 60-day alpha) to market.json")

    # 5. Credibility Memos for all 50 companies
    memos_dict = {}
    for comp in companies:
        t = comp["ticker"]
        sc = scores_dict[t]
        c_promises = [p for p in promises if p["ticker"] == t]
        memos_dict[t] = memo.generate_company_memo(t, comp, sc, c_promises)

    with open(os.path.join(config.OUT, "memos.json"), "w") as f:
        json.dump(memos_dict, f, indent=2)
    print(f"Exported {len(memos_dict)} institutional credibility memos to memos.json")

    # 6. Corpus stats
    outcomes_agg = {}
    for p in promises:
        o = p["resolution"]["outcome"]
        outcomes_agg[o] = outcomes_agg.get(o, 0) + 1

    stats_out = {
        "total_companies": len(companies),
        "total_promises": len(promises),
        "outcomes": outcomes_agg,
        "base_rate": round(base_rt * 100, 1),
        "top_delivery_ticker": company_scores[0]["ticker"],
        "top_delivery_score": company_scores[0]["score"],
        "lowest_delivery_ticker": company_scores[-1]["ticker"],
        "lowest_delivery_score": company_scores[-1]["score"],
    }
    with open(os.path.join(config.OUT, "stats.json"), "w") as f:
        json.dump(stats_out, f, indent=2)

    # Print Top 10 and Bottom 5 Leaderboard Preview
    print("\n" + "=" * 80)
    print(f"{'Rank':<5}{'Ticker':<8}{'Company Name':<28}{'Say-Do':<8}{'Grade':<7}{'80% CI':<14}{'Delivery Ratio':<15}")
    print("-" * 80)
    for sc in company_scores[:10]:
        ci_str = f"{sc['ci80'][0]}-{sc['ci80'][1]}"
        ratio_str = f"{sc['delivery_ratio']:.2f}x"
        print(f"#{sc['rank']:<4}{sc['ticker']:<8}{sc['name'][:26]:<28}{sc['score']:<8}{sc['grade']:<7}{ci_str:<14}{ratio_str:<15}")
    print("...")
    for sc in company_scores[-5:]:
        ci_str = f"{sc['ci80'][0]}-{sc['ci80'][1]}"
        ratio_str = f"{sc['delivery_ratio']:.2f}x"
        print(f"#{sc['rank']:<4}{sc['ticker']:<8}{sc['name'][:26]:<28}{sc['score']:<8}{sc['grade']:<7}{ci_str:<14}{ratio_str:<15}")
    print("=" * 80)

    return {
        "scores": company_scores,
        "model": model_out,
        "market": market_stats,
        "stats": stats_out,
    }


if __name__ == "__main__":
    run_pipeline()
