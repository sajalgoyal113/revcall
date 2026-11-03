"""Test suite for Meta Model API and Concall Forensics Intelligence."""
import json
import os
import unittest

from engine import meta_api

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestMetaAPI(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT, "data", "companies.json")) as f:
            self.companies = {c["ticker"]: c for c in json.load(f)}
        with open(os.path.join(ROOT, "data", "promises.json")) as f:
            self.promises = json.load(f)
        with open(os.path.join(ROOT, "data", "out", "scores.json")) as f:
            self.scores = {c["ticker"]: c for c in json.load(f)["companies"]}

    def test_fetch_web_earnings_intel(self):
        """Web intelligence retriever should fetch headlines or gracefully return list."""
        articles = meta_api.fetch_web_earnings_intel("NVDA", "NVIDIA", max_articles=2)
        self.assertIsInstance(articles, list)
        if articles:
            self.assertIn("title", articles[0])
            self.assertIn("source", articles[0])

    def test_generate_meta_concall_reliability_brief(self):
        """Meta concall reliability brief should generate structured report with 4 institutional sections."""
        ticker = "NVDA"
        c_meta = self.companies[ticker]
        c_score = self.scores[ticker]
        c_proms = sorted([p for p in self.promises if p["ticker"] == ticker], key=lambda x: x.get("call_date", ""), reverse=True)
        latest = c_proms[0]
        past = c_proms[1:]

        res = meta_api.generate_meta_concall_reliability_brief(
            ticker=ticker,
            company_meta=c_meta,
            company_score=c_score,
            latest_promise=latest,
            past_promises=past,
            web_articles=[],
            api_key=None,
        )

        self.assertTrue(res["success"])
        self.assertIn("content", res)
        content = res["content"]
        self.assertIn("1. Latest Earnings Call Brief", content)
        self.assertIn("2. Guidance Reliability Forensics", content)
        self.assertIn("3. Bayesian Model Delivery Forecast", content)
        self.assertIn("4. Actionable Institutional Verdict", content)
        self.assertIn(ticker, content)
        # Should cite specific past incident
        self.assertIn("Form 10-Q", content)

    def test_reliability_archetypes_differentiation(self):
        """Sandbaggers (NVDA) vs Over-promisers (TSLA/INTC) should be accurately classified."""
        for ticker, expected_archetype in [("NVDA", "Conservative Sandbagger"), ("TSLA", "Stretch Over-Promiser")]:
            c_meta = self.companies[ticker]
            c_score = self.scores[ticker]
            c_proms = sorted([p for p in self.promises if p["ticker"] == ticker], key=lambda x: x.get("call_date", ""), reverse=True)
            res = meta_api.generate_meta_concall_reliability_brief(
                ticker=ticker,
                company_meta=c_meta,
                company_score=c_score,
                latest_promise=c_proms[0],
                past_promises=c_proms[1:],
                web_articles=[],
                api_key=None,
            )
            self.assertIn(expected_archetype, res["content"])


if __name__ == "__main__":
    unittest.main()
