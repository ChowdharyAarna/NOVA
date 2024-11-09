import streamlit as st
from intermediary import *

st.title("Eat Easy")
st.write('''Are you a vegetarian and don't know where to find good vegetarian options? Don't worry FoodieAI got you covered.
         We will find your favorite local restaurants and all their vegetarian friendly options.''')

with st.form("dietary_restrictions"):
    # Stores the dietary restrictions as a list
    options = st.multiselect("What dietary restrictions do you have?",
    ["Vegetarian", "Gluten Free", "Low-Carb", "Nut Allergies", "Lactose Intolerant"])

    st.form_submit_button()

inter = Intermediary()
inter.set_restrictions(options)

with st.form("location"):
    zipcode = st.text_input("What is your zipcode")

    submitted_1 = st.form_submit_button()

if submitted_1:
    # print(zipcode)
    st.header("Restaurant Recomendations", divider = "gray")
    # print(inter.input_zip(zipcode))
    st.write(inter.input_zip(zipcode))

with st.form("restaurant"):
    # Stores the dietary restrictions as a list
    rst = st.text_input("Restaurant Name:")

    # Every form must have a submit button.
    submitted_2 = st.form_submit_button()

if submitted_2:
    inter.set_restrictions(options)
    st.header("Menu Recommendations", divider = "gray")
    st.write(inter.input_website(rst))

options = []
st.image("logo2.png")
# Get your output back
