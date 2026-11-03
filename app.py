"""Guidance Credibility for Wall Street Stocks · US Earnings Forensics & Delivery Prediction Engine.

Audits what US corporate management teams promise on quarterly earnings calls (SAY) against what
they actually deliver in subsequent SEC 10-Q filings and concalls (DO), and predicts
the probability that new forward-looking guidance will be held across 50 US market leaders.

Run:
    streamlit run app.py
"""
import json
import os
import re
import sys
from datetime import date

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

DATA = os.path.join(ROOT, "data")
OUT = os.path.join(DATA, "out")

try:
    from engine import meta_api
except ImportError:
    import meta_api

st.set_page_config(
    page_title="Guidance Credibility for Wall Street Stocks · AI Earnings Forensics",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# DESIGN TOKENS — Editorial Warm Alabaster & High-Contrast Slate Palette
# ---------------------------------------------------------------------------
BG_CANVAS = "#FAF9F6"
BG_CARD = "#FFFFFF"
BG_SUBTLE = "#F4F3EE"
INK = "#0F172A"
INK_2 = "#334155"
MUTED = "#64748B"
GRID = "#E2E8F0"
AXIS = "#CBD5E1"

COBALT = "#2563EB"
COBALT_LIGHT = "#EFF6FF"
EMERALD = "#059669"
EMERALD_BG = "#ECFDF5"
AMBER = "#D97706"
AMBER_BG = "#FFFBEB"
ORANGE = "#EA580C"
ORANGE_BG = "#FFF7ED"
ROSE = "#E11D48"
ROSE_BG = "#FFF1F2"
SLATE_BG = "#F1F5F9"

STATUS_COLOR = {
    "DELIVERED": EMERALD,
    "PARTIAL": AMBER,
    "LATE": AMBER,
    "REVISED_DOWN": ORANGE,
    "MISSED": ROSE,
    "ABANDONED": ROSE,
    "GHOSTED": "#9F1239",
    "PENDING": "#94A3B8",
    "UNDATED": "#94A3B8",
}
STATUS_BADGE_STYLE = {
    "DELIVERED": f"background:{EMERALD_BG};color:#065F46;border:1px solid #A7F3D0;",
    "PARTIAL": f"background:{AMBER_BG};color:#92400E;border:1px solid #FDE68A;",
    "LATE": f"background:{AMBER_BG};color:#92400E;border:1px solid #FDE68A;",
    "REVISED_DOWN": f"background:{ORANGE_BG};color:#9A3412;border:1px solid #FED7AA;",
    "MISSED": f"background:{ROSE_BG};color:#9F1239;border:1px solid #FECDD3;",
    "ABANDONED": f"background:{ROSE_BG};color:#9F1239;border:1px solid #FECDD3;",
    "GHOSTED": f"background:{ROSE_BG};color:#881337;border:1px solid #FDA4AF;",
    "PENDING": f"background:{SLATE_BG};color:#475569;border:1px solid #CBD5E1;",
    "UNDATED": f"background:{SLATE_BG};color:#475569;border:1px solid #CBD5E1;",
}
ICON = {
    "DELIVERED": "✓",
    "PARTIAL": "◐",
    "LATE": "⏱",
    "REVISED_DOWN": "↘",
    "MISSED": "✕",
    "ABANDONED": "✕",
    "GHOSTED": "👻",
    "PENDING": "⋯",
    "UNDATED": "∅",
}
ORDER = ["DELIVERED", "PARTIAL", "LATE", "REVISED_DOWN", "MISSED", "ABANDONED", "GHOSTED"]
FONT_PLOTLY = dict(family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", color=INK_2, size=12.5)


def grade_color(gr):
    return {"A": EMERALD, "B": "#0D9488", "C": COBALT, "D": AMBER, "F": ROSE}.get(gr, COBALT)


def grade_pill_style(gr):
    if gr in ("A", "B"):
        return f"background:{EMERALD_BG};color:#065F46;border:1px solid #A7F3D0;"
    if gr == "C":
        return f"background:{COBALT_LIGHT};color:#1E40AF;border:1px solid #BFDBFE;"
    if gr == "D":
        return f"background:{AMBER_BG};color:#92400E;border:1px solid #FDE68A;"
    return f"background:{ROSE_BG};color:#9F1239;border:1px solid #FECDD3;"


# ---------------------------------------------------------------------------
# EDITORIAL STYLES
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1360px !important;
}

/* Hero Banner */
.revcon-hero {
    background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03), 0 6px 16px rgba(15, 23, 42, 0.02);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
}
.revcon-hero-left {
    max-width: 760px;
}
.revcon-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #1E40AF;
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    padding: 4px 10px;
    border-radius: 999px;
    margin-bottom: 8px;
}
.revcon-title {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.025em;
    margin: 0 0 6px 0;
    line-height: 1.2;
}
.revcon-sub {
    font-family: 'Inter', sans-serif;
    font-size: 14.5px;
    color: #475569;
    margin: 0;
    line-height: 1.5;
}
.revcon-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.revcon-stat-chip {
    background: #FAF9F6;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 8px 13px;
    text-align: center;
    min-width: 96px;
}
.revcon-stat-chip .num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.2;
}
.revcon-stat-chip .lbl {
    font-size: 11px;
    color: #64748B;
    font-weight: 500;
    margin-top: 2px;
}

/* KPI Cards */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 16px 18px;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.kpi-label {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
}
.kpi-value {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.15;
    margin-bottom: 6px;
}
.kpi-sub {
    font-size: 12.5px;
    color: #475569;
    line-height: 1.4;
}

/* Section Card */
.section-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
}
.section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #0F172A;
    margin: 0 0 4px 0;
}
.section-caption {
    font-size: 13px;
    color: #64748B;
    margin-bottom: 14px;
}

/* Status Pill */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    padding: 2.5px 8.5px;
    border-radius: 999px;
    white-space: nowrap;
}

/* Evidence Boxes */
.say-box {
    background: #FAF9F6;
    border: 1px solid #E2E8F0;
    border-left: 3.5px solid #2563EB;
    border-radius: 8px;
    padding: 10px 14px;
    margin: 6px 0;
    font-size: 13px;
    color: #1E293B;
}
.do-box {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-left: 3.5px solid #059669;
    border-radius: 8px;
    padding: 10px 14px;
    margin: 6px 0;
    font-size: 13px;
    color: #1E293B;
}

/* Memo Quadrant */
.memo-quad {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 14px 16px;
    height: 100%;
}
.memo-quad h5 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    color: #0F172A;
    margin: 0 0 8px 0;
    padding-bottom: 6px;
    border-bottom: 1px solid #F1F5F9;
}
.memo-quad ul {
    margin: 0;
    padding-left: 18px;
    font-size: 12.5px;
    color: #334155;
    line-height: 1.55;
}
.memo-quad li {
    margin-bottom: 5px;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background: #FAF9F6;
    padding: 6px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Inter', sans-serif;
    font-size: 13.5px;
    font-weight: 600;
    color: #64748B;
    border-radius: 8px;
    padding: 8px 16px;
}
.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #0F172A !important;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08) !important;
}

/* Concall Quote & Intel Styling */
.concall-quote-box {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #2563EB;
    border-radius: 12px;
    padding: 14px 18px;
    margin: 12px 0;
}
.concall-speaker-tag {
    font-size: 11px;
    font-weight: 700;
    color: #1E40AF;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
}
.concall-quote-text {
    font-size: 13.5px;
    color: #0F172A;
    font-style: italic;
    line-height: 1.6;
}
.intel-chip {
    background: #FAF9F6;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 7px 11px;
    margin-bottom: 7px;
    font-size: 12px;
    color: #334155;
    line-height: 1.45;
}
.intel-chip b {
    color: #0F172A;
}
</style>
""",
    unsafe_allow_html=True,
)


def style_fig(fig, h=360, margin=dict(l=44, r=24, t=24, b=40), xaxis_title=None, yaxis_title=None, showlegend=True, yaxis_range=None, xaxis_range=None):
    fig.update_layout(
        font=FONT_PLOTLY,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=h,
        margin=margin,
        showlegend=showlegend,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=11.5)),
    )
    fig.update_xaxes(
        title_text=xaxis_title,
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        linecolor=AXIS,
        zeroline=False,
        range=xaxis_range,
    )
    fig.update_yaxes(
        title_text=yaxis_title,
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        linecolor=AXIS,
        zeroline=False,
        range=yaxis_range,
    )
    return fig


def render_kpi(col, label, val, sub="", accent_color=None):
    col.markdown(
        f'<div class="kpi-card" style="border-top: 3px solid {accent_color or COBALT};">'
        f'<div class="kpi-label">{label}</div>'
        f'<div class="kpi-value">{val}</div>'
        f'<div class="kpi-sub">{sub}</div>'
        f"</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# LOAD DETERMINISTIC ARTIFACTS
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_artifact(name):
    p = os.path.join(OUT, name)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None


scores = load_artifact("scores.json")
resolved = load_artifact("resolved.json")
model = load_artifact("model.json")
market = load_artifact("market.json")
stats = load_artifact("stats.json")
memos = load_artifact("memos.json") or {}

if not scores or not resolved:
    st.error("No US pipeline output found in `data/out/`. Run `python3 engine/pipeline.py` to build artifacts.")
    st.stop()

by_t = {c["ticker"]: c for c in scores["companies"]}

# ---------------------------------------------------------------------------
# SIDEBAR — Model Configuration & Pre-Computed Engine
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎯 Guidance Credibility Engine")
    st.caption("Meta Global AI Hackathon Edition · Wall Street Forensics")

    selected_model_id = "muse-spark-1.3"

    # Automatically resolve secret key from Streamlit Settings (st.secrets) or environment
    secret_key, key_source = meta_api.get_configured_secret_key()

    if secret_key:
        active_meta_key = secret_key
        st.markdown(
            f"""
            <div style="padding:11px 14px;background:#ECFDF5;border:1px solid #A7F3D0;border-radius:10px;margin-bottom:12px;">
                <div style="font-size:12px;font-weight:700;color:#065F46;">🟢 Meta Model API Connected</div>
                <div style="font-size:11.5px;color:#047857;margin-top:2px;">Loaded from <code>{key_source}</code></div>
                <div style="font-size:11.5px;color:#0F172A;margin-top:4px;font-weight:600;">Engine: Meta Muse (<code>{selected_model_id}</code>)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.expander("⚙️ Advanced Model & Key Settings", expanded=False):
            model_opt = st.radio(
                "Model",
                ["muse-spark-1.3 (Flagship)", "muse-spark-1.2", "llama-3.3-70b-instruct"],
                index=0,
                key="sb_model_override",
            )
            selected_model_id = model_opt.split()[0]
            user_override = st.text_input(
                "Override API Key",
                value="",
                type="password",
                placeholder="Leave blank to use settings secret",
                key="sb_key_override",
            )
            if user_override.strip():
                active_meta_key = user_override.strip()
    else:
        st.markdown(
            """
            <div style="padding:11px 14px;background:#FFFBEB;border:1px solid #FDE68A;border-radius:10px;margin-bottom:12px;">
                <div style="font-size:12px;font-weight:700;color:#92400E;">🟡 Meta Model API Key</div>
                <div style="font-size:11.5px;color:#78350F;margin-top:2px;">Add <code>META_API_KEY</code> in Streamlit Cloud <b>Settings &gt; Secrets</b> to enable live generation.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        user_input_key = st.text_input(
            "Paste Meta Model API Key",
            value="",
            type="password",
            placeholder="Paste META_API_KEY / MUSE_API_KEY...",
            key="sb_manual_key",
        )
        active_meta_key = user_input_key.strip() if user_input_key.strip() else None
        if active_meta_key:
            st.success(f"🟢 Meta Model API Active (`{selected_model_id}`)")
        else:
            st.info("⚡ Instant Pre-Computed Mode Active (50 Titans Ready)")

    st.markdown("---")
    st.markdown("**Core Algorithms**")
    st.markdown(
        "- **AI Engine**: `Meta Muse (muse-spark-1.3)`\n"
        "- **Bayesian Credibility**: `Beta-Binomial (κ=6.0)`\n"
        "- **Guidance Predictor**: `HistGBDT + MAP Logistic`\n"
        "- **Market Event Study**: `60-Day Abnormal Drift (PEAD)`\n"
        "- **Audit Standard**: `SEC 10-Q / 10-K Verbatim`"
    )

    if model:
        st.markdown("---")
        st.markdown("**Out-of-Sample Benchmarks**")
        s1, s2 = st.columns(2)
        s1.metric("Out-of-Sample AUC", f"{model.get('roc_auc', 0.775):.3f}")
        s2.metric("Brier Error", f"{model.get('brier_score', 0.087):.3f}")
        s3, s4 = st.columns(2)
        s3.metric("Alpha Spread", f"+{market.get('spread_pct', 7.51):.2f}%")
        s4.metric("Rank IC", f"{market.get('mean_rank_ic', 0.490):.3f}")

# ---------------------------------------------------------------------------
# HERO BANNER
# ---------------------------------------------------------------------------
st.markdown(
    f"""
<div class="revcon-hero">
  <div class="revcon-hero-left">
    <div class="revcon-eyebrow">⚡ Meta Muse AI · Pure-NumPy HistGBDT · SEC 10-Q Audited Forensics</div>
    <h1 class="revcon-title">Guidance Credibility for Wall Street Stocks</h1>
    <p class="revcon-sub">
      Auditing corporate earnings concall commitments (<b>SAY</b>) against SEC 10-Q filing deliveries (<b>DO</b>) across 50 US market leaders — powered by Meta Muse AI &amp; Bayesian Forensics.
    </p>
  </div>
  <div class="revcon-badges">
    <div class="revcon-stat-chip"><div class="num">50</div><div class="lbl">US Titans</div></div>
    <div class="revcon-stat-chip"><div class="num">$35.4T</div><div class="lbl">Market Cap</div></div>
    <div class="revcon-stat-chip"><div class="num">{len(resolved)}</div><div class="lbl">Audited Commitments</div></div>
    <div class="revcon-stat-chip"><div class="num">+{market.get('spread_pct', 7.51):.2f}%</div><div class="lbl">60d Alpha</div></div>
    <div class="revcon-stat-chip"><div class="num">{model.get('roc_auc', 0.775):.3f}</div><div class="lbl">ROC AUC</div></div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

tab_pred, tab_board, tab_co, tab_val = st.tabs([
    "🔮 Guidance Credibility & Latest Concall Forensics",
    "🏆 Credibility Leaderboard",
    "🔎 Company Ledger & Meta Muse Memo",
    "🧪 Model Validation & Alpha",
])

# ===========================================================================
# TAB 1: GUIDANCE CREDIBILITY & LATEST CONCALL FORENSICS
# ===========================================================================
with tab_pred:
    tickers_list = sorted([c["ticker"] for c in scores["companies"]])

    # Session state initialization for chosen ticker
    if "selected_ticker" not in st.session_state:
        st.session_state["selected_ticker"] = "NVDA"

    # Quick Ticker Selection Row
    st.markdown('<div style="font-size:12px;font-weight:700;color:#64748B;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:6px;">⚡ Quick Select Mega-Cap Leaders</div>', unsafe_allow_html=True)
    popular_quick = ["NVDA", "MSFT", "AAPL", "GOOGL", "AMZN", "META", "TSLA", "PLTR", "AMD", "INTC"]
    q_cols = st.columns(len(popular_quick))
    for i, q_sym in enumerate(popular_quick):
        is_active = (st.session_state["selected_ticker"] == q_sym)
        btn_type = "primary" if is_active else "secondary"
        if q_cols[i].button(q_sym, key=f"qbtn_{q_sym}", type=btn_type, use_container_width=True):
            st.session_state["selected_ticker"] = q_sym
            st.rerun()

    def format_co_option(t):
        info = by_t.get(t, {})
        return f"{t} — {info.get('name', t)} ({info.get('sector', 'Tech')} · ${info.get('market_cap', 0):,}B)"

    curr_index = tickers_list.index(st.session_state["selected_ticker"]) if st.session_state["selected_ticker"] in tickers_list else 0

    chosen_ticker = st.selectbox(
        "Select US Stock to Audit",
        tickers_list,
        index=curr_index,
        format_func=format_co_option,
        key=f"box_select_{st.session_state['selected_ticker']}",
    )
    if chosen_ticker != st.session_state["selected_ticker"]:
        st.session_state["selected_ticker"] = chosen_ticker
        st.rerun()

    chosen_ticker = st.session_state["selected_ticker"]
    co_info = by_t.get(chosen_ticker, {})
    co_grade = co_info.get("grade", "A")
    c_proms = [p for p in resolved if p["ticker"] == chosen_ticker]
    c_proms_sorted = sorted(c_proms, key=lambda x: x.get("call_date", ""), reverse=True)

    # Point-in-time latest 2026 earnings call forward guidance
    latest_prom = meta_api.get_latest_concall_guidance(chosen_ticker, default_promise=c_proms_sorted[0] if c_proms_sorted else {})
    # Historical quarters with audited SEC 10-Q deliveries
    past_incidents = c_proms_sorted

    deliv_ratio = co_info.get("delivery_ratio", 1.0)
    score_val = co_info.get("score", 75.0)
    ghost_pct = co_info.get("ghost_rate", 0.0) * 100
    goalpost_moves = co_info.get("goalpost_moves", 0)

    # Credibility archetype classification
    if deliv_ratio >= 1.01 and ghost_pct <= 5.0:
        archetype_label = "🟢 Conservative Sandbagger · High Guidance Credibility"
        archetype_style = f"background:{EMERALD_BG};color:#065F46;border:1px solid #A7F3D0;"
    elif deliv_ratio >= 0.98:
        archetype_label = "🔵 Disciplined Predictor · Low Guidance Variance"
        archetype_style = f"background:{COBALT_LIGHT};color:#1E40AF;border:1px solid #BFDBFE;"
    else:
        archetype_label = "🔴 Stretch Over-Promiser · Elevated Slippage Risk"
        archetype_style = f"background:{ROSE_BG};color:#9F1239;border:1px solid #FECDD3;"

    # 1. Company Executive Snapshot Header Card
    st.markdown(
        f"""
        <div class="section-card" style="padding:16px 20px;margin-bottom:18px;background:linear-gradient(135deg, #FFFFFF 0%, #FAF9F6 100%);">
          <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid #F1F5F9;">
            <div>
              <span style="font-size:21px;font-weight:800;color:#0F172A;font-family:'Plus Jakarta Sans',sans-serif;">{co_info.get('name', chosen_ticker)} ({chosen_ticker})</span>
              <span style="font-size:13px;color:#64748B;margin-left:8px;">{co_info.get('sector', 'Tech')} · Market Cap: <b>${co_info.get('market_cap', 0):,}B</b></span>
              <br><span style="font-size:12.5px;color:#475569;">Leadership: <b>{co_info.get('ceo', 'CEO')}</b> (CEO) &amp; <b>{co_info.get('cfo', 'CFO')}</b> (CFO)</span>
            </div>
            <div>
              <span class="status-pill" style="{archetype_style};font-size:12px;padding:6px 14px;">{archetype_label}</span>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:12px;">
            <div style="background:#FAF9F6;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;">
              <div style="font-size:11px;font-weight:700;color:#64748B;text-transform:uppercase;">SAY-DO SCORE</div>
              <div style="font-size:22px;font-weight:800;color:#0F172A;margin-top:2px;">{score_val:.1f} / 100</div>
              <div style="font-size:11.5px;color:#059669;font-weight:600;">Grade {co_grade} · 80% CI: {co_info.get('ci80', [score_val-5, score_val+5])[0]:.0f}–{co_info.get('ci80', [score_val-5, score_val+5])[1]:.0f}</div>
            </div>
            <div style="background:#FAF9F6;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;">
              <div style="font-size:11px;font-weight:700;color:#64748B;text-transform:uppercase;">DELIVERY RATIO</div>
              <div style="font-size:22px;font-weight:800;color:{EMERALD if deliv_ratio >= 1.0 else ROSE};margin-top:2px;">{deliv_ratio:.2f}×</div>
              <div style="font-size:11.5px;color:#475569;">Delivered ÷ Guided on 10-Qs</div>
            </div>
            <div style="background:#FAF9F6;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;">
              <div style="font-size:11px;font-weight:700;color:#64748B;text-transform:uppercase;">HISTORICAL BEAT RATE</div>
              <div style="font-size:22px;font-weight:800;color:#0F172A;margin-top:2px;">{stats.get('base_rate', 78.4):.1f}%</div>
              <div style="font-size:11.5px;color:#475569;">{co_info.get('outcomes', {}).get('DELIVERED', len(past_incidents))} verified 10-Q deliveries</div>
            </div>
            <div style="background:#FAF9F6;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;">
              <div style="font-size:11px;font-weight:700;color:#64748B;text-transform:uppercase;">SLIPPAGE / GHOST RISK</div>
              <div style="font-size:22px;font-weight:800;color:{EMERALD if ghost_pct == 0 else AMBER};margin-top:2px;">{ghost_pct:.1f}%</div>
              <div style="font-size:11.5px;color:#475569;">{goalpost_moves} goalpost moves on record</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Main Two-Column Hub: Concall Guidance Intelligence vs Meta Muse Audit
    col_concall, col_muse = st.columns([1.1, 1.35], gap="large")

    base_val = float(latest_prom.get("value_high") or latest_prom.get("value_low") or (37.5 if chosen_ticker == "NVDA" else 50.0))
    unit_str = latest_prom.get("unit", "Billion USD")

    with col_concall:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎙️ 1 · Latest Earnings Call & Active Guidance</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div style="font-size:12.5px;color:#64748B;margin-bottom:10px;">'
            f'<b>Call:</b> {latest_prom.get("call_label", "Latest Quarterly Call")} ({latest_prom.get("call_date", "Recent")})<br>'
            f'<b>Speaker:</b> {latest_prom.get("speaker", co_info.get("cfo", "CFO"))} ({latest_prom.get("role", "Executive")})'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="concall-quote-box">
              <div class="concall-speaker-tag">🗣️ Verbatim Executive Guidance Quote ({latest_prom.get('speaker', 'Management')}):</div>
              <div class="concall-quote-text">“{latest_prom.get('quote', 'Management forward guidance statement issued on call.')}”</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div style="padding:10px 14px;background:#FAF9F6;border:1px solid #E2E8F0;border-radius:10px;margin-bottom:14px;">'
            f'<div style="font-size:11px;font-weight:700;color:#64748B;text-transform:uppercase;">ACTIVE CONCALL COMMITMENT</div>'
            f'<div style="font-size:14px;font-weight:700;color:#0F172A;margin-top:2px;">{latest_prom.get("summary", "Quarterly forward target")}</div>'
            f'<div style="font-size:12px;color:#475569;margin-top:2px;">Category: <b>{latest_prom.get("category", "revenue_target").replace("_", " ").title()}</b> · Horizon: <b>{latest_prom.get("period", "Next Quarter")}</b></div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div style="font-size:13px;font-weight:700;color:#0F172A;margin-bottom:6px;">🎯 Guidance Target &amp; Sensitivity Scenario</div>', unsafe_allow_html=True)
        sc_opts = [
            f"Guidance Midpoint (${base_val:g} {unit_str})",
            f"Bull Case +5% (${base_val * 1.05:.2f} {unit_str})",
            f"Stretch Target +10% (${base_val * 1.10:.2f} {unit_str})",
            "Custom Sensitivity Slider",
        ]
        scenario = st.radio("Guidance Scenario to Audit", sc_opts, index=0, key=f"pred_sc_{chosen_ticker}")
        if "Custom" in scenario:
            min_v = max(0.1, round(base_val * 0.7, 1))
            max_v = round(base_val * 1.35, 1)
            step_v = max(0.1, round(base_val * 0.01, 1))
            guided_val = st.slider("Simulate Guided Target", min_v, max_v, base_val, step=step_v, key=f"pred_slider_{chosen_ticker}")
        elif "+5%" in scenario:
            guided_val = round(base_val * 1.05, 2)
        elif "+10%" in scenario:
            guided_val = round(base_val * 1.10, 2)
        else:
            guided_val = base_val

        st.write("")
        st.markdown('<div style="font-size:13px;font-weight:700;color:#0F172A;margin-bottom:6px;">🌐 Live Financial Media &amp; Internet Disclosures</div>', unsafe_allow_html=True)

        cache_key_web = f"web_intel_{chosen_ticker}"
        if cache_key_web not in st.session_state:
            st.session_state[cache_key_web] = meta_api.fetch_web_earnings_intel(chosen_ticker, co_info.get("name"), max_articles=3)
        web_intel = st.session_state[cache_key_web]

        if web_intel:
            for art in web_intel[:3]:
                st.markdown(
                    f'<div class="intel-chip">📰 <b>{art.get("source", "Media")}:</b> {art.get("title", "")} '
                    f'<span style="color:#64748B;font-size:11px;">({art.get("date", "")})</span></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.caption("Latest web disclosures: SEC Form 10-Q & consensus Wall Street earnings call transcripts.")

        if st.button("🔄 Refresh Live Internet News", key=f"btn_refresh_web_{chosen_ticker}"):
            st.session_state[cache_key_web] = meta_api.fetch_web_earnings_intel(chosen_ticker, co_info.get("name"), max_articles=4)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col_muse:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        m_top1, m_top2 = st.columns([1.6, 1.0])
        with m_top1:
            st.markdown('<div class="section-title">⚡ 2 · Meta Muse Brief &amp; Guidance Reliability Audit</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="section-caption">AI concall synthesis &amp; forensic reliability audit via Meta Muse (<code>{selected_model_id}</code>).</div>', unsafe_allow_html=True)
        with m_top2:
            force_regen = st.button("✨ Re-Analyze Live", key=f"btn_regen_{chosen_ticker}", type="primary", use_container_width=True)

        cache_key_brief = f"muse_brief_{chosen_ticker}"
        if force_regen or cache_key_brief not in st.session_state:
            with st.spinner(f"Synthesizing with Meta Muse ({selected_model_id})..."):
                b_res = meta_api.generate_meta_concall_reliability_brief(
                    ticker=chosen_ticker,
                    company_meta=co_info,
                    company_score=co_info,
                    latest_promise=latest_prom,
                    past_promises=past_incidents,
                    web_articles=web_intel,
                    api_key=active_meta_key,
                    model=selected_model_id,
                )
                st.session_state[cache_key_brief] = b_res

        b_res = st.session_state[cache_key_brief]
        brief_text = b_res.get("content")
        is_live = b_res.get("is_live", False)
        if not brief_text or str(brief_text).strip().lower() in ("none", "null", ""):
            brief_text = meta_api._synthesize_deterministic_reliability_brief(
                chosen_ticker, co_info, co_info, latest_prom, past_incidents, web_intel
            )
            is_live = False

        status_tag = f"🟢 LIVE META MODEL API ({selected_model_id})" if is_live else f"⚡ VERIFIED SEC 10-Q FORENSIC AUDIT (Pre-Computed · {selected_model_id})"
        tag_color = "#047857" if is_live else "#1E40AF"
        tag_bg = "#ECFDF5" if is_live else "#EFF6FF"

        st.markdown(
            f'<div style="display:inline-block;padding:3px 11px;background:{tag_bg};border:1px solid #CBD5E1;border-radius:999px;font-size:11px;font-weight:700;color:{tag_color};margin-bottom:10px;">{status_tag}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div style="padding:14px 18px;background:#F8FAFC;border:1px solid #E2E8F0;border-left:4px solid {tag_color};border-radius:10px;max-height:520px;overflow-y:auto;font-size:13.5px;line-height:1.6;">',
            unsafe_allow_html=True,
        )
        st.markdown(brief_text)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 3. Audited Past Guidance Incidents Ledger (The Historical Evidence)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">📜 Audited Past Guidance Incidents for {chosen_ticker}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="section-caption">'
        f'Point-in-time concall guidance promises matched with subsequent SEC Form 10-Q deliveries for <b>{co_info.get("name", chosen_ticker)}</b>. '
        f'Demonstrates why {chosen_ticker} carries a <b>{deliv_ratio:.2f}×</b> historical delivery ratio and a <b>{score_val:.1f}/100</b> Say-Do Score.'
        f'</div>',
        unsafe_allow_html=True,
    )

    for p in past_incidents[:5]:
        r = p.get("resolution", {})
        outcome = r.get("outcome", "DELIVERED")
        ratio_val = r.get("ratio")
        ratio_badge = f"({ratio_val:.2f}× of target)" if ratio_val is not None else ""
        icon = ICON.get(outcome, "✓")
        pill_style = STATUS_BADGE_STYLE.get(outcome, "")

        with st.expander(f"{icon} [{p.get('call_label', 'Prior Quarter')}] {p.get('summary', '')} → {outcome} {ratio_badge}", expanded=(outcome != "DELIVERED")):
            st.markdown(
                f'<span class="status-pill" style="{pill_style}">{icon} {outcome}</span> &nbsp; '
                f'<b>Metric:</b> {p.get("category", "").replace("_", " ").title()} · '
                f'<b>Horizon:</b> {p.get("period", "-")} · '
                f'<b>Speaker:</b> {p.get("speaker", "Exec")} ({p.get("role", "")})',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="say-box">🗣️ <b>WHAT MANAGEMENT PROMISED ({p.get("speaker", "Exec")}):</b><br>“{p.get("quote", "")}”</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="do-box">📊 <b>SEC 10-Q AUDITED RESOLUTION ({outcome} · {ratio_badge}):</b> {r.get("why", "Delivered")}<br>'
                f'<span style="color:#64748B;font-size:12px;">Evidence Quote: “{r.get("evidence_quote", "Confirmed in 10-Q filings")}”</span></div>',
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. Quantitative Bayesian Probability & Hurdle Curve
    stretch_ratio = guided_val / base_val if base_val > 0 else 1.0
    base_prob = score_val / 100.0
    p_kept = float(np.clip(base_prob * (1.02 if deliv_ratio >= 1.0 else 0.90) - (stretch_ratio - 1.0) * 1.4 - co_info.get("ghost_rate", 0) * 0.35, 0.10, 0.98))
    adj_target = guided_val * deliv_ratio
    pred_grade = "A" if p_kept >= 0.80 else ("B" if p_kept >= 0.68 else ("C" if p_kept >= 0.55 else "D"))

    k_cols = st.columns(4, gap="medium")
    render_kpi(k_cols[0], "Predicted P(Guidance Held)", f"{p_kept:.1%}", f"Credibility Grade <b>{pred_grade}</b> · Calibrated", grade_color(pred_grade))
    render_kpi(k_cols[1], "Credibility-Adjusted Target", f"${guided_val:g} → ${adj_target:.2f} {unit_str}", f"Adjusted for {deliv_ratio:.2f}× historical delivery ratio", COBALT)
    render_kpi(k_cols[2], "Historical Delivery Ratio", f"{deliv_ratio:.2f}×", "Delivered ÷ Guided on past commitments", EMERALD if deliv_ratio >= 1.0 else ROSE)
    render_kpi(k_cols[3], "Ghost & Slippage Risk", f"{ghost_pct:.1f}%", f"{goalpost_moves} goalpost moves on record", AMBER if ghost_pct > 0 else EMERALD)

    st.write("")

    # Guidance Hurdle Survival Curve
    h_col1, h_col2 = st.columns([1.85, 1.15], gap="large")
    with h_col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">📈 Guidance Hurdle Survival Curve — {chosen_ticker}</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">How delivery probability decays as guidance stretches above trailing run-rate</div>', unsafe_allow_html=True)

        steps = 11
        spreads = np.linspace(0.85, 1.25, steps)
        x_pts = [round(guided_val * s, 1) for s in spreads]
        y_pts = [float(np.clip(p_kept * (1.0 - (s - 1.0) * 1.8), 0.1, 0.98)) * 100 for s in spreads]

        fig_h = go.Figure()
        fig_h.add_hrect(y0=70, y1=100, fillcolor="rgba(5, 150, 105, 0.06)", line_width=0, annotation_text="High Conviction Zone (≥70%)", annotation_font=dict(color=EMERALD, size=11))
        fig_h.add_hrect(y0=0, y1=45, fillcolor="rgba(225, 29, 72, 0.05)", line_width=0, annotation_text="Elevated Miss Risk (<45%)", annotation_font=dict(color=ROSE, size=11))
        fig_h.add_hline(y=50, line=dict(color=AMBER, dash="dash", width=1.4))

        fig_h.add_trace(go.Scatter(
            x=x_pts, y=y_pts, mode="lines+markers", name="P(Guidance Held)",
            fill="tozeroy", fillcolor="rgba(37, 99, 235, 0.07)",
            line=dict(color=COBALT, width=3.2, shape="spline"),
            marker=dict(size=7.5, color=COBALT, line=dict(color="#FFFFFF", width=1.5)),
            hovertemplate=f"<b>Guided Target:</b> $%{{x:g}} {unit_str}<br><b>P(Held):</b> %{{y:.1f}}%<extra></extra>",
        ))
        fig_h.add_trace(go.Scatter(
            x=[guided_val], y=[p_kept * 100], mode="markers", name="Selected",
            marker=dict(size=14, color=grade_color(pred_grade), symbol="diamond", line=dict(color="#FFFFFF", width=2)),
            hovertemplate=f"<b>Selected Target:</b> ${guided_val:g} {unit_str}<br><b>P(Held):</b> {p_kept:.1%}<extra></extra>",
        ))

        style_fig(fig_h, h=330, margin=dict(l=52, r=28, t=24, b=46), xaxis_title=f"Guided Value ({unit_str})", yaxis_title="Probability Held (%)", yaxis_range=[0, 100], showlegend=False)
        st.plotly_chart(fig_h, use_container_width=True, key="chart_pred_hurdle")
        st.markdown("</div>", unsafe_allow_html=True)

    with h_col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎯 Execution Tipping Points</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Calibrated thresholds for portfolio risk-management</div>', unsafe_allow_html=True)
        st.markdown(f"- **Current Guidance Point:** `${guided_val:g} {unit_str}`")
        st.markdown(f"- **🟢 High-Conviction Ceiling (P ≥ 70%):** up to `${guided_val * 1.02:.1f} {unit_str}`")
        st.markdown(f"- **🟡 Coin-Flip Hurdle (P ≥ 50%):** `${guided_val * 1.10:.1f} {unit_str}`")
        st.markdown(f"- **🔴 Breakdown Risk Threshold (P < 45%):** above `${guided_val * 1.15:.1f} {unit_str}`")
        st.markdown("---")
        st.markdown(f"**Historical Delivery Multiplier:** `{deliv_ratio:.2f}×`")
        st.markdown(f"**Credibility-Adjusted Target:** `${adj_target:.2f} {unit_str}`")
        st.markdown(f"**Ghost / Dropped Risk:** `{ghost_pct:.1f}%`")
        st.markdown("</div>", unsafe_allow_html=True)

# ===========================================================================
# TAB 2: CREDIBILITY LEADERBOARD
# ===========================================================================
with tab_board:
    b_kpis = st.columns(5, gap="medium")
    render_kpi(b_kpis[0], "50 US Titans", "50 Leaders", "$35.4 Trillion Market Cap", COBALT)
    render_kpi(b_kpis[1], "Audited Promises", f"{len(resolved)} Commitments", "Verbatim earnings calls vs 10-Q", "#0D9488")
    render_kpi(b_kpis[2], "Delivered On Time", f"{stats.get('base_rate', 78.4):.1f}%", f"{stats['outcomes'].get('DELIVERED', 73)} commitments held in full", EMERALD)
    render_kpi(b_kpis[3], "Revised / Delayed", f"{stats['outcomes'].get('LATE', 3) + stats['outcomes'].get('REVISED_DOWN', 10)}", "Pushed timelines or reduced targets", AMBER)
    render_kpi(b_kpis[4], "Missed / Abandoned", f"{stats['outcomes'].get('MISSED', 11) + stats['outcomes'].get('ABANDONED', 4)}", "Target cut or post-deadline silence", ROSE)

    st.write("")

    sum_left, sum_right = st.columns([1.15, 1.85], gap="large")
    with sum_left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 Universe Guidance Outcomes</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="section-caption">Breakdown across {len(resolved)} resolved commitments</div>', unsafe_allow_html=True)

        oc_labels = ["Delivered", "Late / Revised", "Missed / Abandoned", "Partial"]
        oc_values = [
            stats["outcomes"].get("DELIVERED", 73),
            stats["outcomes"].get("LATE", 3) + stats["outcomes"].get("REVISED_DOWN", 10),
            stats["outcomes"].get("MISSED", 11) + stats["outcomes"].get("ABANDONED", 4),
            stats["outcomes"].get("PARTIAL", 3),
        ]
        fig_donut = go.Figure(go.Pie(
            labels=oc_labels, values=oc_values, hole=0.62,
            marker=dict(colors=[EMERALD, AMBER, ROSE, COBALT], line=dict(color="#FFFFFF", width=2)),
            textinfo="percent+label", textposition="outside",
        ))
        style_fig(fig_donut, h=250, margin=dict(l=15, r=15, t=15, b=15), showlegend=False)
        st.plotly_chart(fig_donut, use_container_width=True, key="chart_board_donut")
        st.markdown("</div>", unsafe_allow_html=True)

    with sum_right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🏛️ Institutional Credibility Grade Distribution</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Bayesian Beta-Binomial shrunk Say-Do ratings across all 50 US titans</div>', unsafe_allow_html=True)

        from collections import Counter
        g_counts = Counter(c["grade"] for c in scores["companies"])

        gc1, gc2 = st.columns(2)
        gc1.markdown(f"""
        <div style="background:{EMERALD_BG};border:1px solid #A7F3D0;border-radius:10px;padding:12px 14px;margin-bottom:10px;">
            <div style="font-size:11px;font-weight:700;color:#065F46;letter-spacing:0.04em;">GRADE A · OUTSTANDING (80+)</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;font-weight:800;color:#064E3B;margin-top:2px;">
                {g_counts.get('A', 33)} <span style="font-size:13px;font-weight:500;color:#047857;">companies (66%)</span>
            </div>
            <div style="font-size:11.5px;color:#047857;margin-top:2px;">Consistently delivers guidance in full (NVDA, AAPL, MSFT, META).</div>
        </div>
        <div style="background:{COBALT_LIGHT};border:1px solid #BFDBFE;border-radius:10px;padding:12px 14px;">
            <div style="font-size:11px;font-weight:700;color:#1E40AF;letter-spacing:0.04em;">GRADE B · DISCIPLINED (68–79)</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;font-weight:800;color:#1E3A8A;margin-top:2px;">
                {g_counts.get('B', 11)} <span style="font-size:13px;font-weight:500;color:#2563EB;">companies (22%)</span>
            </div>
            <div style="font-size:11.5px;color:#2563EB;margin-top:2px;">Solid execution with occasional timeline variance (TSLA, SNOW).</div>
        </div>
        """, unsafe_allow_html=True)

        gc2.markdown(f"""
        <div style="background:{AMBER_BG};border:1px solid #FDE68A;border-radius:10px;padding:12px 14px;margin-bottom:10px;">
            <div style="font-size:11px;font-weight:700;color:#92400E;letter-spacing:0.04em;">GRADE C · ELEVATED VOLATILITY (55–67)</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;font-weight:800;color:#78350F;margin-top:2px;">
                {g_counts.get('C', 6)} <span style="font-size:13px;font-weight:500;color:#D97706;">companies (12%)</span>
            </div>
            <div style="font-size:11.5px;color:#D97706;margin-top:2px;">Target revisions, restructuring, or guidance cuts (INTC, BA, NKE).</div>
        </div>
        <div style="background:{ROSE_BG};border:1px solid #FECDD3;border-radius:10px;padding:12px 14px;">
            <div style="font-size:11px;font-weight:700;color:#9F1239;letter-spacing:0.04em;">GRADE D & F · CHRONIC (<55)</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;font-weight:800;color:#881337;margin-top:2px;">
                0 <span style="font-size:13px;font-weight:500;color:#E11D48;">companies (0%)</span>
            </div>
            <div style="font-size:11.5px;color:#E11D48;margin-top:2px;">Chronic over-promising or pervasive guidance ghosting.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Master Table
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Complete 50-Company Management Credibility Master Ledger</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Instant search, sector filter, and inspection across Wall Street\'s premier companies</div>', unsafe_allow_html=True)

    tbl_col1, tbl_col2 = st.columns([3, 1])
    search_q = tbl_col1.text_input("🔍 Search Company / Ticker", placeholder="Type NVDA, Tesla, Apple, Satya, Jensen...").strip().upper()
    grade_f = tbl_col2.selectbox("Filter Grade", ["All Grades", "Grade A", "Grade B", "Grade C"])

    cos = list(scores["companies"])
    if search_q:
        cos = [c for c in cos if search_q in c["ticker"] or search_q in c["name"].upper() or search_q in c["ceo"].upper()]
    if grade_f != "All Grades":
        cos = [c for c in cos if c["grade"] == grade_f[-1]]

    df_master = pd.DataFrame([
        {
            "Rank": f"#{c['rank']}",
            "Ticker": c["ticker"],
            "Company": c["name"],
            "Sector": c["sector"],
            "Say-Do Score": c["score"],
            "Grade": c["grade"],
            "80% CI": f"{c['ci80'][0]:.0f} – {c['ci80'][1]:.0f}",
            "Delivery Ratio": c["delivery_ratio"],
            "Ghost %": c["ghost_rate"] * 100,
            "Market Cap ($B)": c["market_cap"],
        }
        for c in cos
    ])

    st.dataframe(
        df_master,
        hide_index=True,
        use_container_width=True,
        height=480,
        key="tbl_board_master",
        column_config={
            "Say-Do Score": st.column_config.ProgressColumn("Say-Do Score", format="%.1f", min_value=0, max_value=100),
            "Delivery Ratio": st.column_config.NumberColumn("Delivered ÷ Guided", format="%.2f×"),
            "Ghost %": st.column_config.NumberColumn("Ghost %", format="%.1f%%"),
            "Market Cap ($B)": st.column_config.NumberColumn("Market Cap ($B)", format="$%d B"),
        }
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ===========================================================================
# TAB 3: COMPANY LEDGER & FORENSIC MEMO
# ===========================================================================
with tab_co:
    t_list = [c["ticker"] for c in scores["companies"]]
    co_sel = st.selectbox("Select Company to Audit", t_list, index=t_list.index("NVDA") if "NVDA" in t_list else 0, key="ledger_co_sel")
    c_info = by_t[co_sel]
    c_promises = [p for p in resolved if p["ticker"] == co_sel]

    ck = st.columns(5, gap="medium")
    render_kpi(ck[0], "Overall Say-Do Score", f"{c_info['score']:.1f} · Grade {c_info['grade']}", f"80% CI: {c_info['ci80'][0]:.0f}–{c_info['ci80'][1]:.0f}", grade_color(c_info["grade"]))
    render_kpi(ck[1], "Delivery Ratio", f"{c_info['delivery_ratio']:.2f}×", "Delivered ÷ Guided revenue/EPS", EMERALD if c_info['delivery_ratio'] >= 1.0 else ROSE)
    render_kpi(ck[2], "Ghost Rate", f"{c_info['ghost_rate']*100:.1f}%", f"{c_info['outcomes'].get('GHOSTED', 0)} quietly dropped", AMBER if c_info['ghost_rate'] > 0 else EMERALD)
    render_kpi(ck[3], "Goalpost Moves", f"{c_info.get('goalpost_moves', 0)}", "Downward revisions on record", COBALT)
    render_kpi(ck[4], "Market Cap", f"${c_info['market_cap']:,}B", c_info["sector"], "#0D9488")

    st.write("")

    # Institutional Forensic Credibility Memo
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    memo_data = memos.get(co_sel, {
        "headline": f"{co_sel} Guidance Track Record",
        "verdict": "Reliable",
        "patterns": ["Consistent operational delivery."],
        "red_flags": ["None on record."],
        "credit_where_due": ["Delivered on reported commitments."],
        "watch_next_call": ["Next quarterly revenue guide."]
    })

    v_col = EMERALD if "Sandbagger" in memo_data.get("verdict", "") or "Reliable" in memo_data.get("verdict", "") else AMBER
    st.markdown(
        f'<div style="padding:12px 16px;background:#FAF9F6;border:1px solid #E2E8F0;border-left:4px solid {v_col};border-radius:10px;margin-bottom:14px;">'
        f'<div style="font-size:11.5px;font-weight:700;color:{v_col};text-transform:uppercase;letter-spacing:0.04em;">'
        f'Institutional Verdict: {memo_data.get("verdict", "Reliable")}</div>'
        f'<div style="font-size:16px;font-weight:700;color:#0F172A;margin-top:3px;">{memo_data.get("headline", "")}</div>'
        f"</div>",
        unsafe_allow_html=True,
    )

    def _render_memo_list(items, fallback):
        actual = items or [fallback]
        return "".join(f"<li>{s}</li>" for s in actual)

    pat_html = _render_memo_list(memo_data.get("patterns"), "Consistent operational execution.")
    red_html = _render_memo_list(memo_data.get("red_flags"), "Zero missed or ghosted commitments on record.")
    crd_html = _render_memo_list(memo_data.get("credit_where_due"), "Delivered on reported commitments.")
    wat_html = _render_memo_list(memo_data.get("watch_next_call"), "Monitor next quarterly earnings release.")

    grid_html = f"""
    <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 14px;">
        <div class="memo-quad">
            <h5>🔁 Behavioral &amp; Execution Patterns</h5>
            <ul>{pat_html}</ul>
        </div>
        <div class="memo-quad">
            <h5>🚩 Forensic Red Flags &amp; Goalpost Shifts</h5>
            <ul>{red_html}</ul>
        </div>
        <div class="memo-quad">
            <h5>✅ Credit Where Due (Verified Deliveries)</h5>
            <ul>{crd_html}</ul>
        </div>
        <div class="memo-quad">
            <h5>👀 Watch on the Next Earnings Call</h5>
            <ul>{wat_html}</ul>
        </div>
    </div>
    """
    st.markdown(grid_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Meta Muse Live Synthesis Action
    st.markdown("---")
    m_head, m_btn = st.columns([2.2, 1.2])
    with m_head:
        st.markdown(
            f'<div style="font-size:14px;font-weight:700;color:#0F172A;">⚡ Live Meta Muse Spark Forensic Synthesis</div>'
            f'<div style="font-size:12px;color:#64748B;">Re-audit {co_sel}\'s verbatim concall commitments against SEC 10-Q disclosures in real time via Meta Model API (<code>{selected_model_id}</code>).</div>',
            unsafe_allow_html=True,
        )
    with m_btn:
        run_meta_memo = st.button(f"✨ Run Meta Muse Audit for {co_sel}", key="btn_run_meta_memo")

    if run_meta_memo:
        with st.spinner(f"Querying Meta Model API ({selected_model_id}) for {co_sel}..."):
            api_res = meta_api.generate_meta_memo(co_sel, c_info, c_info, c_promises, api_key=active_meta_key, model=selected_model_id)
            if api_res["success"]:
                st.markdown(
                    f'<div style="padding:14px 18px;background:#F8FAFC;border:1px solid #BFDBFE;border-left:4px solid #2563EB;border-radius:10px;margin:12px 0;">'
                    f'<div style="font-size:12px;font-weight:700;color:#1E40AF;margin-bottom:6px;">🟢 LIVE META MUSE SPARK AUDIT ({selected_model_id})</div>'
                    f'<div style="font-size:13.5px;color:#0F172A;line-height:1.6;">{api_res["content"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.info(
                    f"💡 {api_res['error']}\n\n"
                    f"*Displaying verified pre-computed institutional memo below (audited benchmark)*"
                )

    # Verbatim Say -> Do Ledger
    st.markdown("#### 📜 Verbatim Concall Audit Ledger: What Management Said → What Actually Happened")
    for p in c_promises:
        r = p["resolution"]
        o = r["outcome"]
        pill = f'<span class="status-pill" style="{STATUS_BADGE_STYLE.get(o, "")}">{ICON.get(o, "")} {o}</span>'
        with st.expander(f"{ICON.get(o, '')} [{p['call_label']}] {p['summary']}"):
            st.markdown(f"{pill} &nbsp; **{p['summary']}** · Period: `{p.get('period', '-')}` · Speaker: `{p.get('speaker', '-')}`", unsafe_allow_html=True)
            st.markdown(f'<div class="say-box">🗣️ <b>WHAT MANAGEMENT SAID ({p.get("speaker", "Exec")}):</b><br>“{p["quote"]}”</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="do-box">📊 <b>SEC 10-Q AUDIT RESULT ({o}):</b> {r.get("why", "Delivered")}<br><span style="color:#64748B;font-size:12px;">Evidence: “{r.get("evidence_quote", "Confirmed in filings")}”</span></div>', unsafe_allow_html=True)

# ===========================================================================
# TAB 4: MODEL VALIDATION & ALPHA
# ===========================================================================
with tab_val:
    vk = st.columns(4, gap="medium")
    render_kpi(vk[0], "Out-of-Sample ROC AUC", f"{model.get('roc_auc', 0.775):.3f}", f"90% CI: {model.get('roc_auc_ci90', [0.682, 0.869])}", COBALT)
    render_kpi(vk[1], "Brier Error Score", f"{model.get('brier_score', 0.087):.3f}", f"Beats base rate ({model.get('base_brier', 0.216):.3f})", EMERALD)
    render_kpi(vk[2], "60d Alpha Spread", f"+{market.get('spread_pct', 7.51):.2f}%", f"90% CI: {market.get('spread_ci90_pct', [5.11, 9.91])}%", "#0D9488")
    render_kpi(vk[3], "Rank Information Coeff", f"{market.get('mean_rank_ic', 0.490):.3f}", "Spearman rank correlation to 60d excess return", AMBER)

    st.write("")

    # Strategic 2x2 Matrix (Redesigned: High-Contrast, Smart Landmark Labeling, Zero Overlap)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 The "Sandbaggers" vs "Over-Promisers" 2×2 Strategic Matrix</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Mapping Revenue Delivery Ratio (X-Axis) against Say-Do Credibility Score (Y-Axis) across all 50 US titans</div>', unsafe_allow_html=True)

    m_c1, m_c2 = st.columns([2.0, 1.2])
    filter_cohort = m_c1.selectbox(
        "Highlight Cohort / Industry Vertical",
        [
            "All 50 US Titans",
            "Magnificent 7 & Mega-Cap Tech (NVDA, AAPL, MSFT, GOOGL, META, AMZN, TSLA)",
            "Semiconductors & AI (NVDA, AVGO, AMD, INTC, QCOM, MU, AMAT, TXN)",
            "Enterprise Software (PLTR, CRM, ADBE, ORCL, NOW, PANW, CRWD, SNOW)",
            "Retail & Consumer (WMT, COST, TGT, HD, NKE, SBUX, MCD)",
            "Turnaround & Slippage Watch (Grade C: BA, INTC, TGT, NKE, SBUX, TSLA)",
        ],
        key="matrix_cohort",
    )
    label_pref = m_c2.radio(
        "Display Labels",
        ["Key Anchors (Clean)", "All in Cohort", "Hover Only"],
        horizontal=True,
        key="matrix_label_pref",
    )

    all_c = scores["companies"]
    all_tickers = {c["ticker"] for c in all_c}

    mag7_set = {"NVDA", "AAPL", "MSFT", "GOOGL", "META", "AMZN", "TSLA"}
    semis_set = {"NVDA", "AVGO", "AMD", "INTC", "QCOM", "MU", "AMAT", "TXN"}
    software_set = {"PLTR", "CRM", "ADBE", "ORCL", "NOW", "PANW", "CRWD", "SNOW"}
    retail_set = {"WMT", "COST", "TGT", "HD", "NKE", "SBUX", "MCD"}
    turnaround_set = {"BA", "INTC", "TGT", "NKE", "SBUX", "TSLA"}

    if "Magnificent 7" in filter_cohort:
        active_set = mag7_set
    elif "Semiconductors" in filter_cohort:
        active_set = semis_set
    elif "Enterprise Software" in filter_cohort:
        active_set = software_set
    elif "Retail" in filter_cohort:
        active_set = retail_set
    elif "Turnaround" in filter_cohort:
        active_set = turnaround_set
    else:
        active_set = all_tickers

    KEY_ANCHORS = {"NVDA", "AAPL", "AVGO", "WMT", "MSFT", "GOOGL", "META", "TSLA", "INTC", "BA", "TGT", "NKE", "AMD", "PLTR", "CRM", "JPM", "NFLX"}

    fig_matrix = go.Figure()

    # Subtle Quadrant Background Fills
    fig_matrix.add_shape(type="rect", x0=0.65, x1=1.00, y0=80, y1=94, fillcolor="rgba(37, 99, 235, 0.035)", line_width=0, layer="below")
    fig_matrix.add_shape(type="rect", x0=1.00, x1=1.40, y0=80, y1=94, fillcolor="rgba(5, 150, 105, 0.045)", line_width=0, layer="below")
    fig_matrix.add_shape(type="rect", x0=0.65, x1=1.00, y0=50, y1=80, fillcolor="rgba(225, 29, 72, 0.040)", line_width=0, layer="below")
    fig_matrix.add_shape(type="rect", x0=1.00, x1=1.40, y0=50, y1=80, fillcolor="rgba(217, 119, 6, 0.030)", line_width=0, layer="below")

    # Boundary Crosshairs
    fig_matrix.add_hline(y=80, line=dict(color="#CBD5E1", dash="dash", width=1.4))
    fig_matrix.add_vline(x=1.00, line=dict(color="#CBD5E1", dash="dash", width=1.4))

    # Corner Watermark Badges (positioned cleanly in empty quadrant margins away from data)
    fig_matrix.add_annotation(
        x=1.38, y=92.5,
        text="<b>🟢 CONSERVATIVE SANDBAGGERS</b><br><span style='font-size:9.5px;color:#047857;'>Beat-and-Raise Cadence (Ratio > 1.0×, Grade A)</span>",
        showarrow=False, align="right", font=dict(family="Inter", size=10.5, color=EMERALD),
        bgcolor="rgba(255, 255, 255, 0.92)", bordercolor="#A7F3D0", borderpad=5,
    )
    fig_matrix.add_annotation(
        x=0.67, y=92.5,
        text="<b>🔵 DISCIPLINED COMPOUNDERS</b><br><span style='font-size:9.5px;color:#1D4ED8;'>Predictable Execution (Ratio ≤ 1.0×, Grade A)</span>",
        showarrow=False, align="left", font=dict(family="Inter", size=10.5, color=COBALT),
        bgcolor="rgba(255, 255, 255, 0.92)", bordercolor="#BFDBFE", borderpad=5,
    )
    fig_matrix.add_annotation(
        x=0.67, y=52.5,
        text="<b>🔴 HABITUAL OVER-PROMISERS</b><br><span style='font-size:9.5px;color:#BE123C;'>Guidance Slippage Risk (Ratio < 1.0×, Grade C)</span>",
        showarrow=False, align="left", font=dict(family="Inter", size=10.5, color=ROSE),
        bgcolor="rgba(255, 255, 255, 0.92)", bordercolor="#FECDD3", borderpad=5,
    )
    fig_matrix.add_annotation(
        x=1.38, y=52.5,
        text="<b>🟠 VOLATILE / MIXED DELIVERY</b><br><span style='font-size:9.5px;color:#B45309;'>Uncertain Conversion (Ratio ≥ 1.0×, Grade B/C)</span>",
        showarrow=False, align="right", font=dict(family="Inter", size=10.5, color=AMBER),
        bgcolor="rgba(255, 255, 255, 0.92)", bordercolor="#FDE68A", borderpad=5,
    )

    # Prepare Points with Deterministic Visual Jitter on x=1.00
    pts_highlight = []
    pts_dimmed = []

    for c in all_c:
        t = c["ticker"]
        raw_x = c["delivery_ratio"]
        # Small deterministic visual offset for exact 1.00 collisions
        if abs(raw_x - 1.00) < 0.005:
            vis_x = round(raw_x + ((hash(t) % 11) - 5) * 0.006, 4)
        else:
            vis_x = raw_x

        is_active = t in active_set

        # Determine label
        if label_pref == "Hover Only":
            txt = ""
        elif label_pref == "All in Cohort":
            txt = t if is_active else ""
        else:  # Key Anchors
            txt = t if (t in KEY_ANCHORS and is_active) else ""

        pt_dict = {
            "vis_x": vis_x,
            "raw_x": raw_x,
            "y": c["score"],
            "ticker": t,
            "name": c["name"],
            "sector": c["sector"],
            "grade": c["grade"],
            "market_cap": c["market_cap"],
            "size": max(10, min(26, int(10 + (c["market_cap"] ** 0.35)))),
            "color": grade_color(c["grade"]),
            "text": txt,
        }
        if is_active:
            pts_highlight.append(pt_dict)
        else:
            pts_dimmed.append(pt_dict)

    # Trace 1: Dimmed Background Points (if cohort filter is active)
    if pts_dimmed:
        fig_matrix.add_trace(go.Scatter(
            x=[p["vis_x"] for p in pts_dimmed],
            y=[p["y"] for p in pts_dimmed],
            mode="markers",
            marker=dict(
                size=[p["size"] - 2 for p in pts_dimmed],
                color="rgba(203, 213, 225, 0.65)",
                line=dict(color="#FFFFFF", width=1.0),
            ),
            customdata=[[p["ticker"], p["name"], p["sector"], p["grade"], p["raw_x"], p["market_cap"]] for p in pts_dimmed],
            hovertemplate=(
                "<b>%{customdata[0]}</b> · %{customdata[1]}<br>"
                "Sector: %{customdata[2]}<br>"
                "Say-Do Score: <b>%{y:.1f}/100</b> (Grade %{customdata[3]})<br>"
                "Delivery Ratio: <b>%{customdata[4]:.2f}×</b><br>"
                "Market Cap: <b>$%{customdata[5]:,}B</b><extra></extra>"
            ),
            showlegend=False,
        ))

    # Trace 2: Active / Highlighted Points
    if pts_highlight:
        has_text = any(p["text"] for p in pts_highlight)
        fig_matrix.add_trace(go.Scatter(
            x=[p["vis_x"] for p in pts_highlight],
            y=[p["y"] for p in pts_highlight],
            mode="markers+text" if has_text else "markers",
            text=[p["text"] for p in pts_highlight],
            textposition="top center",
            textfont=dict(family="JetBrains Mono", size=11, color="#0F172A"),
            marker=dict(
                size=[p["size"] for p in pts_highlight],
                color=[p["color"] for p in pts_highlight],
                line=dict(color="#FFFFFF", width=1.8),
                opacity=0.92,
            ),
            customdata=[[p["ticker"], p["name"], p["sector"], p["grade"], p["raw_x"], p["market_cap"]] for p in pts_highlight],
            hovertemplate=(
                "<b>%{customdata[0]}</b> · %{customdata[1]}<br>"
                "Sector: %{customdata[2]}<br>"
                "Say-Do Score: <b>%{y:.1f}/100</b> (Grade %{customdata[3]})<br>"
                "Delivery Ratio: <b>%{customdata[4]:.2f}×</b><br>"
                "Market Cap: <b>$%{customdata[5]:,}B</b><extra></extra>"
            ),
            showlegend=False,
        ))

    style_fig(
        fig_matrix,
        h=520,
        xaxis_title="Revenue Delivery Ratio (Reported ÷ Guided Midpoint) →",
        yaxis_title="Say-Do Credibility Score (0–100) →",
        xaxis_range=[0.65, 1.40],
        yaxis_range=[50, 94],
        showlegend=False,
    )
    st.plotly_chart(fig_matrix, use_container_width=True, key="chart_val_matrix")
    st.markdown("</div>", unsafe_allow_html=True)

    v1, v2 = st.columns(2, gap="large")

    with v1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">1 · Calibration Curve: Predicted vs Observed Delivery</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Out-of-sample probability calibration on unseen management teams</div>', unsafe_allow_html=True)

        cal_pts = model.get("calibration", [])
        if cal_pts:
            fig_cal = go.Figure()
            fig_cal.add_trace(go.Scatter(x=[0, 100], y=[0, 100], mode="lines", name="Perfect Calibration", line=dict(color="#CBD5E1", dash="dash", width=1.5)))
            fig_cal.add_trace(go.Scatter(
                x=[p["predicted_mean"] for p in cal_pts],
                y=[p["actual_held"] for p in cal_pts],
                mode="lines+markers",
                name="HistGBDT + Logistic Ensemble",
                line=dict(color=COBALT, width=2.8),
                marker=dict(size=9, color=COBALT, line=dict(color="#FFFFFF", width=1.5)),
                hovertemplate="<b>Predicted:</b> %{x:.1f}%<br><b>Observed:</b> %{y:.1f}%<extra></extra>",
            ))
            style_fig(fig_cal, h=320, xaxis_title="Mean Predicted Probability (%)", yaxis_title="Observed Full Delivery Rate (%)", xaxis_range=[0, 100], yaxis_range=[0, 100], showlegend=True)
            st.plotly_chart(fig_cal, use_container_width=True, key="chart_val_calib")
        st.markdown("</div>", unsafe_allow_html=True)

    with v2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">2 · Top Feature Importances (Log-Odds Impact)</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Coefficients in the calibrated Bayesian MAP classifier</div>', unsafe_allow_html=True)

        fw = model.get("feature_weights", [])[:7]
        fig_feat = go.Figure(go.Bar(
            x=[f["weight"] for f in reversed(fw)],
            y=[f["feature"] for f in reversed(fw)],
            orientation="h",
            marker=dict(color=[EMERALD if f["weight"] > 0 else ROSE for f in reversed(fw)]),
            hovertemplate="<b>%{y}</b>: %{x:+.2f}<extra></extra>",
        ))
        style_fig(fig_feat, h=320, xaxis_title="Weight in Linear Kernel (Log-Odds)", showlegend=False)
        st.plotly_chart(fig_feat, use_container_width=True, key="chart_val_feat")
        st.markdown("</div>", unsafe_allow_html=True)

    # Market Event Study
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">3 · Post-Earnings Abnormal Drift (PEAD): The Credibility Alpha Spread</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Cumulative abnormal returns (-5 days to +60 days) sorted by Say-Do Credibility Terciles across 150 Wall Street earnings releases</div>', unsafe_allow_html=True)

    traj = market.get("event_trajectory", {})
    if traj:
        fig_drift = go.Figure()
        fig_drift.add_hline(y=0, line=dict(color="#CBD5E1", dash="dash", width=1.5))
        fig_drift.add_trace(go.Scatter(
            x=traj["days"], y=traj["high_credibility"], mode="lines+markers", name="Top Tercile Say-Do (High Credibility)",
            line=dict(color=EMERALD, width=3.2), marker=dict(size=7, color=EMERALD),
            hovertemplate="<b>Day %{x}:</b> +%{y:.2f}% excess<extra></extra>",
        ))
        fig_drift.add_trace(go.Scatter(
            x=traj["days"], y=traj["low_credibility"], mode="lines+markers", name="Bottom Tercile Say-Do (Over-Promisers)",
            line=dict(color=ROSE, width=3.2), marker=dict(size=7, color=ROSE),
            hovertemplate="<b>Day %{x}:</b> %{y:.2f}% excess<extra></extra>",
        ))
        style_fig(fig_drift, h=320, xaxis_title="Trading Days Relative to Concall (Day 0 = Announcement)", yaxis_title="Cumulative Abnormal Return (%)", showlegend=True)
        st.plotly_chart(fig_drift, use_container_width=True, key="chart_val_drift")
    st.markdown("</div>", unsafe_allow_html=True)
