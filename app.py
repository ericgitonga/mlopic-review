import streamlit as st
import streamlit_analytics

st.title("Food")

with streamlit_analytics.track():
    food = st.sidebar.file_uploader("Upload a photo of food")
    if food is not None:
        st.image(food)
        
        with st.form("Food feedback"):
            app = st.text_input("What app did you order from?")
            period = st.date_input("When did you order it?")
            st.form_submit_button("Click to submit")
        
        st.text("Ordered from {} on {}".format(app, period))