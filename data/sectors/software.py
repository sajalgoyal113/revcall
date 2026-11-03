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
    },
    # -------------------------------------------------------------------------
    # 2025 COMMITMENTS & AUDITED RESOLUTIONS
    # -------------------------------------------------------------------------
    {
        "id": "PLTR:2025-02-03#0",
        "ticker": "PLTR",
        "call_date": "2025-02-03",
        "call_label": "Q4 2024 Earnings Call (Feb 3, 2025)",
        "speaker": "Dave Glazer",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 2025 revenue guidance between $858 million and $862 million",
        "quote": "For the first quarter of 2025, we expect revenue of between $858 million and $862 million, and adjusted income from operations of $341 million to $345 million.",
        "value_low": 858.0, "value_high": 862.0, "unit": "Million USD",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Driven by AIP commercial customer bootcamp conversions.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-05",
            "ratio": 1.028,
            "why": "Reported Q1 2025 revenue of $884 million (up 39% YoY), beating the high end of guidance ($862M) by $22M.",
            "evidence_quote": "Alex Karp: In Q1 2025, our revenue surged 39% year-over-year to $884 million, fueled by unrelenting demand for AIP across U.S. enterprise and defense.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "PLTR:2025-02-03#1",
        "ticker": "PLTR",
        "call_date": "2025-02-03",
        "call_label": "Q4 2024 Earnings Call (Feb 3, 2025)",
        "speaker": "Dave Glazer",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 total revenue between $3.741 billion and $3.761 billion",
        "quote": "For the full year 2025, we expect revenue of between $3.741 billion and $3.761 billion, and U.S. commercial revenue in excess of $1.080 billion.",
        "value_low": 3741.0, "value_high": 3761.0, "unit": "Million USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to continued momentum in US government and commercial adoption.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-05",
            "ratio": 1.02,
            "why": "On the Q1 2025 earnings call (May 5, 2025), Palantir raised full-year guidance to over $3.89 billion (36% YoY growth), easily outperforming the initial range.",
            "evidence_quote": "Dave Glazer: Given the extraordinary momentum in our business, we are raising our full year 2025 revenue guidance to between $3.890 billion and $3.902 billion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "CRM:2025-02-26#0",
        "ticker": "CRM",
        "call_date": "2025-02-26",
        "call_label": "Q4 FY25 Earnings Call (Feb 26, 2025)",
        "speaker": "Amy Weaver",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 FY26 revenue guidance between $9.71 billion and $9.76 billion",
        "quote": "For the first quarter of fiscal 2026, we expect revenue of $9.71 billion to $9.76 billion, up 7% to 8% year-over-year.",
        "value_low": 9.71, "value_high": 9.76, "unit": "Billion USD",
        "period": "Q1 FY26", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assumes continuous expansion in Agentforce and Data Cloud subscriptions.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-28",
            "ratio": 1.006,
            "why": "Reported Q1 FY26 revenue of $9.80 billion, outperforming the top end of the guided range ($9.76B).",
            "evidence_quote": "Marc Benioff: Q1 was an outstanding quarter. Revenue reached $9.80 billion, driven by rapid customer adoption of our Agentforce platform.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "ADBE:2025-03-12#0",
        "ticker": "ADBE",
        "call_date": "2025-03-12",
        "call_label": "Q1 FY25 Earnings Call (Mar 12, 2025)",
        "speaker": "Dan Durn",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 FY25 total revenue target between $5.77 billion and $5.82 billion",
        "quote": "In Q2 fiscal 2025, Adobe targets total revenue of $5.77 billion to $5.82 billion and digital media net new ARR of approximately $445 million.",
        "value_low": 5.77, "value_high": 5.82, "unit": "Billion USD",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Driven by Firefly GenAI monetization across Creative Cloud and Document Cloud.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-06-12",
            "ratio": 1.010,
            "why": "Reported Q2 FY25 revenue of $5.87 billion, beating the top of the guided range ($5.82B) by $50 million.",
            "evidence_quote": "Form 10-Q: Adobe achieved record Q2 revenue of $5.87 billion, representing 11% year-over-year growth.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "ORCL:2025-03-10#0",
        "ticker": "ORCL",
        "call_date": "2025-03-10",
        "call_label": "Q3 FY25 Earnings Call (Mar 10, 2025)",
        "speaker": "Safra Catz",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Q4 FY25 total revenue growth between 9% and 11% in constant currency and total cloud revenue growth 24% to 28%",
        "quote": "In Q4, total revenues are expected to grow from 9% to 11% in constant currency, and total cloud revenue is expected to grow from 24% to 28%.",
        "value_low": 9.0, "value_high": 11.0, "unit": "% CC",
        "period": "Q4 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to OCI datacenter capacity energization schedules.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-06-11",
            "ratio": 1.00,
            "why": "Reported Q4 FY25 total revenue of $15.9 billion (up 11% in CC) and cloud revenue of $6.7 billion (up 27%), meeting both targets.",
            "evidence_quote": "Safra Catz: Total cloud revenue was up 27% to $6.7 billion, and total revenue reached $15.9 billion, up 11% as guided.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NOW:2025-01-29#0",
        "ticker": "NOW",
        "call_date": "2025-01-29",
        "call_label": "Q4 2024 Earnings Call (Jan 29, 2025)",
        "speaker": "Gina Mastantuono",
        "role": "CFO",
        "category": "segment_guidance",
        "summary": "Q1 2025 subscription revenues between $2,995 million and $3,000 million",
        "quote": "For the first quarter of 2025, we expect subscription revenues between $2,995 million and $3,000 million, representing 18.5% to 19% year-over-year growth.",
        "value_low": 2995.0, "value_high": 3000.0, "unit": "Million USD",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Reflects strong Now Assist Pro Plus SKU upsells.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-23",
            "ratio": 1.002,
            "why": "Reported Q1 2025 subscription revenue of $3,005 million, delivering ahead of the high end of guidance ($3,000M).",
            "evidence_quote": "Bill McDermott: ServiceNow delivered another standout quarter with subscription revenue surpassing $3.0 billion, up 19% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "PANW:2025-02-13#0",
        "ticker": "PANW",
        "call_date": "2025-02-13",
        "call_label": "Q2 FY25 Earnings Call (Feb 13, 2025)",
        "speaker": "Dipak Golechha",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 FY25 total revenue between $2.26 billion and $2.29 billion and NGS ARR between $5.03 billion and $5.08 billion",
        "quote": "For the third quarter of fiscal 2025, we expect Next-Generation Security ARR of $5.03 billion to $5.08 billion, and total revenue between $2.26 billion and $2.29 billion.",
        "value_low": 2.26, "value_high": 2.29, "unit": "Billion USD",
        "period": "Q3 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Accelerating platformization agreements with enterprise accounts.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-20",
            "ratio": 1.009,
            "why": "Reported Q3 FY25 total revenue of $2.30 billion and NGS ARR of $5.09 billion, exceeding guided ceilings on both fronts.",
            "evidence_quote": "Nikesh Arora: We crossed $5.0 billion in NGS ARR to reach $5.09 billion, while Q3 revenue grew 15% to $2.3 billion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "CRWD:2025-03-04#0",
        "ticker": "CRWD",
        "call_date": "2025-03-04",
        "call_label": "Q4 FY25 Earnings Call (Mar 4, 2025)",
        "speaker": "Burt Podbere",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 FY26 total revenue between $1,100.6 million and $1,106.4 million",
        "quote": "For the first quarter of fiscal 2026, total revenue is expected to be $1,100.6 million to $1,106.4 million, representing 20% growth year-over-year.",
        "value_low": 1100.6, "value_high": 1106.4, "unit": "Million USD",
        "period": "Q1 FY26", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Reflects customer commitment packages and Falcon Flex module additions.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-06-03",
            "ratio": 1.00,
            "why": "Reported Q1 FY26 total revenue of $1,103.0 million, squarely within the guided range.",
            "evidence_quote": "Form 10-Q: Total revenue was $1.10 billion, a 20% increase compared to $921.0 million in the first quarter of fiscal 2025.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "SNOW:2025-02-26#0",
        "ticker": "SNOW",
        "call_date": "2025-02-26",
        "call_label": "Q4 FY25 Earnings Call (Feb 26, 2025)",
        "speaker": "Mike Scarpelli",
        "role": "CFO",
        "category": "segment_guidance",
        "summary": "Q1 FY26 product revenue between $955 million and $960 million",
        "quote": "For the first quarter of fiscal 2026, we expect product revenue of between $955 million and $960 million, representing year-over-year growth of 21% to 22%.",
        "value_low": 955.0, "value_high": 960.0, "unit": "Million USD",
        "period": "Q1 FY26", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assumes stable enterprise compute consumption on Cortex and Iceberg tables.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-21",
            "ratio": 1.038,
            "why": "Reported Q1 FY26 product revenue of $996.8 million, up 26% year-over-year and beating guidance top end ($960M) by 3.8%.",
            "evidence_quote": "Sridhar Ramaswamy: Product revenue grew 26% year-over-year to $996.8 million in Q1, demonstrating accelerating customer workload consumption.",
            "y": 1.0, "revisions": 0
        }
    }
]
