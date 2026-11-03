"""Master Verification & Evaluation Runner for RevCon US Corporate Guidance Forensics.

Executes:
1. Dataset compilation and integrity verification (`build_dataset.py`)
2. End-to-end evaluation pipeline (`engine/pipeline.py`)
3. Presentation and web dashboard generation (`generate_presentation.py`)
4. Full automated test suite (`unittest discover tests`)
"""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import build_dataset
from engine import pipeline
import generate_presentation


def main():
    print("=" * 78)
    print("  REVCON US · MASTER VERIFICATION & EVALUATION RUNNER")
    print("  Institutional Guidance Credibility Forensics for 50 US Market Titans")
    print("=" * 78)

    # Step 1: Re-build & Validate Dataset
    print("\n[STEP 1/4] Compiling & Validating Guidance Dataset...")
    build_dataset.build_and_validate()

    # Step 2: Run End-to-End Pipeline
    print("\n[STEP 2/4] Running Institutional Pipeline...")
    res = pipeline.run_pipeline()

    # Step 3: Generate Presentation HTML
    print("\n[STEP 3/4] Generating Interactive Presentation Dashboard...")
    generate_presentation.generate_dashboard()

    # Step 4: Run Automated Test Suite
    print("\n[STEP 4/4] Executing Comprehensive Test Suite...")
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(ROOT, "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)

    if not test_result.wasSuccessful():
        print("\n❌ TESTS FAILED! Check traceback above.")
        sys.exit(1)

    print("\n" + "=" * 78)
    print("  ✅ ALL SYSTEMS VERIFIED & PASSING WITH INSTITUTIONAL INTEGRITY")
    print(f"  • Companies Evaluated        : {len(res['scores'])}")
    print(f"  • Resolved Promises Audited  : {res['stats']['total_promises']}")
    print(f"  • Universe Base Rate         : {res['stats']['base_rate']}%")
    print(f"  • Maximum Say-Do Score       : {res['stats']['top_delivery_score']} ({res['stats']['top_delivery_ticker']}) [Strictly < 90]")
    print(f"  • Minimum Say-Do Score       : {res['stats']['lowest_delivery_score']} ({res['stats']['lowest_delivery_ticker']})")
    print(f"  • Out-of-Sample ROC-AUC      : {res['model']['roc_auc']} (90% CI: {res['model']['roc_auc_ci90']})")
    print(f"  • Brier Error Score          : {res['model']['brier_score']} (vs Base {res['model']['base_brier']})")
    print(f"  • 60-Day Alpha Spread        : +{res['market']['spread_pct']}%")
    print("=" * 78)


if __name__ == "__main__":
    main()
