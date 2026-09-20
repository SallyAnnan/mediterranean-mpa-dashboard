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

    import textwrap

    def render_html(html):
        st.markdown(
            textwrap.dedent(html).strip(),
            unsafe_allow_html=True,
        )

    # --------------------------------------------------------
    # Candidate Gaps page styling
    # --------------------------------------------------------

    render_html("""
    <style>

    /* Candidate page */

    .candidate-page {
        width: 100%;
        max-width: 1088px;
        margin: 0 auto;
    }

    .candidate-eyebrow {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .candidate-title {
        color: #262522;
        font-family: Georgia, serif;
        font-size: 31px;
        font-weight: 700;
        line-height: 1.15;
        letter-spacing: -0.025em;
        margin: 0;
    }

    .candidate-description {
        color: #6d6b65;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 1.55;
        max-width: 710px;
        margin-top: 12px;
    }

    .candidate-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 50px;
        padding-top: 10px;
        padding-bottom: 28px;
        border-bottom: 1px solid #dedbd3;
    }

    .candidate-title-area {
        flex: 1;
    }

    .candidate-counts {
        display: flex;
        gap: 54px;
        padding-top: 2px;
        min-width: 220px;
    }

    .candidate-count {
        text-align: center;
    }

    .candidate-count-number {
        font-family: Georgia, serif;
        font-size: 28px;
        line-height: 1;
        color: #1f5f8b;
        margin-bottom: 8px;
    }

    .candidate-count-number.muted {
        color: #aaa79d;
    }

    .candidate-count-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        white-space: nowrap;
    }

    /* Distribution */

    .distribution-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 34px;
        margin-bottom: 12px;
    }

    .distribution-box {
        position: relative;
        height: 115px;
        border: 1px solid #dedbd3;
        background: #f8f7f3;
        overflow: hidden;
    }

    .distribution-negative-zone {
        position: absolute;
        left: 9%;
        right: 50%;
        top: 26px;
        bottom: 31px;
        background: #f8efec;
    }

    .distribution-positive-zone {
        position: absolute;
        left: 50%;
        right: 9%;
        top: 26px;
        bottom: 31px;
        background: #eef5f0;
    }

    .distribution-axis {
        position: absolute;
        left: 9%;
        right: 9%;
        bottom: 31px;
        height: 1px;
        background: #d7d4cc;
    }

    .distribution-zero {
        position: absolute;
        left: 50%;
        bottom: 25px;
        width: 1px;
        height: 13px;
        background: #bbb8b0;
    }

    .distribution-dot {
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        z-index: 4;
    }

    .distribution-dot.negative {
        background: #b4483d;
    }

    .distribution-dot.negative-soft {
        background: #c66a4e;
    }

    .distribution-dot.neutral {
        background: #85877b;
    }

    .distribution-dot.positive-soft {
        background: #56856d;
    }

    .distribution-dot.positive {
        background: #2f7253;
    }

    .distribution-tick {
        position: absolute;
        bottom: 13px;
        transform: translateX(-50%);
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
    }

    .distribution-caption-left {
        position: absolute;
        left: 9%;
        bottom: 2px;
        color: #b4483d;
        font-family: Arial, sans-serif;
        font-size: 8px;
        font-style: italic;
    }

    .distribution-caption-right {
        position: absolute;
        right: 9%;
        bottom: 2px;
        color: #2f7253;
        font-family: Arial, sans-serif;
        font-size: 8px;
        font-style: italic;
    }

    /* Filters */

    .filter-area {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 28px;
        padding: 9px;
        background: #eeece6;
        border: 1px solid #dedbd3;
    }

    /* Make Streamlit's native controls match the reference */

    div[data-testid="stTextInput"] input {
        height: 38px !important;
        background: #f8f7f3 !important;
        border: 1px solid #d9d6ce !important;
        border-radius: 0 !important;
        color: #3e3d39 !important;
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #aaa79d !important;
    }

    div[data-baseweb="select"] > div {
        min-height: 38px !important;
        background: #f8f7f3 !important;
        border: 1px solid #d9d6ce !important;
        border-radius: 0 !important;
        color: #5f5d57 !important;
        font-family: Arial, sans-serif !important;
        font-size: 12px !important;
    }

    div[data-baseweb="select"] span {
        color: #5f5d57 !important;
        font-size: 12px !important;
    }

    .filter-button button {
        height: 38px !important;
        background: #eef5f8 !important;
        color: #28648b !important;
        border: 1px solid #d2e1e8 !important;
        border-radius: 0 !important;
        font-size: 12px !important;
        font-weight: 500 !important;
    }

    .filter-button button:hover {
        background: #e4eff4 !important;
        border-color: #c5d9e3 !important;
        color: #1f5f8b !important;
    }

    /* Table heading */

    .ranking-label {
        color: #aaa79d;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 27px;
        margin-bottom: 12px;
    }

    .ranking-header {
        display: grid;
        grid-template-columns: 2.35fr 0.8fr 1.35fr 1.15fr 0.85fr;
        align-items: center;
        padding: 0 13px 10px 13px;
        border-bottom: 1px solid #cbc8c0;
        color: #88857e;
        font-family: Arial, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .ranking-row {
        display: grid;
        grid-template-columns: 2.35fr 0.8fr 1.35fr 1.15fr 0.85fr;
        align-items: center;
        min-height: 59px;
        padding: 0 13px;
        border-bottom: 1px solid #e2dfd8;
        background: #f8f7f3;
    }

    .ranking-row:nth-child(even) {
        background: #f3f1ec;
    }

    .ranking-name {
        color: #292824;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 500;
        line-height: 1.35;
        padding-right: 15px;
    }

    .ranking-country {
        color: #77746d;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }

    .ranking-s {
        display: flex;
        align-items: center;
        gap: 10px;
        color: #a93f35;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
    }

    .s-bar {
        width: 58px;
        height: 4px;
        background: #dedbd4;
        position: relative;
        overflow: hidden;
    }

    .s-bar-fill {
        height: 100%;
        background: #b4483d;
    }

    .ranking-gap {
        color: #b4483d;
        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 500;
    }

    .confidence-badge {
        display: inline-block;
        width: fit-content;
        padding: 4px 9px;
        font-family: Arial, sans-serif;
        font-size: 9px;
        border-radius: 3px;
    }

    .confidence-high {
        background: #e2f0e8;
        color: #397258;
    }

    .confidence-medium {
        background: #f4edd9;
        color: #8c6c28;
    }

    .confidence-low {
        background: #eee8e4;
        color: #8a6a5c;
    }

    .protection-badge {
        display: inline-block;
        background: #e1edf5;
        color: #356581;
        padding: 5px 8px;
        border-radius: 3px;
        font-family: Arial, sans-serif;
        font-size: 9px;
        line-height: 1.2;
    }

    .no-results {
        padding: 30px 15px;
        border-bottom: 1px solid #dedbd3;
        color: #88857e;
        font-family: Arial, sans-serif;
        font-size: 12px;
        background: #f8f7f3;
    }

    </style>
    """)

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="candidate-page">
        <div class="candidate-header">

        <div class="candidate-title-area">
            <div class="candidate-eyebrow">
                Mediterranean · Decision support
            </div>

            <div class="candidate-title">
                Candidate Gap Index — S
            </div>

            <div class="candidate-description">
                S measures how much observed industrial fishing effort differs
                from modelled counterfactual effort. Negative values indicate
                more fishing than expected; positive values indicate less.
                A low score is a signal for investigation only.
            </div>
        </div>

        <div class="candidate-counts">

            <div class="candidate-count">
                <div class="candidate-count-number">1,288</div>
                <div class="candidate-count-label">assessed MPAs</div>
            </div>

            <div class="candidate-count">
                <div class="candidate-count-number muted">117</div>
                <div class="candidate-count-label">not assessed</div>
            </div>

        </div>

        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Real assessed data
    # --------------------------------------------------------

    assessed_df = df[df["assessed"] == True].copy()

    # --------------------------------------------------------
    # Distribution
    # --------------------------------------------------------

    st.markdown(
        '<div class="candidate-page">'
        '<div class="distribution-label">'
        'S distribution · sample of 20 assessed MPAs · click to select'
        '</div>',
        unsafe_allow_html=True,
    )

    # Take 20 representative MPAs spread across the real S range.
    if len(assessed_df) >= 20:

        sorted_for_distribution = assessed_df.sort_values("S").reset_index(drop=True)

        sample_positions = [
            round(i * (len(sorted_for_distribution) - 1) / 19)
            for i in range(20)
        ]

        distribution_sample = sorted_for_distribution.iloc[sample_positions].copy()

    else:
        distribution_sample = assessed_df.copy()

    distribution_html = """
    <div class="distribution-box">
        <div class="distribution-negative-zone"></div>
        <div class="distribution-positive-zone"></div>
        <div class="distribution-axis"></div>
        <div class="distribution-zero"></div>
    """

    # Carefully place the real 20 S values on the axis.
    for i, (_, row) in enumerate(distribution_sample.iterrows()):

        s_value = float(row["S"])

        # Convert -1..+1 to position within the graph.
        left_position = 9 + ((s_value + 1) / 2) * 82

        # Spread dots vertically so they do not all overlap.
        dot_levels = [42, 57, 72, 50, 65]
        top_position = dot_levels[i % len(dot_levels)]

        if s_value <= -0.55:
            dot_class = "negative"
        elif s_value < -0.10:
            dot_class = "negative-soft"
        elif s_value <= 0.10:
            dot_class = "neutral"
        elif s_value < 0.55:
            dot_class = "positive-soft"
        else:
            dot_class = "positive"

        mpa_name = str(row.get("mpa_name", "MPA"))

        distribution_html += (
            f'<div class="distribution-dot {dot_class}" '
            f'style="left:{left_position:.2f}%;top:{top_position}px;" '
            f'title="{mpa_name} · S = {s_value:.2f}"></div>'
        )

    distribution_html += """
        <div class="distribution-tick" style="left:9%;">−1</div>
        <div class="distribution-tick" style="left:29.5%;">−0.5</div>
        <div class="distribution-tick" style="left:50%;">0</div>
        <div class="distribution-tick" style="left:70.5%;">+0.5</div>
        <div class="distribution-tick" style="left:91%;">+1</div>

        <div class="distribution-caption-left">
            ← candidate gap
        </div>

        <div class="distribution-caption-right">
            protection signal →
        </div>
    </div>
    """

    st.markdown(
        textwrap.dedent(distribution_html),
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # Filters
    # --------------------------------------------------------

    countries = sorted(
        assessed_df["iso3"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    confidence_options = [
        "All confidence levels",
        "High",
        "Medium",
        "Low",
    ]

    s_options = [
        "All S values",
        "Candidate gaps (S < 0)",
        "Strong candidate gaps (S < -0.5)",
        "Positive values (S > 0)",
    ]

    # Keep filter values in session state so Clear filters works.
    if "candidate_search" not in st.session_state:
        st.session_state.candidate_search = ""

    if "candidate_country" not in st.session_state:
        st.session_state.candidate_country = "All countries"

    if "candidate_confidence" not in st.session_state:
        st.session_state.candidate_confidence = "All confidence levels"

    if "candidate_s_filter" not in st.session_state:
        st.session_state.candidate_s_filter = "All S values"

    search_col, country_col, confidence_col, s_col, clear_col = st.columns(
        [2.7, 1.0, 1.25, 1.25, 0.75],
        gap="small",
    )

    with search_col:
        search_value = st.text_input(
            "Search",
            value=st.session_state.candidate_search,
            placeholder="Search by name or country...",
            label_visibility="collapsed",
            key="candidate_search_input",
        )

    with country_col:
        country_value = st.selectbox(
            "Country",
            ["All countries"] + countries,
            index=(
                ["All countries"] + countries
            ).index(st.session_state.candidate_country)
            if st.session_state.candidate_country
            in (["All countries"] + countries)
            else 0,
            label_visibility="collapsed",
            key="candidate_country_input",
        )

    with confidence_col:
        confidence_value = st.selectbox(
            "Confidence",
            confidence_options,
            index=confidence_options.index(
                st.session_state.candidate_confidence
            ),
            label_visibility="collapsed",
            key="candidate_confidence_input",
        )

    with s_col:
        s_filter_value = st.selectbox(
            "S",
            s_options,
            index=s_options.index(
                st.session_state.candidate_s_filter
            ),
            label_visibility="collapsed",
            key="candidate_s_input",
        )

    with clear_col:
        st.markdown('<div class="filter-button">', unsafe_allow_html=True)

        clear_clicked = st.button(
            "Clear filters",
            key="candidate_clear_filters",
            use_container_width=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # Apply filters
    # --------------------------------------------------------

    if clear_clicked:
        st.session_state.candidate_search = ""
        st.session_state.candidate_country = "All countries"
        st.session_state.candidate_confidence = "All confidence levels"
        st.session_state.candidate_s_filter = "All S values"
        st.rerun()

    st.session_state.candidate_search = search_value
    st.session_state.candidate_country = country_value
    st.session_state.candidate_confidence = confidence_value
    st.session_state.candidate_s_filter = s_filter_value

    filtered_df = assessed_df.copy()

    if search_value.strip():
        search_lower = search_value.strip().lower()

        filtered_df = filtered_df[
            filtered_df["mpa_name"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(search_lower, na=False)
            |
            filtered_df["iso3"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(search_lower, na=False)
        ]

    if country_value != "All countries":
        filtered_df = filtered_df[
            filtered_df["iso3"].astype(str) == country_value
        ]

    if confidence_value != "All confidence levels":
        filtered_df = filtered_df[
            filtered_df["confidence"]
            .fillna("")
            .astype(str)
            .str.lower()
            == confidence_value.lower()
        ]

    if s_filter_value == "Candidate gaps (S < 0)":
        filtered_df = filtered_df[filtered_df["S"] < 0]

    elif s_filter_value == "Strong candidate gaps (S < -0.5)":
        filtered_df = filtered_df[filtered_df["S"] < -0.5]

    elif s_filter_value == "Positive values (S > 0)":
        filtered_df = filtered_df[filtered_df["S"] > 0]

    # Sort from lowest S to highest.
    filtered_df = filtered_df.sort_values(
        "S",
        ascending=True,
        na_position="last",
    )

    # --------------------------------------------------------
    # Ranking table
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="candidate-page">
            <div class="ranking-label">
                Protected areas · sorted by candidate gap
            </div>

            <div class="ranking-header">
                <div>Protected area ↕</div>
                <div>Country ↕</div>
                <div>S / candidate gap ↑</div>
                <div>Abs. gap (hrs) ↕</div>
                <div>Confidence ↕</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Real table rows
    # --------------------------------------------------------

    rows_html = '<div class="candidate-page">'

    if filtered_df.empty:

        rows_html += """
        <div class="no-results">
            No assessed MPAs match the current filters.
        </div>
        """

    else:

        # Show the first 50 for now.
        # Pagination / scrolling comes after the visual layout is correct.
        display_df = filtered_df.head(50)

        for _, row in display_df.iterrows():

            name = str(row.get("mpa_name", "Unnamed MPA"))
            country = str(row.get("iso3", "—"))

            try:
                s_value = float(row["S"])
            except Exception:
                s_value = 0.0

            try:
                gap_value = float(row["abs_gap_hours"])
            except Exception:
                gap_value = 0.0

            confidence = str(row.get("confidence", "—"))

            # Confidence styling.
            confidence_lower = confidence.lower()

            if confidence_lower == "high":
                confidence_class = "confidence-high"
            elif confidence_lower == "medium":
                confidence_class = "confidence-medium"
            else:
                confidence_class = "confidence-low"

            # Relative bar length.
            bar_width = min(abs(s_value), 1.0) * 100

            # Absolute gap formatting.
            if abs(gap_value) >= 1_000_000:
                gap_text = f"{gap_value / 1_000_000:+.1f}m hrs"
            elif abs(gap_value) >= 1_000:
                gap_text = f"{gap_value / 1_000:+.1f}k hrs"
            else:
                gap_text = f"{gap_value:+.0f} hrs"

            rows_html += f"""
            <div class="ranking-row">

                <div class="ranking-name">
                    {name}
                </div>

                <div class="ranking-country">
                    {country}
                </div>

                <div class="ranking-s">
                    <span>{s_value:+.2f}</span>
                    <span class="s-bar">
                        <span
                            class="s-bar-fill"
                            style="width:{bar_width:.1f}%"
                        ></span>
                    </span>
                </div>

                <div class="ranking-gap">
                    {gap_text}
                </div>

                <div>
                    <span class="confidence-badge {confidence_class}">
                        {confidence}
                    </span>
                </div>

            </div>
            """

    rows_html += "</div>"

    st.markdown(
        textwrap.dedent(rows_html),
        unsafe_allow_html=True,
    )
