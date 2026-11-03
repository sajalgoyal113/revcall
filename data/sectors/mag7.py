"""Guidance commitments and SEC 10-Q/10-K resolutions for Magnificent 7 US Equities:
NVDA, MSFT, AAPL, GOOGL, AMZN, META, TSLA.
"""

MAG7_PROMISES = [
    # -------------------------------------------------------------------------
    # NVIDIA (NVDA)
    # -------------------------------------------------------------------------
    {
        "id": "NVDA:2024-05-22#0",
        "ticker": "NVDA",
        "call_date": "2024-05-22",
        "call_label": "Q1 FY25 Earnings Call (May 22, 2024)",
        "speaker": "Colette Kress",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 FY25 Revenue guidance of $28.0 billion plus or minus 2%",
        "quote": "Revenue is expected to be $28.0 billion, plus or minus 2%. We expect sequential growth across all market platforms led by Data Center.",
        "value_low": 27.44, "value_high": 28.56, "unit": "Billion USD",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to wafer supply allocation and supply chain packaging ramp.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-28",
            "ratio": 1.073,
            "why": "Reported Q2 FY25 revenue of $30.04 billion in Form 10-Q, beating guided midpoint ($28.0B) by 7.3%.",
            "evidence_quote": "Colette Kress: Q2 revenue was a record $30.04 billion, up 15% sequentially and up 122% from a year ago.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NVDA:2024-05-22#1",
        "ticker": "NVDA",
        "call_date": "2024-05-22",
        "call_label": "Q1 FY25 Earnings Call (May 22, 2024)",
        "speaker": "Colette Kress",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Q2 FY25 GAAP Gross Margin guidance of 74.8% plus or minus 50 bps",
        "quote": "GAAP and non-GAAP gross margins are expected to be 74.8% and 75.5%, respectively, plus or minus 50 basis points. For the full year, gross margins are expected to be in the mid-70% range.",
        "value_low": 74.3, "value_high": 75.3, "unit": "%",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-28",
            "ratio": 1.004,
            "why": "Reported Q2 FY25 GAAP gross margin of 75.1% in Form 10-Q, perfectly within the guided 74.3%–75.3% band.",
            "evidence_quote": "GAAP gross margin for the second quarter was 75.1% and non-GAAP gross margin was 75.7%.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NVDA:2024-05-22#2",
        "ticker": "NVDA",
        "call_date": "2024-05-22",
        "call_label": "Q1 FY25 Earnings Call (May 22, 2024)",
        "speaker": "Jensen Huang",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Blackwell architecture sample shipments in Q2 and customer production ramp in Q4 FY25",
        "quote": "We will see Blackwell architecture shipping sample systems to customers in Q2 and ramping into production in Q4 of this fiscal year.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY25-Q4", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Depends on TSMC CoWoS-L packaging qualification and yield stability.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-20",
            "ratio": 1.0,
            "why": "Confirmed on Q3 FY25 earnings call: Blackwell production in full swing with 13,000 samples shipped and billions in Q4 revenue.",
            "evidence_quote": "Colette Kress: Blackwell production is in full swing. We delivered 13,000 GPU samples in Q3 to customers like Microsoft and Oracle.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NVDA:2024-08-28#0",
        "ticker": "NVDA",
        "call_date": "2024-08-28",
        "call_label": "Q2 FY25 Earnings Call (Aug 28, 2024)",
        "speaker": "Colette Kress",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q3 FY25 Revenue guidance of $32.5 billion plus or minus 2%",
        "quote": "Revenue is expected to be $32.5 billion, plus or minus 2%. We anticipate Data Center growth to continue sequentially.",
        "value_low": 31.85, "value_high": 33.15, "unit": "Billion USD",
        "period": "Q3 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-20",
            "ratio": 1.079,
            "why": "Reported Q3 FY25 revenue of $35.08 billion in Form 10-Q, beating guided midpoint ($32.5B) by 7.9%.",
            "evidence_quote": "Colette Kress: Third quarter revenue was a record $35.08 billion, up 17% sequentially and up 94% from a year ago.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NVDA:2024-08-28#1",
        "ticker": "NVDA",
        "call_date": "2024-08-28",
        "call_label": "Q2 FY25 Earnings Call (Aug 28, 2024)",
        "speaker": "Colette Kress",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Full year FY25 GAAP Gross Margin expected in mid-70% range",
        "quote": "For the full year, we expect gross margins to be in the mid-70% range, as we transition from Hopper to Blackwell architecture.",
        "value_low": 74.0, "value_high": 76.0, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to Blackwell initial ramp manufacturing costs.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-02-26",
            "ratio": 1.0,
            "why": "Reported full year FY25 GAAP gross margin of 75.0% in Form 10-K, delivering exactly at midpoint of guided range.",
            "evidence_quote": "Full year GAAP gross margin was 75.0%, up from 72.7% in fiscal 2024.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # MICROSOFT (MSFT)
    # -------------------------------------------------------------------------
    {
        "id": "MSFT:2024-04-25#0",
        "ticker": "MSFT",
        "call_date": "2024-04-25",
        "call_label": "Q3 FY24 Earnings Call (Apr 25, 2024)",
        "speaker": "Amy Hood",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q4 FY24 Azure revenue growth of 30% to 31% in constant currency",
        "quote": "In Azure, we expect Q4 revenue growth in constant currency to be 30% to 31%, with roughly 7 points of growth from AI services.",
        "value_low": 30.0, "value_high": 31.0, "unit": "%",
        "period": "Q4 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Capacity constraints in AI GPU infrastructure may cap upside.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-30",
            "ratio": 1.0,
            "why": "Reported Q4 FY24 Azure constant currency growth of 30% (AI contributed 8 points vs 7 guided).",
            "evidence_quote": "Amy Hood: Azure revenue grew 29% and 30% in constant currency, including 8 points from AI services where demand remained higher than our available capacity.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MSFT:2024-04-25#1",
        "ticker": "MSFT",
        "call_date": "2024-04-25",
        "call_label": "Q3 FY24 Earnings Call (Apr 25, 2024)",
        "speaker": "Amy Hood",
        "role": "CFO",
        "category": "capex_guidance",
        "summary": "Capital expenditures to increase sequentially each quarter through FY25",
        "quote": "We expect capital expenditures to increase sequentially each quarter driven by cloud and AI infrastructure investments.",
        "value_low": None, "value_high": None, "unit": "Sequential Increase",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by data center construction delivery and semiconductor lead times.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.0,
            "why": "Capex increased sequentially: Q3 FY24 $14.0B -> Q4 FY24 $19.0B -> Q1 FY25 $20.0B in SEC filings.",
            "evidence_quote": "Form 10-Q: Capital expenditures including finance leases were $20.0 billion in Q1 FY25 compared to $19.0 billion in Q4 FY24.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MSFT:2024-07-30#0",
        "ticker": "MSFT",
        "call_date": "2024-07-30",
        "call_label": "Q4 FY24 Earnings Call (Jul 30, 2024)",
        "speaker": "Amy Hood",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q1 FY25 Azure revenue growth of 28% to 29% in constant currency",
        "quote": "In Azure, we expect Q1 constant currency revenue growth of 28% to 29%, reflecting continued demand with acceleration expected in H2.",
        "value_low": 28.0, "value_high": 29.0, "unit": "%",
        "period": "Q1 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Constrained by AI capacity availability.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.15,
            "why": "Reported Q1 FY25 Azure constant currency growth of 34%, easily beating guided 28%–29% range.",
            "evidence_quote": "Amy Hood: Azure revenue grew 33% and 34% in constant currency, exceeding expectations due to strong non-AI execution alongside 12 points of AI contribution.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MSFT:2024-07-30#1",
        "ticker": "MSFT",
        "call_date": "2024-07-30",
        "call_label": "Q4 FY24 Earnings Call (Jul 30, 2024)",
        "speaker": "Satya Nadella",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Accelerating enterprise adoption of Microsoft 365 Copilot seats across enterprise",
        "quote": "We expect customer seat expansions for M365 Copilot to accelerate as corporate customers complete deployment pilots and scale to general enterprise rollouts.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY25-H1", "period_kind": "HALF", "strength": "aspirational",
        "conditions": "Subject to corporate IT budget approval cycles and security review timelines.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "PARTIAL",
            "knowable_at": "2024-10-30",
            "ratio": 0.85,
            "why": "Customer expansions continued (+60% QoQ seat count), but CIO feedback noted ROI measurement friction delaying company-wide rollouts.",
            "evidence_quote": "Satya Nadella: Daily active users doubled, but enterprise deployment cycles remain measured as organizations establish internal workflow governance.",
            "y": 0.5, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # APPLE (AAPL)
    # -------------------------------------------------------------------------
    {
        "id": "AAPL:2024-05-02#0",
        "ticker": "AAPL",
        "call_date": "2024-05-02",
        "call_label": "Q2 FY24 Earnings Call (May 2, 2024)",
        "speaker": "Luca Maestri",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q3 FY24 Revenue expected to grow low single digits year-over-year",
        "quote": "For the June quarter, we expect our total company revenue to grow low single digits year over year, with Services revenue growing double digits.",
        "value_low": 2.0, "value_high": 4.0, "unit": "%",
        "period": "Q3 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming macroeconomic conditions do not worsen and FX impact of approximately 1.5 percentage points.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-01",
            "ratio": 1.25,
            "why": "Reported Q3 FY24 revenue of $85.78 billion, representing 4.9% YoY growth (above guided 2-4% band).",
            "evidence_quote": "Luca Maestri: We achieved revenue of $85.8 billion, up 5% year-over-year, driven by quarterly record Services revenue of $24.2 billion, up 14%.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AAPL:2024-05-02#1",
        "ticker": "AAPL",
        "call_date": "2024-05-02",
        "call_label": "Q2 FY24 Earnings Call (May 2, 2024)",
        "speaker": "Luca Maestri",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Q3 FY24 Gross Margin expected between 45.5% and 46.5%",
        "quote": "Gross margin is expected to be between 45.5% and 46.5%. Operating expenses are expected to be between $14.3 billion and $14.5 billion.",
        "value_low": 45.5, "value_high": 46.5, "unit": "%",
        "period": "Q3 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-01",
            "ratio": 1.006,
            "why": "Reported Q3 FY24 gross margin of 46.3% in Form 10-Q, within top half of the guided 45.5%–46.5% band.",
            "evidence_quote": "Gross margin for the quarter was 46.3%, benefiting from favorable product mix and Services expansion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AAPL:2024-08-01#0",
        "ticker": "AAPL",
        "call_date": "2024-08-01",
        "call_label": "Q3 FY24 Earnings Call (Aug 1, 2024)",
        "speaker": "Tim Cook",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Apple Intelligence U.S. English rollout scheduled for fall 2024 in iOS 18.1",
        "quote": "We will be rolling out Apple Intelligence for U.S. English users this fall with iOS 18.1, iPadOS 18.1, and macOS Sequoia 15.1, followed by additional features over the coming months.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Fall", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Dependent on model safety audits and private cloud compute infrastructure readiness.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-28",
            "ratio": 1.0,
            "why": "Apple Intelligence officially launched on October 28, 2024 as part of iOS 18.1 release.",
            "evidence_quote": "Apple Newsroom (Oct 28, 2024): Apple Intelligence is available today for iPhone, iPad, and Mac users through a free software update with the release of iOS 18.1.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AAPL:2024-08-01#1",
        "ticker": "AAPL",
        "call_date": "2024-08-01",
        "call_label": "Q3 FY24 Earnings Call (Aug 1, 2024)",
        "speaker": "Luca Maestri",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q4 FY24 Revenue growth to continue at similar year-over-year rate as Q3 (~5%)",
        "quote": "For the September quarter, we expect our year-over-year revenue growth to be similar to the June quarter growth rate of approximately 5%.",
        "value_low": 4.5, "value_high": 5.5, "unit": "%",
        "period": "Q4 FY24", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-31",
            "ratio": 1.2,
            "why": "Reported Q4 FY24 revenue of $94.93 billion, representing 6.1% YoY growth (above the ~5% guided rate).",
            "evidence_quote": "Luca Maestri: We generated September quarter revenue of $94.9 billion, up 6% year-over-year, setting September quarter revenue records in the Americas, Europe, and Asia Pacific.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # ALPHABET (GOOGL)
    # -------------------------------------------------------------------------
    {
        "id": "GOOGL:2024-04-25#0",
        "ticker": "GOOGL",
        "call_date": "2024-04-25",
        "call_label": "Q1 2024 Earnings Call (Apr 25, 2024)",
        "speaker": "Ruth Porat",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Google Cloud operating margin to continue expanding profitability in 2024",
        "quote": "In Google Cloud, we are pleased with the operating profitability inflection and expect margins to continue to expand over the course of 2024 as we scale infrastructure efficiently.",
        "value_low": None, "value_high": None, "unit": "Expansion",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-23",
            "ratio": 1.0,
            "why": "Reported Q2 2024 Cloud operating income of $1.17B (11.3% margin, up from 9.0% in Q1 and 4.9% prior year).",
            "evidence_quote": "Sundar Pichai: Google Cloud delivered quarterly revenues of $10.3 billion, surpassing $10 billion for the first time, with operating profit of $1.2 billion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "GOOGL:2024-04-25#1",
        "ticker": "GOOGL",
        "call_date": "2024-04-25",
        "call_label": "Q1 2024 Earnings Call (Apr 25, 2024)",
        "speaker": "Ruth Porat",
        "role": "CFO",
        "category": "capex_guidance",
        "summary": "Quarterly capital expenditures of roughly $12 billion per quarter in 2024",
        "quote": "Looking ahead, we expect quarterly CapEx throughout the year to be roughly at or above the Q1 level of $12 billion, driven by investments in technical infrastructure.",
        "value_low": 11.5, "value_high": 13.0, "unit": "Billion USD/Quarter",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by data center facility delivery and custom TPU/GPU procurement.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-29",
            "ratio": 1.05,
            "why": "Reported quarterly Capex of $13.2B in Q2 and $13.0B in Q3 2024 in Form 10-Q filings.",
            "evidence_quote": "Anat Ashkenazi: Capital expenditures in the third quarter were $13 billion, driven by investment in servers and data centers.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "GOOGL:2024-07-23#0",
        "ticker": "GOOGL",
        "call_date": "2024-07-23",
        "call_label": "Q2 2024 Earnings Call (Jul 23, 2024)",
        "speaker": "Sundar Pichai",
        "role": "CEO",
        "category": "product_launch",
        "summary": "AI Overviews in Search to reach over 1 billion monthly users by end of 2024",
        "quote": "With our generative AI overviews now live in the U.S. and rolling out internationally, we are on track to bring this experience to over 1 billion people by the end of the year.",
        "value_low": 1.0, "value_high": 1.0, "unit": "Billion Users",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Dependent on infrastructure latency reductions and query cost optimizations.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-29",
            "ratio": 1.0,
            "why": "Sundar Pichai confirmed on Q3 2024 call that AI Overviews reached over 1 billion monthly users across more than 100 countries.",
            "evidence_quote": "Sundar Pichai: AI Overviews are now reaching over 1 billion people every month, with engagement and satisfaction metrics increasing globally.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # AMAZON (AMZN)
    # -------------------------------------------------------------------------
    {
        "id": "AMZN:2024-04-30#0",
        "ticker": "AMZN",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Brian Olsavsky",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Net sales expected between $144.0 billion and $149.0 billion",
        "quote": "Net sales are expected to be between $144.0 billion and $149.0 billion, or to grow between 7% and 11% compared with second quarter 2023.",
        "value_low": 144.0, "value_high": 149.0, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Anticipates an unfavorable foreign exchange impact of approximately 60 basis points.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-01",
            "ratio": 1.01,
            "why": "Reported Q2 2024 net sales of $147.98 billion in Form 10-Q, squarely inside the guided range ($144B–$149B).",
            "evidence_quote": "Form 10-Q: Net sales increased 10% to $148.0 billion in the second quarter, compared with $134.4 billion in second quarter 2023.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AMZN:2024-04-30#1",
        "ticker": "AMZN",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Brian Olsavsky",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Q2 2024 Operating income expected between $10.0 billion and $14.0 billion",
        "quote": "Operating income is expected to be between $10.0 billion and $14.0 billion, compared with $7.7 billion in second quarter 2023.",
        "value_low": 10.0, "value_high": 14.0, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-01",
            "ratio": 1.22,
            "why": "Reported Q2 2024 operating income of $14.67 billion, beating the top end of the guided range ($14.0B) by $672M.",
            "evidence_quote": "Operating income was $14.7 billion for the second quarter, compared with $7.7 billion in the second quarter of 2023.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "AMZN:2024-08-01#0",
        "ticker": "AMZN",
        "call_date": "2024-08-01",
        "call_label": "Q2 2024 Earnings Call (Aug 1, 2024)",
        "speaker": "Andy Jassy",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Project Kuiper initial commercial satellite broadband service rollout in late 2024",
        "quote": "We remain on track to start beta testing Project Kuiper later this year with early commercial customers as launch production ramps.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H2", "period_kind": "HALF", "strength": "firm",
        "conditions": "Contingent on third-party commercial rocket launch schedules (ULA Atlas V / Vulcan).",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "LATE",
            "knowable_at": "2024-10-31",
            "ratio": 0.5,
            "why": "Commercial deployment shifted into 2025 following launch schedule adjustments and satellite production qualification.",
            "evidence_quote": "Brian Olsavsky: We are adjusting our deployment schedule with satellite deployment accelerating in early 2025 as launch slots become available.",
            "y": 0.5, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # META PLATFORMS (META)
    # -------------------------------------------------------------------------
    {
        "id": "META:2024-04-24#0",
        "ticker": "META",
        "call_date": "2024-04-24",
        "call_label": "Q1 2024 Earnings Call (Apr 24, 2024)",
        "speaker": "Susan Li",
        "role": "CFO",
        "category": "capex_guidance",
        "summary": "Full year 2024 Capital expenditures raised to $35 billion to $40 billion",
        "quote": "We anticipate our full year 2024 capital expenditures will be in the range of $35 billion to $40 billion, increased from our prior range of $30 billion to $37 billion, as we continue to accelerate our infrastructure investments.",
        "value_low": 35.0, "value_high": 40.0, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by GPU procurement and data center construction milestones.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-02-05",
            "ratio": 1.04,
            "why": "Reported full year 2024 Capex of $39.24 billion in Form 10-K, delivering within the guided $35B–$40B range.",
            "evidence_quote": "Form 10-K: Capital expenditures, including principal payments on finance leases, were $39.24 billion for full year 2024.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "META:2024-04-24#1",
        "ticker": "META",
        "call_date": "2024-04-24",
        "call_label": "Q1 2024 Earnings Call (Apr 24, 2024)",
        "speaker": "Susan Li",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q2 2024 Total revenue expected between $36.5 billion and $39.0 billion",
        "quote": "We expect second quarter 2024 total revenue to be in the range of $36.5 billion to $39.0 billion. Our guidance assumes foreign currency is roughly a 1% headwind.",
        "value_low": 36.5, "value_high": 39.0, "unit": "Billion USD",
        "period": "Q2 2024", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assuming 1% foreign currency exchange headwind.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-31",
            "ratio": 1.03,
            "why": "Reported Q2 2024 revenue of $39.07 billion in Form 10-Q, exceeding the high end of the guided range ($39.0B).",
            "evidence_quote": "Susan Li: Second quarter total revenue was $39.1 billion, up 22% year-over-year, driven by strong advertiser demand across online commerce and gaming.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "META:2024-07-31#0",
        "ticker": "META",
        "call_date": "2024-07-31",
        "call_label": "Q2 2024 Earnings Call (Jul 31, 2024)",
        "speaker": "Mark Zuckerberg",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Release of frontier open-source Llama 3.1 405B model and broad industry adoption",
        "quote": "With Llama 3.1 405B now launched, we expect open source AI to become the industry standard, and Meta AI is on track to be the most used AI assistant by year-end.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H2", "period_kind": "HALF", "strength": "firm",
        "conditions": None,
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.0,
            "why": "Llama 3.1 shipped July 2024; on Q3 call, Meta AI confirmed approaching 500 million monthly active users.",
            "evidence_quote": "Mark Zuckerberg: Meta AI now has almost 500 million monthly active users, and we continue to see healthy adoption across WhatsApp and Instagram.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # TESLA (TSLA)
    # -------------------------------------------------------------------------
    {
        "id": "TSLA:2024-01-24#0",
        "ticker": "TSLA",
        "call_date": "2024-01-24",
        "call_label": "Q4 2023 Earnings Call (Jan 24, 2024)",
        "speaker": "Elon Musk",
        "role": "CEO",
        "category": "revenue_growth",
        "summary": "2024 vehicle volume growth rate to be notably lower than in 2023",
        "quote": "In 2024, our vehicle volume growth rate may be notably lower than the growth rate achieved in 2023, as our teams work on the launch of the next-generation vehicle at Gigafactory Texas.",
        "value_low": 5.0, "value_high": 15.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "hedged",
        "conditions": "Between two major growth waves (Model 3/Y ramp and Next-Gen platform).",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2025-01-29",
            "ratio": 0.0,
            "why": "Delivered 1,789,226 vehicles in 2024 vs 1,808,581 in 2023, resulting in negative volume growth (-1.1%), missing even modest positive growth expectations.",
            "evidence_quote": "Form 10-K: Total vehicle deliveries decreased 1% year-over-year to 1,789,226 in 2024.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "TSLA:2024-01-24#1",
        "ticker": "TSLA",
        "call_date": "2024-01-24",
        "call_label": "Q4 2023 Earnings Call (Jan 24, 2024)",
        "speaker": "Elon Musk",
        "role": "CEO",
        "category": "manufacturing_ramp",
        "summary": "Cybertruck production ramp to reach annual rate of 250,000 units by 2025",
        "quote": "I'd guess that we will reach a volume production rate of about 250,000 Cybertrucks a year sometime in 2025. That's our best estimate.",
        "value_low": 250000, "value_high": 250000, "unit": "Units/Year",
        "period": "2025", "period_kind": "YEAR", "strength": "hedged",
        "conditions": "Constrained by 4680 battery dry electrode manufacturing yield and body panel stamping tolerances.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "LATE",
            "knowable_at": "2024-10-23",
            "ratio": 0.50,
            "why": "Ramp pace proved slower than projected; annualized run-rate reached approximately 75,000–90,000 units by late 2024, pushing 250k milestone out.",
            "evidence_quote": "Vaibhav Taneja: Cybertruck reached positive gross margin in Q3 for the first time, though production scale remains in initial ramp curve.",
            "y": 0.5, "revisions": 1
        }
    },
    {
        "id": "TSLA:2024-04-23#0",
        "ticker": "TSLA",
        "call_date": "2024-04-23",
        "call_label": "Q1 2024 Earnings Call (Apr 23, 2024)",
        "speaker": "Elon Musk",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Energy storage deployment expected to increase by at least 100% in 2024",
        "quote": "Our energy storage business continues to grow remarkably. We expect deployments to increase by at least 100% year-over-year in 2024.",
        "value_low": 100.0, "value_high": 100.0, "unit": "% Growth",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by Megapack Megafactory Lathrop manufacturing line throughput.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-29",
            "ratio": 1.25,
            "why": "Reported energy storage deployment of 31.4 GWh in 2024 compared to 14.7 GWh in 2023, an increase of 114% (beating guided 100%+ rate).",
            "evidence_quote": "Form 10-K: Energy storage deployments reached a record 31.4 GWh in 2024, up 114% compared to 14.7 GWh in 2023.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "TSLA:2024-07-23#0",
        "ticker": "TSLA",
        "call_date": "2024-07-23",
        "call_label": "Q2 2024 Earnings Call (Jul 23, 2024)",
        "speaker": "Vaibhav Taneja",
        "role": "CFO",
        "category": "gross_margin",
        "summary": "Automotive gross margin ex-regulatory credits to stabilize in second half 2024",
        "quote": "We expect automotive gross margin excluding regulatory credits to see stabilization in the second half of the year as cost reductions offset pricing dynamics.",
        "value_low": 16.0, "value_high": 17.5, "unit": "%",
        "period": "2024-H2", "period_kind": "HALF", "strength": "target",
        "conditions": "Subject to financing rate promotion subsidies and tariff impacts.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "PARTIAL",
            "knowable_at": "2024-10-23",
            "ratio": 0.88,
            "why": "Auto gross margin ex-credits rose to 17.1% in Q3 due to Cybertruck margin turn, but dipped to 15.5% in Q4 with zero-interest financing promos.",
            "evidence_quote": "Form 10-Q: Automotive gross margin excluding regulatory credits was 17.1% in Q3 2024 and 15.5% in Q4 2024.",
            "y": 0.5, "revisions": 1
        }
    },
    {
        "id": "TSLA:2024-04-23#1",
        "ticker": "TSLA",
        "call_date": "2024-04-23",
        "call_label": "Q1 2024 Earnings Call (Apr 23, 2024)",
        "speaker": "Elon Musk",
        "role": "CEO",
        "category": "product_launch",
        "summary": "Production launch of new low-cost $25,000 consumer vehicle in early 2025",
        "quote": "We have updated our future vehicle lineup to accelerate the launch of new vehicles ahead of our previously communicated start of production in late 2025, including more affordable models.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2025-H1", "period_kind": "HALF", "strength": "aspirational",
        "conditions": "Utilizing aspects of next-gen platform alongside current Model 3/Y production lines.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-10-23",
            "ratio": 0.25,
            "why": "On Q3 2024 call, Elon Musk dismissed a regular $25k non-autonomous vehicle as 'pointless', pivoting engineering strictly to autonomous Cybercab.",
            "evidence_quote": "Elon Musk: Having a regular $25k model is pointless. It would be silly. Everything will be fully autonomous Cybercab.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "TSLA:2023-10-18#0",
        "ticker": "TSLA",
        "call_date": "2023-10-18",
        "call_label": "Q3 2023 Earnings Call (Oct 18, 2023)",
        "speaker": "Elon Musk",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Long-term multi-year compound annual growth rate of 50% vehicle deliveries",
        "quote": "For many years, we expect to achieve 50% compound annual growth in vehicle deliveries as our manufacturing scale compounds.",
        "value_low": 50.0, "value_high": 50.0, "unit": "% CAGR",
        "period": "2021-2024", "period_kind": "YEAR", "strength": "aspirational",
        "conditions": "Dependent on global macro stability and EV adoption curve.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2025-01-29",
            "ratio": 0.40,
            "why": "Vehicle deliveries peaked in 2023 at 1.81M and declined to 1.79M in 2024 (-1% YoY), failing to sustain the 50% compound target by a wide margin.",
            "evidence_quote": "Form 10-K: Total vehicle deliveries were 1,789,226 in 2024 compared to 1,808,581 in 2023.",
            "y": 0.0, "revisions": 2
        }
    }
]
