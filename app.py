import streamlit as st

st.title("🎯 Hello from Streamlit!")
st.write("If you can see this, Streamlit Cloud works in your corporate environment!")

st.success("✅ Test successful!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"👋 Hello, {name}! The app is working!")
