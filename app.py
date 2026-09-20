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

    # --------------------------------------------------------
    # CANDIDATE GAPS PAGE STYLES
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* Candidate page navigation */

        .candidate-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #deddd7;
            padding: 0 0 0 0;
            margin-bottom: 38px;
            height: 58px;
        }

        .candidate-brand {
            font-family: Georgia, serif;
            font-size: 15px;
            font-weight: 600;
            color: #262522;
            white-space: nowrap;
        }

        .candidate-brand-sub {
            font-family: Arial, sans-serif;
            font-size: 9px;
            letter-spacing: 0.13em;
            color: #aaa79d;
            margin-top: 4px;
        }

        .candidate-logo {
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        .candidate-logo-mark {
            width: 22px;
            height: 22px;
            border: 1.5px solid #1f5f8b;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: #1f5f8b;
            font-size: 11px;
        }

        .candidate-section-label {
            color: #a29f94;
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 0.13em;
            text-transform: uppercase;
        }

        .candidate-description {
            color: #77756e;
            font-size: 13px;
            line-height: 1.55;
            max-width: 670px;
        }

        .candidate-count {
            text-align: center;
        }

        .candidate-count-number {
            font-family: Georgia, serif;
            font-size: 27px;
            color: #1f5f8b;
            line-height: 1;
        }

        .candidate-count-number.muted {
            color: #aaa79d;
        }

        .candidate-count-label {
            color: #aaa79d;
            font-size: 10px;
            margin-top: 7px;
        }

        /* Distribution */

        .distribution-label {
            color: #aaa79d;
            font-size: 9px;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 9px;
        }

        .distribution-box {
            position: relative;
            height: 150px;
            border: 1px solid #deddd7;
            background: #f7f6f2;
            overflow: hidden;
        }

        .distribution-negative {
            position: absolute;
            left: 14%;
            right: 50%;
            top: 28px;
            bottom: 42px;
            background: #fbf3f0;
        }

        .distribution-positive {
            position: absolute;
            left: 50%;
            right: 14%;
            top: 28px;
            bottom: 42px;
            background: #f1f6f1;
        }

        .distribution-axis {
            position: absolute;
            left: 14%;
            right: 14%;
            bottom: 42px;
            height: 1px;
            background: #d4d1c8;
        }

        .distribution-zero {
            position: absolute;
            left: 50%;
            top: 28px;
            bottom: 42px;
            width: 1px;
            background: #d4d1c8;
        }

        .distribution-dot {
            position: absolute;
            width: 11px;
            height: 11px;
            border-radius: 50%;
            transform: translate(-50%, -50%);
        }

        .distribution-tick {
            position: absolute;
            bottom: 14px;
            transform: translateX(-50%);
            color: #aaa79d;
            font-family: monospace;
            font-size: 9px;
        }

        .distribution-note-left {
            position: absolute;
            left: 14%;
            bottom: 1px;
            transform: translateX(10%);
            color: #b25b49;
            font-size: 9px;
            font-style: italic;
        }

        .distribution-note-right {
            position: absolute;
            right: 14%;
            bottom: 1px;
            transform: translateX(-10%);
            color: #377457;
            font-size: 9px;
            font-style: italic;
        }

        /* Filter bar */

        .filter-shell {
            background: #eeece6;
            border: 1px solid #dedbd3;
            padding: 10px;
            margin-top: 26px;
            margin-bottom: 25px;
        }

        /* Ranking table */

        .ranking-header {
            display: grid;
            grid-template-columns: 2.25fr 0.9fr 1.45fr 1.25fr 1.05fr;
            align-items: center;
            padding: 0 14px 10px 14px;
            border-bottom: 1px solid #cfcac0;
            color: #77756e;
            font-size: 9px;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .ranking-row {
            display: grid;
            grid-template-columns: 2.25fr 0.9fr 1.45fr 1.25fr 1.05fr;
            align-items: center;
            min-height: 54px;
            padding: 0 14px;
            border-bottom: 1px solid #e5e2db;
            background: #f7f6f2;
        }

        .ranking-row:nth-child(even) {
            background: #f3f2ee;
        }

        .ranking-name {
            color: #262522;
            font-size: 12px;
            font-weight: 500;
        }

        .ranking-country {
            color: #77756e;
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
            min-width: 43px;
        }

        .ranking-s-bar {
            width: 58px;
            height: 4px;
            background: #deddd7;
            position: relative;
        }

        .ranking-s-fill {
            position: absolute;
            left: 0;
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
            font-size: 9px;
            font-weight: 600;
        }

        .confidence-high {
            background: #dfeee5;
            color: #387256;
        }

        .confidence-medium {
            background: #f3ecd9;
            color: #896b28;
        }

        .confidence-low {
            background: #eee5e3;
            color: #87594e;
        }

        .rules-placeholder {
            display: inline-block;
            background: #dfebf4;
            color: #35617e;
            padding: 5px 8px;
            border-radius: 4px;
            font-size: 9px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # TOP NAVIGATION
    # --------------------------------------------------------

    nav_left, nav_candidate, nav_not_assessed, nav_method = st.columns(
        [3.8, 1, 1, 1],
        gap="small",
    )

    with nav_left:
        if st.button(
            "◯  MPA Enforcement Intelligence",
            key="candidate_logo",
        ):
            st.session_state.page = "welcome"
            st.rerun()

        st.markdown(
            """
            <div style="
                margin-left:31px;
                margin-top:-15px;
                color:#aaa79d;
                font-size:8px;
                letter-spacing:0.13em;
            ">
                MEDITERRANEAN · DECISION SUPPORT
            </div>
            """,
            unsafe_allow_html=True,
        )

    with nav_candidate:
        st.markdown(
            """
            <div style="
                color:#1f5f8b;
                font-size:12px;
                font-weight:600;
                text-align:center;
                padding-top:10px;
                padding-bottom:12px;
                border-bottom:2px solid #1f5f8b;
            ">
                Candidate gaps
            </div>
            """,
            unsafe_allow_html=True,
        )

    with nav_not_assessed:
        if st.button(
            "Not assessed",
            key="candidate_nav_not_assessed",
        ):
            st.session_state.page = "not_assessed"
            st.rerun()

    with nav_method:
        if st.button(
            "Methodology",
            key="candidate_nav_methodology",
        ):
            st.session_state.page = "methodology"
            st.rerun()

    # --------------------------------------------------------
    # PAGE INTRO
    # --------------------------------------------------------

    st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True)

    intro_left, intro_count_1, intro_count_2 = st.columns(
        [5.4, 1, 1],
        gap="large",
    )

    with intro_left:

        st.markdown(
            """
            <div style="
                font-family:Georgia, serif;
                font-size:25px;
                font-weight:600;
                color:#262522;
                margin-bottom:8px;
            ">
                Candidate Gap Index — S
            </div>

            <div class="candidate-description">
                S measures how much observed industrial fishing effort differs
                from modelled counterfactual effort. Negative values indicate
                more fishing than expected; positive values indicate less.
                A low score is a signal for investigation only.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with intro_count_1:

        st.markdown(
            """
            <div class="candidate-count">
                <div class="candidate-count-number">1,288</div>
                <div class="candidate-count-label">assessed MPAs</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with intro_count_2:

        st.markdown(
            """
            <div class="candidate-count">
                <div class="candidate-count-number muted">117</div>
                <div class="candidate-count-label">not assessed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="
            border-bottom:1px solid #deddd7;
            margin-top:26px;
            margin-bottom:35px;
        "></div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # DATA
    # --------------------------------------------------------

    assessed_df = df[df["assessed"] == True].copy()

    assessed_df["S"] = pd.to_numeric(
        assessed_df["S"],
        errors="coerce",
    )

    assessed_df = assessed_df.dropna(subset=["S"])

    # --------------------------------------------------------
    # S DISTRIBUTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="distribution-label">
            S distribution · sample of 20 assessed MPAs · click to select
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Select 20 real MPAs distributed across the S range.
    sorted_sample = assessed_df.sort_values("S").reset_index(drop=True)

    if len(sorted_sample) > 20:
        sample_positions = [
            round(i * (len(sorted_sample) - 1) / 19)
            for i in range(20)
        ]
        distribution_df = sorted_sample.iloc[
            sample_positions
        ].copy()
    else:
        distribution_df = sorted_sample.copy()

    distribution_html = """
    <div class="distribution-box">
        <div class="distribution-negative"></div>
        <div class="distribution-positive"></div>
        <div class="distribution-axis"></div>
        <div class="distribution-zero"></div>
    """

    dot_heights = [
        69, 48, 34, 57, 43,
        62, 45, 57, 37, 51,
        40, 60, 47, 31, 56,
        43, 61, 38, 55, 45,
    ]

    for i, (_, row) in enumerate(
        distribution_df.iterrows()
    ):

        s_value = float(row["S"])

        left_percent = 14 + ((s_value + 1) / 2) * 72

        top_percent = dot_heights[
            i % len(dot_heights)
        ]

        if s_value < -0.65:
            dot_color = "#a63d32"
        elif s_value < -0.3:
            dot_color = "#c2674e"
        elif s_value < 0:
            dot_color = "#c88c51"
        elif s_value < 0.35:
            dot_color = "#8b8b78"
        elif s_value < 0.7:
            dot_color = "#4f8568"
        else:
            dot_color = "#28664b"

        distribution_html += f"""
            <div
                class="distribution-dot"
                title="{str(row.get('mpa_name', 'MPA'))}"
                style="
                    left:{left_percent:.2f}%;
                    top:{top_percent}%;
                    background:{dot_color};
                "
            ></div>
        """

    distribution_html += """
        <div class="distribution-tick" style="left:14%;">−1</div>
        <div class="distribution-tick" style="left:32%;">−0.5</div>
        <div class="distribution-tick" style="left:50%;">0</div>
        <div class="distribution-tick" style="left:68%;">+0.5</div>
        <div class="distribution-tick" style="left:86%;">+1</div>

        <div class="distribution-note-left">
            ← candidate gap
        </div>

        <div class="distribution-note-right">
            protection signal →
        </div>
    </div>
    """

    st.markdown(
        distribution_html,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # FILTER BAR
    # --------------------------------------------------------

    filter_container = st.container()

    with filter_container:

        f1, f2, f3, f4, f5, f6 = st.columns(
            [2.6, 1, 1.25, 1.15, 1.15, 0.8],
            gap="small",
        )

        with f1:
            search_value = st.text_input(
                "Search",
                placeholder="⌕  Search by name or country...",
                label_visibility="collapsed",
                key="candidate_search",
            )

        with f2:

            countries = [
                "All countries"
            ] + sorted(
                assessed_df["iso3"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            selected_country = st.selectbox(
                "Country",
                countries,
                label_visibility="collapsed",
                key="candidate_country",
            )

        with f3:

            confidence_options = [
                "All confidence levels",
                "High",
                "Medium",
                "Low",
            ]

            selected_confidence = st.selectbox(
                "Confidence",
                confidence_options,
                label_visibility="collapsed",
                key="candidate_confidence",
            )

        with f4:

            restriction_options = [
                "Restricted",
                "All rules",
            ]

            selected_restriction = st.selectbox(
                "Fishing rules",
                restriction_options,
                label_visibility="collapsed",
                key="candidate_restriction",
            )

        with f5:

            s_options = [
                "All S values",
                "Candidate gaps (S < 0)",
                "Protection signal (S ≥ 0)",
            ]

            selected_s = st.selectbox(
                "S range",
                s_options,
                label_visibility="collapsed",
                key="candidate_s_range",
            )

        with f6:

            if st.button(
                "Clear filters",
                key="candidate_clear_filters",
            ):
                st.session_state.candidate_search = ""
                st.session_state.candidate_country = "All countries"
                st.session_state.candidate_confidence = "All confidence levels"
                st.session_state.candidate_restriction = "Restricted"
                st.session_state.candidate_s_range = "All S values"
                st.rerun()

    # --------------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------------

    filtered_df = assessed_df.copy()

    if search_value:

        search_lower = search_value.lower()

        name_match = (
            filtered_df["mpa_name"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(
                search_lower,
                regex=False,
            )
        )

        country_match = (
            filtered_df["iso3"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(
                search_lower,
                regex=False,
            )
        )

        filtered_df = filtered_df[
            name_match | country_match
        ]

    if selected_country != "All countries":

        filtered_df = filtered_df[
            filtered_df["iso3"].astype(str)
            == selected_country
        ]

    if selected_confidence != "All confidence levels":

        filtered_df = filtered_df[
            filtered_df["confidence"]
            .astype(str)
            .str.lower()
            == selected_confidence.lower()
        ]

    if selected_s == "Candidate gaps (S < 0)":

        filtered_df = filtered_df[
            filtered_df["S"] < 0
        ]

    elif selected_s == "Protection signal (S ≥ 0)":

        filtered_df = filtered_df[
            filtered_df["S"] >= 0
        ]

    # --------------------------------------------------------
    # TABLE HEADER
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            color:#aaa79d;
            font-size:9px;
            letter-spacing:0.1em;
            text-transform:uppercase;
            margin:8px 0 9px 0;
        ">
            Protected areas · sorted by candidate gap
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sort by S
    table_df = filtered_df.sort_values(
        "S",
        ascending=True,
    ).copy()

    # --------------------------------------------------------
    # RANKING TABLE
    # --------------------------------------------------------

    table_html = """
    <div class="ranking-header">
        <div>Protected area ↕</div>
        <div>Country ↕</div>
        <div>S / candidate gap ↑</div>
        <div>Abs. gap (hrs) ↕</div>
        <div>Confidence ↕</div>
    </div>
    """

    # Show the first 10 rows for the initial view.
    for _, row in table_df.head(10).iterrows():

        name = str(
            row.get(
                "mpa_name",
                "Unnamed MPA",
            )
        )

        iso3 = str(
            row.get(
                "iso3",
                "—",
            )
        )

        s_value = float(
            row.get(
                "S",
                0,
            )
        )

        gap = row.get(
            "abs_gap_hours",
            None,
        )

        confidence = str(
            row.get(
                "confidence",
                "not assessed",
            )
        ).strip()

        confidence_lower = confidence.lower()

        if confidence_lower == "high":
            confidence_class = "confidence-high"
        elif confidence_lower == "medium":
            confidence_class = "confidence-medium"
        elif confidence_lower == "low":
            confidence_class = "confidence-low"
        else:
            confidence_class = "confidence-medium"

        if s_value < 0:
            s_color = "#a63d32"
            fill_color = "#a63d32"
            bar_width = min(
                58,
                max(
                    3,
                    abs(s_value) * 58,
                ),
            )
        else:
            s_color = "#377457"
            fill_color = "#377457"
            bar_width = min(
                58,
                max(
                    3,
                    abs(s_value) * 58,
                ),
            )

        if pd.notna(gap):
            gap_text = f"+{gap:,.0f} hrs"
        else:
            gap_text = "—"

        # Fishing rules are not present in the ranking parquet.
        # We do not invent a rule.
        rules_text = "Protection data"

        table_html += f"""
        <div class="ranking-row">

            <div class="ranking-name">
                {name}
            </div>

            <div class="ranking-country">
                {iso3}
            </div>

            <div class="ranking-s">

                <span
                    class="ranking-s-value"
                    style="color:{s_color};"
                >
                    {s_value:+.2f}
                </span>

                <span class="ranking-s-bar">
                    <span
                        class="ranking-s-fill"
                        style="
                            width:{bar_width:.1f}px;
                            background:{fill_color};
                        "
                    ></span>
                </span>

            </div>

            <div class="ranking-gap">
                {gap_text}
            </div>

            <div>
                <span class="confidence-tag {confidence_class}">
                    {confidence.capitalize()}
                </span>
            </div>

        </div>
        """

    if len(table_df) == 0:

        table_html += """
        <div style="
            padding:35px;
            text-align:center;
            color:#77756e;
            font-size:12px;
        ">
            No assessed protected areas match these filters.
        </div>
        """

    st.markdown(
        table_html,
        unsafe_allow_html=True,
    )
