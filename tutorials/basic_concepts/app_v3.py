"""
Use streamlit dataframe method to visualize data:
Usage:
streamlit run app_v3.py
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write('Writing dataframe with numpy:')
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.write('Writing a dataframe with styling using the pandas Styler')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write('Static table generation with streamlit:')
st.table(pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
))