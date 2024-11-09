import streamlit as st
import pandas as pd
import numpy as np
from intermediary import *

st.title("Being Vegetarian is :green[COOL] :sunglasses:")
st.write("Are you a vegetarian and don't know where to find good vegetarian options. Don't worry VeggieAI got you covered.")
with st.form("dietary_restrictions"):
    # Stores the dietary restrictions as a list
    options = st.multiselect("What dietary restrictions do you have?",
    ["Vegetarian", "Gluten Free", "Low-Carb", "Nut Allergies", "Lactose Intolerant"])
    
    # Stores the URL of website
    rst = st.text_input("Restaurant Website URL:")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

if submitted:
    inter = Intermediary()
    inter.set_restrictions(options)
    st.header("Recommendations", divider = "gray")
    st.write(inter.input_website(web))
  

restaurants = st.sidebar.text_input("Which restaurants would you like to eat at?")

# Get your output back
