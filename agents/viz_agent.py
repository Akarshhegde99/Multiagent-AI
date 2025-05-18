import streamlit as st
import plotly.express as px

def render_charts(df):
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if not numeric_cols:
        st.warning("No numeric columns to plot.")
        return

    col1, col2 = st.columns(2)

    with col1:
        col_name = st.selectbox("Select column for histogram", numeric_cols)
        fig = px.histogram(df, x=col_name)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        if len(numeric_cols) >= 2:
            x_axis = st.selectbox("X-axis", numeric_cols, key="x")
            y_axis = st.selectbox("Y-axis", numeric_cols, key="y")
            fig2 = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[0])
            st.plotly_chart(fig2, use_container_width=True)
