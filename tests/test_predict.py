"""Test suite for Predictive Model, Feature Extraction, and LOCO Evaluation."""
import json
import os
import unittest
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from engine import predict, score


class TestPredict(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT, "data", "promises.json")) as f:
            self.promises = json.load(f)
        with open(os.path.join(ROOT, "data", "companies.json")) as f:
            self.companies = json.load(f)
        with open(os.path.join(ROOT, "data", "out", "model.json")) as f:
            self.model_out = json.load(f)

        self.base_rt = score.calculate_base_rate(self.promises)
        self.scores_dict = {
            c["ticker"]: score.score_company(self.promises, c["ticker"], prior=self.base_rt)
            for c in self.companies
        }

    def test_feature_vector_dimension_and_finite(self):
        """Feature vector must match FEATURE_NAMES and have finite numerical values."""
        for p in self.promises:
            t = p["ticker"]
            fv = predict.extract_features(p, self.scores_dict[t])
            self.assertEqual(len(fv), len(predict.FEATURE_NAMES))
            self.assertTrue(np.all(np.isfinite(fv)))

    def test_loco_evaluation_metrics(self):
        """LOCO ROC-AUC must be strong (>= 0.75) and Brier score must beat base rate."""
        auc = self.model_out["roc_auc"]
        self.assertGreaterEqual(auc, 0.75, f"LOCO ROC-AUC {auc} is below acceptable benchmark")
        self.assertLessEqual(auc, 1.0)

        brier = self.model_out["brier_score"]
        base_brier = self.model_out["base_brier"]
        self.assertLess(brier, base_brier, "Model Brier score failed to beat uninformed base rate")

    def test_single_promise_inference(self):
        """Predictor must produce valid probability and delivery-adjusted target."""
        predictor = predict.EnsemblePredictor()
        # Mock feature vector
        mock_p = self.promises[0]
        res = predictor.predict_guidance(mock_p, self.scores_dict[mock_p["ticker"]])
        self.assertIn("p_held", res)
        self.assertGreaterEqual(res["p_held"], 0.05)
        self.assertLessEqual(res["p_held"], 0.98)
        self.assertIn("credibility_adjusted_target", res)


if __name__ == "__main__":
    unittest.main()
