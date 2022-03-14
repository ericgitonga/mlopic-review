import streamlit as st

st.title("Food")

if st.sidebar.checkbox("Select to activate camera"):
    food = st.sidebar.camera_input("take a pic")
    if food is not None:
        st.image(food)