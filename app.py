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
            font-size: 2.8rem;
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
            font-size: 1.05rem;
            line-height: 1.65;
            max-width: 700px;
        }

        .notice {
            background: #fbf1e4;
            border-left: 3px solid #c47a2c;
            padding: 1rem 1.2rem;
            margin: 1.5rem 0;
            color: #5d4630;
            line-height: 1.55;
        }

        .metric-label {
            color: #77756e;
            font-size: 0.8rem;
            margin-bottom: 0.25rem;
        }

        .metric-value {
            color: #262522;
            font-family: Georgia, serif;
            font-size: 2rem;
            line-height: 1.2;
        }

        .site-footer {
            border-top: 1px solid #deddd7;
            margin-top: 4rem;
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
<div style="
    border-bottom: 1px solid #deddd7;
    padding: 0.5rem 0 1rem 0;
    margin-bottom: 3rem;
">
    <div style="
        color: #1f5f8b;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.04em;
    ">
        ◯ &nbsp; MPA Enforcement Intelligence
    </div>

    <div style="
        color: #9a9992;
        font-size: 0.65rem;
        letter-spacing: 0.12em;
        margin-top: 0.2rem;
        margin-left: 1.8rem;
    ">
        MEDITERRANEAN · DECISION SUPPORT
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Page introduction
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
    fishing effort with what a comparable unprotected area would be
    expected to experience.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="notice">
    <strong>A candidate gap is a signal for investigation, not proof of
    illegal fishing or failed enforcement.</strong>
    Multiple explanations may account for an observed difference between
    expected and observed fishing effort.
</div>
""",
    unsafe_allow_html=True,
)

# Dataset overview
st.markdown("### Dataset overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-label">Assessed MPAs</div>
        <div class="metric-value">1,288</div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="metric-label">Not assessed</div>
        <div class="metric-value">117</div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="metric-label">Analysis period</div>
        <div class="metric-value">2015–</div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
<div class="site-footer">
    AIS data · Industrial fishing vessels &nbsp; · &nbsp;
    Not a verdict. A signal for investigation. &nbsp; · &nbsp;
    Mediterranean basin coverage
</div>
""",
    unsafe_allow_html=True,
)
