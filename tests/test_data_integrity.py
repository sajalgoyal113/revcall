"""Test suite for Guidance Commitments and SEC Filing Data Integrity."""
import json
import os
import unittest
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDataIntegrity(unittest.TestCase):
    def setUp(self):
        prom_file = os.path.join(ROOT, "data", "promises.json")
        comp_file = os.path.join(ROOT, "data", "companies.json")
        with open(prom_file) as f:
            self.promises = json.load(f)
        with open(comp_file) as f:
            self.companies = json.load(f)

    def test_promise_count_and_coverage(self):
        """Must have at least 100 promises and all 50 companies represented."""
        self.assertGreaterEqual(len(self.promises), 100)
        self.assertEqual(len(self.companies), 50)
        universe_tickers = {c["ticker"] for c in self.companies}
        promise_tickers = {p["ticker"] for p in self.promises}
        missing = universe_tickers - promise_tickers
        self.assertEqual(len(missing), 0, f"Missing promises for companies: {missing}")

    def test_unique_promise_ids(self):
        """Every guidance promise must possess a globally unique identifier."""
        seen = set()
        for p in self.promises:
            pid = p["id"]
            self.assertNotIn(pid, seen, f"Duplicate promise ID detected: {pid}")
            seen.add(pid)

    def test_strict_point_in_time_dates(self):
        """Knowable filing date must never precede the concall date (no lookahead bias)."""
        for p in self.promises:
            call_dt = date.fromisoformat(p["call_date"])
            knowable_dt = date.fromisoformat(p["resolution"]["knowable_at"])
            self.assertGreaterEqual(
                knowable_dt, call_dt,
                f"Lookahead bias in {p['id']}: knowable {knowable_dt} < call {call_dt}"
            )

    def test_outcome_credit_math(self):
        """Resolution y values must match audited credit values."""
        credit_map = {
            "DELIVERED": 1.0,
            "PARTIAL": 0.5,
            "LATE": 0.5,
            "REVISED_DOWN": 0.25,
            "MISSED": 0.0,
            "ABANDONED": 0.0,
            "GHOSTED": 0.0,
        }
        for p in self.promises:
            outc = p["resolution"]["outcome"]
            self.assertIn(outc, credit_map, f"Invalid outcome {outc} in {p['id']}")
            y = p["resolution"]["y"]
            self.assertEqual(y, credit_map[outc], f"Credit mismatch in {p['id']}")

    def test_realistic_base_rate_and_negative_outcomes(self):
        """Base rate must fall in [65%, 85%] with ample negative evidence."""
        total_credit = sum(p["resolution"]["y"] for p in self.promises)
        base_rate = total_credit / len(self.promises)
        self.assertGreaterEqual(base_rate, 0.65)
        self.assertLessEqual(base_rate, 0.85)

        negative_count = sum(1 for p in self.promises if p["resolution"]["outcome"] != "DELIVERED")
        self.assertGreaterEqual(negative_count, 20, "Dataset lacks sufficient negative/adjusted guidance")


if __name__ == "__main__":
    unittest.main()
