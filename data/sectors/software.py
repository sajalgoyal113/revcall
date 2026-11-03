"""Guidance commitments and SEC 10-Q/10-K resolutions for Enterprise Software & Cloud:
PLTR, CRM, ADBE, ORCL, NOW, PANW, CRWD, SNOW.
"""

SOFTWARE_PROMISES = [
    # -------------------------------------------------------------------------
    # PALANTIR TECHNOLOGIES (PLTR)
    # -------------------------------------------------------------------------
    {
        "id": "PLTR:2024-02-05#0",
        "ticker": "PLTR",
        "call_date": "2024-02-05",
        "call_label": "Q4 2023 Earnings Call (Feb 5, 2024)",
        "speaker": "Ryan Taylor",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 U.S. Commercial revenue growth expected to exceed 40%",
        "quote": "We expect full year 2024 U.S. Commercial revenue to exceed $640 million, representing a growth rate of at least 40% driven by AIP demand.",
        "value_low": 40.0, "value_high": 40.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Powered by AIP bootcamps converting to production enterprise licenses.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-04",
            "ratio": 1.35,
            "why": "Guidance was raised consecutively (to 45% in May, 47% in Aug), with Q3 U.S. commercial revenue surging 54% YoY to $179M.",
            "evidence_quote": "Alex Karp (Q3 2024 Call): U.S. commercial business is growing at an astonishing 54% year-over-year, as AIP bootcamps prove uniquely effective.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "PLTR:2024-05-06#0",
        "ticker": "PLTR",
        "call_date": "2024-05-06",
        "call_label": "Q1 2024 Earnings Call (May 6, 2024)",
        "speaker": "Ryan Taylor",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2024 GAAP Operating Income and GAAP Net Income to remain positive in each quarter",
        "quote": "We expect GAAP operating income and GAAP net income to be positive in each quarter of the year, maintaining our sixth consecutive quarter of GAAP profitability.",
        "value_low": None, "value_high": None, "unit": "GAAP Profitable",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-06",
            "ratio": 1.0,
            "why": "GAAP profitability achieved in every quarter, fulfilling the final criterion for S&P 500 inclusion, which took effect September 23, 2024.",
            "evidence_quote": "S&P Dow Jones Indices (Sept 6, 2024): Palantir Technologies will be added to the S&P 500 prior to the open of trading on September 23.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # SALESFORCE (CRM)
    # -------------------------------------------------------------------------
    {
        "id": "CRM:2024-02-28#0",
        "ticker": "CRM",
        "call_date": "2024-02-28",
        "call_label": "Q4 FY24 Earnings Call (Feb 28, 2024)",
        "speaker": "Amy Weaver",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year FY25 Non-GAAP operating margin guidance of 32.5%",
        "quote": "For fiscal 2025, we are initiating non-GAAP operating margin guidance of 32.5%, representing a 200 basis point expansion year-over-year.",
        "value_low": 32.5, "value_high": 32.5, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes disciplined head count management and real estate consolidation.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-04",
            "ratio": 1.01,
            "why": "Delivered non-GAAP operating margin of 32.8% in Q1 and 33.7% in Q2, raising full-year target to 32.8%.",
            "evidence_quote": "Amy Weaver: Q2 non-GAAP operating margin expanded to 33.7%, up 210 basis points year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "CRM:2024-02-28#1",
        "ticker": "CRM",
        "call_date": "2024-02-28",
        "call_label": "Q4 FY24 Earnings Call (Feb 28, 2024)",
        "speaker": "Amy Weaver",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 FY25 Revenue expected between $9.11 billion and $9.16 billion",
        "quote": "For the first quarter, we expect revenue of $9.11 billion to $9.16 billion, up approximately 11% year-over-year in constant currency.",
        "value_low": 9.11, "value_high": 9.16, "unit": "Billion USD",
        "period": "Q1 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming ongoing enterprise budget elongation in professional services.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-05-29",
            "ratio": 0.998,
            "why": "Reported Q1 FY25 revenue of $9.133 billion in Form 10-Q, narrowly missing the $9.145B guided midpoint; stock fell 19% in single-day reaction.",
            "evidence_quote": "Form 10-Q: Total revenue for the first quarter was $9.13 billion, up 11% as professional services and deal compression moderated growth.",
            "y": 0.0, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # ADOBE (ADBE)
    # -------------------------------------------------------------------------
    {
        "id": "ADBE:2023-12-13#0",
        "ticker": "ADBE",
        "call_date": "2023-12-13",
        "call_label": "Q4 FY23 Earnings Call (Dec 13, 2023)",
        "speaker": "Dan Durn",
        "role": "CFO",
        "category": "commercial_milestone",
        "summary": "Pending $20 billion acquisition of Figma to proceed through global antitrust reviews",
        "quote": "We continue to engage with regulatory authorities in the UK and EU to demonstrate the pro-competitive merits of the proposed Figma combination.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H1", "period_kind": "HALF", "strength": "target",
        "conditions": "Subject to CMA Phase 2 and European Commission clearance.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "ABANDONED",
            "knowable_at": "2023-12-18",
            "ratio": 0.0,
            "why": "Adobe and Figma mutually terminated merger agreement on Dec 18, 2023 following UK CMA blockage, paying $1.0B termination fee.",
            "evidence_quote": "Adobe Press Release (Dec 18, 2023): Adobe and Figma mutually agree to terminate merger agreement due to no clear path to receive regulatory approvals.",
            "y": 0.0, "revisions": 1
        }
    },
    {
        "id": "ADBE:2024-03-14#0",
        "ticker": "ADBE",
        "call_date": "2024-03-14",
        "call_label": "Q1 FY24 Earnings Call (Mar 14, 2024)",
        "speaker": "Dan Durn",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 FY24 Total revenue guidance of $5.25 billion to $5.30 billion",
        "quote": "For the second quarter, we are targeting revenue of $5.25 billion to $5.30 billion, with Digital Media segment revenue of $3.87 billion to $3.90 billion.",
        "value_low": 5.25, "value_high": 5.30, "unit": "Billion USD",
        "period": "Q2 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-06-13",
            "ratio": 1.009,
            "why": "Reported Q2 FY24 revenue of $5.309 billion in Form 10-Q, exceeding the high end of the guided range ($5.30B).",
            "evidence_quote": "Shantanu Narayen: Q2 was a record quarter with revenue of $5.31 billion, driven by strong AI-infused product adoption across Creative Cloud.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # ORACLE (ORCL)
    # -------------------------------------------------------------------------
    {
        "id": "ORCL:2024-03-11#0",
        "ticker": "ORCL",
        "call_date": "2024-03-11",
        "call_label": "Q3 FY24 Earnings Call (Mar 11, 2024)",
        "speaker": "Safra Catz",
        "role": "CEO",
        "category": "revenue_growth",
        "summary": "Oracle Cloud Infrastructure (OCI) Gen2 revenue to grow over 50% in FY25",
        "quote": "We expect Gen2 Cloud Infrastructure revenue to grow over 50% in fiscal 2025 as large GPU AI cluster contracts ramp into revenue.",
        "value_low": 50.0, "value_high": 50.0, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by data center electrical substation delivery and Nvidia Blackwell cluster procurement.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-09",
            "ratio": 1.05,
            "why": "Reported Q1 FY25 Cloud Infrastructure (IaaS) revenue grew 46% (up to 52% in constant currency), with RPO surging 53% to $99 billion.",
            "evidence_quote": "Safra Catz: In Q1, total cloud revenue was up 22% to $5.6 billion, and Cloud Infrastructure revenue was up 45% in USD and 52% in constant currency.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # SERVICENOW (NOW)
    # -------------------------------------------------------------------------
    {
        "id": "NOW:2024-04-24#0",
        "ticker": "NOW",
        "call_date": "2024-04-24",
        "call_label": "Q1 2024 Earnings Call (Apr 24, 2024)",
        "speaker": "Gina Mastantuono",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Subscription revenue guidance of $2.505 billion to $2.510 billion (21.5% to 22.0% CC)",
        "quote": "For Q2, we expect subscription revenues between $2.505 billion and $2.510 billion, representing 21.5% to 22.0% year-over-year growth in constant currency.",
        "value_low": 2.505, "value_high": 2.510, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-24",
            "ratio": 1.012,
            "why": "Reported Q2 2024 subscription revenue of $2.542 billion (23.0% constant currency growth), beating the guided high end by $32M.",
            "evidence_quote": "Form 10-Q: Subscription revenues were $2.54 billion for the second quarter of 2024, representing 23% year-over-year growth.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # PALO ALTO NETWORKS (PANW)
    # -------------------------------------------------------------------------
    {
        "id": "PANW:2024-02-20#0",
        "ticker": "PANW",
        "call_date": "2024-02-20",
        "call_label": "Q2 FY24 Earnings Call (Feb 20, 2024)",
        "speaker": "Nikesh Arora",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Full year FY24 Total billings guidance reduced by ~$600 million due to platformization shift",
        "quote": "We are accelerating our platformization strategy. As a consequence of giving customers promotional free periods, we are reducing our full year billings guidance to $10.1 billion to $10.2 billion from $10.7 billion to $10.8 billion.",
        "value_low": 10.1, "value_high": 10.2, "unit": "Billion USD",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Short-term billings dilution to gain multi-module consolidation market share.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-02-20",
            "ratio": 0.945,
            "why": "Guidance cut represented a 5.6% guidance reduction; shares dropped 28.4% the following morning.",
            "evidence_quote": "Dipak Golechha: We are reducing our FY24 billings guidance by $600 million to reflect our accelerated platformization ramp.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "PANW:2024-02-20#1",
        "ticker": "PANW",
        "call_date": "2024-02-20",
        "call_label": "Q2 FY24 Earnings Call (Feb 20, 2024)",
        "speaker": "Dipak Golechha",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Next-Gen Security (NGS) ARR to reach $3.95 billion to $4.00 billion by end of FY24",
        "quote": "We expect Next-Generation Security ARR to be in the range of $3.95 billion to $4.00 billion at the end of fiscal 2024, growing approximately 38% to 40%.",
        "value_low": 3.95, "value_high": 4.00, "unit": "Billion USD",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-19",
            "ratio": 1.055,
            "why": "Delivered $4.22 billion in NGS ARR at the end of fiscal 2024 (up 43% YoY), beating guided $4.0B threshold.",
            "evidence_quote": "Form 10-K: Next-Gen Security ARR reached $4.22 billion as of July 31, 2024, demonstrating strong customer platformization conversions.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # CROWDSTRIKE (CRWD)
    # -------------------------------------------------------------------------
    {
        "id": "CRWD:2024-06-04#0",
        "ticker": "CRWD",
        "call_date": "2024-06-04",
        "call_label": "Q1 FY25 Earnings Call (Jun 4, 2024)",
        "speaker": "Burt Podbere",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year FY25 Total revenue guidance raised to $3.976 billion to $4.011 billion",
        "quote": "For the full fiscal year 2025, we are increasing our revenue guidance to $3,976.3 million to $4,010.7 million, or 30% to 31% growth.",
        "value_low": 3976.3, "value_high": 4010.7, "unit": "Million USD",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumed normal enterprise sales conversion and Falcon Flex platform uptake.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-08-28",
            "ratio": 0.975,
            "why": "Following the July 19, 2024 Windows Falcon content update crash, CrowdStrike reduced FY25 revenue guidance by $100M to $3.89B–$3.90B on Aug 28.",
            "evidence_quote": "Burt Podbere (Q2 FY25 Call): We are lowering our full-year revenue guidance to reflect approximately $60M of customer commitment package incentives and elongated sales cycles.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "CRWD:2024-08-28#0",
        "ticker": "CRWD",
        "call_date": "2024-08-28",
        "call_label": "Q2 FY25 Earnings Call (Aug 28, 2024)",
        "speaker": "George Kurtz",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Customer gross retention rate to remain resilient above 97% despite July 19 outage",
        "quote": "Our gross retention remained strong at 98% in Q2, and based on our customer conversations and commitment packages, we expect retention to remain above 97% through the second half.",
        "value_low": 97.0, "value_high": 97.0, "unit": "%",
        "period": "FY25-H2", "period_kind": "HALF", "strength": "firm",
        "conditions": "Contingent on rollout of updated kernel testing architecture and customer satisfaction credits.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-26",
            "ratio": 1.01,
            "why": "Gross retention held at 98.0% in Q3 FY25, confirming minimal customer churn despite the outage.",
            "evidence_quote": "George Kurtz (Q3 FY25 Call): Gross retention rate remained industry-leading at 98%, underscoring the mission-critical nature of the Falcon platform.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # SNOWFLAKE (SNOW)
    # -------------------------------------------------------------------------
    {
        "id": "SNOW:2024-02-28#0",
        "ticker": "SNOW",
        "call_date": "2024-02-28",
        "call_label": "Q4 FY24 Earnings Call (Feb 28, 2024)",
        "speaker": "Mike Scarpelli",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "FY25 Product revenue growth guidance lowered to 22% ($3.25 billion) under incoming CEO",
        "quote": "For fiscal 2025, product revenue is expected to be approximately $3.25 billion, representing 22% year-over-year growth, as we factor in customer tier-storage optimization headwinds.",
        "value_low": 3.25, "value_high": 3.25, "unit": "Billion USD",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Simultaneous announcement of Frank Slootman's retirement as CEO.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-02-28",
            "ratio": 0.88,
            "why": "Guidance marked a dramatic deceleration from 38% prior year growth; stock dropped 18% in after-hours trading.",
            "evidence_quote": "Mike Scarpelli: We are taking a more conservative posture in our guide given consumption patterns observed in Q4.",
            "y": 0.25, "revisions": 1
        }
    }
]
