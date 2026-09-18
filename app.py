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
    # PAGE HEADER
    # --------------------------------------------------------

    st.markdown(
        '<div class="eyebrow">Mediterranean · Candidate gaps</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "# Where observed fishing differs from expected"
    )

    st.markdown(
        """
        <div class="intro">
        Explore candidate enforcement gaps by comparing observed industrial
        fishing effort with the effort expected in comparable unprotected water.
        A lower S value indicates a larger difference between observed and expected effort.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # BACK BUTTON
    # --------------------------------------------------------

    if st.button("← Back to overview"):
        st.session_state.page = "welcome"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # ASSESSED DATA
    # --------------------------------------------------------

    assessed_df = df[df["assessed"] == True].copy()

    # Make sure S is numeric
    assessed_df["S"] = pd.to_numeric(
        assessed_df["S"],
        errors="coerce"
    )

    assessed_df = assessed_df.dropna(subset=["S"])

    # --------------------------------------------------------
    # DISTRIBUTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            border-top:1px solid #dedbd3;
            border-bottom:1px solid #dedbd3;
            padding:25px 0 30px 0;
            margin:10px 0 30px 0;
        ">
            <div style="
                font-size:11px;
                letter-spacing:1.8px;
                color:#77756e;
                font-weight:600;
                text-transform:uppercase;
                margin-bottom:8px;
            ">
                Candidate gap index
            </div>

            <div style="
                font-family:Georgia, serif;
                font-size:25px;
                color:#262522;
                margin-bottom:8px;
            ">
                Distribution of S across assessed protected areas
            </div>

            <div style="
                color:#77756e;
                font-size:13px;
                line-height:1.5;
            ">
                Each point represents one assessed protected area.
                Select an area below to inspect its observed and expected effort.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # S DISTRIBUTION CHART
    # --------------------------------------------------------

    import plotly.graph_objects as go

    chart_df = assessed_df.copy()

    chart_df["y"] = 0

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=chart_df["S"],
            y=chart_df["y"],
            mode="markers",
            marker=dict(
                size=8,
                opacity=0.55,
            ),
            customdata=chart_df[
                [
                    "mpa_name",
                    "iso3",
                    "S",
                    "abs_gap_hours",
                    "confidence",
                ]
            ],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "%{customdata[1]}<br>"
                "S = %{customdata[2]:.3f}<br>"
                "Absolute gap = %{customdata[3]:,.0f} hours<br>"
                "Confidence = %{customdata[4]}"
                "<extra></extra>"
            ),
        )
    )

    fig.add_vline(
        x=0,
        line_width=1,
        line_dash="dash",
    )

    fig.update_layout(
        height=150,
        margin=dict(l=10, r=10, t=10, b=35),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis=dict(
            range=[-1, 1],
            tickmode="array",
            tickvals=[-1, -0.5, 0, 0.5, 1],
            ticktext=[
                "-1",
                "-0.5",
                "0",
                "+0.5",
                "+1",
            ],
            title="S",
            zeroline=False,
            showgrid=False,
        ),
        yaxis=dict(
            visible=False,
            range=[-1, 1],
        ),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        },
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            font-family:Georgia, serif;
            font-size:22px;
            margin:25px 0 15px 0;
            color:#262522;
        ">
            Explore assessed areas
        </div>
        """,
        unsafe_allow_html=True,
    )

    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(
        [1.5, 1, 1, 1]
    )

    with filter_col1:
        search = st.text_input(
            "Search protected area",
            placeholder="Search by name...",
        )

    with filter_col2:
        countries = ["All"] + sorted(
            assessed_df["iso3"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_country = st.selectbox(
            "Country",
            countries,
        )

    with filter_col3:
        confidence_options = [
            "All",
            "High",
            "Medium",
            "Low",
        ]

        selected_confidence = st.selectbox(
            "Confidence",
            confidence_options,
        )

    with filter_col4:
        protection_options = ["All"]

        if "iucn_cat" in assessed_df.columns:
            protection_options += sorted(
                assessed_df["iucn_cat"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        selected_protection = st.selectbox(
            "Protection level",
            protection_options,
        )

    # --------------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------------

    filtered_df = assessed_df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["mpa_name"]
            .fillna("")
            .str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    if selected_country != "All":
        filtered_df = filtered_df[
            filtered_df["iso3"] == selected_country
        ]

    if selected_confidence != "All":
        filtered_df = filtered_df[
            filtered_df["confidence"]
            .astype(str)
            .str.lower()
            == selected_confidence.lower()
        ]

    if selected_protection != "All":
        filtered_df = filtered_df[
            filtered_df["iucn_cat"]
            .astype(str)
            == selected_protection
        ]

    # --------------------------------------------------------
    # MASTER / DETAIL LAYOUT
    # --------------------------------------------------------

    table_col, detail_col = st.columns(
        [1.35, 0.9],
        gap="large",
    )

    # --------------------------------------------------------
    # LEFT: RANKING TABLE
    # --------------------------------------------------------

    with table_col:

        st.markdown(
            f"""
            <div style="
                color:#77756e;
                font-size:12px;
                margin-bottom:12px;
            ">
                {len(filtered_df):,} areas shown
            </div>
            """,
            unsafe_allow_html=True,
        )

        display_df = filtered_df.sort_values(
            "S",
            ascending=True,
        ).copy()

        display_df["S"] = display_df["S"].round(3)

        display_df["abs_gap_hours"] = display_df[
            "abs_gap_hours"
        ].round(0)

        table_columns = [
            "mpa_name",
            "S",
            "abs_gap_hours",
            "confidence",
        ]

        available_columns = [
            col for col in table_columns
            if col in display_df.columns
        ]

        st.dataframe(
            display_df[available_columns],
            use_container_width=True,
            hide_index=True,
            column_config={
                "mpa_name": st.column_config.TextColumn(
                    "Protected area",
                ),
                "S": st.column_config.NumberColumn(
                    "S",
                    format="%.3f",
                ),
                "abs_gap_hours": st.column_config.NumberColumn(
                    "Absolute gap (hours)",
                    format="%,.0f",
                ),
                "confidence": st.column_config.TextColumn(
                    "Confidence",
                ),
            },
        )

    # --------------------------------------------------------
    # RIGHT: DETAIL PANEL
    # --------------------------------------------------------

    with detail_col:

        st.markdown(
            """
            <div style="
                border-left:1px solid #dedbd3;
                padding-left:25px;
                min-height:400px;
            ">
            """,
            unsafe_allow_html=True,
        )

        if len(filtered_df) > 0:

            selected_index = st.selectbox(
                "Inspect protected area",
                filtered_df.index,
                format_func=lambda i: filtered_df.loc[
                    i, "mpa_name"
                ],
            )

            selected = filtered_df.loc[selected_index]

            name = selected.get(
                "mpa_name",
                "Unnamed protected area",
            )

            s_value = float(selected["S"])

            observed = selected.get(
                "observed_hours_cells",
                None,
            )

            expected = selected.get(
                "expected_hours_inside",
                None,
            )

            abs_gap = selected.get(
                "abs_gap_hours",
                None,
            )

            confidence = selected.get(
                "confidence",
                "not assessed",
            )

            # Normalise confidence casing
            confidence_display = str(
                confidence
            ).strip().capitalize()

            if confidence_display.lower() == "Not assessed".lower():
                confidence_display = "not assessed"

            st.markdown(
                f"""
                <div style="
                    font-size:11px;
                    letter-spacing:1.6px;
                    color:#77756e;
                    text-transform:uppercase;
                    margin-bottom:8px;
                ">
                    Protected area
                </div>

                <div style="
                    font-family:Georgia, serif;
                    font-size:28px;
                    line-height:1.15;
                    color:#262522;
                    margin-bottom:20px;
                ">
                    {name}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # S
            st.markdown(
                f"""
                <div style="
                    font-size:11px;
                    letter-spacing:1.5px;
                    color:#77756e;
                    text-transform:uppercase;
                ">
                    Candidate gap index
                </div>

                <div style="
                    font-family:Georgia, serif;
                    font-size:46px;
                    color:#1f5f8b;
                    margin:3px 0 4px 0;
                ">
                    {s_value:.3f}
                </div>
                """,
                unsafe_allow_html=True,
            )

            if s_value < -0.5:
                interpretation = (
                    "Observed fishing effort is substantially "
                    "higher relative to expected effort."
                )
            elif s_value < 0:
                interpretation = (
                    "Observed fishing effort is higher than "
                    "expected effort."
                )
            elif s_value < 0.5:
                interpretation = (
                    "Observed fishing effort is below "
                    "expected effort."
                )
            else:
                interpretation = (
                    "Observed fishing effort is substantially "
                    "below expected effort."
                )

            st.markdown(
                f"""
                <div style="
                    background:#eeece6;
                    border:1px solid #dedbd3;
                    padding:14px;
                    margin:12px 0 22px 0;
                    color:#5f5d57;
                    font-size:13px;
                    line-height:1.55;
                ">
                    {interpretation}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Observed vs expected
            st.markdown(
                """
                <div style="
                    font-family:Georgia, serif;
                    font-size:20px;
                    color:#262522;
                    margin-bottom:12px;
                ">
                    Fishing effort
                </div>
                """,
                unsafe_allow_html=True,
            )

            effort_col1, effort_col2 = st.columns(2)

            with effort_col1:
                if pd.notna(observed):
                    st.metric(
                        "Observed",
                        f"{observed:,.0f} h",
                    )

            with effort_col2:
                if pd.notna(expected):
                    st.metric(
                        "Expected",
                        f"{expected:,.0f} h",
                    )

            if pd.notna(abs_gap):
                st.markdown(
                    f"""
                    <div style="
                        margin-top:10px;
                        color:#62615c;
                        font-size:13px;
                    ">
                        Absolute gap: <strong>
                        {abs_gap:,.0f} hours
                        </strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Confidence
            st.markdown(
                f"""
                <div style="
                    border-top:1px solid #dedbd3;
                    margin-top:25px;
                    padding-top:18px;
                ">
                    <div style="
                        font-size:11px;
                        letter-spacing:1.5px;
                        color:#77756e;
                        text-transform:uppercase;
                    ">
                        Confidence
                    </div>

                    <div style="
                        font-family:Georgia, serif;
                        font-size:20px;
                        margin-top:4px;
                        color:#262522;
                    ">
                        {confidence_display}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Context
            st.markdown(
                """
                <div style="
                    border-top:1px solid #dedbd3;
                    margin-top:20px;
                    padding-top:18px;
                ">
                    <div style="
                        font-family:Georgia, serif;
                        font-size:20px;
                        color:#262522;
                        margin-bottom:10px;
                    ">
                        Context
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            context_items = []

            if pd.notna(selected.get("iso3", None)):
                context_items.append(
                    f"Country: {selected['iso3']}"
                )

            if pd.notna(selected.get("iucn_cat", None)):
                context_items.append(
                    f"Protection category: {selected['iucn_cat']}"
                )

            if pd.notna(selected.get("site_type", None)):
                context_items.append(
                    f"Site type: {selected['site_type']}"
                )

            if pd.notna(selected.get("area_km2", None)):
                context_items.append(
                    f"Area: {selected['area_km2']:,.1f} km²"
                )

            for item in context_items:
                st.markdown(
                    f"""
                    <div style="
                        color:#62615c;
                        font-size:13px;
                        padding:6px 0;
                        border-bottom:1px solid #eeece6;
                    ">
                        {item}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Provenance
            source = selected.get(
                "predictions_source",
                None,
            )

            if pd.notna(source):
                st.markdown(
                    f"""
                    <div style="
                        margin-top:22px;
                        color:#9a9992;
                        font-size:11px;
                        line-height:1.5;
                    ">
                        Prediction source: {source}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.markdown(
                """
                <div style="
                    padding:50px 10px;
                    color:#77756e;
                    text-align:center;
                ">
                    No protected areas match the selected filters.
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )
