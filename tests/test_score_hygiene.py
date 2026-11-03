"""Test suite for Bayesian Say-Do Credibility Score Hygiene and Distribution."""
import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestScoreHygiene(unittest.TestCase):
    def setUp(self):
        scores_file = os.path.join(ROOT, "data", "out", "scores.json")
        with open(scores_file) as f:
            self.data = json.load(f)
        self.companies = self.data["companies"]

    def test_no_score_greater_than_or_equal_to_90(self):
        """CRITICAL: Say-Do scores must be properly Bayesian-regularized with NO scores >= 90."""
        violators = [c for c in self.companies if c["score"] >= 90.0]
        self.assertEqual(
            len(violators), 0,
            f"Artificial score inflation detected! Companies scoring >= 90: {[(c['ticker'], c['score']) for c in violators]}"
        )

    def test_top_scores_realistic(self):
        """Top companies must score in realistic 84-89 range (Grade A)."""
        top_score = self.companies[0]["score"]
        self.assertGreaterEqual(top_score, 84.0)
        self.assertLess(top_score, 90.0)

    def test_underperformer_scores(self):
        """Troubled/struggling companies must receive lower scores (under 70, Grade C or lower)."""
        score_by_ticker = {c["ticker"]: c for c in self.companies}
        troubled = ["BA", "INTC", "NKE", "SBUX", "TGT"]
        for t in troubled:
            self.assertIn(t, score_by_ticker)
            sc = score_by_ticker[t]["score"]
            self.assertLess(
                sc, 70.0,
                f"Troubled company {t} has unregularized high score: {sc}"
            )
            self.assertIn(score_by_ticker[t]["grade"], ("C", "D", "F"))

    def test_credible_intervals_valid(self):
        """80% credible interval bounds must satisfy 0 <= ci[0] <= score <= ci[1] <= 100."""
        for c in self.companies:
            ci = c["ci80"]
            sc = c["score"]
            self.assertGreaterEqual(ci[0], 0.0)
            self.assertLessEqual(ci[1], 100.0)
            self.assertLessEqual(ci[0], sc, f"{c['ticker']} lower CI ({ci[0]}) > score ({sc})")
            self.assertGreaterEqual(ci[1], sc, f"{c['ticker']} upper CI ({ci[1]}) < score ({sc})")

    def test_company_count(self):
        """Scores artifact must contain exactly 50 companies."""
        self.assertEqual(len(self.companies), 50)


if __name__ == "__main__":
    unittest.main()
