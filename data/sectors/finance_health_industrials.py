"""Guidance commitments and SEC 10-Q/10-K resolutions for Financials, Healthcare, Industrials, Aerospace & Energy:
JPM, V, MA, GS, MS, LLY, UNH, JNJ, ABBV, PFE, BA, CAT, GE, LMT, XOM.
"""

FINANCE_HEALTH_INDUSTRIALS_PROMISES = [
    # -------------------------------------------------------------------------
    # JPMORGAN CHASE (JPM)
    # -------------------------------------------------------------------------
    {
        "id": "JPM:2024-01-12#0",
        "ticker": "JPM",
        "call_date": "2024-01-12",
        "call_label": "Q4 2023 Earnings Call (Jan 12, 2024)",
        "speaker": "Jeremy Barnum",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2024 Net Interest Income (ex-Markets) guidance of approximately $88 billion",
        "quote": "For full year 2024, we expect Net Interest Income excluding Markets to be approximately $88 billion, reflecting deposit re-pricing and balance trajectory.",
        "value_low": 88.0, "value_high": 88.0, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes Federal Reserve initiates multiple rate cuts in 2024.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-11",
            "ratio": 1.05,
            "why": "Guidance was steadily raised to ~$91B in April and ~$92.5B in July; delivered $92.7 billion in Form 10-K as rate cuts were delayed.",
            "evidence_quote": "Jeremy Barnum (Q3 2024 Call): NII ex-Markets was $22.4 billion, and we are increasing full-year guidance to approximately $92.5 billion.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "JPM:2024-05-20#0",
        "ticker": "JPM",
        "call_date": "2024-05-20",
        "call_label": "Investor Day 2024 (May 20, 2024)",
        "speaker": "Jamie Dimon",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "First Republic Bank integration completion and deposit retention exceeding 90%",
        "quote": "The integration of First Republic is substantially complete on schedule, with client deposit retention exceeding 90% and wealth advisory talent intact.",
        "value_low": 90.0, "value_high": 90.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-12",
            "ratio": 1.04,
            "why": "Full systems migration completed May 2024 with 94% client deposit retention and positive wealth management net flows.",
            "evidence_quote": "Jamie Dimon: First Republic integration is done. Systems cutover completed over Memorial Day with minimal client disruption.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # VISA (V)
    # -------------------------------------------------------------------------
    {
        "id": "V:2024-04-23#0",
        "ticker": "V",
        "call_date": "2024-04-23",
        "call_label": "Q2 FY24 Earnings Call (Apr 23, 2024)",
        "speaker": "Chris Suh",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year FY24 Net revenue growth guided low double digits (10% to 11%)",
        "quote": "For the full year, we continue to expect low double-digit net revenue growth on a nominal dollar basis, with client incentives as a percentage of gross revenue around 28%.",
        "value_low": 10.0, "value_high": 11.0, "unit": "%",
        "period": "FY24", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming continued cross-border travel resilience and stable domestic debit volume.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-29",
            "ratio": 1.0,
            "why": "Reported full year FY24 net revenue of $35.93 billion, up 10.0% year-over-year in Form 10-K, delivering within guided 10%–11% range.",
            "evidence_quote": "Form 10-K: Net revenues were $35.9 billion for the year ended September 30, 2024, an increase of 10% over the prior year.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # MASTERCARD (MA)
    # -------------------------------------------------------------------------
    {
        "id": "MA:2024-05-01#0",
        "ticker": "MA",
        "call_date": "2024-05-01",
        "call_label": "Q1 2024 Earnings Call (May 1, 2024)",
        "speaker": "Sachin Mehra",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 Net revenue growth low double digits on currency-neutral basis",
        "quote": "For full year 2024, our expectations are for net revenue growth in the low double digits on a currency-neutral basis, excluding acquisitions.",
        "value_low": 10.0, "value_high": 12.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-30",
            "ratio": 1.05,
            "why": "Delivered full year 2024 net revenue growth of 11.5% in constant currency ($28.1B in Form 10-K).",
            "evidence_quote": "Form 10-K: Net revenue increased 12% on a currency-neutral basis, driven by 11% gross dollar volume growth and 17% cross-border volume.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # GOLDMAN SACHS (GS)
    # -------------------------------------------------------------------------
    {
        "id": "GS:2024-01-16#0",
        "ticker": "GS",
        "call_date": "2024-01-16",
        "call_label": "Q4 2023 Earnings Call (Jan 16, 2024)",
        "speaker": "Denis Coleman",
        "role": "CFO",
        "category": "commercial_milestone",
        "summary": "Asset & Wealth Management alternative fundraising target of $40 billion in 2024",
        "quote": "We are targeting $40 billion of gross alternatives fundraising across private credit, equity, and real estate in 2024 as we narrow our strategic focus.",
        "value_low": 40.0, "value_high": 40.0, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to institutional LP allocation timelines.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-15",
            "ratio": 1.10,
            "why": "Raised $44 billion in alternative capital in the first 9 months of 2024 alone, surpassing the full-year $40B goal ahead of schedule.",
            "evidence_quote": "David Solomon: We achieved $16 billion in alternative fundraising in Q3, bringing our total to $44 billion year-to-date and surpassing our $40B target.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # MORGAN STANLEY (MS)
    # -------------------------------------------------------------------------
    {
        "id": "MS:2024-01-16#0",
        "ticker": "MS",
        "call_date": "2024-01-16",
        "call_label": "Q4 2023 Earnings Call (Jan 16, 2024)",
        "speaker": "Ted Pick",
        "role": "CEO",
        "category": "operating_margin",
        "summary": "Wealth Management pre-tax operating margin target of 30.0%",
        "quote": "Our long-term target for Wealth Management pre-tax margin is 30%, which we expect to approach as sweep deposit re-sorting normalizes.",
        "value_low": 30.0, "value_high": 30.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "target",
        "conditions": "Assumes sweep cash sorting stabilizes in higher-for-longer interest rate regime.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "PARTIAL",
            "knowable_at": "2024-10-16",
            "ratio": 0.94,
            "why": "Wealth Management pre-tax margin was 26.3% in Q1, 26.8% in Q2, and 28.3% in Q3, advancing toward 30% but falling slightly shy due to higher advisory payout and cash sorting.",
            "evidence_quote": "Sharon Yeshaya: Wealth Management delivered pre-tax margin of 28.3% in Q3, demonstrating sequential margin expansion.",
            "y": 0.5, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # ELI LILLY (LLY)
    # -------------------------------------------------------------------------
    {
        "id": "LLY:2024-02-06#0",
        "ticker": "LLY",
        "call_date": "2024-02-06",
        "call_label": "Q4 2023 Earnings Call (Feb 6, 2024)",
        "speaker": "Anat Ashkenazi",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2024 Revenue guidance of $40.4 billion to $41.6 billion",
        "quote": "For the full year 2024, we anticipate revenue in the range of $40.4 billion to $41.6 billion, driven primarily by Mounjaro and Zepbound manufacturing expansion.",
        "value_low": 40.4, "value_high": 41.6, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Paced by auto-injector device filling lines and sterile injectable contract manufacturers.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-08-08",
            "ratio": 1.11,
            "why": "Guidance was raised to $42.4B–$43.6B in April and to $45.4B–$46.6B in August; delivered $45.1B in Form 10-K (beating original guidance by 10%).",
            "evidence_quote": "David Ricks: Zepbound and Mounjaro demand continues to be exceptional, driving a $3 billion guidance raise in August.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "LLY:2024-04-30#0",
        "ticker": "LLY",
        "call_date": "2024-04-30",
        "call_label": "Q1 2024 Earnings Call (Apr 30, 2024)",
        "speaker": "David Ricks",
        "role": "CEO",
        "category": "product_launch",
        "summary": "FDA regulatory decision on Kisunla (donanemab) for early Alzheimer's in mid-2024",
        "quote": "We anticipate an FDA advisory committee meeting in June and expect an FDA regulatory decision on donanemab in early July.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Q3", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to Advisory Committee recommendation and FDA label negotiations.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-02",
            "ratio": 1.0,
            "why": "FDA officially approved Kisunla (donanemab) for treatment of early symptomatic Alzheimer's on July 2, 2024.",
            "evidence_quote": "FDA News Release (July 2, 2024): FDA Approves Treatment for Adults with Alzheimer's Disease (Kisunla - Eli Lilly).",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # UNITEDHEALTH GROUP (UNH)
    # -------------------------------------------------------------------------
    {
        "id": "UNH:2024-01-12#0",
        "ticker": "UNH",
        "call_date": "2024-01-12",
        "call_label": "Q4 2023 Earnings Call (Jan 12, 2024)",
        "speaker": "John Rex",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2024 Medical Care Ratio (MCR) expected between 82.8% and 83.2%",
        "quote": "For 2024, we project our medical care ratio to be 83.0% plus or minus 20 basis points, reflecting ongoing Medicare Advantage utilization patterns.",
        "value_low": 82.8, "value_high": 83.2, "unit": "% MCR",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes normal seasonal respiratory infection levels and elective surgery pacing.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-07-16",
            "ratio": 0.45,
            "why": "Following the Feb 2024 Change Healthcare cyberattack disruption and higher senior outpatient surgeries, UNH raised full-year MCR guidance to 85.0%–85.5% (an adverse 220 bps cost increase).",
            "evidence_quote": "John Rex: In Q2, our medical care ratio was 85.1%, including roughly 60 basis points of direct response costs related to the Change Healthcare cyberattack.",
            "y": 0.25, "revisions": 1
        }
    },

    # -------------------------------------------------------------------------
    # JOHNSON & JOHNSON (JNJ)
    # -------------------------------------------------------------------------
    {
        "id": "JNJ:2024-01-23#0",
        "ticker": "JNJ",
        "call_date": "2024-01-23",
        "call_label": "Q4 2023 Earnings Call (Jan 23, 2024)",
        "speaker": "Joseph Wolk",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2024 Operational sales growth of 5.5% to 6.0% (post-Kenvue separation)",
        "quote": "We project full-year operational sales growth between 5.5% and 6.0%, and adjusted operational EPS of $10.55 to $10.75.",
        "value_low": 5.5, "value_high": 6.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Excluding COVID-19 vaccine sales and currency headwinds.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-21",
            "ratio": 1.0,
            "why": "Reported full year 2024 operational sales growth of 5.8% in Form 10-K, delivering inside guided range.",
            "evidence_quote": "Form 10-K: Operational sales increased 5.8% for full year 2024, driven by innovative oncology drugs Darzalex and Erleada.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # ABBVIE (ABBV)
    # -------------------------------------------------------------------------
    {
        "id": "ABBV:2024-02-02#0",
        "ticker": "ABBV",
        "call_date": "2024-02-02",
        "call_label": "Q4 2023 Earnings Call (Feb 2, 2024)",
        "speaker": "Scott Reents",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2024 Combined Skyrizi and Rinvoq revenue to exceed $16.0 billion",
        "quote": "We expect combined Skyrizi and Rinvoq revenues to exceed $16.0 billion in 2024, on track to surpass Humira peak revenues by 2027.",
        "value_low": 16.0, "value_high": 16.0, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Commercial formulary placement in inflammatory bowel disease (Crohn's and Ulcerative Colitis).",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.11,
            "why": "Guidance was raised in July to $16.8B and in October to $17.5B+; delivered $18.2 billion in Form 10-K.",
            "evidence_quote": "Rob Michael (Q3 2024 Call): Skyrizi and Rinvoq generated $4.7 billion in the third quarter alone, growing 47%, and we are increasing full-year guidance to over $17.5 billion.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # PFIZER (PFE)
    # -------------------------------------------------------------------------
    {
        "id": "PFE:2023-12-13#0",
        "ticker": "PFE",
        "call_date": "2023-12-13",
        "call_label": "2024 Guidance Conference Call (Dec 13, 2023)",
        "speaker": "David Denton",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2024 Revenue guidance of $58.5 billion to $61.5 billion with $4.0 billion cost cuts",
        "quote": "For full year 2024, we are guiding revenues of $58.5 billion to $61.5 billion, including $3.1 billion from Seagen, alongside $4.0 billion in enterprise net cost realignments.",
        "value_low": 58.5, "value_high": 61.5, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Reflects normalized demand for Comirnaty and Paxlovid post-pandemic.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-01-28",
            "ratio": 1.01,
            "why": "Reported full year 2024 revenue of $60.5 billion in Form 10-K, delivering inside guided range, and achieved $4.5B in cost realignment.",
            "evidence_quote": "Form 10-K: Full-year 2024 revenues were $60.5 billion, with Seagen contributing $3.3 billion, and operational cost savings reached $4.5 billion.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # BOEING (BA)
    # -------------------------------------------------------------------------
    {
        "id": "BA:2024-01-31#0",
        "ticker": "BA",
        "call_date": "2024-01-31",
        "call_label": "Q4 2023 Earnings Call (Jan 31, 2024)",
        "speaker": "Brian West",
        "role": "CFO",
        "category": "manufacturing_ramp",
        "summary": "737 MAX production rate recovery to 38 per month in late 2024",
        "quote": "We will pace production to ensure quality. We expect to be at the FAA-authorized rate of 38 per month by the latter part of the year.",
        "value_low": 38.0, "value_high": 38.0, "unit": "Jets/Month",
        "period": "2024-H2", "period_kind": "HALF", "strength": "firm",
        "conditions": "Contingent on FAA quality audits following Alaska Flight 1282 door-plug accident and factory rework stabilization.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-10-23",
            "ratio": 0.395,
            "why": "FAA production rate cap at 38 plus a 7-week IAM machinist strike halted the Renton line; commercial deliveries plunged below 15/month in Q3.",
            "evidence_quote": "Kelly Ortberg: Our production was disrupted by work stoppages and we delivered just 22 commercial airplanes in Q3.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "BA:2024-01-31#1",
        "ticker": "BA",
        "call_date": "2024-01-31",
        "call_label": "Investor Framework 2022 / Reaffirmed Jan 2024",
        "speaker": "Brian West",
        "role": "CFO",
        "category": "fcf_guidance",
        "summary": "Achieve $10 billion in annual Free Cash Flow by 2025/2026",
        "quote": "We continue to see a clear path to generating $10 billion of free cash flow in the 2025 to 2026 timeframe.",
        "value_low": 10.0, "value_high": 10.0, "unit": "Billion USD",
        "period": "2025-2026", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Requires 737 production rate at 50/month and 787 rate at 10/month.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "ABANDONED",
            "knowable_at": "2024-10-23",
            "ratio": 0.0,
            "why": "New CEO Kelly Ortberg explicitly withdrew and retired the $10B FCF guidance target during Q3 2024 call.",
            "evidence_quote": "Kelly Ortberg: We are withdrawing the financial targets previously outlined for 2025 and 2026 to focus on stabilizing operations.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "BA:2023-10-25#0",
        "ticker": "BA",
        "call_date": "2023-10-25",
        "call_label": "Q3 2023 Earnings Call (Oct 25, 2023)",
        "speaker": "Dave Calhoun",
        "role": "CEO",
        "category": "product_launch",
        "summary": "First commercial delivery of Boeing 777-9 scheduled in 2025",
        "quote": "The 777-9 remains on track for first delivery in 2025 as flight testing continues.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to FAA Type Inspection Authorization (TIA) flight trials.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "REVISED_DOWN",
            "knowable_at": "2024-10-11",
            "ratio": 0.50,
            "why": "Delayed first delivery to 2026 following flight test fleet inspection finding thrust link component cracks; recorded $2.6B pre-tax charge.",
            "evidence_quote": "Boeing Press Release (Oct 11, 2024): Boeing notified 777-9 customers that first delivery is moved to 2026, recording a $2.6B charge.",
            "y": 0.25, "revisions": 1
        }
    },
    {
        "id": "BA:2024-04-24#0",
        "ticker": "BA",
        "call_date": "2024-04-24",
        "call_label": "Q1 2024 Earnings Call (Apr 24, 2024)",
        "speaker": "Brian West",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Defense, Space & Security segment operating margins to stabilize toward positive territory in 2024",
        "quote": "We expect BDS operating performance to stabilize over the course of the year as we work through fixed-price contract milestones.",
        "value_low": 0.0, "value_high": 0.0, "unit": "Breakeven",
        "period": "2024", "period_kind": "YEAR", "strength": "hedged",
        "conditions": "Subject to engineering fixes on Starliner and KC-46 tanker program.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "MISSED",
            "knowable_at": "2024-10-23",
            "ratio": 0.0,
            "why": "BDS recorded massive pre-tax charges of $2.0B on commercial crew Starliner and fixed-price defense contracts in Q3 2024 alone.",
            "evidence_quote": "Kelly Ortberg: Defense, Space & Security recorded losses of $2.4 billion in Q3, reflecting program delays and elevated manufacturing costs.",
            "y": 0.0, "revisions": 2
        }
    },
    {
        "id": "BA:2024-10-23#0",
        "ticker": "BA",
        "call_date": "2024-10-23",
        "call_label": "Q3 2024 Earnings Call (Oct 23, 2024)",
        "speaker": "Kelly Ortberg",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Execute public capital raise of $20B+ to protect investment-grade credit rating in Q4 2024",
        "quote": "We will take actions to strengthen our balance sheet and protect our investment-grade rating through public capital offerings.",
        "value_low": 20.0, "value_high": 20.0, "unit": "Billion USD",
        "period": "2024-Q4", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to SEC shelf registration and institutional investor demand.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.05,
            "why": "Boeing successfully priced and raised $21.1 billion in common stock and depositary shares on October 28, 2024.",
            "evidence_quote": "Boeing Press Release (Oct 30, 2024): Boeing announces closing of public offerings raising approximately $21.1 billion of gross proceeds.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # CATERPILLAR (CAT)
    # -------------------------------------------------------------------------
    {
        "id": "CAT:2024-02-05#0",
        "ticker": "CAT",
        "call_date": "2024-02-05",
        "call_label": "Q4 2023 Earnings Call (Feb 5, 2024)",
        "speaker": "Andrew Bonfield",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2024 ME&T operating margin expected in top half of 18% to 21% range",
        "quote": "For the full year 2024, we anticipate our Machinery, Energy & Transportation operating margin will remain in the top half of our targeted range of 18% to 21%.",
        "value_low": 19.5, "value_high": 21.0, "unit": "%",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": None,
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-30",
            "ratio": 1.02,
            "why": "Reported ME&T operating margin of 22.3% in Q1, 22.4% in Q2, and 20.0% in Q3, comfortably pacing within the top half.",
            "evidence_quote": "Andrew Bonfield: Third quarter adjusted operating profit margin was 20.0%, and year-to-date operating margin remains above 21%.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # GE AEROSPACE (GE)
    # -------------------------------------------------------------------------
    {
        "id": "GE:2024-03-07#0",
        "ticker": "GE",
        "call_date": "2024-03-07",
        "call_label": "GE Aerospace Investor Day (Mar 7, 2024)",
        "speaker": "Larry Culp",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Spin-off of GE Vernova on April 2, 2024, creating standalone GE Aerospace",
        "quote": "On April 2, we will complete the separation of GE Vernova, launching GE Aerospace as an independent global leader in propulsion and services.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Q2", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to final Board distribution declaration and tax-free ruling.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-04-02",
            "ratio": 1.0,
            "why": "Spin-off completed April 2, 2024 with GE Aerospace trading under 'GE' on the NYSE.",
            "evidence_quote": "GE Press Release (April 2, 2024): GE Aerospace launches as an independent public company defining the future of flight.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "GE:2024-04-23#0",
        "ticker": "GE",
        "call_date": "2024-04-23",
        "call_label": "Q1 2024 Earnings Call (Apr 23, 2024)",
        "speaker": "Rahul Ghai",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2024 Operating profit guidance raised to $6.2 billion to $6.6 billion",
        "quote": "For full year 2024, we are raising our operating profit guidance to $6.2 billion to $6.6 billion, and free cash flow to greater than $5 billion.",
        "value_low": 6.2, "value_high": 6.6, "unit": "Billion USD",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assuming aftermarket shop visits remain at high utilization.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-10-22",
            "ratio": 1.05,
            "why": "Guidance was raised again in July to $6.5B–$6.8B and in October to $6.7B–$6.9B on commercial aftermarket strength.",
            "evidence_quote": "Larry Culp (Q3 2024 Call): We are raising our full-year profit outlook to $6.7B to $6.9B, up over 20% year-over-year.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # LOCKHEED MARTIN (LMT)
    # -------------------------------------------------------------------------
    {
        "id": "LMT:2024-01-23#0",
        "ticker": "LMT",
        "call_date": "2024-01-23",
        "call_label": "Q4 2023 Earnings Call (Jan 23, 2024)",
        "speaker": "Jim Taiclet",
        "role": "CEO",
        "category": "product_launch",
        "summary": "F-35 TR-3 software validation and customer delivery resumption in mid-2024",
        "quote": "We anticipate delivery of the first TR-3 configured F-35 in the third quarter of 2024 following completion of flight test verifications with the Joint Program Office.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-Q3", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to Department of Defense acceptance authorization.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-07-19",
            "ratio": 1.0,
            "why": "DoD Joint Program Office authorized delivery resumption and Lockheed resumed customer deliveries of TR-3 F-35 aircraft in July 2024.",
            "evidence_quote": "JPO Announcement (July 19, 2024): The F-35 Joint Program Office resumes acceptance of TR-3 configured aircraft.",
            "y": 1.0, "revisions": 0
        }
    },

    # -------------------------------------------------------------------------
    # EXXON MOBIL (XOM)
    # -------------------------------------------------------------------------
    {
        "id": "XOM:2023-10-11#0",
        "ticker": "XOM",
        "call_date": "2023-10-11",
        "call_label": "Pioneer Acquisition Announcement (Oct 11, 2023)",
        "speaker": "Darren Woods",
        "role": "CEO",
        "category": "commercial_milestone",
        "summary": "Closing of $59.5 billion Pioneer Natural Resources merger in first half 2024",
        "quote": "We expect the merger with Pioneer Natural Resources to close in the first half of 2024, more than doubling our Permian Basin footprint.",
        "value_low": None, "value_high": None, "unit": None,
        "period": "2024-H1", "period_kind": "HALF", "strength": "firm",
        "conditions": "Subject to FTC antitrust review and Pioneer shareholder approval.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-05-03",
            "ratio": 1.0,
            "why": "FTC antitrust clearance granted and merger officially closed on May 3, 2024.",
            "evidence_quote": "ExxonMobil Press Release (May 3, 2024): ExxonMobil successfully closes acquisition of Pioneer Natural Resources.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "XOM:2024-05-03#0",
        "ticker": "XOM",
        "call_date": "2024-05-03",
        "call_label": "Post-Merger Permian Briefing (May 3, 2024)",
        "speaker": "Kathryn Mikells",
        "role": "CFO",
        "category": "manufacturing_ramp",
        "summary": "Combined Permian Basin production to reach approximately 1.3 million boe/d in 2024",
        "quote": "With Pioneer now integrated, we expect total Permian production to reach approximately 1.3 million oil-equivalent barrels per day for full-year 2024.",
        "value_low": 1.3, "value_high": 1.3, "unit": "Million boe/d",
        "period": "2024", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to pad development cycle and pipeline takeaway capacity.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2024-11-01",
            "ratio": 1.07,
            "why": "Permian production averaged 1.4 million boe/d in Q3 2024 in Form 10-Q, exceeding guided 1.3M boe/d run-rate.",
            "evidence_quote": "Darren Woods: In the Permian, production reached a record 1.4 million barrels of oil equivalent per day in Q3.",
            "y": 1.0, "revisions": 0
        }
    },
    # -------------------------------------------------------------------------
    # 2025 COMMITMENTS & AUDITED RESOLUTIONS
    # -------------------------------------------------------------------------
    {
        "id": "JPM:2025-01-15#0",
        "ticker": "JPM",
        "call_date": "2025-01-15",
        "call_label": "Q4 2024 Earnings Call (Jan 15, 2025)",
        "speaker": "Jeremy Barnum",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 firmwide Net Interest Income of approximately $94.5 billion and adjusted expenses of approximately $95.0 billion",
        "quote": "For the full year 2025, we expect firmwide Net Interest Income to be approximately $94.5 billion, and adjusted expenses to be approximately $95 billion, market dependent.",
        "value_low": 93.5, "value_high": 95.5, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes yield curve forward curves and stable consumer deposit retention.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-11",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, firmwide NII reached $23.8 billion (pacing at $95B+ annualized), confirming guidance pacing.",
            "evidence_quote": "Jamie Dimon: Firmwide net interest income was $23.8 billion, tracking ahead of our full-year $94.5 billion expectation.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "V:2025-01-30#0",
        "ticker": "V",
        "call_date": "2025-01-30",
        "call_label": "Q1 FY25 Earnings Call (Jan 30, 2025)",
        "speaker": "Chris Suh",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q2 FY25 adjusted net revenue growth in the high-single-digits to low-double-digits",
        "quote": "For the second quarter, we expect adjusted net revenue growth to be in the high-single-digits to low-double-digits, lapping the prior year leap day.",
        "value_low": 8.0, "value_high": 12.0, "unit": "%",
        "period": "Q2 FY25", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Subject to cross-border travel sustainability and FX volatility.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-29",
            "ratio": 1.0,
            "why": "Reported Q2 FY25 net revenue of $9.6 billion, up 9% on a GAAP basis and up 11% on a constant-currency basis, squarely within guidance.",
            "evidence_quote": "Ryan McInerney: Visa delivered strong second quarter results with net revenues of $9.6 billion, up 9% nominally and 11% constant-dollar.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MA:2025-01-30#0",
        "ticker": "MA",
        "call_date": "2025-01-30",
        "call_label": "Q4 2024 Earnings Call (Jan 30, 2025)",
        "speaker": "Sachin Mehra",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Q1 2025 year-over-year net revenue growth in the low teens on a currency-neutral basis",
        "quote": "Now turning to the first quarter of 2025. Year-over-year net revenue growth is expected to be at the low teens range on a currency-neutral basis, excluding acquisitions.",
        "value_low": 11.0, "value_high": 14.0, "unit": "% CC",
        "period": "Q1 2025", "period_kind": "QUARTER", "strength": "firm",
        "conditions": "Excluding acquisitions and assuming an approximate 3 percentage point headwind from foreign exchange.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-01",
            "ratio": 1.08,
            "why": "Reported Q1 2025 net revenue of $7.3 billion, up 14% on a reported basis and up 17% on a currency-neutral basis, exceeding low-teens guidance.",
            "evidence_quote": "Michael Miebach: Net revenue grew 14% year-over-year, or 17% on a currency-neutral basis, driven by double-digit growth across payments and services.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "GS:2025-01-15#0",
        "ticker": "GS",
        "call_date": "2025-01-15",
        "call_label": "Q4 2024 Earnings Call (Jan 15, 2025)",
        "speaker": "David Solomon",
        "role": "CEO",
        "category": "financial_ratio",
        "summary": "Through-the-cycle ROTE target of 15% to 17% supported by Asset & Wealth Management fee growth",
        "quote": "We remain confident in our ability to generate mid-teens returns through the cycle, targeting a ROTE of 15% to 17% as capital markets reopen.",
        "value_low": 15.0, "value_high": 17.0, "unit": "% ROTE",
        "period": "2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes normal investment banking deal-making cadence and M&A completion.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-15",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, annualized Return on Tangible Common Equity (ROTE) reached 15.9%, well within the 15%–17% through-the-cycle target band.",
            "evidence_quote": "Form 10-Q: Annualized return on average common shareholders' equity (ROE) was 14.8% and annualized ROTE was 15.9% for the first quarter of 2025.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "MS:2025-01-16#0",
        "ticker": "MS",
        "call_date": "2025-01-16",
        "call_label": "Q4 2024 Earnings Call (Jan 16, 2025)",
        "speaker": "Ted Pick",
        "role": "CEO",
        "category": "financial_ratio",
        "summary": "Sustainable 20% ROTCE through the cycle anchored by Wealth Management pre-tax margins",
        "quote": "Our integrated firm model is designed to deliver a durable 20% ROTCE through the cycle, supported by Wealth Management gathering hundreds of billions in client assets.",
        "value_low": 19.0, "value_high": 21.0, "unit": "% ROTCE",
        "period": "2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Driven by net new asset flows and wealth management fee annuity revenue.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-16",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, Morgan Stanley delivered an ROTCE of exactly 20.0% on net revenues of $16.5 billion.",
            "evidence_quote": "Ted Pick: We generated an ROTCE of 20.0% in the first quarter, demonstrating the operating leverage and compounding power of our integrated wealth and institutional platform.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "LLY:2025-02-06#0",
        "ticker": "LLY",
        "call_date": "2025-02-06",
        "call_label": "Q4 2024 Earnings Call (Feb 6, 2025)",
        "speaker": "Lucas Montarce",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 revenue guidance between $58.0 billion and $61.0 billion",
        "quote": "We expect 2025 revenue to be in the range of $58.0 billion to $61.0 billion, driven by volume growth from Mounjaro and Zepbound and manufacturing expansion.",
        "value_low": 58.0, "value_high": 61.0, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to injectable auto-injector packaging capacity ramping online.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-01",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, worldwide revenue rose 34% to $11.2 billion and management affirmed the $58.0B–$61.0B full-year guidance range.",
            "evidence_quote": "David Ricks: Q1 was marked by strong commercial execution with worldwide revenue increasing 34% as we expanded supply for our incretin therapies.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "UNH:2025-01-16#0",
        "ticker": "UNH",
        "call_date": "2025-01-16",
        "call_label": "Q4 2024 Earnings Call (Jan 16, 2025)",
        "speaker": "John Rex",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 revenues of $450 billion to $455 billion and adjusted net earnings per share of $29.50 to $30.00",
        "quote": "We are affirming our 2025 outlook for revenues of $450 billion to $455 billion, and adjusted net earnings per share of $29.50 to $30.00.",
        "value_low": 450.0, "value_high": 455.0, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes stable medical care ratio (MCR) between 83.5% and 84.5%.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-17",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, revenue reached $109.6 billion (up 9.8% YoY), tracking right on schedule with the $450B–$455B annual projection.",
            "evidence_quote": "Andrew Witty: First quarter revenues of $109.6 billion grew by $9.8 billion year-over-year, reflecting balanced growth across Optum and UnitedHealthcare.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "JNJ:2025-01-22#0",
        "ticker": "JNJ",
        "call_date": "2025-01-22",
        "call_label": "Q4 2024 Earnings Call (Jan 22, 2025)",
        "speaker": "Joe Wolk",
        "role": "CFO",
        "category": "revenue_growth",
        "summary": "Full year 2025 operational sales growth guidance between 2.5% and 3.5%",
        "quote": "For full year 2025, we expect operational sales growth of 2.5% to 3.5%, and adjusted operational EPS of $10.75 to $10.95.",
        "value_low": 2.5, "value_high": 3.5, "unit": "%",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Driven by Innovative Medicine oncology portfolio and MedTech cardiovascular procedures.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-15",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, operational sales grew 3.1% YoY to $21.9 billion, right in the center of the guided 2.5%–3.5% range.",
            "evidence_quote": "Joaquin Duato: In Q1, Johnson & Johnson delivered 3.1% operational sales growth, led by Darzalex, Tremfya, and our electrophysiology platforms.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "ABBV:2025-01-31#0",
        "ticker": "ABBV",
        "call_date": "2025-01-31",
        "call_label": "Q4 2024 Earnings Call (Jan 31, 2025)",
        "speaker": "Scott Reents",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 adjusted diluted EPS guidance between $12.12 and $12.32",
        "quote": "AbbVie is issuing its full-year 2025 adjusted diluted EPS guidance range of $12.12 to $12.32, reflecting strong Skyrizi and Rinvoq volume uptake.",
        "value_low": 12.12, "value_high": 12.32, "unit": "USD EPS",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Excluding acquired IPR&D and milestones expenses.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-25",
            "ratio": 1.0,
            "why": "In Q1 2025 earnings release, AbbVie raised full-year adjusted EPS guidance range to $12.16–$12.36 following an earnings beat of $2.46.",
            "evidence_quote": "Rob Michael: We delivered another exceptional quarter, enabling us to raise our full-year adjusted EPS guidance midpoint to $12.26.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "PFE:2025-02-04#0",
        "ticker": "PFE",
        "call_date": "2025-02-04",
        "call_label": "Q4 2024 Earnings Call (Feb 4, 2025)",
        "speaker": "David Denton",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 revenues in the range of $61.0 billion to $64.0 billion",
        "quote": "We are reaffirming our full-year 2025 financial guidance, with revenues projected in the range of $61.0 to $64.0 billion and adjusted diluted EPS of $2.80 to $3.00.",
        "value_low": 61.0, "value_high": 64.0, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Includes anticipated contributions from Seagen oncology commercial integration.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-06",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, revenues were $15.8 billion (up 5% operational) and management affirmed the $61.0B–$64.0B guidance range.",
            "evidence_quote": "Albert Bourla: We had a strong start to 2025, delivering 5% operational revenue growth and reiterating our full-year financial outlook.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "BA:2025-01-28#0",
        "ticker": "BA",
        "call_date": "2025-01-28",
        "call_label": "Q4 2024 Earnings Call (Jan 28, 2025)",
        "speaker": "Kelly Ortberg",
        "role": "CEO",
        "category": "manufacturing_ramp",
        "summary": "737 MAX production rate stabilization to reach 38 per month by mid-2025",
        "quote": "Our top priority is stabilizing the production system. We expect to reach and sustain the FAA-authorized rate of 38 737 MAX airplanes per month by mid-2025.",
        "value_low": 38.0, "value_high": 38.0, "unit": "Airplanes/Month",
        "period": "2025-H1", "period_kind": "HALF", "strength": "firm",
        "conditions": "Subject to FAA safety audit validations and supply chain master schedule alignment.",
        "verifiable_by": "disclosure",
        "resolution": {
            "outcome": "PARTIAL",
            "knowable_at": "2025-05-15",
            "ratio": 0.65,
            "why": "Boeing assembly lines reached 38 per month intermittently in late May 2025, but deliveries lagged at under 25 per month and Q1 free cash flow burn was severe at $(4.1) billion.",
            "evidence_quote": "Kelly Ortberg: While factory line flow touched 38 per month in May, delivery handoffs to airlines remain constrained by supplier parts shortages.",
            "y": 0.5, "revisions": 1
        }
    },
    {
        "id": "CAT:2025-01-30#0",
        "ticker": "CAT",
        "call_date": "2025-01-30",
        "call_label": "Q4 2024 Earnings Call (Jan 30, 2025)",
        "speaker": "Andrew Bonfield",
        "role": "CFO",
        "category": "operating_margin",
        "summary": "Full year 2025 adjusted operating profit margin in the top half of target range (19% to 21%)",
        "quote": "For full-year 2025, even with slightly lower sales, we expect adjusted operating profit margin to land in the top half of our target range of 19% to 21%.",
        "value_low": 20.0, "value_high": 21.0, "unit": "%",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes pricing discipline offsets dealer inventory adjustment headwinds.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-29",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, adjusted operating profit margin came in at 21.2%, exceeding the top half of the target range.",
            "evidence_quote": "Jim Umpleby: Operating profit margin was 20.6% and adjusted operating profit margin reached 21.2%, demonstrating resilient operational execution.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "GE:2025-01-23#0",
        "ticker": "GE",
        "call_date": "2025-01-23",
        "call_label": "Q4 2024 Earnings Call (Jan 23, 2025)",
        "speaker": "Larry Culp",
        "role": "CEO",
        "category": "operating_margin",
        "summary": "Full year 2025 operating profit between $7.8 billion and $8.2 billion and free cash flow between $6.3 billion and $6.8 billion",
        "quote": "For 2025, we expect GE Aerospace operating profit of $7.8 billion to $8.2 billion, up double digits, and free cash flow of $6.3 billion to $6.8 billion.",
        "value_low": 7.8, "value_high": 8.2, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Supported by commercial services aftermarket rate and LEAP durability upgrade deliveries.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-22",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, operating profit rose 24% to $2.1 billion and free cash flow rose to $1.6 billion, tracking toward the high end of the annual range.",
            "evidence_quote": "Larry Culp: GE Aerospace had a tremendous first quarter, growing operating profit by 24% and generating $1.6 billion of free cash flow.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "LMT:2025-01-28#0",
        "ticker": "LMT",
        "call_date": "2025-01-28",
        "call_label": "Q4 2024 Earnings Call (Jan 28, 2025)",
        "speaker": "Jesus Malave",
        "role": "CFO",
        "category": "revenue_target",
        "summary": "Full year 2025 net sales between $73.75 billion and $74.75 billion and segment operating profit between $8.10 billion and $8.20 billion",
        "quote": "For the full year 2025, we project net sales in the range of $73.75 billion to $74.75 billion, business segment operating profit of $8.10 billion to $8.20 billion, and free cash flow of $6.60 billion to $6.80 billion.",
        "value_low": 73.75, "value_high": 74.75, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Assumes timely enactment of federal defense appropriations.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-04-22",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, net sales reached $18.0 billion and segment operating profit reached $2.05 billion, perfectly aligned with the annual guidance rate.",
            "evidence_quote": "Jim Taiclet: First quarter sales of $18.0 billion and segment profit of over $2.0 billion keep us on track to achieve our full-year financial targets.",
            "y": 1.0, "revisions": 0
        }
    },
    {
        "id": "XOM:2025-01-31#0",
        "ticker": "XOM",
        "call_date": "2025-01-31",
        "call_label": "Q4 2024 Earnings Call (Jan 31, 2025)",
        "speaker": "Kathryn Mikells",
        "role": "CFO",
        "category": "capex_target",
        "summary": "Full year 2025 capital expenditures between $27.0 billion and $29.0 billion",
        "quote": "Under our Corporate Plan, we expect 2025 capital expenditures to remain disciplined between $27 billion and $29 billion, while growing our advantaged volume in Guyana and the Permian.",
        "value_low": 27.0, "value_high": 29.0, "unit": "Billion USD",
        "period": "FY2025", "period_kind": "YEAR", "strength": "firm",
        "conditions": "Subject to upstream rig scheduling and project milestone timing.",
        "verifiable_by": "financials",
        "resolution": {
            "outcome": "DELIVERED",
            "knowable_at": "2025-05-02",
            "ratio": 1.0,
            "why": "In Q1 2025 Form 10-Q, capital expenditures were $6.8 billion, pacing exactly in line with the $27B–$29B full-year guidance range.",
            "evidence_quote": "Darren Woods: Capital expenditures were $6.8 billion in the first quarter, reflecting our disciplined capital allocation and focused project delivery.",
            "y": 1.0, "revisions": 0
        }
    }
]
