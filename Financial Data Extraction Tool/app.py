import streamlit as st
import pandas as pd
import helper
st.title("Financial Extractor Tool")
financial_data_df = pd.DataFrame({
    "Measure": ["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
    "Value": ["", "", "", "", ""]
    })

col1,col2 = st.columns([3,2])

with col1:
    st.header("Extractor tool")
    article = st.text_area("Paste your article here",height=300)
    if st.button("extract"):
        financial_data_df = helper.extract_financial_info(article)

with col2:

    st.markdown("<br/>" * 3, unsafe_allow_html=True) # Creates 5 lines of vertical space
    st.dataframe(
        financial_data_df,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True
    )