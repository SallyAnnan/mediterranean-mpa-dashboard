import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mediterranean MPA Enforcement Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# Load dashboard data
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

header {
    background: transparent;
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
</style>
""",
    unsafe_allow_html=True,
)

# Header and pages
# ============================================================

if st.session_state.page == "welcome":

    # Header
    st.markdown(
        """
    <div style="border-bottom:1px solid #deddd7;padding:0.5rem 0 1rem 0;margin-bottom:3rem;">
    <div style="color:#1f5f8b;font-size:0.85rem;font-weight:600;letter-spacing:0.04em;">
    ◯ &nbsp; MPA Enforcement Intelligence
    </div>
    <div style="color:#9a9992;font-size:0.65rem;letter-spacing:0.12em;margin-top:0.2rem;margin-left:1.8rem;">
    MEDITERRANEAN · DECISION SUPPORT
    </div>
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
# ============================================================

elif st.session_state.page == "candidate_gaps":

    import html as html_lib
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

    # TODO: confirm wording with the modelling team
    LIMIT_TEXT = {
        "cell overlap": "Main limitation: the AIS grid cells used for this "
                        "estimate only partly overlap the protected area.",
        "AIS coverage": "Main limitation: AIS observability in this area. "
                        "Some fishing may not appear in vessel-tracking data.",
        "both": "Limited both by partial overlap between the AIS grid "
                "cells and the protected area, and by AIS observability.",
    }

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
        grid-template-columns: 2.3fr 0.9fr 1.5fr 1.3fr 1.2fr;
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
    .ranking-scroll .ranking-row { min-width: 640px; }

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

    .st-key-table_wrap > * { min-width: 640px; }

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

        limited_by = str(row.get("confidence_limited_by", "") or "").strip()
        conf_text = LIMIT_TEXT.get(
            limited_by,
            f"Main limitation: {html_lib.escape(limited_by)}."
            if limited_by
            else "No specific limitation recorded.",
        )

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
        else:
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
        site_type = html_lib.escape(str(row.get("site_type", "—")))
        status_year = row.get("status_year", None)
        area = row.get("area_km2", None)
        n_cells = row.get("n_cells", None)

        context_bits = [
            f"IUCN category: {iucn}",
            f"Site type: {site_type}",
        ]
        if pd.notna(status_year):
            context_bits.append(f"Status year: {int(status_year)}")
        if pd.notna(area):
            context_bits.append(f"Area: {float(area):,.1f} km²")
        if pd.notna(n_cells):
            context_bits.append(f"AIS grid cells used: {int(n_cells):,}")
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

    # TODO(priority-column): Tiago's 5-day-old message said sorting on S
    # alone puts tiny, barely-fished areas at the top (confirmed: still
    # true on the current file — sub-4-km² sites dominate the top of S).
    # He mentioned a Priority column, weighted by effort at stake, meant
    # to replace this sort. It is not in the current mpa_ranking.parquet
    # (checked: only `rank` and `S` exist). Once Tiago confirms which
    # file has it, swap the line below for:
    #   table_df = filtered_df.sort_values("Priority", ascending=True)
    table_df = filtered_df.sort_values("S", ascending=True).copy()

    row_items = []   # (wdpa_id, html)

    for idx, (_, row) in enumerate(table_df.head(10).iterrows()):

        name = html_lib.escape(str(row.get("mpa_name", "Unnamed MPA")))
        country = html_lib.escape(str(row.get("country", "—")))
        s_value = float(row.get("S", 0))
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
            '<div class="ranking-s">'
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
        '<div>S / candidate gap ↑</div>'
        '<div>Abs. gap (hrs) ↕</div>'
        '<div>Confidence ↕</div>'
        '</div>'
    )

    with table_col:
        st.markdown(
            clean_html(
                """
                <div class="table-caption">
                    Protected areas · sorted by candidate gap
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
