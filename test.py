import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# My first Application. Kya baat hai...
""")

st.sidebar.header('User Input Parameters')

uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is None:
    data = pd.read_csv("data.csv")
else:
    data = pd.read_csv(uploaded_file)
st.write(data)




