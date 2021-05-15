import streamlit as st

min_v = st.text_input('Minimum Value for Zoom')
max_v = st.text_input('Maximum Value for Zoom')

if min_v and max_v:
    st.write(int(min_v))

