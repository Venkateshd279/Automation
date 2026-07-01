# Stramlit 
Streamlit is the python framework we use it for frontend. It's used for mvp (minimal viable product)

Streanlit is free python library used to build the webapp without knowing about HTML, CSS or JavaScript

#### Layman in framework:
Someone has already made biriyani powder we use that, that's like framework.

Step 1: pip install streamlit 

Step 2: import streamlit ex: import streamlit as st

st.title("Hello")

step 3: To run the file 
streamlit run app.py 

### 1. Streamlit components

st.title() Bigheading
st.header() sub heading
st.subheader() small heading
st.write() normal text
st.markdown() text with format (ex:bold)

### 2. Input components

name = st.text_input("Enter your name")

### 3. Button 

st.button("Click me!"):

### 4. Slider 

number = st.slider("Select a number:", 0, 100, 50)

### 5. Select box 
city = st.selectbox("Select your city:", ["Chennai", "Bangalore", "Hyderabad", "Mumbai"])

### 6. message 

st.success("This is a success message!")
st.info("This is an info message.")
st.warning("This is a warning message.")

  