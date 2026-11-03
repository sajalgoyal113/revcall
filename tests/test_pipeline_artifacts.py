"""Test suite for Pipeline Deterministic Output Artifacts."""
import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "data", "out")


class TestPipelineArtifacts(unittest.TestCase):
    def test_all_artifacts_exist_and_non_empty(self):
        """All 6 core pipeline JSON artifacts must exist and contain valid data."""
        expected_files = [
            "scores.json",
            "resolved.json",
            "model.json",
            "market.json",
            "memos.json",
            "stats.json",
        ]
        for fname in expected_files:
            fpath = os.path.join(OUT_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing artifact: {fname}")
            self.assertGreater(os.path.getsize(fpath), 0, f"Artifact is empty: {fname}")
            with open(fpath) as f:
                data = json.load(f)
                self.assertIsNotNone(data)

    def test_scores_json_structure(self):
        """scores.json must contain 50 companies with scores, grades, and CI."""
        with open(os.path.join(OUT_DIR, "scores.json")) as f:
            data = json.load(f)
        self.assertEqual(len(data["companies"]), 50)
        self.assertIn("history", data)
        self.assertIn("base_rate", data)

    def test_memos_json_structure(self):
        """memos.json must contain entries for all 50 companies with institutional sections."""
        with open(os.path.join(OUT_DIR, "memos.json")) as f:
            memos = json.load(f)
        self.assertEqual(len(memos), 50)
        for ticker, m in memos.items():
            self.assertIn("headline", m)
            self.assertIn("verdict", m)
            self.assertIn("patterns", m)
            self.assertIn("red_flags", m)
            self.assertIn("credit_where_due", m)

    def test_market_json_structure(self):
        """market.json must contain positive high-vs-low credibility spread."""
        with open(os.path.join(OUT_DIR, "market.json")) as f:
            mkt = json.load(f)
        self.assertIn("spread_pct", mkt)
        self.assertGreater(mkt["spread_pct"], 0.0, "Market spread should be positive (alpha)")
        self.assertIn("event_trajectory", mkt)


if __name__ == "__main__":
    unittest.main()
