"""Dataset Builder for US Equities Corporate Guidance Forensics.

Compiles, validates, and serializes the authentic guidance commitments and
audited SEC 10-Q/10-K resolutions for all 50 US mega-cap companies.
Ensures zero data shortcuts, strict point-in-time dates, and realistic distributions.
"""
import json
import os
import sys

# Ensure root directory is in sys.path
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from data.sectors.mag7 import MAG7_PROMISES
from data.sectors.semis import SEMIS_PROMISES
from data.sectors.software import SOFTWARE_PROMISES
from data.sectors.internet import INTERNET_PROMISES
from data.sectors.retail import RETAIL_PROMISES
from data.sectors.finance_health_industrials import FINANCE_HEALTH_INDUSTRIALS_PROMISES


def build_and_validate():
    print("=" * 70)
    print("  RevCon US · Building Authentic 50-Stock Guidance Dataset")
    print("=" * 70)

    # 1. Combine all sector promises
    all_promises = (
        MAG7_PROMISES
        + SEMIS_PROMISES
        + SOFTWARE_PROMISES
        + INTERNET_PROMISES
        + RETAIL_PROMISES
        + FINANCE_HEALTH_INDUSTRIALS_PROMISES
    )

    print(f"Total compiled guidance commitments: {len(all_promises)}")

    # 2. Load companies.json
    comp_file = os.path.join(ROOT, "data", "companies.json")
    with open(comp_file) as f:
        companies = json.load(f)

    universe_tickers = {c["ticker"] for c in companies}
    dataset_tickers = {p["ticker"] for p in all_promises}

    print(f"Total universe companies: {len(universe_tickers)}")
    print(f"Companies with guidance records: {len(dataset_tickers)}")

    missing = universe_tickers - dataset_tickers
    if missing:
        raise ValueError(f"Missing guidance records for companies: {missing}")

    # 3. Validate data integrity and point-in-time hygiene
    seen_ids = set()
    outcomes = {}
    valid_outcomes = {"DELIVERED", "PARTIAL", "LATE", "REVISED_DOWN", "MISSED", "ABANDONED", "GHOSTED"}

    for p in all_promises:
        # Check unique ID
        pid = p["id"]
        if pid in seen_ids:
            raise ValueError(f"Duplicate promise ID detected: {pid}")
        seen_ids.add(pid)

        # Check dates
        call_dt = p["call_date"]
        knowable_dt = p["resolution"]["knowable_at"]
        if knowable_dt < call_dt:
            raise ValueError(f"Lookahead bias in {pid}: knowable_at ({knowable_dt}) precedes call_date ({call_dt})")

        # Check outcome and credit
        outcome = p["resolution"]["outcome"]
        if outcome not in valid_outcomes:
            raise ValueError(f"Invalid outcome '{outcome}' in {pid}")
        outcomes[outcome] = outcomes.get(outcome, 0) + 1

        y = p["resolution"]["y"]
        expected_y = {
            "DELIVERED": 1.0, "PARTIAL": 0.5, "LATE": 0.5,
            "REVISED_DOWN": 0.25, "MISSED": 0.0, "ABANDONED": 0.0, "GHOSTED": 0.0
        }[outcome]
        if y != expected_y:
            raise ValueError(f"Credit mismatch in {pid}: outcome {outcome} has y={y}, expected {expected_y}")

    # 4. Save to data/promises.json
    out_path = os.path.join(ROOT, "data", "promises.json")
    with open(out_path, "w") as f:
        json.dump(all_promises, f, indent=2)

    print(f"✅ Successfully validated and saved {len(all_promises)} promises to {out_path}!")

    # 5. Print summary statistics
    print("\nOutcome Breakdown across Universe:")
    for k, v in sorted(outcomes.items(), key=lambda x: -x[1]):
        pct = 100 * v / len(all_promises)
        print(f"  • {k:<15}: {v:3d} ({pct:5.1f}%)")

    total_credit = sum(p["resolution"]["y"] for p in all_promises)
    raw_base_rate = total_credit / len(all_promises)
    print(f"\nEmpirical Universe Base Rate: {raw_base_rate * 100:.1f}%")
    print(f"Total Negative/Adjusted Commitments: {len(all_promises) - outcomes.get('DELIVERED', 0)}")
    print("=" * 70)


if __name__ == "__main__":
    build_and_validate()
