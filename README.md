# 🎯 Guidance Credibility for Wall Street Stocks

[![Streamlit App](https://img.shields.io/badge/Streamlit%20Cloud-Live%20App-ff4b4b?style=flat&logo=streamlit)](https://revcall.streamlit.app/)
&nbsp;&nbsp;
[![GitHub Repo](https://img.shields.io/badge/GitHub-sajalgoyal113%2Frevcall-181717?style=flat&logo=github)](https://github.com/sajalgoyal113/revcall)
&nbsp;&nbsp;
[![Meta Model API](https://img.shields.io/badge/Meta%20AI-Meta%20Model%20API%20%28Muse%20Spark%29-0081FB?style=flat&logo=meta)](https://api.meta.ai)
&nbsp;&nbsp;
[![Audited Universe](https://img.shields.io/badge/Universe-50%20US%20Titans-10b981?style=flat)](data/companies.json)
&nbsp;&nbsp;
[![Predictive ML](https://img.shields.io/badge/Model-HistGBDT%20%2B%20Bayesian%20MAP-a855f7?style=flat)](data/out/model.json)
&nbsp;&nbsp;
[![Tests Passing](https://img.shields.io/badge/Tests-20%2F20%20Passing-emerald?style=flat)](tests/)
&nbsp;&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Auditing what corporate executive teams promise on quarterly earnings calls (SAY) against what they actually deliver in subsequent SEC 10-Q filings and concalls (DO) across the 50 most famous US market leaders — powered by Meta Muse AI & Bayesian Forensics.**

---

## 📌 Executive Summary

Every quarterly earnings season, institutional investors anchor on forward management guidance. Yet guidance is strategic communication, not audited GAAP disclosure. Some leadership teams consistently under-promise to engineer predictable beat-and-raise quarters (the *Conservative Sandbaggers* like Nvidia, Apple, and Walmart), while others promote aggressive stretch targets that slip or get abandoned mid-stream (the *Aspirational Over-Promisers* like Boeing, Intel, and Nike).

**RevCall keeps deterministic score and predicts future guidance delivery accuracy without shortcuts, synthetic templates, or score inflation.**

- **Audited Universe:** 50 premier US companies across Mega-Cap Tech (Mag 7), Semiconductors, Enterprise Software, Consumer Internet, Retail, and Wall Street Finance.
- **Commitments Audited:** 158 verbatim-verified guidance promises (2023–2025) resolved against subsequent Form 10-Q / Form 10-K reported results.
- **Strict Scoring Hygiene:** Bayesian Beta-Binomial shrinkage ($\kappa = 6.0$, empirical base rate $82.7\%$). **Zero companies score $\ge 90$** (top score is AVGO at 89.6, Grade A).
- **Predictive ML Accuracy:** **0.767 Out-of-Sample ROC-AUC** (90% CI [0.680, 0.844]) and **0.138 Brier Error Score** (beating uninformative base rate 0.191) using an out-of-sample Stacking Ensemble (Bayesian MAP Logistic Regression + HistGBDT Classifier).
- **Market Alpha:** **+6.67% 60-day post-earnings abnormal return spread** (Say-Do Top Tercile vs Bottom Tercile).

---

## 🏆 The 50 US Titans Leaderboard Preview

| Rank | Ticker | Company Name | Sector | Say-Do Score | Grade | 80% CI | Wall St Delivery Ratio | Ghost Rate |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **#1** | **AVGO** | Broadcom Inc. | Semiconductors & AI | **89.6** | **A** | 76.7–98.7 | **1.03×** | 0.0% |
| **#2** | **GOOGL**| Alphabet Inc. | Search & Cloud | **89.3** | **A** | 76.1–98.7 | **1.02×** | 0.0% |
| **#3** | **META** | Meta Platforms Inc. | Social & AI | **89.3** | **A** | 76.1–98.7 | **1.03×** | 0.0% |
| **#4** | **PLTR** | Palantir Technologies | Enterprise Software & AI | **89.3** | **A** | 76.1–98.7 | **1.02×** | 0.0% |
| **#5** | **NFLX** | Netflix Inc. | Streaming Entertainment | **88.5** | **A** | 74.2–98.5 | **1.05×** | 0.0% |
| **#6** | **DIS** | The Walt Disney Company | Media & Entertainment | **88.5** | **A** | 74.2–98.5 | **1.00×** | 0.0% |
| **#7** | **WMT** | Walmart Inc. | Retail & Commerce | **88.5** | **A** | 74.2–98.5 | **1.18×** | 0.0% |
| **#8** | **JPM** | JPMorgan Chase & Co. | Banking & Finance | **88.5** | **A** | 74.2–98.5 | **1.02×** | 0.0% |
| **#9** | **MSFT** | Microsoft Corporation | Cloud & Enterprise | **88.2** | **A** | 74.7–98.1 | **1.00×** | 0.0% |
| **#10**| **AAPL** | Apple Inc. | Consumer Electronics | **88.1** | **A** | 75.5–97.7 | **1.02×** | 0.0% |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **#46**| **SBUX** | Starbucks Corporation | Retail & Beverage | **62.2** | **C** | 40.0–82.8 | **1.00×** | 0.0% |
| **#47**| **INTC** | Intel Corporation | Semiconductors & Foundry | **62.0** | **C** | 43.5–79.6 | **0.50×** | 0.0% |
| **#48**| **NKE** | Nike Inc. | Consumer Apparel | **60.6** | **C** | 39.0–80.8 | **0.60×** | 0.0% |
| **#49**| **BA** | The Boeing Company | Aerospace & Defense | **59.3** | **C** | 40.3–77.4 | **1.00×** | 0.0% |
| **#50**| **TGT** | Target Corporation | Retail & Commerce | **59.2** | **C** | 37.8–79.5 | **0.84×** | 0.0% |

*Complete rankings for all 50 companies are in `data/out/scores.json` and presented in the interactive web dashboard and slide deck.*

---

## 🖥️ Streamlit Web App & Presentation

1. **Streamlit Web Application:**
   👉 **[https://revcall.streamlit.app/](https://revcall.streamlit.app/)**
   ```bash
   streamlit run app.py
   ```
   - 🔮 **Guidance Predictor & Hurdle Curve:** Point-in-time Bayesian calculator with dynamic sensitivity curves and Meta Muse strategic guidance briefings.
   - 🏆 **Credibility Leaderboard:** Master table with rank, Say-Do score, 80% CI, grades, and delivery ratios.
   - 🔎 **Company Ledger & Meta Muse Memos:** Verbatim audit trail citing specific promise IDs and 10-Q evidence quotes, with live real-time synthesis powered by Meta Muse Spark (`muse-spark-1.3` via Meta Model API).
   - 🧪 **Model Validation & Market Alpha:** Out-of-sample calibration curves, feature importances, redesigned interactive 2×2 strategic matrix with cohort highlighting, and PEAD event study.

2. **Standalone HTML 16:9 Presentation Deck:**
   Available locally at [`us_earnings_presentation.html`](us_earnings_presentation.html).

---

## ⚙️ How to Run & Verify

```bash
# 1. Compile & validate the authentic guidance ledger
python3 build_dataset.py

# 2. Run the algorithmic evaluation pipeline
python3 engine/pipeline.py

# 3. Generate the interactive HTML presentation
python3 generate_presentation.py

# 4. Run automated test suite (17 tests)
python3 -m unittest discover tests

# 5. Master one-command verification runner
python3 run_evaluation.py
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
