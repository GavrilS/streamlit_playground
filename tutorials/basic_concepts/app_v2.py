"""
First tutorial app - use data to create a table
Usage:
streamlit run app_v2.py
"""

import streamlit as st
import pandas as pd

# Showing app data with 'st.write()'
st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
}))