import streamlit as st

st.title("Student Registration Form")

new_username = st.text_input("Choose a username")
new_password = st.text_input("Choose a password", type="password")  

if st.button("Register"):
    st.success(f"Account created for {new_username}!")  