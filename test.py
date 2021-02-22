import streamlit as st
import pandas as pd
import numpy as np


st.write(
    """
# Cathodic Protection Design. Khoya khoya chand. KHula aasmaan.
## DNVGL-RP-F103
"""
)

st.sidebar.header("User Input Parameters")


uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is None:
    data = pd.read_csv("data.csv")
else:
    data = pd.read_csv(uploaded_file)

if st.checkbox("Show Input"):
    st.table(data)

aa = st.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phonewa")
)

st.write(np.random.randn(5, 3))
