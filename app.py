import streamlit as st

st.title("Food")

food = st.sidebar.file_uploader("Upload a photo of food")
if food is not None:
    st.image(food)