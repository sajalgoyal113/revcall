"""Guidance commitments and SEC 10-Q/10-K resolutions for Digital Media & Consumer Internet:
NFLX, DIS, SPOT, UBER, ABNB, COIN.
"""

INTERNET_PROMISES = [
    # -------------------------------------------------------------------------
    # NETFLIX (NFLX)
    # -------------------------------------------------------------------------
    {
        "id": "NFLX:2024-01-23#0",
        "ticker": "NFLX",
        "call_date": "2024-01-23",
        "call_label": "Q4 2023 Earnings Call (Jan 23, 2024)",
        "speaker": "Spencer Neumann",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 Total revenue growth guided 13% to 15% (foreign exchange neutral)",
        "quote": "For the full year 2024, we forecast healthy double-digit revenue growth of 13% to 15% on a currency-neutral basis, driven by continued membership expansion and pricing adjustments.",
        "value_low": 13.0, "value_high": 15.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming continued paid sharing adoption and initial ad-tier monetization scale.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-21",
            "ratio": 1.05,
            "why": "Guidance was raised in July to 14%–15% and in October to 15%; delivered full year revenue of $39.0 billion (up 15.5% YoY).",
            "evidence_quote": "Spencer Neumann (Q4 2024 Call): Revenue increased 15% for the full year 2024, delivering at the high end of our expectations.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NFLX:2024-04-18#0",
        "ticker": "NFLX",
        "call_date": "2024-04-18",
        "call_label": "Q1 2024 Earnings Call (Apr 18, 2024)",
        "speaker": "Spencer Neumann",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2024 Operating margin guidance raised to 25.0% (from 24.0%)",
        "quote": "We are increasing our full-year 2024 operating margin forecast to 25%, up from 24% previously, due to our strong Q1 performance and expense discipline.",
        "value_low": 25.0, "value_high": 25.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-21",
            "ratio": 1.06,
            "why": "Operating margin was raised again in October to 27%, delivering 26.7% for the full year 2024.",
            "evidence_quote": "Form 10-K: Operating margin for the year ended December 31, 2024 was 26.7%, up from 20.6% in 2023.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # WALT DISNEY (DIS)
    # -------------------------------------------------------------------------
    {
        "id": "DIS:2024-02-07#0",
        "ticker": "DIS",
        "call_date": "2024-02-07",
        "call_label": "Q1 FY24 Earnings Call (Feb 7, 2024)",
        "speaker": "Hugh Johnston",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Combined Direct-to-Consumer (DTC) streaming businesses to reach profitability by Q4 FY24",
        "quote": "We continue to expect our combined streaming businesses to reach profitability in the fourth quarter of fiscal 2024, with further margin improvement in fiscal 2025.",
        "value_low": 0.0, "value_high": 0.0, "unit": "Breakeven",
        "period": "FY24-Q4", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Dependent on password sharing crackdown ramp and Disney+ ad-tier subscriber growth.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-07",
            "ratio": 1.0,
            "why": "Achieved streaming profitability a quarter ahead of guidance in Q3 FY24 (operating income of $47 million across Disney+, Hulu, and ESPN+).",
            "evidence_quote": "Hugh Johnston (Q3 FY24 Call): DTC streaming achieved profitability a quarter earlier than guided, generating $47 million of operating income.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "DIS:2024-08-07#0",
        "ticker": "DIS",
        "call_date": "2024-08-07",
        "call_label": "Q3 FY24 Earnings Call (Aug 7, 2024)",
        "speaker": "Hugh Johnston",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Q4 FY24 Experiences segment operating income expected to decline by mid-single digits",
        "quote": "In Experiences, we expect operating income in the fourth quarter to decline by mid-single digits compared to the prior year, reflecting a moderation in consumer demand at our domestic parks.",
        "value_low": -4.0, "value_high": -7.0, "unit": "% YoY Decline",
        "period": "Q4 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Higher pre-opening costs for Disney Cruise Line fleet expansion.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-14",
            "ratio": 1.0,
            "why": "Reported Q4 FY24 Experiences operating income of $1.66 billion, down 6.0% YoY, matching the guided mid-single digit decline.",
            "evidence_quote": "Form 10-K: Experiences operating income decreased 6% to $1.66 billion in the fourth quarter due to lower domestic parks attendance.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # SPOTIFY (SPOT)
    # -------------------------------------------------------------------------
    {
        "id": "SPOT:2024-02-06#0",
        "ticker": "SPOT",
        "call_date": "2024-02-06",
        "call_label": "Q4 2023 Earnings Call (Feb 6, 2024)",
        "speaker": "Daniel Ek",
        "role": "CEO",
        "category": "operating_margin",
        "summary": "Full year 2024 Operating profit to turn sustainably positive following cost restructuring",
        "quote": "We have fundamentally transformed our cost structure. In 2024, you will see Spotify deliver meaningful, sustainable operating profitability across all four quarters.",
        "value_low": None, "value_high": None, "unit": "Sustainable Profit",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-12",
            "ratio": 1.15,
            "why": "Reported operating profit in every quarter of 2024 (€168M in Q1, €266M in Q2, €454M in Q3), totaling over €1.3B for the year vs a loss of -€449M in 2023.",
            "evidence_quote": "Daniel Ek (Q3 2024 Call): Operating income reached a record €454 million, more than 10x the prior year, driven by gross margin expansion to 31.1%.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "SPOT:2024-07-23#0",
        "ticker": "SPOT",
        "call_date": "2024-07-23",
        "call_label": "Q2 2024 Earnings Call (Jul 23, 2024)",
        "speaker": "Christian Luiga",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Q3 2024 Gross margin guidance of 30.0%",
        "quote": "For the third quarter, we are forecasting a gross margin of 30.0%, reflecting improved marketplace contribution and audiobook economics.",
        "value_low": 30.0, "value_high": 30.0, "unit": "%",
        "period": "Q3 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-12",
            "ratio": 1.037,
            "why": "Reported Q3 2024 gross margin of 31.1% in Form 6-K, beating guidance by 110 basis points.",
            "evidence_quote": "Form 6-K: Gross margin for the third quarter expanded to 31.1%, compared to 26.4% in the third quarter of 2023.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # UBER TECHNOLOGIES (UBER)
    # -------------------------------------------------------------------------
    {
        "id": "UBER:2024-02-07#0",
        "ticker": "UBER",
        "call_date": "2024-02-07",
        "call_label": "Investor Day 2024 (Feb 14, 2024)",
        "speaker": "Prashanth Mahendra-Rajah",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "3-Year Compound Annual Growth: Gross Bookings mid-to-high teens and Adjusted EBITDA 30% to 40%",
        "quote": "Over the next three years, we expect Gross Bookings to grow at a mid-to-high teens CAGR, and Adjusted EBITDA to grow at a 30% to 40% CAGR, generating over $6 billion in annual free cash flow.",
        "value_low": 16.0, "value_high": 19.0, "unit": "% CAGR",
        "period": "2024-2026", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming continued platform cross-sell between Mobility and Delivery.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-31",
            "ratio": 1.02,
            "why": "Throughout 2024, Gross Bookings grew 19%–21% CC YoY, and Adjusted EBITDA grew over 50% YoY ($1.69B in Q3 alone), pacing ahead of 3-year targets.",
            "evidence_quote": "Dara Khosrowshahi: Q3 was another milestone with gross bookings up 20% in constant currency and adjusted EBITDA up 55% to $1.7 billion.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # AIRBNB (ABNB)
    # -------------------------------------------------------------------------
    {
        "id": "ABNB:2024-08-06#0",
        "ticker": "ABNB",
        "call_date": "2024-08-06",
        "call_label": "Q2 2024 Earnings Call (Aug 6, 2024)",
        "speaker": "Ellie Mertz",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 2024 Revenue guidance of $3.67 billion to $3.73 billion (8% to 10% YoY growth)",
        "quote": "For the third quarter, we expect revenue of $3.67 billion to $3.73 billion, or 8% to 10% year-over-year growth, as we see shorter booking lead times in the U.S.",
        "value_low": 3.67, "value_high": 3.73, "unit": "Billion USD",
        "period": "Q3 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Reflecting consumer caution and delayed summer leisure booking trends in North America.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-07",
            "ratio": 1.008,
            "why": "Reported Q3 2024 revenue of $3.732 billion in Form 10-Q, hitting the top end of the guided $3.67B–$3.73B range.",
            "evidence_quote": "Form 10-Q: Revenue increased 10% to $3.73 billion in the third quarter of 2024, driven by solid demand across Europe and Latin America.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # COINBASE GLOBAL (COIN)
    # -------------------------------------------------------------------------
    {
        "id": "COIN:2024-05-02#0",
        "ticker": "COIN",
        "call_date": "2024-05-02",
        "call_label": "Q1 2024 Earnings Call (May 2, 2024)",
        "speaker": "Alesia Haas",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Subscription and services revenue expected between $525 million and $600 million",
        "quote": "We anticipate Q2 subscription and services revenue to be between $525 million and $600 million, benefiting from average crypto asset prices and USDC market cap expansion.",
        "value_low": 525.0, "value_high": 600.0, "unit": "Million USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming stable crypto market capitalization and interest rate environment.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-01",
            "ratio": 1.06,
            "why": "Reported Q2 2024 subscription and services revenue of $599.0 million, near the top of the guided range.",
            "evidence_quote": "Form 10-Q: Subscription and services revenue was $599.0 million in the second quarter, up 79% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    }
]
