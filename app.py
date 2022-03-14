import streamlit as st
import streamlit_analytics

st.title("Food")

with streamlit_analytics.track():
    food = st.sidebar.file_uploader("Upload a photo of food")
    if food is not None:
        st.image(food)
        
#        with st.form("Food feedback"):
        app = st.selectbox("What app did you order from?",
                          ["Glovo", "Jumia", "Uber Eats", "Other"])
        if app == "Other":
            app = st.text_input("If other, what app did you use?")
        eatery = st.selectbox("What restaurant did you order from?",
                             ["Java", "Art Caffe", "Urban Burger",
                              "Pizza Inn", "Other"])
        if eatery == "Other":
            eatery = st.text_input("If other, what restaurant did you order from?")
        period = st.date_input("When did you order it?")
#            st.form_submit_button("Click to submit")
        if st.button("Click to submit information"):
            st.text("I ordered the above from {} using the {} app on {}".format(eatery, app, period))