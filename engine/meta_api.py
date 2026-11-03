"""Meta Model API Client for RevCall US Earnings Forensics.

Integrates Meta's Muse model family (muse-spark-1.3, muse-spark-1.2, muse-wonder-1.0)
and open-weights Llama models (llama-3.3-70b-instruct, llama-3.1-405b-instruct)
via the Meta Model API (https://api.meta.ai/v1).

Exclusively uses Meta AI developer endpoints. Zero third-party or Google AI dependencies.
"""
import json
import os
import requests

META_MODEL_BASE_URL = os.environ.get("META_MODEL_BASE_URL", "https://api.meta.ai/v1")
DEFAULT_META_MODEL = "muse-spark-1.3"

AVAILABLE_META_MODELS = [
    "muse-spark-1.3",
    "muse-spark-1.2",
    "llama-3.3-70b-instruct",
    "llama-3.1-405b-instruct",
    "llama-3.1-70b-instruct",
    "llama-3.1-8b-instruct",
]


def resolve_meta_api_key(explicit_key=None):
    """Resolves the Meta Model API key from user input, Streamlit secrets, or environment."""
    if explicit_key and str(explicit_key).strip():
        return str(explicit_key).strip()

    # Try Streamlit secrets if running inside Streamlit
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            for k in ("META_API_KEY", "MUSE_API_KEY", "MODEL_API_KEY", "META_MODEL_API_KEY"):
                if k in st.secrets and st.secrets[k]:
                    return str(st.secrets[k]).strip()
    except Exception:
        pass

    # Try environment variables
    for k in ("META_API_KEY", "MUSE_API_KEY", "MODEL_API_KEY", "META_MODEL_API_KEY"):
        val = os.environ.get(k)
        if val and val.strip():
            return val.strip()

    return None


def call_meta_model(prompt, system_prompt=None, model=DEFAULT_META_MODEL, api_key=None, max_tokens=1200, temperature=0.2):
    """Executes a chat completion call against the Meta Model API.

    Returns:
        dict: {"success": bool, "content": str, "model": str, "error": str or None}
    """
    key = resolve_meta_api_key(api_key)
    if not key:
        return {
            "success": False,
            "content": "",
            "model": model,
            "error": "No Meta Model API Key found. Set META_API_KEY, MUSE_API_KEY, or MODEL_API_KEY in the sidebar or environment."
        }

    url = f"{META_MODEL_BASE_URL.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=25)
        if response.status_code == 200:
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            return {
                "success": True,
                "content": content,
                "model": model,
                "error": None,
                "usage": data.get("usage", {}),
            }
        else:
            return {
                "success": False,
                "content": "",
                "model": model,
                "error": f"Meta Model API returned HTTP {response.status_code}: {response.text[:300]}",
            }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "content": "",
            "model": model,
            "error": "Meta Model API request timed out after 25 seconds.",
        }
    except Exception as e:
        return {
            "success": False,
            "content": "",
            "model": model,
            "error": f"Connection error: {str(e)}",
        }


def generate_meta_memo(ticker, company_meta, company_score, promises, api_key=None, model=DEFAULT_META_MODEL):
    """Generates an institutional forensic credibility memo using Meta Muse Spark."""
    system_prompt = (
        "You are an elite Wall Street Forensic Accounting & Concall Analyst working for an institutional hedge fund. "
        "Your role is to strictly audit executive management guidance against reported SEC 10-Q filing evidence. "
        "Maintain institutional tone, forensic skepticism, and cite specific numbers, dates, and promises."
    )

    promises_context = []
    for p in promises[:6]:
        r = p.get("resolution", {})
        promises_context.append(
            f"- [{p.get('call_label')}] {p.get('speaker')} ({p.get('role')}): \"{p.get('quote')}\"\n"
            f"  Result: {r.get('outcome')} (Credit y={r.get('y')}) | SEC Filing: \"{r.get('evidence_quote')}\" | Why: {r.get('why')}"
        )

    user_prompt = f"""Audit the guidance credibility track record for {ticker} ({company_meta.get('name')}, {company_meta.get('sector')}).
Leadership: {company_meta.get('ceo')} (CEO), {company_meta.get('cfo')} (CFO).
Quantitative Metrics:
- Say-Do Credibility Score: {company_score.get('score', 75.0)}/100 (Grade {company_score.get('grade', 'B')})
- 80% Bayesian Credible Interval: {company_score.get('ci80', [65, 85])}
- Wall Street Delivery Ratio: {company_score.get('delivery_ratio', 1.0):.2f}x of guided range
- Ghost Rate: {company_score.get('ghost_rate', 0)*100:.1f}%

Verified Concall vs SEC 10-Q Evidence:
{chr(10).join(promises_context)}

Synthesize a structured institutional audit memo in Markdown with these 4 sections:
### 1. Executive Verdict & Credibility Classification
(Classify as Conservative Sandbagger, Disciplined Compounder, or Habitual Over-Promiser, and explain why.)

### 2. Behavioral & Execution Patterns
(Highlight 2-3 persistent behaviors in how guidance is framed, e.g. beat-and-raise cadence, operational vs financial spreads.)

### 3. Forensic Red Flags & Goalpost Shifts
(Examine whether any commitments were revised down, postponed, or quietly dropped.)

### 4. Watchpoints for the Next Earnings Concall
(Specific guidance metrics, margin hurdles, or capex commitments analysts should cross-examine on the next call.)
"""

    res = call_meta_model(user_prompt, system_prompt=system_prompt, model=model, api_key=api_key)
    return res


def generate_meta_guidance_analysis(ticker, company_info, guided_cat, guided_val, horizon, firmness, quote, p_held, adj_target, api_key=None, model=DEFAULT_META_MODEL):
    """Generates an executive briefing on a new guidance statement using Meta Muse Spark."""
    system_prompt = (
        "You are an institutional Wall Street quantitative equity researcher specializing in post-earnings announcement drift (PEAD) "
        "and management guidance delivery forecasting. Analyze forward guidance statements using deterministic track record data."
    )

    user_prompt = f"""Analyze this newly issued forward guidance commitment for {ticker} ({company_info.get('name')}):
- Guided Metric: {guided_cat} = {guided_val}
- Horizon: {horizon}
- Management Tone / Firmness: {firmness}
- Verbatim Quote: "{quote}"

Management Historical Track Record:
- Say-Do Score: {company_info.get('score')}/100 (Grade {company_info.get('grade')})
- Historical Delivery Ratio: {company_info.get('delivery_ratio'):.2f}x
- Ghost Rate: {company_info.get('ghost_rate', 0)*100:.1f}%
- Bayesian Predicted P(Guidance Held): {p_held:.1%}
- Credibility-Adjusted Target: {adj_target}

Deliver a concise 3-paragraph institutional assessment:
1. Probability Analysis: Why does the model assign a {p_held:.1%} survival probability to this guidance?
2. Sandbagging vs Over-Promising: Does the adjusted target ({adj_target}) imply conservative sandbagging or stretch vulnerability?
3. Actionable Investor Implication: How should an institutional portfolio manager position for the next quarterly 10-Q release?
"""

    return call_meta_model(user_prompt, system_prompt=system_prompt, model=model, api_key=api_key)
