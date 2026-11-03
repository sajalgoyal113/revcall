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
    }
]
