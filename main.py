import streamlit as st
from agents import run_agent

st.set_page_config(
    page_title="Business Opportunity Agent",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Business Opportunity Intelligence Agent")
st.markdown("Powered by Claude AI + LangGraph")
with st.expander("🗺️ View Agent Graph"):
    st.graphviz_chart("""
        digraph {
            bgcolor="#0e1117"
            node [style=filled fillcolor="#1b2a4a" color="#2e6da4" fontcolor="white" fontname="Arial"]
            edge [color="#2e6da4"]
            START [fillcolor="#2e6da4" shape=oval]
            END [fillcolor="#2e6da4" shape=oval]
            START -> Researcher
            Researcher -> Scorer
            Scorer -> Summariser
            Summariser -> END
        }
    """)

st.sidebar.header("Company Profile")
company_profile = st.sidebar.text_area(
    "Describe your company:",
    placeholder="e.g. We are a Melbourne-based cloud software company specialising in AI solutions for the banking sector...",
    height=200
)

run_button = st.sidebar.button("🚀 Find Opportunities", type="primary")

if run_button:
    if not company_profile:
        st.warning("Please enter a company profile first!")
    else:
        with st.spinner("Agent is working..."):
            result = run_agent(company_profile)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔍 Opportunities Found")
            st.write(result["opportunities"][0])

            st.subheader("📊 Scores & Reasoning")
            st.write(result["scores"][0])

        with col2:
            st.subheader("📝 Executive Summary")
            st.info(result["summary"])