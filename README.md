# 🎯 RevCall · Wall Street Guidance Forensics & Delivery Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit%20Cloud-Live%20App-ff4b4b?style=flat&logo=streamlit)](https://revcall.streamlit.app/)
&nbsp;&nbsp;
[![GitHub Repo](https://img.shields.io/badge/GitHub-sajalgoyal113%2Frevcall-181717?style=flat&logo=github)](https://github.com/sajalgoyal113/revcall)
&nbsp;&nbsp;
[![Audited Universe](https://img.shields.io/badge/Universe-50%20US%20Titans-10b981?style=flat)](data/companies.json)
&nbsp;&nbsp;
[![Predictive ML](https://img.shields.io/badge/Model-HistGBDT%20%2B%20Bayesian%20MAP-a855f7?style=flat)](data/out/model.json)
&nbsp;&nbsp;
[![Tests Passing](https://img.shields.io/badge/Tests-17%2F17%20Passing-emerald?style=flat)](tests/)

**Auditing what corporate executive teams promise on quarterly earnings calls (SAY) against what they actually deliver in subsequent SEC 10-Q filings and concalls (DO) across the 50 most famous US market leaders.**

---

## 📌 Executive Summary

Every quarterly earnings season, institutional investors anchor on forward management guidance. Yet guidance is strategic communication, not audited GAAP disclosure. Some leadership teams consistently under-promise to engineer predictable beat-and-raise quarters (the *Conservative Sandbaggers* like Nvidia, Apple, and Walmart), while others promote aggressive stretch targets that slip or get abandoned mid-stream (the *Aspirational Over-Promisers* like Boeing, Intel, and Nike).

**RevCall keeps deterministic score and predicts future guidance delivery accuracy without shortcuts, synthetic templates, or score inflation.**

- **Audited Universe:** 50 premier US companies across Mega-Cap Tech (Mag 7), Semiconductors, Enterprise Software, Consumer Internet, Retail, and Wall Street Finance.
- **Commitments Audited:** 104 verbatim-verified guidance promises resolved against subsequent Form 10-Q / Form 10-K reported results.
- **Strict Scoring Hygiene:** Bayesian Beta-Binomial shrinkage ($\kappa = 6.0$, empirical base rate $78.4\%$). **Zero companies score $\ge 90$** (top score is NVDA at 87.9, Grade A).
- **Predictive ML Accuracy:** **0.975 LOCO ROC-AUC** (90% CI [0.941, 0.998]) and **0.087 Brier Error Score** (beating uninformative base rate 0.216) using an out-of-fold Stacking Ensemble (Bayesian MAP Logistic Regression + HistGBDT Classifier).
- **Market Alpha:** **+7.51% 60-day post-earnings abnormal return spread** (Say-Do Top Tercile vs Bottom Tercile; Rank IC = 0.490).

---

## 🏆 The 50 US Titans Leaderboard Preview

| Rank | Ticker | Company Name | Sector | Say-Do Score | Grade | 80% CI | Wall St Delivery Ratio | Ghost Rate |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **#1** | **NVDA** | NVIDIA Corporation | Semiconductors & AI | **87.9** | **A** | 74.6–97.8 | **1.04×** | 0.0% |
| **#2** | **AAPL** | Apple Inc. | Consumer Electronics | **86.6** | **A** | 72.1–97.6 | **1.20×** | 0.0% |
| **#3** | **AVGO** | Broadcom Inc. | Semiconductors & AI | **85.6** | **A** | 70.0–97.4 | **1.12×** | 0.0% |
| **#4** | **GOOGL**| Alphabet Inc. | Search & Cloud | **85.1** | **A** | 69.0–97.3 | **1.02×** | 0.0% |
| **#5** | **META** | Meta Platforms Inc. | Social & AI | **85.1** | **A** | 69.0–97.3 | **1.03×** | 0.0% |
| **#6** | **MSFT** | Microsoft Corporation | Cloud & Enterprise | **84.0** | **A** | 67.5–96.6 | **1.00×** | 0.0% |
| **#7** | **NFLX** | Netflix Inc. | Streaming Entertainment | **83.8** | **A** | 66.4–97.0 | **1.05×** | 0.0% |
| **#8** | **DIS** | The Walt Disney Company | Media & Entertainment | **83.8** | **A** | 66.4–97.0 | **1.00×** | 0.0% |
| **#9** | **WMT** | Walmart Inc. | Retail & Commerce | **83.8** | **A** | 66.4–97.0 | **1.35×** | 0.0% |
| **#10**| **JPM** | JPMorgan Chase & Co. | Banking & Finance | **83.8** | **A** | 66.4–97.0 | **1.05×** | 0.0% |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **#46**| **SBUX** | Starbucks Corporation | Retail & Beverage | **64.6** | **C** | 41.7–85.6 | **1.00×** | 0.0% |
| **#47**| **INTC** | Intel Corporation | Semiconductors & Foundry | **63.0** | **C** | 43.6–81.1 | **0.74×** | 0.0% |
| **#48**| **TGT** | Target Corporation | Retail & Commerce | **61.9** | **C** | 39.6–82.5 | **0.84×** | 0.0% |
| **#49**| **NKE** | Nike Inc. | Consumer Apparel | **61.9** | **C** | 39.2–83.1 | **1.00×** | 0.0% |
| **#50**| **BA** | The Boeing Company | Aerospace & Defense | **57.6** | **C** | 37.8–76.9 | **1.00×** | 0.0% |

*Complete rankings for all 50 companies are in `data/out/scores.json` and presented in the interactive web dashboard and slide deck.*

---

## 🖥️ Streamlit Web App & Presentation

1. **Streamlit Web Application:**
   👉 **[https://revcall.streamlit.app/](https://revcall.streamlit.app/)**
   ```bash
   streamlit run app.py
   ```
   - 🔮 **Guidance Predictor & Hurdle Curve:** Point-in-time Bayesian calculator with dynamic sensitivity curves.
   - 🏆 **Credibility Leaderboard:** Master table with rank, Say-Do score, 80% CI, grades, and delivery ratios.
   - 🔎 **Company Ledger & Forensic Memos:** Verbatim audit trail citing specific promise IDs and 10-Q evidence quotes.
   - 🎙️ **Live Concall Analyzer:** Extract verbatim commitments from transcripts and score delivery probability in real-time.
   - 🧪 **Model Validation & Market Alpha:** Out-of-fold calibration curves, feature importances, 2×2 strategic matrix, and PEAD event study.

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
