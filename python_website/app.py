# app.py
import streamlit as st

st.set_page_config(page_title="Naghmana's Web App", layout="centered")

st.title(" Welcome to My Streamlit Website")
st.subheader("This site was built in 15 minutes!")

st.write("""
Hello, I'm **Naghmana** and this is a quick demo of how we can build a website using Streamlit and Python.

You can use this space to showcase:
- Your projects
- Your resume
- Your contact info
- Or even create tools (like a BMI calculator!)
""")

st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", caption="Beautiful Image", use_column_width=True)

st.success(" This is a success message")
st.warning(" This is a warning message")
st.error(" This is an error message")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Thanks for visiting")

if st.button("Click Me"):
    st.balloons()
