import streamlit as st
import pandas as pd
import numpy as np

st.title("Being Vegetarian is :green[COOL] :sunglasses:")
veg = st.button("Are you a vegetarian?")
options = st.multiselect("What dietary restrictions do you have?",
    ["Vegetarian", "Gluten Free", "Low-Carb", "Nut Allergies", "Lactose Intolerant"]
)
df = pd.DataFrame(
    np.random.randn(500,2) / [100, 100] + [2000, 1000],
    columns=["lat", "lon"],
)
st.map(df)

add_selectbox = st.sidebar.text_input("How restaurant would you like to eat at?")

# Get your output back
st.write()