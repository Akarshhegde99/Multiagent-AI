import streamlit as st
from agents import data_agent, analysis_agent, viz_agent, ai_agent
from agents import data_agent, analysis_agent, viz_agent, ai_agent  # already there


# Must be the first Streamlit command in the script
st.set_page_config(page_title="MultiAgent AI", layout="wide")

st.title("📊 MultiAgent AI - CSV Insight Engine")

with st.sidebar:
    st.image("https://static.streamlit.io/examples/logo.png", width=200)
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = data_agent.load_csv(uploaded_file)

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Data Preview", "📊 Analysis", "📈 Visualizations", "🤖 AI Insights"])

    with tab1:
        st.subheader("CSV Preview")
        st.dataframe(df.head(), use_container_width=True)

    with tab2:
        st.subheader("Data Analysis")
        st.dataframe(analysis_agent.describe_data(df), use_container_width=True)

    with tab3:
        st.subheader("Data Visualizations")
        viz_agent.render_charts(df)

    # ... earlier code remains unchanged ...

    with tab4:
        st.subheader("AI-Powered Insights")

        if st.button("Generate Insights"):
            with st.spinner("Thinking..."):
                prompt   = ai_agent.generate_prompt(df)
                response = ai_agent.query_ai(prompt)

            st.success("Done!")
            st.markdown(response)          # ← show the AI answer


else:
    st.info("Upload a CSV file to get started.")
