import streamlit as st

st.set_page_config(
    page_title="Mediterranean MPA Enforcement Intelligence",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

    st.button("Explore candidate gaps  →")

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
<span class="dataset-number">21</span>
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

# TEMPORARY DATA CHECK
st.markdown("---")
st.subheader("Temporary data check")

import pandas as pd

DATA_PATH = "data/mpa_ranking.parquet"

try:
    df = pd.read_parquet(DATA_PATH)

    st.success(f"Data loaded: {len(df):,} rows")

    st.write("**Columns:**")
    st.write(list(df.columns))

    st.write("**First 5 rows:**")
    st.dataframe(df.head(), use_container_width=True)

except Exception as e:
    st.error("Could not load the ranking data.")
    st.exception(e)
