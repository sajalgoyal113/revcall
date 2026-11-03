"""Guidance commitments and SEC 10-Q/10-K resolutions for Retail, Restaurants & Consumer Goods:
WMT, COST, TGT, HD, NKE, SBUX, MCD.
"""

RETAIL_PROMISES = [
    # -------------------------------------------------------------------------
    # WALMART (WMT)
    # -------------------------------------------------------------------------
    {
        "id": "WMT:2024-02-20#0",
        "ticker": "WMT",
        "call_date": "2024-02-20",
        "call_label": "Q4 FY24 Earnings Call (Feb 20, 2024)",
        "speaker": "John David Rainey",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year FY25 Net sales growth guided 3.0% to 4.0% in constant currency",
        "quote": "For fiscal 2025, we expect consolidated net sales to increase 3.0% to 4.0% in constant currency, and adjusted operating income to increase 4.0% to 6.0%.",
        "value_low": 3.0, "value_high": 4.0, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming steady consumer grocery demand and inflation moderation.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-19",
            "ratio": 1.35,
            "why": "Guidance was steadily raised in May (to 3.75%–4.75%) and in August (to 4.75%–5.25%); delivered Q3 net sales growth of 5.5% CC ($169.6B).",
            "evidence_quote": "John David Rainey (Q3 FY25 Call): Sales grew 5.5% in constant currency, and adjusted operating income increased 8.2%, pacing above our full-year outlook.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "WMT:2024-05-16#0",
        "ticker": "WMT",
        "call_date": "2024-05-16",
        "call_label": "Q1 FY25 Earnings Call (May 16, 2024)",
        "speaker": "Doug McMillon",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Global eCommerce and advertising (Walmart Connect) to maintain 20%+ growth momentum",
        "quote": "Our global eCommerce sales grew 21% led by store-fulfilled pickup and delivery, and global advertising grew 24%. We expect strong double-digit momentum to persist all year.",
        "value_low": 20.0, "value_high": 20.0, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-19",
            "ratio": 1.15,
            "why": "In Q2 global eCommerce grew 21% and in Q3 grew 27%, with Walmart Connect advertising up 26%.",
            "evidence_quote": "Doug McMillon: In Q3, eCommerce was up 27% globally, and our higher-margin advertising business grew 26%, reshaping our operating profit mix.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # COSTCO WHOLESALE (COST)
    # -------------------------------------------------------------------------
    {
        "id": "COST:2024-05-30#0",
        "ticker": "COST",
        "call_date": "2024-05-30",
        "call_label": "Q3 FY24 Earnings Call (May 30, 2024)",
        "speaker": "Gary Millerchip",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Core comparable sales growth of 6% to 8% across warehouse network",
        "quote": "Adjusted core comparable sales were 6.5% in the third quarter. We expect customer traffic and core item volume to sustain mid-single to high-single-digit comps.",
        "value_low": 6.0, "value_high": 8.0, "unit": "%",
        "period": "FY24-Q4", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Excluding the volatile impacts of gasoline prices and foreign exchange fluctuations.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-26",
            "ratio": 1.02,
            "why": "Reported Q4 FY24 adjusted core comp sales growth of 6.9% in Form 10-K, squarely inside the guided range.",
            "evidence_quote": "Form 10-K: Comparable sales excluding the impacts of gasoline prices and foreign exchange increased 6.9% for the 16-week fourth quarter.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "COST:2024-07-10#0",
        "ticker": "COST",
        "call_date": "2024-07-10",
        "call_label": "Special Announcement (Jul 10, 2024)",
        "speaker": "Gary Millerchip",
        "role": "CFO",
        "category": "commercial_milestone",
        "summary": "Annual membership fee increase of $5 for Gold Star and $10 for Executive effective Sept 1, 2024",
        "quote": "Costco will increase annual membership fees by $5 for U.S. and Canada Gold Star, Business, and Business add-on members, and $10 for Executive Members, effective September 1, 2024.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY25-Q1", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "First membership fee hike since June 2017.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-09-01",
            "ratio": 1.0,
            "why": "Implemented seamlessly on September 1, 2024 across 52 million member accounts with zero measurable uptick in cancellations.",
            "evidence_quote": "Gary Millerchip (Q4 FY24 Call): The fee increase took effect on September 1 and renewal rates remain historically strong at 92.9% in North America.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # TARGET (TGT)
    # -------------------------------------------------------------------------
    {
        "id": "TGT:2024-03-05#0",
        "ticker": "TGT",
        "call_date": "2024-03-05",
        "call_label": "Q4 2023 Earnings Call (Mar 5, 2024)",
        "speaker": "Michael Fiddelke",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 Comparable sales expected to increase 0% to 2%",
        "quote": "For the full year, we expect comparable sales to be in a range from a modest increase of 0% to 2%, with operating income margin rate expected between 5.3% and 5.6%.",
        "value_low": 0.0, "value_high": 2.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming gradual recovery in discretionary apparel, home, and electronics spending.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-11-20",
            "ratio": 0.0,
            "why": "In Nov 2024, Target lowered full-year comp guidance to approximately flat (-1% to flat) and cut EPS guidance due to apparel weakness and port strike logistics costs; shares tumbled 21%.",
            "evidence_quote": "Brian Cornell (Q3 2024 Call): We are guiding full-year comparable sales to be roughly flat, reflecting persistent consumer discretionary caution.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "TGT:2024-03-05#1",
        "ticker": "TGT",
        "call_date": "2024-03-05",
        "call_label": "Q4 2023 Earnings Call (Mar 5, 2024)",
        "speaker": "Brian Cornell",
        "role": "CEO",
        "category": "operating_margin",
        "summary": "Full year 2024 Operating income margin rate of 5.3% to 5.6%",
        "quote": "We anticipate operating income margin rate of approximately 5.3% to 5.6% as inventory shrink stabilizes and supply chain efficiencies flow through.",
        "value_low": 5.3, "value_high": 5.6, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-11-20",
            "ratio": 0.84,
            "why": "Reported Q3 2024 operating margin rate of 4.6% (down 60 bps YoY) due to promotional discounting and inventory holding costs.",
            "evidence_quote": "Form 10-Q: Operating income margin was 4.6% in the third quarter of 2024 compared to 5.2% in the prior year.",
            "y": 0.0, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # HOME DEPOT (HD)
    # -------------------------------------------------------------------------
    {
        "id": "HD:2024-02-20#0",
        "ticker": "HD",
        "call_date": "2024-02-20",
        "call_label": "Q4 2023 Earnings Call (Feb 20, 2024)",
        "speaker": "Richard McPhail",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year FY24 Comparable sales expected to decline approximately 1.0%",
        "quote": "For fiscal 2024, we expect comparable sales to decline approximately 1.0%, as higher interest rates and consumer uncertainty continue to pressure larger renovation projects.",
        "value_low": -1.5, "value_high": -0.5, "unit": "%",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to 30-year fixed mortgage rates and existing home turnover volumes.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-08-13",
            "ratio": 0.30,
            "why": "In August 2024, Home Depot lowered full-year comp guidance from -1.0% to -3.0% to -4.0% citing prolonged consumer caution and project deferrals.",
            "evidence_quote": "Richard McPhail (Q2 FY24 Call): We now expect full-year comparable sales to decline between 3.0% and 4.0% as higher interest rates weigh on home improvement demand.",
            "y": 0.25, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # NIKE (NKE)
    # -------------------------------------------------------------------------
    {
        "id": "NKE:2024-03-21#0",
        "ticker": "NKE",
        "call_date": "2024-03-21",
        "call_label": "Q3 FY24 Earnings Call (Mar 21, 2024)",
        "speaker": "Matthew Friend",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year FY25 Revenue and earnings expected to grow year-over-year",
        "quote": "Looking ahead to fiscal 2025, we expect full-year revenue and operating profit to grow year-over-year, supported by our innovation pipeline.",
        "value_low": 1.0, "value_high": 3.0, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming Summer Olympics Paris product launches drive positive consumer footwear momentum.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-06-27",
            "ratio": 0.0,
            "why": "On June 27, 2024, Nike shocked markets by slashing FY25 revenue guidance to down mid-single digits (down ~10% in H1); stock plunged 20% in worst single day in company history.",
            "evidence_quote": "Matthew Friend (Q4 FY24 Call): We now expect fiscal 2025 revenue to be down mid-single digits, reflecting lower wholesale orders and digital traffic declines.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "NKE:2024-06-27#0",
        "ticker": "NKE",
        "call_date": "2024-06-27",
        "call_label": "Q4 FY24 Earnings Call (Jun 27, 2024)",
        "speaker": "John Donahoe",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Management transition and turnaround plan to stabilize classic lifestyle footwear franchises",
        "quote": "We are aggressively managing our classic franchises like Air Force 1, Air Jordan 1, and Dunk, pulling back allocation to create space for performance innovation.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY25-H1", "period_kind": "HALF", "strength": "target",
        "conditions": "Consumer pivot from lifestyle heritage retros to modern running competitors (On, Hoka).",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "ABANDONED",
            "knowable_at": "2024-09-19",
            "ratio": 0.0,
            "why": "Strategy abandoned as CEO John Donahoe stepped down on Sept 19, 2024; incoming CEO Elliott Hill withdrew full-year FY25 guidance entirely on Oct 1.",
            "evidence_quote": "Matthew Friend (Q1 FY25 Call): Given the CEO transition, we are withdrawing our full-year guidance and intend to provide quarterly guidance for the balance of the fiscal year.",
            "y": 0.0, "revisions": 2
        }
    },

    # -------------------------------------------------------------------------
    # STARBUCKS (SBUX)
    # -------------------------------------------------------------------------
    {
        "id": "SBUX:2024-01-30#0",
        "ticker": "SBUX",
        "call_date": "2024-01-30",
        "call_label": "Q1 FY24 Earnings Call (Jan 30, 2024)",
        "speaker": "Rachel Ruggeri",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year FY24 Global comparable store sales guided 4.0% to 6.0%",
        "quote": "For full year fiscal 2024, we are guiding global comparable store sales growth of 4% to 6%, and consolidated revenue growth of 7% to 10%.",
        "value_low": 4.0, "value_high": 6.0, "unit": "%",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming sequential improvement in U.S. occasional customer visits and China stabilization.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-04-30",
            "ratio": 0.0,
            "why": "On April 30, 2024, Starbucks slashed guidance: Q2 comp sales fell 4% in U.S. and 11% in China; full-year comp guidance was cut to negative.",
            "evidence_quote": "Rachel Ruggeri (Q2 FY24 Call): We are lowering our full-year guidance to low single-digit revenue growth and flat to negative comparable store sales.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "SBUX:2024-04-30#0",
        "ticker": "SBUX",
        "call_date": "2024-04-30",
        "call_label": "Q2 FY24 Earnings Call (Apr 30, 2024)",
        "speaker": "Laxman Narasimhan",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Triple Shot Reinvention with Two Pumps turnaround plan to recover store throughput and traffic",
        "quote": "We are executing our Triple Shot Reinvention with Two Pumps strategy to improve store partner experience, increase morning drive-thru speed of service, and reignite traffic.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY24-H2", "period_kind": "HALF", "strength": "aspirational",
        "conditions": "Customer mobile order & pay bottle-necks easing during peak morning windows.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "ABANDONED",
            "knowable_at": "2024-08-13",
            "ratio": 0.0,
            "why": "Strategy abruptly terminated on Aug 13, 2024 as Starbucks fired Laxman Narasimhan and replaced him with Chipotle CEO Brian Niccol to implement 'Back to Starbucks'.",
            "evidence_quote": "Starbucks Press Release (Aug 13, 2024): Brian Niccol appointed Chairman and CEO of Starbucks, bringing proven retail turnaround leadership.",
            "y": 0.0, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # MCDONALD'S (MCD)
    # -------------------------------------------------------------------------
    {
        "id": "MCD:2024-04-30#0",
        "ticker": "MCD",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Chris Kempczinski",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Nationwide launch of $5 Meal Deal in U.S. to restore lower-income diner frequency",
        "quote": "We must be laser-focused on affordability. We are collaborating with our franchisees to launch an entry-level $5 meal deal across our U.S. restaurants this summer.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Summer", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Franchisee cooperative margin subsidy alignment.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-06-25",
            "ratio": 1.0,
            "why": "Launched on June 25, 2024 across 95%+ of U.S. restaurants and extended through December 2024 after lifting value perception.",
            "evidence_quote": "Ian Borden (Q2 2024 Call): The $5 Meal Deal launched in late June and has driven incremental guest counts, especially among lower-income consumers.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MCD:2024-04-30#1",
        "ticker": "MCD",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "Ian Borden",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 Global comparable sales expected to remain positive",
        "quote": "While the consumer environment is pressured, we expect full-year global comparable sales to be positive, supported by menu innovation and value offerings.",
        "value_low": 1.0, "value_high": 3.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to Middle East conflict boycott headwinds and European consumer inflation.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-07-29",
            "ratio": 0.0,
            "why": "Q2 2024 global comp sales turned negative (-1.0% YoY), marking the first quarterly comp decline in 13 quarters.",
            "evidence_quote": "Form 10-Q: Global comparable sales decreased 1.0% in the second quarter of 2024, reflecting negative comps across all three operating segments.",
            "y": 0.0, "revisions": 1
        }
    },
    # -------------------------------------------------------------------------
    # 2025 COMMITMENTS & AUDITED RESOLUTIONS
    # -------------------------------------------------------------------------
    {
        "id": "WMT:2025-02-20#0",
        "ticker": "WMT",
        "call_date": "2025-02-20",
        "call_label": "Q4 FY25 Earnings Call (Feb 20, 2025)",
        "speaker": "John David Rainey",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Q1 FY26 consolidated net sales increase of 3.0% to 4.0% in constant currency",
        "quote": "For the first quarter of fiscal 2026, we expect consolidated net sales to increase 3.0% to 4.0% in constant currency, and operating income to increase 3.5% to 5.5%.",
        "value_low": 3.0, "value_high": 4.0, "unit": "% CC",
        "period": "Q1 FY26", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Assumes approximately 100 bps headwind from lapping the prior year leap day.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-15",
            "ratio": 1.0,
            "why": "Reported Q1 FY26 total constant-currency revenue growth of 4.0% (total revenue $165.6B), meeting the top of the guided range.",
            "evidence_quote": "Form 10-Q: Total revenue grew 2.5% to $165.6 billion, or 4.0% on a constant currency basis, with Walmart U.S. comp sales up 4.5%.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "COST:2025-03-06#0",
        "ticker": "COST",
        "call_date": "2025-03-06",
        "call_label": "Q2 FY25 Earnings Call (Mar 6, 2025)",
        "speaker": "Gary Millerchip",
        "role": "CFO",
        "category": "commercial_milestone",
        "summary": "Full year FY25 warehouse expansion plan of 26 to 29 net new warehouse openings",
        "quote": "We remain on track for our full year warehouse opening plans, targeting between 26 and 29 net new locations globally for fiscal 2025.",
        "value_low": 26.0, "value_high": 29.0, "unit": "Warehouses",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to construction permitting and supply chain equipment delivery.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-29",
            "ratio": 1.0,
            "why": "In Q3 FY25 disclosure, Costco affirmed 27 warehouse openings achieved or in final construction, right in the center of the guided band.",
            "evidence_quote": "Gary Millerchip: Through the third quarter we opened 18 net new warehouses and are tracking toward 28 for the full fiscal year.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "TGT:2025-03-04#0",
        "ticker": "TGT",
        "call_date": "2025-03-04",
        "call_label": "Q4 2024 Earnings Call (Mar 4, 2025)",
        "speaker": "Jim Lee",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q1 2025 comparable sales expected around flat to modestly positive despite profit pressure",
        "quote": "In light of ongoing consumer uncertainty, the Company expects to see meaningful profit pressure in its first quarter, with comparable sales expected around flat to modestly positive.",
        "value_low": 0.0, "value_high": 1.5, "unit": "%",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "cautious",
        "conditions": "Assumes February cold weather impact and discretionary category softness.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2025-05-21",
            "ratio": -0.53,
            "why": "Q1 2025 total comparable sales declined 0.8% (store comps down 1.8%), failing to achieve the flat-to-positive expectation due to apparel weakness.",
            "evidence_quote": "Brian Cornell: Digital comps grew nearly 5% led by same-day delivery, though total comparable sales declined 0.8% due to soft apparel store traffic.",
            "y": 0.0, "revisions": 1
        }
    },
    {
        "id": "HD:2025-02-25#0",
        "ticker": "HD",
        "call_date": "2025-02-25",
        "call_label": "Q4 2024 Earnings Call (Feb 25, 2025)",
        "speaker": "Richard McPhail",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Fiscal 2025 total sales growth of approximately 2.8% and comparable sales growth of approximately 1.0%",
        "quote": "For fiscal 2025, we expect total sales growth of approximately 2.8%, comparable sales growth of approximately 1.0%, and operating margin of approximately 13.0%.",
        "value_low": 2.0, "value_high": 3.5, "unit": "%",
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes gradual stabilization in the housing turnover cycle.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-20",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, Home Depot reported total sales up 2.9% and reaffirmed full-year sales and comp guidance.",
            "evidence_quote": "Ted Decker: First quarter results were in line with our expectations, and we are reaffirming our guidance for total sales growth of approximately 2.8%.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "NKE:2025-03-20#0",
        "ticker": "NKE",
        "call_date": "2025-03-20",
        "call_label": "Q3 FY25 Earnings Call (Mar 20, 2025)",
        "speaker": "Matthew Friend",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year FY25 revenue guidance lowered to down high-single-digits with Q4 revenue down low-double-digits",
        "quote": "We now expect Q4 to reflect the largest impact from these Win Now actions, with reported revenue down low-double-digits as we aggressively right-size Classic inventory.",
        "value_low": -14.0, "value_high": -10.0, "unit": "% YoY",
        "period": "Q4 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Intentional suppression of retro Air Force 1 and Dunk shipments to rebuild market pull.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2025-06-26",
            "ratio": 0.60,
            "why": "Full-year revenue guidance was cut from down mid-single-digits to down 9%, as wholesale cancellations and classic franchise clearance weighed heavily on revenues.",
            "evidence_quote": "Form 10-Q: Full-year revenues declined 9% reported, driven by a 12% drop in Q4 as the company restructured its wholesale channel and curtailed inventory.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "SBUX:2025-01-28#0",
        "ticker": "SBUX",
        "call_date": "2025-01-28",
        "call_label": "Q1 FY25 Earnings Call (Jan 28, 2025)",
        "speaker": "Brian Niccol",
        "role": "CEO",
        "category": "operational_target",
        "summary": "Suspension of full year fiscal 2025 financial guidance to execute multi-year Back to Starbucks turnaround",
        "quote": "Given our CEO transition and the current state of the business, we are suspending our full year fiscal 2025 financial guidance to focus entirely on our Back to Starbucks plan.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "FY25", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Requires operational overhaul of store staffing, condiment bars, and drink sequencing.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "ABANDONED",
            "knowable_at": "2025-01-28",
            "ratio": 0.0,
            "why": "Official withdrawal and abandonment of full-year revenue and margin guidance amidst a 4% drop in global comparable store sales and 8% traffic drop.",
            "evidence_quote": "Rachel Ruggeri: We believe it is prudent to suspend our full-year guidance for fiscal 2025 as we refocus our investments on customer experience and store operations.",
            "y": 0.0, "revisions": 1
        }
    },
    {
        "id": "MCD:2025-02-10#0",
        "ticker": "MCD",
        "call_date": "2025-02-10",
        "call_label": "Q4 2024 Earnings Call (Feb 10, 2025)",
        "speaker": "Ian Borden",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2025 operating margin to land in the mid-to-high 40% range",
        "quote": "For the full year 2025, we expect operating margin to be in the mid-to-high 40% range, driven by top-line systemwide sales recovery and franchise performance.",
        "value_low": 45.0, "value_high": 49.0, "unit": "%",
        "period": "2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to consumer value platform adoption and international market stabilization.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-30",
            "ratio": 1.0,
            "why": "Reported Q1 2025 operating margin of 46.8%, tracking directly within the guided mid-to-high 40% band.",
            "evidence_quote": "Form 10-Q: Operating margin was 46.8% for the first quarter of 2025, supported by restaurant margin expansion across franchised markets.",
            "y": 1.0, "revisions": 0
        }
    }
]
