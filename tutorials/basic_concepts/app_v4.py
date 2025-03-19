"""
Drawing a line chart and plotting a map with streamlit
Usage:
streamlit run app_v4.py
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write('Drawing a chart:')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.write('Plotting a map:')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)