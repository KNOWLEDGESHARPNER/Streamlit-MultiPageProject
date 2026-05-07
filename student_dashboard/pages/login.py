import streamlit as st

st.title("Student Login Form")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "student" and password == "password123":
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password.")