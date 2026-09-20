import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mediterranean MPA Enforcement Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# Load dashboard data
DATA_PATH = "data/mpa_ranking.parquet"
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
        if pd.isna(value):
            return "—"
        value = abs(float(value))
        if value >= 1000:
            return f"+{value / 1000:,.1f}k hrs"
        return f"+{value:,.0f} hrs"

    def reset_candidate_filters():
        # Must run as an on_click callback. Assigning to a widget's
        # session_state key AFTER the widget was created in the same
        # run raises a StreamlitAPIException.
        st.session_state.candidate_search = ""
        st.session_state.candidate_country = "All countries"
        st.session_state.candidate_confidence = "All confidence levels"
        st.session_state.candidate_restriction = "Restricted"
        st.session_state.candidate_s_range = "All S values"

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
        grid-template-columns: 2.15fr 0.72fr 1.35fr 1.15fr 1.05fr 1.25fr;
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

    .rule-tag {
        display: inline-block;
        background: #dfebf4;
        color: #35617e;
        padding: 5px 8px;
        border-radius: 4px;
        font-family: Arial, sans-serif;
        font-size: 9px;
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
        st.button(
            "Not assessed",
            key="candidate_not_assessed_nav",
            type="tertiary",
        )

    with nav_method:
        st.button(
            "Methodology",
            key="candidate_methodology_nav",
            type="tertiary",
        )

    # ========================================================
    # INTRO
    # ========================================================

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
                """
                <div class="candidate-count-number" style="color:#1f5f8b;">
                    1,288
                </div>
                <div class="candidate-count-label">assessed MPAs</div>
                """
            ),
            unsafe_allow_html=True,
        )

    with count_b:

        st.markdown(
            clean_html(
                """
                <div class="candidate-count-number" style="color:#aaa79d;">
                    117
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

    # ========================================================
    # DISTRIBUTION
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
        distribution_df = sorted_sample.iloc[positions].copy()
    else:
        distribution_df = sorted_sample.copy()

    dot_heights = [
        69, 48, 34, 57, 43,
        62, 45, 57, 37, 51,
        40, 60, 47, 31, 56,
        43, 61, 38, 55, 45,
    ]

    dots_html = ""

    for i, (_, row) in enumerate(distribution_df.iterrows()):

        s_value = float(row["S"])

        left_percent = 14 + ((s_value + 1) / 2) * 72
        top_percent = dot_heights[i % len(dot_heights)]

        if s_value < -0.65:
            dot_color = "#a63d32"
        elif s_value < -0.30:
            dot_color = "#c2674e"
        elif s_value < 0:
            dot_color = "#c88c51"
        elif s_value < 0.35:
            dot_color = "#8b8b78"
        elif s_value < 0.70:
            dot_color = "#4f8568"
        else:
            dot_color = "#28664b"

        mpa_name = html_lib.escape(
            str(row.get("mpa_name", "Protected area")),
            quote=True,
        )

        dots_html += (
            f'<div class="distribution-dot" title="{mpa_name}" '
            f'style="left:{left_percent:.2f}%;top:{top_percent}%;'
            f'background:{dot_color};"></div>'
        )

    ticks_html = "".join(
        f'<div class="distribution-tick" style="left:{pos}%;">{label}</div>'
        for pos, label in [
            (14, "−1"), (32, "−0.5"), (50, "0"), (68, "+0.5"), (86, "+1"),
        ]
    )

    distribution_html = (
        '<div class="distribution-box">'
        '<div class="distribution-negative"></div>'
        '<div class="distribution-positive"></div>'
        '<div class="distribution-axis"></div>'
        '<div class="distribution-zero"></div>'
        + dots_html
        + ticks_html
        + '<div class="distribution-note-left">← candidate gap</div>'
        + '<div class="distribution-baseline">baseline</div>'
        + '<div class="distribution-note-right">protection signal →</div>'
        + "</div>"
    )

    st.markdown(distribution_html, unsafe_allow_html=True)

    # ========================================================
    # FILTER BAR
    # ========================================================

    with st.container(key="filter_shell"):

        f1, f2, f3, f4, f5, f6 = st.columns(
            [2.65, 1.0, 1.28, 1.08, 1.12, 0.82],
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
                assessed_df["iso3"].dropna().astype(str).unique().tolist()
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
            selected_restriction = st.selectbox(
                "Fishing rules",
                ["Restricted", "All rules"],
                label_visibility="collapsed",
                key="candidate_restriction",
            )

        with f5:
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

        with f6:
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
            filtered_df["iso3"].fillna("").astype(str)
            .str.lower().str.contains(q, regex=False)
        )
        filtered_df = filtered_df[name_match | country_match]

    if selected_country != "All countries":
        filtered_df = filtered_df[
            filtered_df["iso3"].astype(str) == selected_country
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
    # TABLE
    # ========================================================

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

    table_df = filtered_df.sort_values("S", ascending=True).copy()

    rows_html = ""

    for _, row in table_df.head(10).iterrows():

        name = html_lib.escape(str(row.get("mpa_name", "Unnamed MPA")))
        country = html_lib.escape(str(row.get("iso3", "—")))
        s_value = float(row.get("S", 0))
        gap_text = fmt_hours(row.get("abs_gap_hours", None))

        confidence = str(row.get("confidence", "not assessed")).strip()

        confidence_class = {
            "high": "confidence-high",
            "medium": "confidence-medium",
            "low": "confidence-low",
        }.get(confidence.lower(), "confidence-medium")

        color = "#a63d32" if s_value < 0 else "#377457"

        # Diverging bar: grows LEFT from the centre tick when S < 0,
        # RIGHT when S >= 0 (like the mockup).
        half = 29
        fill_w = min(half, abs(s_value) * half)
        fill_left = half - fill_w if s_value < 0 else half

        # No fishing-rules column in the parquet yet -> don't invent one.
        rule_text = "—"

        rows_html += (
            '<div class="ranking-row">'
            f'<div class="ranking-name">{name}</div>'
            f'<div class="ranking-country">{country}</div>'
            '<div class="ranking-s">'
            f'<span class="ranking-s-value" style="color:{color};">'
            f'{s_value:+.2f}</span>'
            '<span class="ranking-s-bar">'
            f'<span class="ranking-s-fill" style="left:{fill_left:.1f}px;'
            f'width:{fill_w:.1f}px;background:{color};"></span>'
            '</span></div>'
            f'<div class="ranking-gap">{gap_text}</div>'
            f'<div><span class="confidence-tag {confidence_class}">'
            f'{html_lib.escape(confidence.capitalize())}</span></div>'
            f'<div><span class="rule-tag">{rule_text}</span></div>'
            '</div>'
        )

    if len(table_df) == 0:
        rows_html = (
            '<div style="padding:35px;text-align:center;'
            'color:#77756e;font-size:12px;">'
            'No assessed protected areas match these filters.</div>'
        )

    table_html = (
        '<div class="ranking-header">'
        '<div>Protected area ↕</div>'
        '<div>Country ↕</div>'
        '<div>S / candidate gap ↑</div>'
        '<div>Abs. gap (hrs) ↕</div>'
        '<div>Confidence ↕</div>'
        '<div>Fishing rules</div>'
        '</div>'
        + rows_html
    )

    st.markdown(table_html, unsafe_allow_html=True)
