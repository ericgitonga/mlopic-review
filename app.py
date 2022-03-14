import streamlit as st
import streamlit_analytics

st.title("Food")

with streamlit_analytics.track():
    food = st.sidebar.file_uploader("Upload a photo of food")
    if food is not None:
        st.image(food)