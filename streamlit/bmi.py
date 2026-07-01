# i wants to calculate the bmi using streamlit and fastapi
# streamlit run streamlit/bmi.py

import streamlit as st

# show title and header
st.title("BMI Calculator")
st.header("This is a simple Streamlit app that calculates your Body Mass Index (BMI)")
st.subheader("You can use this app to calculate your BMI based on your weight and height.")

# i wants to get the weight and height from the user
weight = st.number_input("Enter your weight in kilograms (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height in meters (m):", min_value=0.0, step=0.01)

# show the values of weight and height
st.write(f"Your weight is: {weight} kg")
st.write(f"Your height is: {height} m")

# I wants to create some button using that it should create the bmi and show the result
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        # show the bmi category
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.error("Height must be greater than zero to calculate BMI.")

# based the bmi it should show warning or success message
if 'bmi' in locals():
    if bmi < 18.5:
        st.warning("You are underweight. Consider consulting a healthcare provider.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight. Keep up the good work!")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight. Consider a healthy diet and regular exercise.")
    else:
        st.error("You are obese. It is advisable to consult a healthcare provider for guidance.")

