"""
Add a progress bar.
Usage:
streamlit run app_v7.py
"""

import time
import streamlit as st

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we are done!'