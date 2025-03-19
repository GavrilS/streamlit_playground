"""
First tutorial app - use data to create a table
Usage:
streamlit run app.py
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

# Magic commands - every time streamlit sees a variable on its own line, it automatically writes
# that to our app using 'st.write()'
df