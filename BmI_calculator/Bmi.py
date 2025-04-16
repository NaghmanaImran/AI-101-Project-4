import streamlit as st  # Typo fixed

# Title of the App
st.title("BMI Calculator App")

# Input fields
height = st.number_input("Enter your height (in meters)", min_value=0.1, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms)", min_value=0.1, format="%.2f")  # Typo fixed

# BMI calculation on button click
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")  # Typo: 'sucess' → 'success'

    # BMI categories
    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")  # Typo: 'sucsess' → 'success'
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
