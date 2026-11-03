"""Guidance commitments and SEC 10-Q/10-K resolutions for Semiconductor & Hardware Equities:
AMD, AVGO, QCOM, INTC, MU, AMAT, TXN.
"""

SEMIS_PROMISES = [
    # -------------------------------------------------------------------------
    # ADVANCED MICRO DEVICES (AMD)
    # -------------------------------------------------------------------------
    {
        "id": "AMD:2024-01-30#0",
        "ticker": "AMD",
        "call_date": "2024-01-30",
        "call_label": "Q4 2023 Earnings Call (Jan 30, 2024)",
        "speaker": "Lisa Su",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Full year 2024 Data Center GPU (MI300) revenue raised to exceed $3.5 billion",
        "quote": "We now expect Data Center GPU revenue to be approximately $3.5 billion in 2024, up from the $2 billion we forecast in October.",
        "value_low": 3.5, "value_high": 3.5, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to CoWoS advanced packaging capacity allocation from TSMC and HBM memory supply.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-29",
            "ratio": 1.43,
            "why": "MI300 GPU guidance was consecutively raised to $4.0B in April, $4.5B in July, and surpassed $5.0B for full year 2024.",
            "evidence_quote": "Lisa Su (Q3 2024 Call): We now expect 2024 Data Center GPU revenue to exceed $5 billion, up from our previous guidance of $4.5 billion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AMD:2024-04-30#0",
        "ticker": "AMD",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Jean Hu",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Revenue guidance of $5.7 billion plus or minus $300 million",
        "quote": "For the second quarter of 2024, AMD expects revenue to be approximately $5.7 billion, plus or minus $300 million.",
        "value_low": 5.4, "value_high": 6.0, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming continued inventory correction in Embedded and Gaming segments.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-30",
            "ratio": 1.024,
            "why": "Reported Q2 2024 revenue of $5.835 billion in Form 10-Q, within top half of the guided range ($5.4B–$6.0B).",
            "evidence_quote": "Form 10-Q: Net revenue for the second quarter of 2024 was $5,835 million, up 9% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AMD:2024-04-30#1",
        "ticker": "AMD",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Jean Hu",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Embedded segment revenue to bottom in Q2 and improve in second half 2024",
        "quote": "In Embedded, we expect revenue to decline sequentially in the second quarter and then begin a gradual recovery in the second half of the year.",
        "value_low": None, "value_high": None, "unit": "H2 Recovery",
        "period": "2024-H2", "period_kind": "HALF", "strength": "target",
        "conditions": "Dependent on industrial automation and communications customer destocking pace.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-10-29",
            "ratio": 0.85,
            "why": "Embedded recovery lagged expectations; Q3 Embedded revenue was $927M (down 25% YoY) and Q4 remained muted due to automotive softness.",
            "evidence_quote": "Jean Hu: Embedded segment revenue was $927 million, down 25% year-over-year, as customer inventory adjustments continued in industrial end markets.",
            "y": 0.25, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # BROADCOM (AVGO)
    # -------------------------------------------------------------------------
    {
        "id": "AVGO:2024-03-07#0",
        "ticker": "AVGO",
        "call_date": "2024-03-07",
        "call_label": "Q1 FY24 Earnings Call (Mar 7, 2024)",
        "speaker": "Hock Tan",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Full year FY24 AI semiconductor revenue guidance raised to exceed $10 billion",
        "quote": "We now anticipate that AI revenue will be much stronger and represent over $10 billion in fiscal 2024, up from our prior guidance of 25% of semiconductor revenue.",
        "value_low": 10.0, "value_high": 10.0, "unit": "Billion USD",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by custom AI accelerator hyperscaler deployment ramps (Google TPU, Meta MTIA).",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-12-12",
            "ratio": 1.22,
            "why": "Broadcom delivered $12.2 billion in AI revenue for fiscal 2024, exceeding the $10B target by 22%.",
            "evidence_quote": "Hock Tan (Q4 FY24 Call): Revenue from AI reached $12.2 billion for the fiscal year, representing 41% of total semiconductor solutions revenue.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AVGO:2024-03-07#1",
        "ticker": "AVGO",
        "call_date": "2024-03-07",
        "call_label": "Q1 FY24 Earnings Call (Mar 7, 2024)",
        "speaker": "Hock Tan",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "VMware integration to reach annualized exit run-rate EBITDA of $8.5 billion by FY25",
        "quote": "We are accelerating the transition of VMware to a subscription model and are on track to achieve our target of $8.5 billion in annualized pro forma EBITDA by fiscal 2025.",
        "value_low": 8.5, "value_high": 8.5, "unit": "Billion USD",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to customer renewal rates on VMware Cloud Foundation (VCF) multi-year bundles.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-05",
            "ratio": 1.0,
            "why": "In Q3 FY24, VMware quarterly revenue reached $3.8B with operating expense rationalization tracking ahead of initial synergy plan.",
            "evidence_quote": "Kirsten Spears: VMware integration is progressing ahead of plan, with booking velocity in VCF accelerating to over 80% subscription penetration.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AVGO:2024-06-12#0",
        "ticker": "AVGO",
        "call_date": "2024-06-12",
        "call_label": "Q2 FY24 Earnings Call (Jun 12, 2024)",
        "speaker": "Kirsten Spears",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year FY24 Adjusted EBITDA guidance raised to approximately 60% of projected revenue",
        "quote": "Fiscal year 2024 revenue guidance is raised to approximately $51.0 billion, and we expect adjusted EBITDA to be approximately 60% of projected revenue.",
        "value_low": 59.5, "value_high": 61.0, "unit": "%",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-12-12",
            "ratio": 1.03,
            "why": "Delivered full year FY24 adjusted EBITDA of $31.93 billion on $51.56 billion revenue, representing a 61.9% adjusted EBITDA margin.",
            "evidence_quote": "Form 10-K: Adjusted EBITDA for fiscal 2024 was $31,932 million, or 62% of net revenue.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # QUALCOMM (QCOM)
    # -------------------------------------------------------------------------
    {
        "id": "QCOM:2024-01-31#0",
        "ticker": "QCOM",
        "call_date": "2024-01-31",
        "call_label": "Q1 FY24 Earnings Call (Jan 31, 2024)",
        "speaker": "Cristiano Amon",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Snapdragon X Elite commercial PC launches with global OEMs in mid-2024",
        "quote": "We remain on track for commercial launches of Snapdragon X Elite powered Copilot+ PCs in mid-2024 across leading OEMs including Acer, ASUS, Dell, HP, Lenovo, and Microsoft.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Mid", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Windows on ARM OS optimization and ISV app emulation readiness.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-06-18",
            "ratio": 1.0,
            "why": "Copilot+ PCs powered by Snapdragon X Elite officially began retail shipping worldwide on June 18, 2024.",
            "evidence_quote": "Microsoft & Qualcomm Press Release (June 18, 2024): The first Copilot+ PCs powered by Snapdragon X Elite and Snapdragon X Plus are available today globally.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "QCOM:2024-05-01#0",
        "ticker": "QCOM",
        "call_date": "2024-05-01",
        "call_label": "Q2 FY24 Earnings Call (May 1, 2024)",
        "speaker": "Akash Palkhiwala",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 FY24 Revenue expected between $8.8 billion and $9.6 billion",
        "quote": "In the third quarter of fiscal 2024, we are forecasting revenues of $8.8 billion to $9.6 billion, with non-GAAP EPS of $2.15 to $2.35.",
        "value_low": 8.8, "value_high": 9.6, "unit": "Billion USD",
        "period": "Q3 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Reflects typical seasonal decline in premium handset demand.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-31",
            "ratio": 1.02,
            "why": "Reported Q3 FY24 revenue of $9.393 billion and non-GAAP EPS of $2.33 in Form 10-Q, both inside top half of guided range.",
            "evidence_quote": "Form 10-Q: Revenues were $9.39 billion, up 11% year-over-year, driven by strength in premium Android tier smartphones.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # INTEL (INTC)
    # -------------------------------------------------------------------------
    {
        "id": "INTC:2024-01-25#0",
        "ticker": "INTC",
        "call_date": "2024-01-25",
        "call_label": "Q4 2023 Earnings Call (Jan 25, 2024)",
        "speaker": "Pat Gelsinger",
        "role": "CEO",
        "category": "manufacturing_ramp",
        "summary": "Intel 18A process node to achieve manufacturing readiness and 1.0 PDK release in 2024",
        "quote": "Intel 18A is expected to achieve manufacturing readiness in the second half of 2024, with our 1.0 PDK release to external customers by mid-year.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H2", "period_kind": "HALF", "strength": "firm",
        "conditions": "Yield improvement on RibbonFET and PowerVia backside power delivery architectures.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-15",
            "ratio": 1.0,
            "why": "Intel released the Intel 18A 1.0 PDK to ecosystem partners and external customers in July 2024.",
            "evidence_quote": "Intel Newsroom: Intel Foundry releases 1.0 Process Design Kit for Intel 18A, enabling external tape-outs on schedule.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "INTC:2024-04-25#0",
        "ticker": "INTC",
        "call_date": "2024-04-25",
        "call_label": "Q1 2024 Earnings Call (Apr 25, 2024)",
        "speaker": "David Zinsner",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Intel Foundry operating loss to peak in 2024 and reach operating breakeven midway to 2030",
        "quote": "We expect Intel Foundry operating losses to peak in 2024 at approximately $7 billion, before improving sequentially toward breakeven by roughly 2027.",
        "value_low": -7.0, "value_high": -7.0, "unit": "Billion USD Operating Loss",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Dependent on external foundry volume scale and wafer pricing parity with TSMC.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-08-01",
            "ratio": 0.40,
            "why": "Foundry losses exceeded initial budget run-rates; in Q2 2024 Foundry operating losses reached $2.8B in a single quarter, pushing full-year projected loss beyond $10B.",
            "evidence_quote": "David Zinsner: Intel Foundry operating loss was $2.8 billion in Q2, as startup costs and accelerated depreciation weighed on segment margins.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "INTC:2024-04-25#1",
        "ticker": "INTC",
        "call_date": "2024-04-25",
        "call_label": "Q1 2024 Earnings Call (Apr 25, 2024)",
        "speaker": "David Zinsner",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Revenue guidance of $12.5 billion to $13.5 billion with gross margin of 43.5%",
        "quote": "For the second quarter of 2024, we expect revenue of $12.5 billion to $13.5 billion, and non-GAAP gross margin of approximately 43.5%.",
        "value_low": 12.5, "value_high": 13.5, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming steady enterprise server CPU demand.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-08-01",
            "ratio": 0.985,
            "why": "Reported Q2 revenue of $12.83 billion, but GAAP gross margin collapsed to 35.4% (non-GAAP 38.7% vs 43.5% guided, a 480 bps miss); announced 15,000 job cuts and suspended dividend.",
            "evidence_quote": "David Zinsner: Second-quarter results were impacted by gross margin headwinds from the accelerated ramp of our AI PC product, unallocated charges, and excess inventory.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "INTC:2024-08-01#0",
        "ticker": "INTC",
        "call_date": "2024-08-01",
        "call_label": "Q2 2024 Earnings Call (Aug 1, 2024)",
        "speaker": "Pat Gelsinger",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Gaudi 3 AI accelerator revenue target of $500 million in 2024",
        "quote": "We expect Gaudi 3 revenue to ramp in the second half of 2024 and generate approximately $500 million in revenue this year.",
        "value_low": 500.0, "value_high": 500.0, "unit": "Million USD",
        "period": "2024", "period_kind": "YEAR", "strength": "target",
        "conditions": "Subject to software stack maturation and hyperscaler server qualification.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-10-31",
            "ratio": 0.50,
            "why": "On Q3 2024 call, Intel lowered Gaudi expectations, admitting software ecosystem adoption proved slower than anticipated and Gaudi 3 would not meet the $500M target.",
            "evidence_quote": "David Zinsner (Q3 2024 Call): Overall demand for Gaudi has moderated and we will not achieve the $500 million target this year due to slower software adoption.",
            "y": 0.0, "revisions": 1
        }
    },
    {
        "id": "INTC:2024-08-01#1",
        "ticker": "INTC",
        "call_date": "2024-08-01",
        "call_label": "Q2 2024 Earnings Call (Aug 1, 2024)",
        "speaker": "David Zinsner",
        "role": "CFO",
        "category": "capex_guidance",
        "summary": "Full year 2024 Gross capital expenditures reduced by over 20% to $25 billion to $27 billion",
        "quote": "We are reducing our gross capital expenditures for 2024 to $25 billion to $27 billion, down from our prior plan of over $30 billion, as part of our comprehensive cost reduction program.",
        "value_low": 25.0, "value_high": 27.0, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Reflecting paused foundry projects in Germany and Poland.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-23",
            "ratio": 1.0,
            "why": "Reported gross capex of $25.8B in Form 10-K, meeting the reduced expenditure guidance.",
            "evidence_quote": "Form 10-K: Gross additions to property, plant and equipment were $25.8 billion in 2024, down from $25.8B in 2023.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # MICRON TECHNOLOGY (MU)
    # -------------------------------------------------------------------------
    {
        "id": "MU:2024-03-20#0",
        "ticker": "MU",
        "call_date": "2024-03-20",
        "call_label": "Q2 FY24 Earnings Call (Mar 20, 2024)",
        "speaker": "Sanjay Mehrotra",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "High Bandwidth Memory (HBM3E) production capacity entirely sold out for calendar 2024",
        "quote": "Our HBM3E is entirely sold out for calendar 2024, and the overwhelming majority of our 2025 capacity is already contracted to tier-1 customers.",
        "value_low": None, "value_high": None, "unit": "100% Sold Out",
        "period": "CY2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Constrained by 1-beta DRAM node yield and advanced packaging through-silicon via (TSV) capacity.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-06-26",
            "ratio": 1.0,
            "why": "Confirmed in Q3 FY24 that calendar 2024 and calendar 2025 capacity were completely booked with multi-billion supply agreements.",
            "evidence_quote": "Sanjay Mehrotra: Our HBM capacity is now completely sold out through calendar 2025, with pricing long-term contracted.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MU:2024-03-20#1",
        "ticker": "MU",
        "call_date": "2024-03-20",
        "call_label": "Q2 FY24 Earnings Call (Mar 20, 2024)",
        "speaker": "Mark Murphy",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Q3 FY24 Gross margin guidance of 25.0% to 28.0%",
        "quote": "Non-GAAP gross margin is expected to be in the range of 25.0% to 28.0%, reflecting sharp price increases across both DRAM and NAND.",
        "value_low": 25.0, "value_high": 28.0, "unit": "%",
        "period": "Q3 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-06-26",
            "ratio": 1.004,
            "why": "Reported Q3 FY24 non-GAAP gross margin of 28.1% in Form 10-Q, beating the top end of the guided 25.0%–28.0% range.",
            "evidence_quote": "Mark Murphy: Non-GAAP gross margin was 28.1%, up over 900 basis points sequentially driven by broad pricing power.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # APPLIED MATERIALS (AMAT)
    # -------------------------------------------------------------------------
    {
        "id": "AMAT:2024-05-16#0",
        "ticker": "AMAT",
        "call_date": "2024-05-16",
        "call_label": "Q2 FY24 Earnings Call (May 16, 2024)",
        "speaker": "Brice Hill",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 FY24 Net revenue expected approximately $6.65 billion plus or minus $400 million",
        "quote": "In the third quarter of fiscal 2024, we expect net revenue to be approximately $6.65 billion, plus or minus $400 million. Non-GAAP diluted EPS is expected to be in the range of $1.83 to $2.19.",
        "value_low": 6.25, "value_high": 7.05, "unit": "Billion USD",
        "period": "Q3 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-15",
            "ratio": 1.02,
            "why": "Reported Q3 FY24 revenue of $6.78 billion and non-GAAP EPS of $2.12 in Form 10-Q, inside the guided range.",
            "evidence_quote": "Form 10-Q: Net revenue for the third quarter of fiscal 2024 was $6.78 billion, up 5% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # TEXAS INSTRUMENTS (TXN)
    # -------------------------------------------------------------------------
    {
        "id": "TXN:2024-04-23#0",
        "ticker": "TXN",
        "call_date": "2024-04-23",
        "call_label": "Q1 2024 Earnings Call (Apr 23, 2024)",
        "speaker": "Rafael Lizardi",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Revenue expected between $3.65 billion and $3.95 billion",
        "quote": "For the second quarter, we expect revenue in the range of $3.65 billion to $3.95 billion, and earnings per share between $1.05 and $1.25.",
        "value_low": 3.65, "value_high": 3.95, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming ongoing customer inventory reduction across automotive and industrial sectors.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-23",
            "ratio": 1.005,
            "why": "Reported Q2 2024 revenue of $3.822 billion and EPS of $1.22 in Form 10-Q, inside guided range.",
            "evidence_quote": "Form 10-Q: Second quarter revenue was $3.82 billion, up 4% sequentially, with EPS of $1.22.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "TXN:2024-04-23#1",
        "ticker": "TXN",
        "call_date": "2024-04-23",
        "call_label": "Q1 2024 Earnings Call (Apr 23, 2024)",
        "speaker": "Haviv Ilan",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Industrial customer inventory digestion cycle to reach bottom by late 2024",
        "quote": "We believe industrial is broad-based in its inventory cycle and will likely trough sometime in the second half of this year.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H2", "period_kind": "HALF", "strength": "hedged",
        "conditions": "Subject to factory automation and power grid capex cycles.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "LATE",
            "knowable_at": "2024-10-22",
            "ratio": 0.65,
            "why": "Industrial sequential recovery remained sluggish; automotive customers continued inventory destocking into Q4 2024.",
            "evidence_quote": "Haviv Ilan: While industrial grew sequentially in Q3, automotive customer inventory reductions accelerated and are continuing.",
            "y": 0.5, "revisions": 1
        }
    },
    # -------------------------------------------------------------------------
    # 2025 COMMITMENTS & AUDITED RESOLUTIONS
    # -------------------------------------------------------------------------
    {
        "id": "AMD:2025-02-04#0",
        "ticker": "AMD",
        "call_date": "2025-02-04",
        "call_label": "Q4 2024 Earnings Call (Feb 4, 2025)",
        "speaker": "Jean Hu",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 2025 revenue of approximately $7.1 billion plus or minus $300 million",
        "quote": "For the first quarter of 2025, AMD expects revenue to be approximately $7.1 billion, plus or minus $300 million.",
        "value_low": 6.80, "value_high": 7.40, "unit": "Billion USD",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to data center MI300 ramp and seasonal client trends.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-06",
            "ratio": 1.047,
            "why": "Reported Q1 2025 revenue of $7.438 billion, exceeding the high end of the guided range ($7.4B) driven by EPYC server and GPU demand.",
            "evidence_quote": "Jean Hu: First quarter revenue was $7.44 billion, up 36% year-over-year, driven by record Data Center segment revenue.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "INTC:2025-01-30#0",
        "ticker": "INTC",
        "call_date": "2025-01-30",
        "call_label": "Q4 2024 Earnings Call (Jan 30, 2025)",
        "speaker": "David Zinsner",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 2025 revenue guidance between $11.7 billion and $12.7 billion with non-GAAP breakeven EPS",
        "quote": "For the first quarter of 2025, we expect revenue of $11.7 billion to $12.7 billion, with gross margin of 36.5% GAAP and 39.5% non-GAAP.",
        "value_low": 11.70, "value_high": 12.70, "unit": "Billion USD",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to normal client seasonality and inventory rebalancing.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2025-04-24",
            "ratio": 0.50,
            "why": "Although Q1 revenue hit $12.67B, GAAP net loss widened to $(0.19) and management revised Q2 guidance down to $11.2B–$12.4B with breakeven non-GAAP EPS, cutting annual foundry projections.",
            "evidence_quote": "Form 10-Q: GAAP net loss was $(0.8) billion and diluted EPS was $(0.19). For Q2 2025, Intel lowered expected revenue to $11.2 billion to $12.4 billion.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "AVGO:2025-03-06#0",
        "ticker": "AVGO",
        "call_date": "2025-03-06",
        "call_label": "Q1 FY25 Earnings Call (Mar 6, 2025)",
        "speaker": "Hock Tan",
        "role": "CEO",
        "category": "revenue_target",
        "summary": "Q2 FY25 revenue guidance of approximately $14.9 billion",
        "quote": "Second quarter fiscal year 2025 revenue guidance is approximately $14.9 billion, representing an anticipated increase of 19% compared to the prior year period.",
        "value_low": 14.60, "value_high": 15.20, "unit": "Billion USD",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Driven by AI semiconductor networking solutions and VMware software integration.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-06-05",
            "ratio": 1.007,
            "why": "Reported Q2 FY25 net revenue of $15.004 billion and AI revenue exceeding $4.4 billion, beating guided midpoint.",
            "evidence_quote": "Hock Tan: Net revenue grew 20% year-over-year to a record $15.0 billion, underpinned by continued strength in AI semiconductor solutions.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "QCOM:2025-02-05#0",
        "ticker": "QCOM",
        "call_date": "2025-02-05",
        "call_label": "Q1 FY25 Earnings Call (Feb 5, 2025)",
        "speaker": "Akash Palkhiwala",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 FY25 GAAP revenues between $10.3 billion and $11.2 billion",
        "quote": "In the second quarter of fiscal 2025, we are forecasting revenues of $10.3 billion to $11.2 billion, with QCT revenues between $8.9 billion and $9.5 billion.",
        "value_low": 10.30, "value_high": 11.20, "unit": "Billion USD",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to handset launch timing across Chinese OEMs and automotive ramp.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-01",
            "ratio": 1.023,
            "why": "Reported Q2 FY25 revenues of $11.0 billion, up 17% year-over-year, well inside guided upper tier.",
            "evidence_quote": "Form 10-Q: Total revenues were $11.0 billion in Q2 FY25 compared to $9.39 billion in the prior year period.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MU:2025-03-20#0",
        "ticker": "MU",
        "call_date": "2025-03-20",
        "call_label": "Q2 FY25 Earnings Call (Mar 20, 2025)",
        "speaker": "Mark Murphy",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 FY25 revenue guidance of $8.8 billion plus or minus $200 million",
        "quote": "For the third quarter of fiscal 2025, we expect revenue of $8.8 billion, plus or minus $200 million, and non-GAAP gross margin of 36.5% plus or minus 100 bps.",
        "value_low": 8.60, "value_high": 9.00, "unit": "Billion USD",
        "period": "Q3 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Driven by HBM3E pricing, volume shipments, and data center SSD demand.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-06-25",
            "ratio": 1.057,
            "why": "Reported Q3 FY25 revenue of $9.30 billion, beating the top end of the guided range ($9.0B) due to sold-out HBM capacity.",
            "evidence_quote": "Sanjay Mehrotra: Micron delivered fiscal Q3 revenue of $9.30 billion, driven by robust AI demand and strong execution across DRAM and NAND.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AMAT:2025-02-13#0",
        "ticker": "AMAT",
        "call_date": "2025-02-13",
        "call_label": "Q1 FY25 Earnings Call (Feb 13, 2025)",
        "speaker": "Brice Hill",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 FY25 net revenue of approximately $7.10 billion plus or minus $400 million",
        "quote": "In the second quarter of fiscal 2025, Applied expects net revenue to be approximately $7.10 billion, plus or minus $400 million.",
        "value_low": 6.70, "value_high": 7.50, "unit": "Billion USD",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to leading-edge foundry logic spending and packaging deliveries.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-15",
            "ratio": 1.0,
            "why": "Reported Q2 FY25 net revenue of exactly $7.100 billion, hitting the guided midpoint on the dot.",
            "evidence_quote": "Form 10-Q: Net revenue for the second quarter ended April 27, 2025 was $7,100 million, up 7% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "TXN:2025-01-23#0",
        "ticker": "TXN",
        "call_date": "2025-01-23",
        "call_label": "Q4 2024 Earnings Call (Jan 23, 2025)",
        "speaker": "Rafael Lizardi",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 2025 revenue in the range of $3.74 billion to $4.06 billion",
        "quote": "TI's outlook for first-quarter 2025 is for revenue in the range of $3.74 billion to $4.06 billion, and earnings per share between $0.94 and $1.16.",
        "value_low": 3.74, "value_high": 4.06, "unit": "Billion USD",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assumes bottoming industrial order patterns and gradual channel restock.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-22",
            "ratio": 1.002,
            "why": "Reported Q1 2025 revenue of $4.069 billion, delivering right at the top edge of the guided $3.74B–$4.06B band.",
            "evidence_quote": "Form 10-Q: First quarter revenue was $4,069 million, an increase of 11% compared to the prior-year period.",
            "y": 1.0, "revisions": 0
        }
    }
]
