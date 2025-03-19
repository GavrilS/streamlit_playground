"""
Adding widgets with streamlit
Usage:
streamlit run app_v5.py
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write('Adding slider')
x = st.slider('x') # <- this is a widget
st.write(x, 'squared is', x*x)

# Accessing widgets by key
st.text_input('Your name', key='name')

st.session_state.name

st.write('Use checkboxes to show/hide data:')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    chart_data

st.write('Use select box for options:')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option 
