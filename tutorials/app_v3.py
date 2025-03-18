"""
Use streamlit dataframe method to visualize data:
Usage:
streamlit run app_v3.py
"""

import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)