import streamlit as st

st.title("Hello World App")
st.header("This is a simple Streamlit app that displays 'Hello, World!'")
st.subheader("You can use this app to test your Streamlit installation.")   
st.write("Hello, World!")
st.text("This is a simple text message.")

name = st.text_input("Enter your name:", "")
st.write(f"Hello, {name}!")

age = st.number_input("Enter your age:")
st.write(f"You are {age} years old.")

if st.button("Click me!"):
    st.write("Button clicked!")

number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected: {number}")

# select for text box 
city = st.selectbox("Select your city:", ["Chennai", "Bangalore", "Hyderabad", "Mumbai"])
st.write(f"You selected: {city}")

#Checkbox for terms and conditions
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing to the terms and conditions.")

# showing messages 
st.success("This is a success message!")
st.info("This is an info message.")
st.warning("This is a warning message.")