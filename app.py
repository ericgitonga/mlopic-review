import streamlit as st
import streamlit_analytics

st.title("Expectations vs. Reality")

with streamlit_analytics.track():
    food_on_menu = st.sidebar.file_uploader("Upload a photo of the food as shown on the menu.")
    food_received = st.sidebar.file_uploader("Upload a photo of the food received.")
    if food_on_menu is not None and food_received is not None:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("# Food On Menu")
            st.image(food_on_menu)
        with c2:
            st.markdown("# Food Received")
            st.image(food_received)
        
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
        if st.button("Click to submit information"):
            st.text("I ordered the above from {} using the {} app on {}".format(eatery, app, period))