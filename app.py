import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mediterranean MPA Enforcement Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load dashboard data (the REAL model output, not the placeholder)
DATA_PATH = "data/mpa_ranking (1).parquet"
df = pd.read_parquet(DATA_PATH)

# Page state
if "page" not in st.session_state:
    st.session_state.page = "welcome"

st.markdown(
    """
<style>
.stApp {
    background-color: #f7f6f2;
    color: #262522;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Remove Streamlit's top bar entirely. It was covering the top of the
   page because .block-container padding is smaller than the bar. */
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

h1, h2, h3 {
    font-family: Georgia, serif;
    color: #262522;
}

h1 {
    font-size: 3rem;
    line-height: 1.08;
    letter-spacing: -0.03em;
}

h2 {
    font-size: 2rem;
    letter-spacing: -0.02em;
}

.eyebrow {
    color: #1f5f8b;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.intro {
    color: #62615c;
    font-size: 1rem;
    line-height: 1.65;
    max-width: 650px;
}

.notice {
    background: #fbf1e4;
    border-left: 3px solid #c47a2c;
    padding: 1rem 1.2rem;
    margin: 1.5rem 0;
    color: #5d4630;
    line-height: 1.55;
    font-size: 0.88rem;
}

.dataset-card {
    background: #eeece6;
    border: 1px solid #dedbd3;
    padding: 1.25rem;
}

.dataset-label {
    color: #9a9992;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}

.dataset-row {
    border-bottom: 1px solid #dedbd3;
    padding: 0.75rem 0;
}

.dataset-row:last-child {
    border-bottom: none;
}

.dataset-number {
    color: #1f5f8b;
    font-family: Georgia, serif;
    font-size: 1.35rem;
    display: inline-block;
    min-width: 70px;
}

.dataset-title {
    color: #262522;
    font-size: 0.82rem;
    font-weight: 500;
}

.dataset-note {
    color: #aaa79d;
    font-size: 0.68rem;
    margin-left: 70px;
    margin-top: 0.15rem;
}

.context-box {
    border: 1px solid #dedbd3;
    padding: 1rem;
    margin-top: 1rem;
    color: #77756e;
    font-size: 0.75rem;
    line-height: 1.6;
}

.stButton > button {
    background-color: #1f5f8b;
    color: white;
    border: none;
    border-radius: 0;
    padding: 0.65rem 1.25rem;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #174d72;
    color: white;
}

.site-footer {
    border-top: 1px solid #deddd7;
    margin-top: 5rem;
    padding-top: 1rem;
    color: #9a9992;
    font-size: 0.75rem;
    text-align: center;
}

/* Logo, identical to the one on the Candidate gaps page */
.brand-static {
    position: relative;
    padding-left: 36px;
    font-family: Georgia, serif;
    font-size: 15px;
    font-weight: 700;
    line-height: 24px;
    color: #262522;
}

.brand-static::before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 26px;
    height: 26px;
    background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26' fill='none' stroke='%231f5f8b' stroke-width='1.4'%3E%3Ccircle cx='13' cy='13' r='11'/%3E%3Cpath d='M5 12c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3Cpath d='M5 16c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: contain;
}

.brand-subtitle {
    color: #aaa79d;
    font-family: Arial, sans-serif;
    font-size: 8px;
    letter-spacing: 0.14em;
    margin-top: 8px;
    margin-left: 34px;
    white-space: nowrap;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# WELCOME PAGE
# ============================================================

if st.session_state.page == "welcome":

    # Header
    st.markdown(
        """
    <div style="border-bottom:1px solid #deddd7;padding:0.5rem 0 1rem 0;margin-bottom:3rem;">
    <div class="brand-static">MPA Enforcement Intelligence</div>
    <div class="brand-subtitle">MEDITERRANEAN · DECISION SUPPORT</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Main welcome layout
    left, right = st.columns([1.35, 0.9], gap="large")

    with left:

        st.markdown(
            '<div class="eyebrow">Mediterranean marine conservation · decision support tool</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
    # Mediterranean MPA<br>Enforcement Intelligence
    """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
    <div class="intro">
    Explore candidate enforcement gaps by comparing observed industrial
    fishing effort with what a comparable unprotected area would be expected
    to experience.
    </div>
    """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
    <div class="notice">
    <strong>A candidate gap is a signal for investigation, not proof of illegal
    fishing or failed enforcement.</strong> Multiple explanations may account
    for any observed difference between expected and observed fishing effort.
    This tool supports enquiry — it does not deliver verdicts.
    </div>
    """,
            unsafe_allow_html=True,
        )

        if st.button("Explore candidate gaps →"):
            st.session_state.page = "candidate_gaps"
            st.rerun()

    with right:

        st.markdown(
            """
    <div class="dataset-card">
    <div class="dataset-label">Dataset overview</div>

    <div class="dataset-row">
    <span class="dataset-number">1,288</span>
    <span class="dataset-title">Assessed MPAs</span>
    <div class="dataset-note">With sufficient AIS coverage</div>
    </div>

    <div class="dataset-row">
    <span class="dataset-number">117</span>
    <span class="dataset-title">Not assessed</span>
    <div class="dataset-note">Insufficient AIS coverage</div>
    </div>

    <div class="dataset-row">
    <span class="dataset-number">2015–</span>
    <span class="dataset-title">Analysis period</span>
    <div class="dataset-note">AIS-derived industrial effort</div>
    </div>

    <div class="dataset-row">
    <span class="dataset-number">19</span>
    <span class="dataset-title">Countries</span>
    <div class="dataset-note">Mediterranean basin</div>
    </div>

    </div>
    """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
    <div class="context-box">
    Fishing effort is derived from Automatic Identification System (AIS)
    vessel tracking data. Industrial vessels only. The candidate gap index
    compares observed effort within a protected area with modelled
    counterfactual effort at an unprotected site with comparable
    characteristics.
    </div>
    """,
            unsafe_allow_html=True,
        )

    # Footer
    st.markdown(
        """
    <div class="site-footer">
    AIS data · Industrial fishing vessels
    &nbsp; · &nbsp;
    Not a verdict. A signal for investigation.
    &nbsp; · &nbsp;
    Mediterranean basin coverage
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================
# CANDIDATE GAPS PAGE
#
# Needs: streamlit >= 1.39, plotly (in requirements.txt), and `df`
# = the FULL ranking table (assessed and not assessed rows) loaded
# above this block from the REAL file, mpa_ranking (1).parquet.
#
# Everything shown here comes from that file. Nothing is invented:
# no fishing rules, no ecological context. Priority is DERIVED at
# load time with Tiago's formula (it is not a stored column).
# ============================================================

elif st.session_state.page == "candidate_gaps":

    import html as html_lib
    import numpy as np
    import plotly.graph_objects as go

    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------

    def clean_html(markup: str) -> str:
        """
        Collapse HTML to ONE line: no indentation, no blank lines.

        Why: Streamlit passes st.markdown() through a Markdown parser.
        - a blank line ends an HTML block
        - anything indented 4+ spaces afterwards becomes a CODE BLOCK
        That is exactly why your tags were showing up as dark code boxes.
        textwrap.dedent() can't fix it because it only removes the
        *common* indent, and it never removes blank lines.
        """
        return " ".join(
            line.strip()
            for line in markup.splitlines()
            if line.strip()
        )

    def fmt_hours(value) -> str:
        # The parquet stores P - O (expected minus observed), so it is
        # NEGATIVE when there is excess fishing. For display we show
        # O - P ("excess hours"): + means more fishing than expected
        # (candidate gap), - means less than expected (protection signal).
        if pd.isna(value):
            return "—"
        excess = -float(value)
        sign = "+" if excess >= 0 else "−"
        mag = abs(excess)
        if mag >= 1000:
            txt = f"{mag / 1000:,.1f}k"
        elif mag >= 10:
            txt = f"{mag:,.0f}"
        else:
            txt = f"{mag:,.1f}"
        return f"{sign}{txt} hrs"

    def reset_candidate_filters():
        # Must run as an on_click callback. Assigning to a widget's
        # session_state key AFTER the widget was created in the same
        # run raises a StreamlitAPIException.
        st.session_state.candidate_search = ""
        st.session_state.candidate_country = "All countries"
        st.session_state.candidate_confidence = "All confidence levels"
        st.session_state.candidate_s_range = "All S values"


    # --------------------------------------------------------
    # SELECTION STATE + DETAIL-PANEL HELPERS
    # --------------------------------------------------------

    st.session_state.setdefault("selected_wdpa", None)
    st.session_state.setdefault("last_chart_pick", None)
    st.session_state.setdefault("chart_version", 0)

    def close_detail():
        st.session_state.selected_wdpa = None
        st.session_state.last_chart_pick = None
        # New chart key => Plotly forgets its old selection
        st.session_state.chart_version += 1

    def select_row(wid):
        st.session_state.selected_wdpa = int(wid)
        st.session_state.last_chart_pick = None
        # clear any dot highlight left in the Plotly chart
        st.session_state.chart_version += 1

    COUNTRY_NAMES = {
        "ALB": "Albania", "CYP": "Cyprus", "DZA": "Algeria",
        "EGY": "Egypt", "ESP": "Spain", "FRA": "France",
        "GIB": "Gibraltar", "GRC": "Greece", "HRV": "Croatia",
        "ISR": "Israel", "ITA": "Italy", "LBN": "Lebanon",
        "MAR": "Morocco", "MCO": "Monaco", "MLT": "Malta",
        "MNE": "Montenegro", "SVN": "Slovenia", "TUN": "Tunisia",
        "TUR": "Türkiye",
    }

    def severity(s):
        if s <= -0.65:
            return "Severe candidate gap", "severe"
        if s < -0.30:
            return "Moderate candidate gap", "moderate"
        if s < 0:
            return "Marginal candidate gap", "mild"
        return "Protection signal", "protection"

    SEVERITY_PALETTE = {
        "severe":     {"bg": "#fce8e6", "border": "#f0c9c4", "fg": "#a63d32"},
        "moderate":   {"bg": "#fbeee6", "border": "#f0d5c2", "fg": "#b5653f"},
        "mild":       {"bg": "#faf3e4", "border": "#ecdfbf", "fg": "#896b28"},
        "protection": {"bg": "#e9f3ec", "border": "#c9e0d1", "fg": "#377457"},
    }

    def confidence_text(row):
        """
        Confidence (data dictionary): the WEAKER of two bands, one from
        protected_fraction (how much of each grid cell the MPA fills)
        and one from observed_share (share of cell-months where AIS saw
        any vessel). We show the two real numbers instead of prose.
        """
        pf = row.get("protected_fraction")
        obs = row.get("observed_share")
        limited = str(row.get("confidence_limited_by", "") or "").strip()
        limiting = {
            "cell overlap": "cell overlap",
            "AIS coverage": "AIS coverage",
            "both": "both measures",
        }.get(limited, limited)

        parts = ["Confidence is the weaker of two measures."]
        if pd.notna(pf):
            parts.append(
                f"On average the MPA fills {float(pf):.0%} of the grid "
                "cells it touches."
            )
        if pd.notna(obs):
            parts.append(
                f"AIS recorded a vessel in {float(obs):.0%} of its "
                "cell-months."
            )
        if limiting:
            parts.append(f"Limiting factor: {html_lib.escape(limiting)}.")
        return " ".join(parts)

    def compute_priority(s_series, expected_series):
        """
        Tiago's formula, exactly as his dashboard uses it:

            priority = S >= 0 ? 0
                     : min(1, -S) * log10(1 + max(expected_hours_inside, 0))

        Areas at or above zero show no shortfall, so they score 0. Below
        zero it is the size of the shortfall (capped at 1) times the log
        of the expected hours at stake, which stops a tiny area at -0.99
        on a few hours from outranking a large one. Computed on assessed
        rows only. NOT stored in the parquet, and the file's `rank`
        column must NOT be used for ordering (it is ordered on S alone,
        logged by Tiago as a defect).
        """
        s_num = pd.to_numeric(s_series, errors="coerce")
        exp_num = pd.to_numeric(expected_series, errors="coerce").clip(lower=0)
        shortfall = (-s_num).clip(upper=1)
        priority = shortfall * np.log10(1 + exp_num)
        return priority.where(s_num < 0, 0.0).fillna(0.0)

    def fmt_total(value) -> str:
        value = float(value)
        if value >= 1000:
            return f"{value / 1000:,.1f}k hrs"
        if value >= 10:
            return f"{value:,.0f} hrs"
        return f"{value:,.1f} hrs"

    def render_provenance_bar(source_df):
        """
        Shows which prediction run produced the numbers on screen, read
        LIVE from the loaded file rather than trusted from its filename
        (a full pipeline rerun can silently overwrite the real ranking
        with the placeholder under the same filename — see Manuel's
        note). Placed in the page header, not a muted footer, so it
        cannot be missed.
        """
        sources = (
            source_df["predictions_source"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        is_placeholder = any(
            s.strip().lower() == "baseline_placeholder" for s in sources
        )
        label = html_lib.escape(" / ".join(sources) if sources else "unknown")

        if is_placeholder:
            bar_html = (
                '<div class="provenance-bar provenance-warn">'
                '⚠ PLACEHOLDER DATA — these figures are not from the real '
                f'prediction model (source: {label}). Do not use for '
                'decisions.</div>'
            )
        else:
            bar_html = (
                '<div class="provenance-bar provenance-ok">'
                f'DATA SOURCE · {label}</div>'
            )

        st.markdown(clean_html(bar_html), unsafe_allow_html=True)

    # ========================================================
    # STYLING
    # ========================================================

    CSS = """
    <style>

    /* ---------- app shell ---------- */

    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: #f4f3ef !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        display: none !important;
    }

    .block-container {
        max-width: 1180px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 4rem !important;
    }

    /* ---------- top navigation ---------- */

    .candidate-nav-subtitle {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 8px;
        letter-spacing: 0.14em;
        margin-top: -8px;
        margin-left: 34px;
        white-space: nowrap;
    }

    .candidate-active-nav {
        color: #1f5f8b;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
        text-align: center;
        padding: 11px 8px 13px 8px;
        border-bottom: 2px solid #1f5f8b;
        white-space: nowrap;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #77756e !important;
        border-radius: 0 !important;
        padding: 10px 8px 13px 8px !important;
        min-height: 0 !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
        font-weight: 400 !important;
        color: #77756e !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"]:hover,
    div[data-testid="stButton"] > button[kind="tertiary"]:hover p {
        background: transparent !important;
        color: #262522 !important;
    }

    /* Logo button: serif title + wave icon drawn with CSS */

    div.st-key-candidate_logo div[data-testid="stButton"] > button[kind="tertiary"] {
        position: relative;
        padding: 0 0 0 36px !important;
        justify-content: flex-start !important;
    }

    div.st-key-candidate_logo div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Georgia, serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #262522 !important;
    }

    div.st-key-candidate_logo button::before {
        content: "";
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 26px;
        height: 26px;
        background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26' fill='none' stroke='%231f5f8b' stroke-width='1.4'%3E%3Ccircle cx='13' cy='13' r='11'/%3E%3Cpath d='M5 12c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3Cpath d='M5 16c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
    }

    /* ---------- intro ---------- */

    .candidate-page-spacer { height: 4px; }

    .candidate-title {
        font-family: Georgia, serif;
        font-size: 26px;
        font-weight: 600;
        line-height: 1.2;
        color: #262522;
        margin: 0;
    }

    .candidate-description {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.55;
        max-width: 690px;
        margin-top: 10px;
    }

    .candidate-count-number {
        font-family: Georgia, serif;
        font-size: 26px;
        line-height: 1;
        text-align: center;
    }

    .candidate-count-label {
        font-family: Arial, sans-serif;
        color: #aaa79d;
        font-size: 9px;
        text-align: center;
        margin-top: 7px;
    }

    /* ---------- distribution ---------- */

    .distribution-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 11px;
    }

    .distribution-box {
        position: relative;
        width: 100%;
        height: 148px;
        border: 1px solid #deddd7;
        background: #f7f6f2;
        overflow: hidden;
        box-sizing: border-box;
    }

    .distribution-negative {
        position: absolute; left: 14%; right: 50%;
        top: 27px; bottom: 42px; background: #fbf4f1;
    }

    .distribution-positive {
        position: absolute; left: 50%; right: 14%;
        top: 27px; bottom: 42px; background: #f1f6f2;
    }

    .distribution-axis {
        position: absolute; left: 14%; right: 14%;
        bottom: 42px; height: 1px; background: #d5d2ca;
    }

    .distribution-zero {
        position: absolute; left: 50%;
        top: 27px; bottom: 42px; width: 1px; background: #d5d2ca;
    }

    .distribution-dot {
        position: absolute;
        width: 10px; height: 10px;
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }

    .distribution-tick {
        position: absolute;
        bottom: 22px;
        transform: translateX(-50%);
        color: #aaa79d;
        font-family: monospace;
        font-size: 9px;
    }

    .distribution-baseline {
        position: absolute;
        left: 50%;
        bottom: 6px;
        transform: translateX(-50%);
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
    }

    .distribution-note-left {
        position: absolute; left: 14%; bottom: 6px;
        color: #b25b49; font-family: Arial, sans-serif;
        font-size: 9px; font-style: italic;
    }

    .distribution-note-right {
        position: absolute; right: 14%; bottom: 6px;
        color: #377457; font-family: Arial, sans-serif;
        font-size: 9px; font-style: italic;
    }

    /* ---------- filter bar ----------
       The old version opened <div class="filter-shell"> in one
       st.markdown and closed it in another. Streamlit wraps every
       call in its own element, so the div could never contain the
       widgets (that's the empty grey strip). A keyed container
       gets a real class we can style: .st-key-filter_shell
       (needs Streamlit >= 1.39). */

    .st-key-filter_shell {
        background: #eeece6;
        border: 1px solid #dedbd3;
        padding: 10px;
        margin-top: 26px;
        margin-bottom: 24px;
    }

    div[data-testid="stTextInput"] div[data-baseweb="input"] {
        background-color: #f7f6f2 !important;
        border: 1px solid #dedbd3 !important;
        border-radius: 0 !important;
        min-height: 38px !important;
    }

    div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
        border-color: #9d9a91 !important;
        box-shadow: none !important;
    }

    div[data-testid="stTextInput"] input {
        background-color: transparent !important;
        border: none !important;
        color: #4f4d47 !important;
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
        padding-left: 34px !important;
        background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23aaa79d' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='M20 20l-4-4'/%3E%3C/svg%3E") !important;
        background-repeat: no-repeat !important;
        background-position: 12px center !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: #f7f6f2 !important;
        border: 1px solid #dedbd3 !important;
        border-radius: 0 !important;
        min-height: 38px !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] * {
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
        color: #5f5d57 !important;
    }

    div[data-testid="stSelectbox"] [data-baseweb="select"] svg {
        fill: #aaa79d !important;
    }

    div[data-baseweb="popover"] ul {
        background: #f7f6f2 !important;
    }

    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] li * {
        background: #f7f6f2 !important;
        color: #4f4d47 !important;
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
    }

    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background: #e8f0f5 !important;
    }

    .st-key-candidate_clear_filters button {
        width: 100%;
        background: #e8f0f5 !important;
        border: 1px solid #d3e1ea !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        min-height: 38px !important;
    }

    .st-key-candidate_clear_filters button p {
        color: #35617e !important;
        font-family: Arial, sans-serif !important;
        font-size: 11px !important;
        font-weight: 400 !important;
    }

    .st-key-candidate_clear_filters button:hover {
        background: #e1ebf1 !important;
        border-color: #c6d9e5 !important;
    }

    /* ---------- table ---------- */

    .table-caption {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .ranking-header,
    .ranking-row {
        display: grid;
        grid-template-columns: 2.1fr 0.85fr 0.8fr 1.45fr 1.2fr 1fr;
        align-items: center;
        padding: 0 14px;
        box-sizing: border-box;
    }

    .ranking-header {
        padding-bottom: 10px;
        border-bottom: 1px solid #cfcac0;
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .ranking-row {
        min-height: 55px;
        border-bottom: 1px solid #e4e1da;
        background: #f7f6f2;
    }

    .ranking-row:nth-of-type(even) { background: #f3f2ee; }

    .ranking-name {
        color: #262522;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 500;
    }

    .ranking-country {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }

    .ranking-s {
        display: flex;
        align-items: center;
        gap: 9px;
    }

    .ranking-s-value {
        font-family: monospace;
        font-size: 12px;
        font-weight: 600;
        min-width: 42px;
    }

    .ranking-s-bar {
        display: inline-block;
        width: 58px;
        height: 4px;
        background: #deddd7;
        position: relative;
    }

    .ranking-s-bar::after {
        content: "";
        position: absolute;
        left: 50%;
        top: -2px;
        width: 1px;
        height: 8px;
        background: #b9b5aa;
    }

    .ranking-s-fill {
        position: absolute;
        top: 0;
        height: 4px;
    }

    .ranking-gap {
        color: #a63d2d;
        font-family: monospace;
        font-size: 12px;
    }

    .confidence-tag {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
    }

    .confidence-high   { background: #dfeee5; color: #387256; }
    .confidence-medium { background: #f3ecd9; color: #896b28; }
    .confidence-low    { background: #eee5e3; color: #87594e; }

    /* ---------- selected row / scroll ---------- */

    .ranking-scroll { overflow-x: auto; }

    .ranking-scroll .ranking-header,
    .ranking-scroll .ranking-row { min-width: 720px; }

    .ranking-row.selected { background: #e4edf5 !important; }
    .ranking-row.selected .ranking-name { color: #1f5f8b; }

    /* ---------- detail panel ---------- */

    .st-key-detail_panel {
        background: #f7f6f2;
        border: 1px solid #dedbd3;
        padding: 22px 24px;
        max-height: 720px;
        overflow-y: auto;
    }

    .st-key-detail_close button {
        width: 30px;
        min-height: 0 !important;
        height: 30px;
        padding: 0 !important;
        background: #f7f6f2 !important;
        border: 1px solid #dedbd3 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }

    .st-key-detail_close button p {
        color: #77756e !important;
        font-size: 15px !important;
        line-height: 1 !important;
    }

    .detail-country {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 9px;
        letter-spacing: 0.12em;
    }

    .detail-name {
        font-family: Georgia, serif;
        font-size: 20px;
        font-weight: 600;
        color: #262522;
        margin-top: 4px;
    }

    .detail-hr {
        border-top: 1px solid #e4e1da;
        margin: 16px 0;
    }

    .detail-s-card {
        border: 1px solid;
        padding: 16px 18px;
        margin-bottom: 22px;
    }

    .detail-s-label {
        font-family: Arial, sans-serif;
        font-size: 9px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .detail-s-value {
        font-family: monospace;
        font-size: 44px;
        line-height: 1.15;
        margin: 6px 0 4px 0;
    }

    .detail-sev {
        font-family: Arial, sans-serif;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 8px;
    }

    .detail-desc {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 12px;
        line-height: 1.5;
    }

    .detail-section-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .detail-effort-row,
    .detail-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: monospace;
        font-size: 12px;
        margin-top: 10px;
    }

    .detail-effort-row span:first-child {
        font-family: Arial, sans-serif;
        color: #4f4d47;
    }

    .detail-track {
        height: 4px;
        background: #e4e1da;
        margin-top: 6px;
    }

    .detail-track div { height: 4px; }

    .detail-gap {
        font-family: monospace;
        font-size: 15px;
        font-weight: 600;
    }

    .detail-text {
        color: #4f4d47;
        font-family: Arial, sans-serif;
        font-size: 12px;
        line-height: 1.55;
    }

    .detail-note {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 12px;
        line-height: 1.55;
        margin-top: 8px;
    }

    /* ---------- clickable rows ---------- */

    .st-key-table_wrap {
        overflow-x: auto;
        gap: 0 !important;
    }

    .st-key-table_wrap > * { min-width: 720px; }

    div[class*="st-key-tablerow_"] {
        position: relative;
        gap: 0 !important;
    }

    /* invisible button stretched over the whole row */
    div[class*="st-key-rowbtn_"] {
        position: absolute !important;
        top: 0; left: 0;
        width: 100% !important;
        height: 100% !important;
    }

    div[class*="st-key-rowbtn_"] button {
        width: 100% !important;
        height: 100% !important;
        opacity: 0;
        cursor: pointer;
        border: none !important;
        background: transparent !important;
    }

    .ranking-row.alt { background: #f3f2ee; }

    div[class*="st-key-tablerow_"]:hover .ranking-row:not(.selected) {
        background: #eceae4;
    }

    /* ---------- provenance bar ---------- */

    .provenance-bar {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        margin-top: 12px;
        font-family: Arial, sans-serif;
        font-size: 10.5px;
    }

    .provenance-ok {
        background: #f4f3ef;
        border: 1px solid #dedbd3;
        color: #77756e;
    }

    .provenance-warn {
        background: #fdecea;
        border: 1px solid #e8b4ac;
        color: #a63d2d;
        font-weight: 600;
    }

    /* ---------- priority column, notes, show-more ---------- */

    .ranking-header .active-sort { color: #1f5f8b; }

    .ranking-priority {
        font-family: monospace;
        font-size: 12px;
        font-weight: 600;
        color: #262522;
    }

    .ranking-priority.zero {
        color: #aaa79d;
        font-weight: 400;
    }

    .table-note {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 11px;
        line-height: 1.55;
        max-width: 720px;
        margin: -2px 0 16px 0;
    }

    .table-count {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 10px;
        padding-top: 14px;
    }

    .st-key-show_more button {
        width: 100%;
        margin-top: 8px;
        background: #e8f0f5 !important;
        border: 1px solid #d3e1ea !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        min-height: 34px !important;
    }

    .st-key-show_more button p {
        color: #35617e !important;
        font-family: Arial, sans-serif !important;
        font-size: 11px !important;
        font-weight: 400 !important;
    }

    .st-key-show_more button:hover {
        background: #e1ebf1 !important;
        border-color: #c6d9e5 !important;
    }

    </style>
    """

    st.markdown(clean_html(CSS), unsafe_allow_html=True)

    # ========================================================
    # TOP NAVIGATION
    # ========================================================

    nav_logo, nav_candidate, nav_not, nav_method = st.columns(
        [4.7, 1, 1, 1],
        gap="small",
    )

    with nav_logo:

        if st.button(
            "MPA Enforcement Intelligence",
            key="candidate_logo",
            type="tertiary",
        ):
            st.session_state.page = "welcome"
            st.rerun()

        st.markdown(
            clean_html(
                """
                <div class="candidate-nav-subtitle">
                    MEDITERRANEAN · DECISION SUPPORT
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with nav_candidate:

        st.markdown(
            clean_html(
                """
                <div class="candidate-active-nav">
                    Candidate gaps
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with nav_not:
        if st.button(
            "Not assessed",
            key="candidate_not_assessed_nav",
            type="tertiary",
        ):
            st.session_state.page = "not_assessed"
            st.rerun()

    with nav_method:
       st.button(
        "Methodology",
        key="candidate_methodology_nav",
        type="tertiary",
        on_click=lambda: st.session_state.update(page="methodology"),
    )

    render_provenance_bar(df)

    # ========================================================
    # INTRO
    # ========================================================

    # Read straight from df rather than hardcoding, so this can never
    # drift out of sync with whatever file is actually loaded.
    n_assessed = int((df["assessed"] == True).sum())
    n_not_assessed = int((df["assessed"] == False).sum())

    st.markdown(
        "<div class='candidate-page-spacer'></div>",
        unsafe_allow_html=True,
    )

    intro, count_a, count_b = st.columns(
        [5.3, 1, 1],
        gap="large",
    )

    with intro:

        st.markdown(
            clean_html(
                """
                <div class="candidate-title">
                    Candidate Gap Index — S
                </div>
                <div class="candidate-description">
                    S measures how much observed industrial fishing effort
                    differs from modelled counterfactual effort. Negative
                    values indicate more fishing than expected; positive
                    values indicate less. A low score is a signal for
                    investigation only.
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with count_a:

        st.markdown(
            clean_html(
                f"""
                <div class="candidate-count-number" style="color:#1f5f8b;">
                    {n_assessed:,}
                </div>
                <div class="candidate-count-label">assessed MPAs</div>
                """
            ),
            unsafe_allow_html=True,
        )

    with count_b:

        st.markdown(
            clean_html(
                f"""
                <div class="candidate-count-number" style="color:#aaa79d;">
                    {n_not_assessed:,}
                </div>
                <div class="candidate-count-label">not assessed</div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.markdown(
        "<div style='border-bottom:1px solid #deddd7;"
        "margin-top:26px;margin-bottom:35px;'></div>",
        unsafe_allow_html=True,
    )

    # ========================================================
    # LOAD ASSESSED DATA
    # ========================================================

    assessed_df = df[df["assessed"] == True].copy()

    assessed_df["S"] = pd.to_numeric(assessed_df["S"], errors="coerce")
    assessed_df = assessed_df.dropna(subset=["S"])
    assessed_df["country"] = (
        assessed_df["iso3"].map(COUNTRY_NAMES).fillna(assessed_df["iso3"])
    )

    # Normalise on read (Manuel): the file uses High / Medium / Low, but
    # never trust the casing.
    assessed_df["confidence"] = (
        assessed_df["confidence"].astype(str).str.strip().str.lower()
    )

    assessed_df["priority"] = compute_priority(
        assessed_df["S"], assessed_df["expected_hours_inside"]
    )

    # TODO(duplicates): overlapping designations of one site appear as
    # several rows here (e.g. Delta de l'Ebre and Cap de Creus x3, with
    # identical numbers). Tiago's dashboard folds them into one row
    # (1,129 rows vs 1,288 assessed). The parquet is NOT folded and we
    # do not have his grouping rule yet. Apply it right here, before
    # anything below, once he confirms it.

    # ========================================================
    # DISTRIBUTION (Plotly, so dots can be clicked)
    # ========================================================

    st.markdown(
        clean_html(
            """
            <div class="distribution-label">
                S distribution · sample of 20 assessed MPAs · click to select
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    sorted_sample = assessed_df.sort_values("S").reset_index(drop=True)

    if len(sorted_sample) > 20:
        positions = [
            round(i * (len(sorted_sample) - 1) / 19)
            for i in range(20)
        ]
        distribution_df = sorted_sample.iloc[positions].reset_index(drop=True)
    else:
        distribution_df = sorted_sample.copy()

    dot_heights = [
        69, 48, 34, 57, 43,
        62, 45, 57, 37, 51,
        40, 60, 47, 31, 56,
        43, 61, 38, 55, 45,
    ]

    def dot_color_for(s):
        if s < -0.65:
            return "#a63d32"
        if s < -0.30:
            return "#c2674e"
        if s < 0:
            return "#c88c51"
        if s < 0.35:
            return "#8b8b78"
        if s < 0.70:
            return "#4f8568"
        return "#28664b"

    xs, ys, hover, colors = [], [], [], []

    for i, (_, r) in enumerate(distribution_df.iterrows()):
        s_val = float(r["S"])

        xs.append(s_val)
        ys.append(100 - dot_heights[i % len(dot_heights)])
        hover.append(f'{r["mpa_name"]} · S {s_val:+.2f}')
        colors.append(dot_color_for(s_val))

    fig = go.Figure()

    Y_BOTTOM, Y_TOP = 28.4, 81.8

    fig.add_shape(type="rect", x0=-1, x1=0, y0=Y_BOTTOM, y1=Y_TOP,
                  fillcolor="#fbf4f1", line_width=0, layer="below")
    fig.add_shape(type="rect", x0=0, x1=1, y0=Y_BOTTOM, y1=Y_TOP,
                  fillcolor="#f1f6f2", line_width=0, layer="below")
    fig.add_shape(type="line", x0=-1, x1=1, y0=Y_BOTTOM, y1=Y_BOTTOM,
                  line=dict(color="#d5d2ca", width=1), layer="below")
    fig.add_shape(type="line", x0=0, x1=0, y0=Y_BOTTOM, y1=Y_TOP,
                  line=dict(color="#d5d2ca", width=1), layer="below")

    for tick, label in [(-1, "−1"), (-0.5, "−0.5"), (0, "0"),
                        (0.5, "+0.5"), (1, "+1")]:
        fig.add_shape(type="line", x0=tick, x1=tick,
                      y0=Y_BOTTOM, y1=Y_BOTTOM - 4,
                      line=dict(color="#d5d2ca", width=1), layer="below")
        fig.add_annotation(x=tick, y=17, text=label, showarrow=False,
                           font=dict(family="monospace", size=10,
                                     color="#aaa79d"))

    fig.add_annotation(x=-1, y=4, xanchor="left", showarrow=False,
                       text="<i>← candidate gap</i>",
                       font=dict(family="Arial", size=10, color="#b25b49"))
    fig.add_annotation(x=0, y=4, showarrow=False, text="baseline",
                       font=dict(family="Arial", size=10, color="#aaa79d"))
    fig.add_annotation(x=1, y=4, xanchor="right", showarrow=False,
                       text="<i>protection signal →</i>",
                       font=dict(family="Arial", size=10, color="#377457"))

    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="markers",
            text=hover,
            hovertemplate="%{text}<extra></extra>",
            marker=dict(size=10, color=colors),
            # Highlighting is done by Plotly itself (NOT by rebuilding the
            # figure): if the figure changes on every click, Streamlit
            # treats it as a new widget, drops the selection and loops.
            selected=dict(marker=dict(opacity=1, size=15)),
            unselected=dict(marker=dict(opacity=0.4)),
            hoverlabel=dict(
                bgcolor="#262522",
                bordercolor="#262522",
                font=dict(family="Arial", size=11, color="#ffffff"),
            ),
        )
    )

    # x range chosen so -1 and +1 sit at 14% and 86% of the width
    fig.update_layout(
        height=148,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#f7f6f2",
        plot_bgcolor="#f7f6f2",
        showlegend=False,
        xaxis=dict(range=[-1.389, 1.389], visible=False, fixedrange=True),
        yaxis=dict(range=[0, 100], visible=False, fixedrange=True),
    )

    event = st.plotly_chart(
        fig,
        theme=None,
        key=f"dist_chart_{st.session_state.chart_version}",
        on_select="rerun",
        selection_mode="points",
        config={"displayModeBar": False},
    )

    picked = None
    try:
        pts = event.selection.points
        if pts:
            picked = int(
                distribution_df.iloc[pts[0]["point_index"]]["wdpa_id"]
            )
    except Exception:
        picked = None

    # Only react when the chart selection actually CHANGES, so that
    # closing the panel / (later) selecting a table row isn't undone.
    if picked != st.session_state.last_chart_pick:
        st.session_state.last_chart_pick = picked
        st.session_state.selected_wdpa = picked

    # ========================================================
    # FILTER BAR
    # ========================================================

    with st.container(key="filter_shell"):

        f1, f2, f3, f4, f5 = st.columns(
            [2.65, 1.15, 1.4, 1.3, 0.9],
            gap="small",
        )

        with f1:
            search_value = st.text_input(
                "Search",
                placeholder="Search by name or country...",
                label_visibility="collapsed",
                key="candidate_search",
            )

        with f2:
            countries = ["All countries"] + sorted(
                assessed_df["country"].dropna().astype(str).unique().tolist()
            )
            selected_country = st.selectbox(
                "Country",
                countries,
                label_visibility="collapsed",
                key="candidate_country",
            )

        with f3:
            selected_confidence = st.selectbox(
                "Confidence",
                ["All confidence levels", "High", "Medium", "Low"],
                label_visibility="collapsed",
                key="candidate_confidence",
            )

        with f4:
            selected_s = st.selectbox(
                "S range",
                [
                    "All S values",
                    "Candidate gaps (S < 0)",
                    "Protection signal (S ≥ 0)",
                ],
                label_visibility="collapsed",
                key="candidate_s_range",
            )

        with f5:
            st.button(
                "Clear filters",
                key="candidate_clear_filters",
                type="secondary",
                on_click=reset_candidate_filters,
            )

    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_df = assessed_df.copy()

    if search_value:
        q = search_value.lower()

        name_match = (
            filtered_df["mpa_name"].fillna("").astype(str)
            .str.lower().str.contains(q, regex=False)
        )
        country_match = (
            filtered_df["country"].fillna("").astype(str)
            .str.lower().str.contains(q, regex=False)
        ) | (
            filtered_df["iso3"].fillna("").astype(str)
            .str.lower().str.contains(q, regex=False)
        )
        filtered_df = filtered_df[name_match | country_match]

    if selected_country != "All countries":
        filtered_df = filtered_df[
            filtered_df["country"].astype(str) == selected_country
        ]

    if selected_confidence != "All confidence levels":
        filtered_df = filtered_df[
            filtered_df["confidence"].astype(str).str.lower()
            == selected_confidence.lower()
        ]

    if selected_s == "Candidate gaps (S < 0)":
        filtered_df = filtered_df[filtered_df["S"] < 0]
    elif selected_s == "Protection signal (S ≥ 0)":
        filtered_df = filtered_df[filtered_df["S"] >= 0]

    # ========================================================
    # DETAIL PANEL
    # ========================================================

    def render_detail(row):

        s_value = float(row["S"])
        sev_label, sev_key = severity(s_value)
        pal = SEVERITY_PALETTE[sev_key]

        name = html_lib.escape(str(row["mpa_name"]))
        country = html_lib.escape(str(row["country"]))

        expected = float(row["expected_hours_inside"])
        gap_pq = float(row["abs_gap_hours"])          # P - O
        observed = max(0.0, expected - gap_pq)        # O = P - (P - O)

        scale = max(observed, expected, 1e-9)
        obs_w = observed / scale * 100
        exp_w = expected / scale * 100

        try:
            period = (
                f"{pd.Timestamp(row['first_month']).year}–"
                f"{pd.Timestamp(row['last_month']).year}"
            )
        except Exception:
            period = "analysis period"

        confidence = str(row["confidence"]).strip()
        conf_class = {
            "high": "confidence-high",
            "medium": "confidence-medium",
            "low": "confidence-low",
        }.get(confidence.lower(), "confidence-medium")

        conf_text = confidence_text(row)
        priority_value = float(row.get("priority", 0))

        if s_value < 0:
            s_desc = (
                "Observed fishing effort exceeds the modelled counterfactual. "
                "This is a signal for investigation."
            )
            gap_desc = (
                "Excess hours represent the absolute scale of the "
                "observed–expected discrepancy. A large absolute gap at a "
                "moderate relative gap can still represent a substantial "
                "enforcement challenge."
            )
            gap_color = "#a63d2d"
            priority_desc = (
                "Shortfall × log10(1 + expected hours). This is what ranks "
                "the table: it favours areas where a lot of fishing was "
                "expected, so a small area cannot top the list on a few "
                "hours alone."
            )
        else:
            priority_desc = (
                "No shortfall (S of 0 or above), so priority is 0."
            )
            s_desc = (
                "Observed fishing effort is below the modelled counterfactual. "
                "This is consistent with a protection effect but does not "
                "prove one."
            )
            gap_desc = (
                "Negative hours mean less fishing was observed than the "
                "model expected."
            )
            gap_color = "#377457"

        iucn = html_lib.escape(str(row.get("iucn_cat", "—")))
        site_raw = str(row.get("site_type", "—"))
        site_type = html_lib.escape(
            {"PA": "Protected area"}.get(site_raw, site_raw)
        )
        status_year = row.get("status_year", None)
        year_known = bool(row.get("designation_year_known", True))
        area = row.get("area_km2", None)
        n_cells = row.get("n_cells", None)

        context_bits = [
            f"IUCN category: {iucn}",
            f"Site type: {site_type}",
        ]
        # status_year is 0 exactly where the designation year is unknown
        # (88 sites), so never print the raw 0.
        if year_known and pd.notna(status_year) and int(status_year) > 0:
            context_bits.append(f"Designated: {int(status_year)}")
        else:
            context_bits.append("Designation year: unknown")
        if pd.notna(area):
            context_bits.append(f"Area: {float(area):,.1f} km²")
        if pd.notna(n_cells):
            context_bits.append(f"AIS grid cells used: {int(n_cells):,}")
        if row.get("resolvable", True) is False or row.get("resolvable") == False:
            context_bits.append(
                "Smaller than one 0.1° grid cell, so the estimate is coarse."
            )
        context_html = "<br>".join(context_bits)

        head_l, head_r = st.columns([6, 1], gap="small")

        with head_l:
            st.markdown(
                clean_html(
                    f"""
                    <div class="detail-country">{country.upper()}</div>
                    <div class="detail-name">{name}</div>
                    """
                ),
                unsafe_allow_html=True,
            )

        with head_r:
            st.button(
                "×",
                key="detail_close",
                type="secondary",
                on_click=close_detail,
            )

        st.markdown(
            clean_html(
                f"""
                <div class="detail-hr"></div>

                <div class="detail-s-card"
                     style="background:{pal['bg']};border-color:{pal['border']};">
                    <div class="detail-s-label" style="color:{pal['fg']};">
                        S / candidate gap index
                    </div>
                    <div class="detail-s-value" style="color:{pal['fg']};">
                        {s_value:+.2f}
                    </div>
                    <div class="detail-sev" style="color:{pal['fg']};">
                        {sev_label}
                    </div>
                    <div class="detail-desc">{s_desc}</div>
                </div>

                <div class="detail-section-label">
                    Effort comparison (total hours, {period})
                </div>

                <div class="detail-effort-row">
                    <span>Observed effort</span>
                    <span style="color:#a63d32;">{fmt_total(observed)}</span>
                </div>
                <div class="detail-track">
                    <div style="width:{obs_w:.1f}%;background:#a63d32;"></div>
                </div>

                <div class="detail-effort-row">
                    <span>Expected effort (counterfactual)</span>
                    <span style="color:#1f5f8b;">{fmt_total(expected)}</span>
                </div>
                <div class="detail-track">
                    <div style="width:{exp_w:.1f}%;background:#1f5f8b;"></div>
                </div>

                <div class="detail-hr"></div>

                <div class="detail-row">
                    <span class="detail-text">Absolute gap</span>
                    <span class="detail-gap" style="color:{gap_color};">
                        {fmt_hours(gap_pq)}
                    </span>
                </div>
                <div class="detail-note">{gap_desc}</div>

                <div class="detail-row" style="margin-top:18px;">
                    <span class="detail-text">Priority score</span>
                    <span class="detail-gap">{priority_value:.2f}</span>
                </div>
                <div class="detail-note">{priority_desc}</div>

                <div class="detail-hr"></div>

                <div class="detail-row">
                    <span class="detail-section-label">Confidence</span>
                    <span class="confidence-tag {conf_class}">
                        {html_lib.escape(confidence.capitalize())}
                    </span>
                </div>
                <div class="detail-text">{conf_text}</div>

                <div class="detail-hr"></div>

                <div class="detail-section-label">Context</div>
                <div class="detail-text">{context_html}</div>

                <div class="detail-hr"></div>

                <div class="detail-section-label">Caveat</div>
                <div class="detail-note">
                    A candidate gap is a signal for investigation, not proof
                    of illegal fishing or failed enforcement.
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    # ========================================================
    # TABLE (+ detail panel when something is selected)
    # ========================================================

    selected_row = None
    if st.session_state.selected_wdpa is not None:
        match = assessed_df[
            assessed_df["wdpa_id"] == st.session_state.selected_wdpa
        ]
        if len(match):
            selected_row = match.iloc[0]

    if selected_row is not None:
        table_col, panel_col = st.columns([1.85, 1], gap="large")
    else:
        table_col, panel_col = st.container(), None

    # Default order: priority DESCENDING (Tiago). Ties (every S >= 0 area
    # scores 0) are broken by S ascending, so the most negative comes first.
    table_df = filtered_df.sort_values(
        ["priority", "S"], ascending=[False, True]
    ).copy()

    # "Show more" pagination. Reset to 10 whenever a filter changes so
    # the person is never left looking at row 40 of a different list.
    filter_signature = (
        search_value, selected_country, selected_confidence, selected_s,
    )
    if st.session_state.get("table_sig") != filter_signature:
        st.session_state.table_sig = filter_signature
        st.session_state.table_limit = 10
    st.session_state.setdefault("table_limit", 10)

    def show_more_rows():
        st.session_state.table_limit += 10

    n_matching = len(table_df)
    n_shown = min(st.session_state.table_limit, n_matching)

    row_items = []   # (wdpa_id, html)

    for idx, (_, row) in enumerate(table_df.head(n_shown).iterrows()):

        name = html_lib.escape(str(row.get("mpa_name", "Unnamed MPA")))
        country = html_lib.escape(str(row.get("country", "—")))
        s_value = float(row.get("S", 0))
        priority_value = float(row.get("priority", 0))
        gap_text = fmt_hours(row.get("abs_gap_hours", None))

        confidence = str(row.get("confidence", "not assessed")).strip()

        confidence_class = {
            "high": "confidence-high",
            "medium": "confidence-medium",
            "low": "confidence-low",
        }.get(confidence.lower(), "confidence-medium")

        color = "#a63d32" if s_value < 0 else "#377457"

        half = 29
        fill_w = min(half, abs(s_value) * half)
        fill_left = half - fill_w if s_value < 0 else half

        wid = int(row["wdpa_id"])
        is_selected = (
            selected_row is not None
            and wid == int(selected_row["wdpa_id"])
        )

        row_class = "ranking-row"
        if idx % 2 == 1:
            row_class += " alt"
        if is_selected:
            row_class += " selected"

        row_html = (
            f'<div class="{row_class}">'
            f'<div class="ranking-name">{name}</div>'
            f'<div class="ranking-country">{country}</div>'
            + (
                f'<div class="ranking-priority">{priority_value:.2f}</div>'
                if priority_value > 0
                else '<div class="ranking-priority zero">0</div>'
            )
            + '<div class="ranking-s">'
            f'<span class="ranking-s-value" style="color:{color};">'
            f'{s_value:+.2f}</span>'
            '<span class="ranking-s-bar">'
            f'<span class="ranking-s-fill" style="left:{fill_left:.1f}px;'
            f'width:{fill_w:.1f}px;background:{color};"></span>'
            '</span></div>'
            f'<div class="ranking-gap" style="color:{color};">'
            f'{gap_text}</div>'
            f'<div><span class="confidence-tag {confidence_class}">'
            f'{html_lib.escape(confidence.capitalize())}</span></div>'
            '</div>'
        )

        row_items.append((wid, row_html))

    header_html = (
        '<div class="ranking-header">'
        '<div>Protected area ↕</div>'
        '<div>Country ↕</div>'
        '<div class="active-sort">Priority ↓</div>'
        '<div>S / candidate gap ↕</div>'
        '<div>Abs. gap (hrs) ↕</div>'
        '<div>Confidence ↕</div>'
        '</div>'
    )

    with table_col:
        st.markdown(
            clean_html(
                """
                <div class="table-caption">
                    Protected areas · ranked by priority
                </div>
                <div class="table-note">
                    Priority weights the size of the shortfall (S below 0)
                    by the fishing hours expected there, so small areas
                    with little at stake do not outrank large ones. Areas
                    with S of 0 or above score 0. S and the absolute gap
                    stay alongside it.
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        with st.container(key="table_wrap"):

            st.markdown(header_html, unsafe_allow_html=True)

            for idx, (wid, row_html) in enumerate(row_items):
                with st.container(key=f"tablerow_{idx}"):
                    st.markdown(row_html, unsafe_allow_html=True)
                    st.button(
                        "Select",
                        key=f"rowbtn_{idx}",
                        on_click=select_row,
                        args=(wid,),
                    )

            if len(table_df) == 0:
                st.markdown(
                    '<div style="padding:35px;text-align:center;'
                    'color:#77756e;font-size:12px;">'
                    'No assessed protected areas match these filters.</div>',
                    unsafe_allow_html=True,
                )

        if n_matching > 0:
            foot_l, foot_r = st.columns([3, 1], gap="small")
            with foot_l:
                st.markdown(
                    clean_html(
                        f"""
                        <div class="table-count">
                            Showing {n_shown:,} of {n_matching:,} assessed
                            protected areas
                        </div>
                        """
                    ),
                    unsafe_allow_html=True,
                )
            with foot_r:
                if n_shown < n_matching:
                    st.button(
                        "Show 10 more",
                        key="show_more",
                        type="secondary",
                        on_click=show_more_rows,
                    )

    if panel_col is not None:
        with panel_col:
            with st.container(key="detail_panel"):
                render_detail(selected_row)
# ============================================================
# NOT ASSESSED PAGE
# Paste this block directly AFTER the candidate_gaps block
# (it starts with `elif`, so it continues the same if/elif chain).
# ============================================================

elif st.session_state.page == "not_assessed":

    import html as html_lib

    def clean_html(markup: str) -> str:
        """One line, no indentation, no blank lines (see candidate page)."""
        return " ".join(
            line.strip() for line in markup.splitlines() if line.strip()
        )

    COUNTRY_NAMES = {
        "ALB": "Albania", "CYP": "Cyprus", "DZA": "Algeria",
        "EGY": "Egypt", "ESP": "Spain", "FRA": "France",
        "GIB": "Gibraltar", "GRC": "Greece", "HRV": "Croatia",
        "ISR": "Israel", "ITA": "Italy", "LBN": "Lebanon",
        "MAR": "Morocco", "MCO": "Monaco", "MLT": "Malta",
        "MNE": "Montenegro", "SVN": "Slovenia", "TUN": "Tunisia",
        "TUR": "Türkiye",
    }

    def go_to(page_name):
        st.session_state.page = page_name

    def render_provenance_bar(source_df):
        """
        Same logic as the Candidate gaps page: shows which prediction
        run produced the numbers, read LIVE from the loaded file rather
        than trusted from its filename. Manuel's note applies to every
        page that reads the ranking, not just Candidate gaps.
        """
        sources = (
            source_df["predictions_source"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        is_placeholder = any(
            s.strip().lower() == "baseline_placeholder" for s in sources
        )
        label = html_lib.escape(" / ".join(sources) if sources else "unknown")

        if is_placeholder:
            bar_html = (
                '<div class="provenance-bar provenance-warn">'
                '⚠ PLACEHOLDER DATA — these figures are not from the real '
                f'prediction model (source: {label}). Do not use for '
                'decisions.</div>'
            )
        else:
            bar_html = (
                '<div class="provenance-bar provenance-ok">'
                f'DATA SOURCE · {label}</div>'
            )

        st.markdown(clean_html(bar_html), unsafe_allow_html=True)

    # ========================================================
    # STYLING
    # ========================================================

    NA_CSS = """
    <style>

    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: #f4f3ef !important;
    }

    header[data-testid="stHeader"] { background: transparent !important; }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"] { display: none !important; }

    .block-container {
        max-width: 1180px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 4rem !important;
    }

    /* ---------- navigation (same as Candidate gaps) ---------- */

    .candidate-nav-subtitle {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 8px;
        letter-spacing: 0.14em;
        margin-top: -8px;
        margin-left: 34px;
        white-space: nowrap;
    }

    .candidate-active-nav {
        color: #1f5f8b;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
        text-align: center;
        padding: 11px 8px 13px 8px;
        border-bottom: 2px solid #1f5f8b;
        white-space: nowrap;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #77756e !important;
        border-radius: 0 !important;
        padding: 10px 8px 13px 8px !important;
        min-height: 0 !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
        font-weight: 400 !important;
        color: #77756e !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"]:hover,
    div[data-testid="stButton"] > button[kind="tertiary"]:hover p {
        background: transparent !important;
        color: #262522 !important;
    }

    div.st-key-na_logo div[data-testid="stButton"] > button[kind="tertiary"] {
        position: relative;
        padding: 0 0 0 36px !important;
        justify-content: flex-start !important;
    }

    div.st-key-na_logo div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Georgia, serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #262522 !important;
    }

    div.st-key-na_logo button::before {
        content: "";
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 26px;
        height: 26px;
        background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26' fill='none' stroke='%231f5f8b' stroke-width='1.4'%3E%3Ccircle cx='13' cy='13' r='11'/%3E%3Cpath d='M5 12c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3Cpath d='M5 16c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
    }

    /* ---------- intro ---------- */

    .na-title {
        font-family: Georgia, serif;
        font-size: 26px;
        font-weight: 600;
        line-height: 1.2;
        color: #262522;
        margin: 0;
    }

    .na-description {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.55;
        max-width: 690px;
        margin-top: 10px;
    }

    /* ---------- explanation box ---------- */

    .na-info {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 40px;
        background: #eeece6;
        border: 1px solid #dedbd3;
        padding: 24px 28px 28px 28px;
        margin: 34px 0 40px 0;
    }

    .na-info-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .na-info-text {
        color: #4f4d47;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.6;
    }

    .na-info-strong {
        color: #262522;
        font-weight: 600;
    }

    .na-info-muted {
        color: #77756e;
        margin-top: 8px;
    }

    /* ---------- table ---------- */

    .na-scroll { overflow-x: auto; }

    .na-header,
    .na-row {
        display: grid;
        grid-template-columns: 2.2fr 1fr 4fr 1fr;
        align-items: center;
        column-gap: 16px;
        padding: 0 14px;
        box-sizing: border-box;
        min-width: 640px;
    }

    .na-header {
        padding-bottom: 12px;
        border-bottom: 1px solid #cfcac0;
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .na-row {
        min-height: 62px;
        border-bottom: 1px solid #e4e1da;
        background: #f7f6f2;
    }

    .na-row.alt { background: #f3f2ee; }

    .na-name {
        color: #262522;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 500;
    }

    .na-country {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }

    .na-reason {
        color: #4f4d47;
        font-family: Arial, sans-serif;
        font-size: 11px;
        line-height: 1.5;
    }

    .na-reason-sub {
        color: #aaa79d;
        margin-top: 2px;
    }

    .na-area {
        color: #aaa79d;
        font-family: monospace;
        font-size: 12px;
        text-align: right;
    }

    .na-header > div:last-child { text-align: right; }

    /* ---------- provenance bar ---------- */

    .provenance-bar {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        margin-top: 12px;
        font-family: Arial, sans-serif;
        font-size: 10.5px;
    }

    .provenance-ok {
        background: #f4f3ef;
        border: 1px solid #dedbd3;
        color: #77756e;
    }

    .provenance-warn {
        background: #fdecea;
        border: 1px solid #e8b4ac;
        color: #a63d2d;
        font-weight: 600;
    }

    </style>
    """

    st.markdown(clean_html(NA_CSS), unsafe_allow_html=True)

    # ========================================================
    # TOP NAVIGATION
    # ========================================================

    nav_logo, nav_candidate, nav_not, nav_method = st.columns(
        [4.7, 1, 1, 1],
        gap="small",
    )

    with nav_logo:
        st.button(
            "MPA Enforcement Intelligence",
            key="na_logo",
            type="tertiary",
            on_click=go_to,
            args=("welcome",),
        )
        st.markdown(
            clean_html(
                """
                <div class="candidate-nav-subtitle">
                    MEDITERRANEAN · DECISION SUPPORT
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with nav_candidate:
        st.button(
            "Candidate gaps",
            key="na_candidate_nav",
            type="tertiary",
            on_click=go_to,
            args=("candidate_gaps",),
        )

    with nav_not:
        st.markdown(
            clean_html(
                """
                <div class="candidate-active-nav">Not assessed</div>
                """
            ),
            unsafe_allow_html=True,
        )

    with nav_method:
    st.button(
        "Methodology",
        key="na_methodology_nav",
        type="tertiary",
        on_click=go_to,
        args=("methodology",),
    )

    render_provenance_bar(df)

    # ========================================================
    # DATA
    # ========================================================

    not_assessed_df = df[df["assessed"] == False].copy()

    not_assessed_df["country"] = (
        not_assessed_df["iso3"]
        .map(COUNTRY_NAMES)
        .fillna(not_assessed_df["iso3"])
    )

    # NOTE: S, observed hours and rank exist in the file for these rows
    # but are deliberately NOT displayed: an unassessed MPA must never
    # look like "no fishing" or "good protection".

    not_assessed_df = not_assessed_df.sort_values(
        ["country", "mpa_name"]
    ).reset_index(drop=True)

    n_not_assessed = len(not_assessed_df)

    # ========================================================
    # INTRO
    # ========================================================

    st.markdown(
        clean_html(
            f"""
            <div style="height:4px;"></div>
            <div class="na-title">{n_not_assessed:,} MPAs not assessed</div>
            <div class="na-description">
                Insufficient Automatic Identification System (AIS) coverage
                means the available vessel tracking data cannot support a
                reliable assessment for these protected areas.
            </div>
            <div style="border-bottom:1px solid #deddd7;
                        margin-top:26px;"></div>
            """
        ),
        unsafe_allow_html=True,
    )

    # ========================================================
    # EXPLANATION BOX
    # ========================================================

    st.markdown(
        clean_html(
            """
            <div class="na-info">

                <div>
                    <div class="na-info-label">Why not assessed?</div>
                    <div class="na-info-text">
                        AIS coverage must meet minimum density thresholds to
                        produce a reliable estimate. Where coverage is below
                        threshold, the model cannot generate a credible
                        counterfactual.
                    </div>
                </div>

                <div>
                    <div class="na-info-label">Critical distinction</div>
                    <div class="na-info-text">
                        <div class="na-info-strong">
                            Absence of recorded AIS activity ≠ absence of
                            fishing.
                        </div>
                        <div class="na-info-muted">
                            Low AIS density can reflect limited transponder
                            use or coverage, not a genuine absence of effort.
                        </div>
                    </div>
                </div>

                <div>
                    <div class="na-info-label">What this means</div>
                    <div class="na-info-text">
                        These MPAs are excluded from the ranking. This is not
                        a positive indicator. It reflects a monitoring gap,
                        not a protection outcome.
                    </div>
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    # ========================================================
    # TABLE
    # ========================================================

    def fmt_area(value):
        if pd.isna(value):
            return "—"
        value = float(value)
        return f"{value:,.2f}" if value < 1 else f"{value:,.1f}"

    rows_html = ""

    for idx, row in not_assessed_df.iterrows():

        name = html_lib.escape(str(row["mpa_name"]))
        country = html_lib.escape(str(row["country"]))

        reason = str(row.get("not_assessed_reason", "") or "").strip()
        reason = html_lib.escape(
            reason[:1].upper() + reason[1:]
            if reason
            else "Insufficient AIS coverage to assess"
        )

        sub_bits = []
        if pd.notna(row.get("n_cells")):
            n_cells = int(row["n_cells"])
            sub_bits.append(f"{n_cells:,} grid cell{'s' if n_cells != 1 else ''}")
        if pd.notna(row.get("n_cell_months")):
            sub_bits.append(
                f"{int(row['n_cell_months']):,} cell-months in the analysis window"
            )
        sub_html = (
            f'<div class="na-reason-sub">{" · ".join(sub_bits)}</div>'
            if sub_bits
            else ""
        )

        alt = " alt" if idx % 2 == 1 else ""

        rows_html += (
            f'<div class="na-row{alt}">'
            f'<div class="na-name">{name}</div>'
            f'<div class="na-country">{country}</div>'
            f'<div class="na-reason">{reason}{sub_html}</div>'
            f'<div class="na-area">{fmt_area(row.get("area_km2"))}</div>'
            '</div>'
        )

    st.markdown(
        '<div class="na-scroll">'
        '<div class="na-header">'
        '<div>Protected area</div>'
        '<div>Country</div>'
        '<div>Reason not assessed</div>'
        '<div>Area (km²)</div>'
        '</div>'
        + rows_html
        + '</div>',
        unsafe_allow_html=True,
    )
# ============================================================
# METHODOLOGY PAGE
# Paste this block directly AFTER the not_assessed block
# (it starts with `elif`, so it continues the same if/elif chain).
#
# All numbers that describe the data (counts, window, confidence
# split, source) are computed from `df`, so they can never drift
# out of sync with the file that is loaded.
# ============================================================

elif st.session_state.page == "methodology":

    import html as html_lib

    def clean_html(markup: str) -> str:
        """One line, no indentation, no blank lines (see candidate page)."""
        return " ".join(
            line.strip() for line in markup.splitlines() if line.strip()
        )

    def go_to(page_name):
        st.session_state.page = page_name

    def render_provenance_bar(source_df):
        """
        Same logic as the other pages: shows which prediction run produced
        the numbers, read LIVE from the loaded file, not from its filename.
        """
        sources = (
            source_df["predictions_source"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
        is_placeholder = any(
            s.strip().lower() == "baseline_placeholder" for s in sources
        )
        label = html_lib.escape(" / ".join(sources) if sources else "unknown")

        if is_placeholder:
            bar_html = (
                '<div class="provenance-bar provenance-warn">'
                '⚠ PLACEHOLDER DATA — these figures are not from the real '
                f'prediction model (source: {label}). Do not use for '
                'decisions.</div>'
            )
        else:
            bar_html = (
                '<div class="provenance-bar provenance-ok">'
                f'DATA SOURCE · {label}</div>'
            )
        st.markdown(clean_html(bar_html), unsafe_allow_html=True)

    # ========================================================
    # STYLING
    # ========================================================

    METH_CSS = """
    <style>

    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: #f4f3ef !important;
    }

    header[data-testid="stHeader"] { background: transparent !important; }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"] { display: none !important; }

    .block-container {
        max-width: 1180px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 4rem !important;
    }

    /* ---------- navigation (same as the other pages) ---------- */

    .candidate-nav-subtitle {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 8px;
        letter-spacing: 0.14em;
        margin-top: -8px;
        margin-left: 34px;
        white-space: nowrap;
    }

    .candidate-active-nav {
        color: #1f5f8b;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
        text-align: center;
        padding: 11px 8px 13px 8px;
        border-bottom: 2px solid #1f5f8b;
        white-space: nowrap;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #77756e !important;
        border-radius: 0 !important;
        padding: 10px 8px 13px 8px !important;
        min-height: 0 !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
        font-weight: 400 !important;
        color: #77756e !important;
    }

    div[data-testid="stButton"] > button[kind="tertiary"]:hover,
    div[data-testid="stButton"] > button[kind="tertiary"]:hover p {
        background: transparent !important;
        color: #262522 !important;
    }

    div.st-key-meth_logo div[data-testid="stButton"] > button[kind="tertiary"] {
        position: relative;
        padding: 0 0 0 36px !important;
        justify-content: flex-start !important;
    }

    div.st-key-meth_logo div[data-testid="stButton"] > button[kind="tertiary"] p {
        font-family: Georgia, serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #262522 !important;
    }

    div.st-key-meth_logo button::before {
        content: "";
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 26px;
        height: 26px;
        background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26' fill='none' stroke='%231f5f8b' stroke-width='1.4'%3E%3Ccircle cx='13' cy='13' r='11'/%3E%3Cpath d='M5 12c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3Cpath d='M5 16c2-2 4-2 6 0s4 2 6 0 3-1 4 0'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
    }

    /* ---------- provenance bar ---------- */

    .provenance-bar {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        margin-top: 12px;
        font-family: Arial, sans-serif;
        font-size: 10.5px;
    }

    .provenance-ok {
        background: #f4f3ef;
        border: 1px solid #dedbd3;
        color: #77756e;
    }

    .provenance-warn {
        background: #fdecea;
        border: 1px solid #e8b4ac;
        color: #a63d2d;
        font-weight: 600;
    }

    /* ---------- intro ---------- */

    .meth-title {
        font-family: Georgia, serif;
        font-size: 26px;
        font-weight: 600;
        line-height: 1.2;
        color: #262522;
        margin: 0;
    }

    .meth-lead {
        color: #77756e;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.55;
        max-width: 690px;
        margin-top: 10px;
    }

    /* ---------- sections ---------- */

    .meth-section {
        display: grid;
        grid-template-columns: 220px 1fr;
        column-gap: 56px;
        padding: 30px 0 22px 0;
        border-top: 1px solid #deddd7;
    }

    .meth-num {
        color: #aaa79d;
        font-family: monospace;
        font-size: 10px;
        letter-spacing: 0.1em;
    }

    .meth-side-title {
        font-family: Georgia, serif;
        font-size: 17px;
        font-weight: 600;
        line-height: 1.3;
        color: #262522;
        margin-top: 6px;
    }

    .meth-body {
        max-width: 720px;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.7;
        color: #4f4d47;
    }

    .meth-body p { margin: 0 0 12px 0; }

    .meth-body strong { color: #262522; }

    .meth-list {
        margin: 0 0 14px 0;
        padding-left: 18px;
    }

    .meth-list li { margin-bottom: 6px; }

    .meth-code {
        font-family: monospace;
        font-size: 12px;
        color: #262522;
    }

    .meth-formula {
        background: #eeece6;
        border: 1px solid #dedbd3;
        padding: 16px 20px;
        margin: 4px 0 16px 0;
        font-family: monospace;
        font-size: 15px;
        color: #262522;
    }

    .meth-formula small {
        display: block;
        margin-top: 8px;
        font-family: Arial, sans-serif;
        font-size: 11px;
        color: #77756e;
    }

    .meth-callout {
        border-left: 3px solid #c47a2c;
        background: #fbf1e4;
        padding: 12px 16px;
        margin: 4px 0 14px 0;
        color: #5d4630;
        font-size: 12.5px;
        line-height: 1.6;
    }

    /* rows used for the S interpretation and the worked example */

    .meth-grid {
        border-top: 1px solid #e4e1da;
        margin: 4px 0 16px 0;
    }

    .meth-grid-row {
        display: grid;
        grid-template-columns: 150px 1fr;
        column-gap: 20px;
        padding: 10px 0;
        border-bottom: 1px solid #e4e1da;
        font-size: 12.5px;
        line-height: 1.6;
    }

    .meth-grid-key {
        font-family: monospace;
        font-size: 12px;
        font-weight: 600;
    }

    .meth-grid-row.example {
        grid-template-columns: 90px repeat(4, 1fr);
        font-family: monospace;
        font-size: 12px;
    }

    .meth-grid-row.example.head {
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.09em;
        text-transform: uppercase;
        color: #77756e;
    }

    /* stat tiles in the data section */

    .meth-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin: 4px 0 16px 0;
    }

    .meth-stat {
        background: #eeece6;
        border: 1px solid #dedbd3;
        padding: 12px 14px;
    }

    .meth-stat-num {
        font-family: Georgia, serif;
        font-size: 20px;
        color: #1f5f8b;
    }

    .meth-stat-label {
        margin-top: 4px;
        font-size: 10px;
        color: #77756e;
    }

    @media (max-width: 800px) {
        .meth-section { grid-template-columns: 1fr; row-gap: 14px; }
        .meth-stats { grid-template-columns: repeat(2, 1fr); }
    }

    </style>
    """

    st.markdown(clean_html(METH_CSS), unsafe_allow_html=True)

    # ========================================================
    # TOP NAVIGATION
    # ========================================================

    nav_logo, nav_candidate, nav_not, nav_method = st.columns(
        [4.7, 1, 1, 1],
        gap="small",
    )

    with nav_logo:
        st.button(
            "MPA Enforcement Intelligence",
            key="meth_logo",
            type="tertiary",
            on_click=go_to,
            args=("welcome",),
        )
        st.markdown(
            clean_html(
                """
                <div class="candidate-nav-subtitle">
                    MEDITERRANEAN · DECISION SUPPORT
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with nav_candidate:
        st.button(
            "Candidate gaps",
            key="meth_candidate_nav",
            type="tertiary",
            on_click=go_to,
            args=("candidate_gaps",),
        )

    with nav_not:
        st.button(
            "Not assessed",
            key="meth_not_assessed_nav",
            type="tertiary",
            on_click=go_to,
            args=("not_assessed",),
        )

    with nav_method:
        st.markdown(
            clean_html(
                """
                <div class="candidate-active-nav">Methodology</div>
                """
            ),
            unsafe_allow_html=True,
        )

    render_provenance_bar(df)

    # ========================================================
    # NUMBERS FROM THE DATA (never typed in by hand)
    # ========================================================

    m_assessed = df[df["assessed"] == True]
    m_not = df[df["assessed"] == False]

    n_total = len(df)
    n_assessed = len(m_assessed)
    n_not = len(m_not)

    n_countries_all = int(df["iso3"].nunique())
    n_countries_assessed = int(m_assessed["iso3"].nunique())

    try:
        year_first = pd.Timestamp(m_assessed["first_month"].min()).year
        year_last = pd.Timestamp(m_assessed["last_month"].max()).year
        window = f"{year_first}–{year_last}"
    except Exception:
        window = "the analysis window"

    conf_counts = (
        m_assessed["confidence"].astype(str).str.strip().str.lower()
        .value_counts()
    )
    n_high = int(conf_counts.get("high", 0))
    n_medium = int(conf_counts.get("medium", 0))
    n_low = int(conf_counts.get("low", 0))

    s_numeric = pd.to_numeric(m_assessed["S"], errors="coerce")
    neg_mask = s_numeric < 0
    n_negative = int(neg_mask.sum())

    if "resolvable" in m_assessed.columns:
        n_subcell = int((m_assessed["resolvable"] == False).sum())
        neg_subcell_share = (
            float((m_assessed.loc[neg_mask, "resolvable"] == False).mean())
            if n_negative
            else 0.0
        )
    else:
        n_subcell = 0
        neg_subcell_share = 0.0

    sources = (
        df["predictions_source"].dropna().astype(str).unique().tolist()
    )
    source_label = html_lib.escape(" / ".join(sources) if sources else "unknown")

    # ========================================================
    # INTRO
    # ========================================================

    st.markdown(
        clean_html(
            """
            <div style="height:4px;"></div>
            <div class="meth-title">Methodology &amp; about</div>
            <div class="meth-lead">
                How the numbers in this dashboard are produced, what they can
                and cannot tell you, and where they come from. This page
                describes the method. It does not add to it.
            </div>
            <div style="height:30px;"></div>
            """
        ),
        unsafe_allow_html=True,
    )

    def section(num, title, body_html):
        st.markdown(
            clean_html(
                f"""
                <div class="meth-section">
                    <div>
                        <div class="meth-num">{num}</div>
                        <div class="meth-side-title">{title}</div>
                    </div>
                    <div class="meth-body">{body_html}</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    # ========================================================
    # 01  WHAT THIS TOOL DOES
    # ========================================================

    section(
        "01",
        "What this tool does",
        """
        <p>Marine Protected Areas (MPAs) are designated to protect marine
        ecosystems, but a designation does not by itself show that fishing
        pressure has fallen. The useful question is not whether there is
        fishing inside an MPA, since some fishing may be legitimate under its
        rules. It is this: <strong>how much industrial fishing would we
        expect here if the area were not protected, and how does that compare
        with what was actually observed?</strong></p>
        <p>The dashboard ranks MPAs by the difference between the two, so that
        people who manage, monitor or enforce them can decide where to look
        first. It is decision support. It does not declare any MPA illegally
        fished, poorly enforced or ineffective.</p>
        <div class="meth-callout"><strong>A candidate gap is a signal for
        investigation, not proof of illegal fishing or failed
        enforcement.</strong></div>
        """,
    )

    # ========================================================
    # 02  COUNTERFACTUAL MODELLING
    # ========================================================

    section(
        "02",
        "Counterfactual modelling",
        f"""
        <p>We cannot observe how much fishing would have happened in a
        protected area had it never been protected. Instead, a machine
        learning model learns how fishing effort relates to the
        characteristics of unprotected water, then estimates the effort
        expected at protected locations. That estimate is the
        counterfactual.</p>
        <ul class="meth-list">
        <li><strong>Model.</strong> Gradient boosting with a Poisson loss,
        because the quantity predicted is fishing effort in hours.</li>
        <li><strong>Comparison water.</strong> Trained on unprotected water
        only, and restricted to the range of conditions that protected areas
        also cover, so that like is compared with like.</li>
        <li><strong>Predictions.</strong> Cross-fitted, and scaled by a
        calibration factor of about 1.224.</li>
        <li><strong>Inputs.</strong> Physical, environmental, geographic and
        neighbourhood features. Raw latitude and longitude are not used.
        Distance to the nearest MPA is not used either, because it behaves
        differently in the unprotected training data than at protected
        locations.</li>
        <li><strong>Evaluation.</strong> Blocked by space and time instead of
        a random split, which reduces leakage and gives a more realistic
        picture of how the model generalises.</li>
        </ul>
        <p><strong>Expected effort (P)</strong> is the model's estimate,
        summed over the cells and months of each MPA.
        <strong>Observed effort (O)</strong> is industrial fishing activity
        inferred from AIS vessel tracking for the same cells and months.
        Both are shown as <strong>total fishing hours over {window}</strong>,
        not per year.</p>
        <p>This dashboard does not train or run the model. It reads the
        MPA-level ranking that the modelling pipeline produced.</p>
        """,
    )

    # ========================================================
    # 03  THE INDEX S
    # ========================================================

    section(
        "03",
        "The candidate gap index, S",
        f"""
        <div class="meth-formula">S = (P − O) / (P + O)
        <small>P = expected (counterfactual) effort &nbsp;·&nbsp;
        O = observed effort</small></div>
        <p>S runs from −1 to +1. A value of −1 means fishing occurred where
        almost none was expected. A value of +1 means the expected effort is
        entirely absent.</p>
        <div class="meth-grid">
        <div class="meth-grid-row">
        <div class="meth-grid-key" style="color:#a63d32;">S below 0</div>
        <div>More fishing observed than expected. These are the candidate
        gaps.</div></div>
        <div class="meth-grid-row">
        <div class="meth-grid-key" style="color:#77756e;">S near 0</div>
        <div>Observed effort is about what the counterfactual expected.</div>
        </div>
        <div class="meth-grid-row">
        <div class="meth-grid-key" style="color:#377457;">S above 0</div>
        <div>Less fishing observed than expected. This is a protection
        signal, but it does not prove that protection caused the
        reduction.</div></div>
        </div>
        <p>An earlier version of the metric, 1 − O/P, had no lower limit and
        could produce absurd values, so it was replaced by S.</p>
        <p>The labels shown in the detail panel (severe, moderate and
        marginal candidate gap, and protection signal) are a reading aid set
        by this dashboard at S = −0.65, −0.30 and 0. They are not part of the
        model.</p>
        <p>In the current file S is below 0 for <strong>{n_negative:,} of
        {n_assessed:,}</strong> assessed MPAs. About
        <strong>{neg_subcell_share:.0%}</strong> of those are smaller than
        one grid cell, which is why S alone is a poor way to order the
        table.</p>
        """,
    )

    # ========================================================
    # 04  WHY S IS NOT ENOUGH
    # ========================================================

    section(
        "04",
        "Why S is not enough on its own",
        """
        <p>S is a proportion, so it says nothing about how much fishing is
        involved. Two MPAs can have the same S with very different amounts of
        effort behind it:</p>
        <div class="meth-grid">
        <div class="meth-grid-row example head">
        <div>MPA</div><div>Expected</div><div>Observed</div><div>S</div>
        <div>Absolute gap</div></div>
        <div class="meth-grid-row example">
        <div>A</div><div>1 hr</div><div>10 hrs</div><div>−0.82</div>
        <div>+9 hrs</div></div>
        <div class="meth-grid-row example">
        <div>B</div><div>1,000 hrs</div><div>10,000 hrs</div>
        <div>−0.82</div><div>+9,000 hrs</div></div>
        </div>
        <p>That is why the <strong>absolute gap in fishing hours</strong> is
        always shown next to S. In the tables it is observed minus expected:
        a plus sign means more fishing than expected, a minus sign means
        less.</p>
        <p>Neither number travels well on its own. Absolute hours are not
        comparable between MPAs of very different sizes, and S is not
        comparable between MPAs whose grid cells overlap them to very
        different degrees. Confidence exists to say that out loud.</p>
        """,
    )

    # ========================================================
    # 05  HOW THE TABLE IS RANKED
    # ========================================================

    section(
        "05",
        "How the table is ranked",
        """
        <div class="meth-formula">priority = 0 &nbsp; if S ≥ 0<br>
        priority = min(1, −S) × log10(1 + expected hours) &nbsp; if S below 0
        <small>expected hours = expected effort inside the MPA over the
        analysis window</small></div>
        <p>Ranking on S alone puts tiny, thinly fished areas at the top: an
        area at S = −0.99 that expected only a few hours of fishing is mostly
        noise. Priority multiplies the size of the shortfall by the logarithm
        of the effort at stake, so a sizeable gap in a heavily fished area
        outranks a near-perfect score on almost nothing.</p>
        <p>Areas with S of 0 or above score 0. Ties are ordered by S, most
        negative first. Priority is worked out by the dashboard from the
        ranking file, for assessed MPAs only. S and the absolute gap keep
        their own columns. The file's own rank column orders by S alone and
        is not used.</p>
        """,
    )

    # ========================================================
    # 06  CONFIDENCE
    # ========================================================

    section(
        "06",
        "Confidence",
        f"""
        <p>Confidence says how far the S of a single MPA can be trusted. It
        is the <strong>weaker</strong> of two measures:</p>
        <ul class="meth-list">
        <li><strong>Cell overlap.</strong> On average, how much of each grid
        cell the MPA fills. The data sit on a 0.1° grid, so an MPA boundary
        cuts through cells and part of each cell's fishing happens outside
        the MPA. The smaller the share, the noisier S becomes.</li>
        <li><strong>AIS coverage.</strong> The share of the MPA's cell-months
        in which AIS recorded any vessel.</li>
        </ul>
        <p>The detail panel shows both numbers and which one is limiting the
        rating: cell overlap, AIS coverage, or both.</p>
        <p>In the current file, <strong>{n_high:,}</strong> assessed MPAs are
        rated High, <strong>{n_medium:,}</strong> Medium and
        <strong>{n_low:,}</strong> Low. <strong>{n_subcell:,}</strong> of the
        {n_assessed:,} are smaller than one grid cell. They stay in the
        ranking, flagged, and almost all are rated Low or Medium.</p>
        """,
    )

    # ========================================================
    # 07  NOT ASSESSED
    # ========================================================

    section(
        "07",
        "MPAs that are not assessed",
        f"""
        <p>An MPA is not assessed when AIS recorded a vessel in fewer than
        10% of its cell-months. Estuaries, coastal lagoons and much of the
        southern rim fall here. Their S comes out close to a perfect score,
        which would mean only that no industrial vessel was ever tracked
        there, not that protection works.</p>
        <p>The <strong>{n_not:,}</strong> MPAs in this group are kept out of
        the ranking and listed on their own page. Missing tracking data is
        never read as absence of fishing.</p>
        """,
    )

    # ========================================================
    # 08  AIS LIMITATIONS AND THE COVERAGE RAMP
    # ========================================================

    section(
        "08",
        "AIS limitations and the coverage ramp",
        f"""
        <p>Fishing effort here is derived from the Automatic Identification
        System (AIS), which tracks vessels. It covers industrial vessels
        only, and it has limits:</p>
        <ul class="meth-list">
        <li>Vessels that do not carry AIS, or whose signal is not received,
        are not observed.</li>
        <li>Coverage is uneven across the basin. It is denser in the northern
        Mediterranean, so estimates along the southern and eastern rim carry
        more uncertainty.</li>
        <li>The absence of AIS-recorded fishing is never proof that no fishing
        took place.</li>
        </ul>
        <p><strong>Coverage grew over time.</strong> 2012 had very low
        coverage, 2013 substantially more, and 2014 was much closer to later
        levels. The main analysis therefore uses 2015 onward. Many MPAs were
        designated between 2013 and 2016, while coverage was still rising, so
        a simple before-and-after comparison can mislead: fishing can appear
        to increase after designation only because tracking improved.</p>
        <p>The project documents this ramp instead of treating the early years
        as normal. Its separate before/after analysis uses a 2017 cutoff for
        the relevant subset of areas, with the reasoning recorded in the
        project decision log (entry D40). Before/after results are not shown
        in this dashboard.</p>
        """,
    )

    # ========================================================
    # 09  WHAT THIS CANNOT TELL YOU
    # ========================================================

    section(
        "09",
        "What this cannot tell you",
        """
        <ul class="meth-list">
        <li><strong>Designation is not regulation.</strong> The protected-area
        register reports no-take status as “Not Reported” for 1,661 of the
        1,663 Mediterranean sites, so it shows that an area is designated,
        not whether fishing is allowed in it. For that reason this tool
        shows no fishing rules for individual MPAs.</li>
        <li><strong>A candidate gap has many possible explanations.</strong>
        Fishing that the site's rules permit, activity at the edge of a site
        or in a neighbouring cell, model error and enforcement gaps can all
        produce it. The index does not tell them apart.</li>
        <li><strong>A protection signal is not proof of protection.</strong>
        Less fishing than expected is consistent with an effect of
        protection but does not establish it.</li>
        <li><strong>Only industrial fishing seen by AIS is measured.</strong>
        It is not all fishing.</li>
        <li><strong>Results depend on modelling choices.</strong> For example,
        restricting the comparison water to conditions that protected areas
        also experience substantially reduced an earlier estimate of the
        effect.</li>
        <li><strong>Some sites appear more than once.</strong> Overlapping
        designations of one site can be separate records in the ranking
        file.</li>
        </ul>
        """,
    )

    # ========================================================
    # 10  DATA AND PROVENANCE
    # ========================================================

    section(
        "10",
        "Data and provenance",
        f"""
        <div class="meth-stats">
        <div class="meth-stat"><div class="meth-stat-num">{n_total:,}</div>
        <div class="meth-stat-label">MPAs in the ranking file</div></div>
        <div class="meth-stat"><div class="meth-stat-num">{n_assessed:,}</div>
        <div class="meth-stat-label">assessed</div></div>
        <div class="meth-stat"><div class="meth-stat-num">{n_not:,}</div>
        <div class="meth-stat-label">not assessed</div></div>
        <div class="meth-stat"><div class="meth-stat-num">{n_countries_all}</div>
        <div class="meth-stat-label">countries ({n_countries_assessed} with
        assessed MPAs)</div></div>
        </div>
        <p>The dashboard reads a single MPA-level ranking file, one row per
        MPA, covering the Mediterranean over {window}. The counts on this page
        are computed from that file each time it loads.</p>
        <p><strong>Prediction source:</strong>
        <span class="meth-code">{source_label}</span></p>
        <p>The source is read from inside the file, not inferred from its
        name. If the bar at the top of any page turns red, the file that was
        loaded is a placeholder build, and its numbers are not results.
        Every column of the ranking is documented in the project data
        dictionary.</p>
        """,
    )
