import streamlit as st
import pandas as pd
import numpy as np

st.title("Being Vegetarian is :green[COOL] :sunglasses:")
st.write("Are you a vegetarian and don't know where to find good vegetarian options. Don't worry VeggieAI got you covered.")
with st.form("dietary_restrictions"):
    options = st.multiselect("What dietary restrictions do you have?",
    ["Vegetarian", "Gluten Free", "Low-Carb", "Nut Allergies", "Lactose Intolerant"])
    st.text_input("Restaurant Website URL:")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    

restaurants = st.sidebar.text_input("Which restaurants would you like to eat at?")

# Get your output back
