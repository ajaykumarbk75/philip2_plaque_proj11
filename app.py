import streamlit as st

# Title
st.title("My First Streamlit App 🚀")

# Text
st.write("Hello! This is a simple Streamlit app.")

# Slider input
number = st.slider("Pick a number", 0, 100, 25)
st.write(f"You picked: {number}")

# Button
if st.button("Click me!"):
    st.success(f"🎉 You clicked the button and your number is {number}!")

# Optional: checkbox
if st.checkbox("Show more info"):
    st.info("Streamlit makes it super easy to build apps with Python!")
