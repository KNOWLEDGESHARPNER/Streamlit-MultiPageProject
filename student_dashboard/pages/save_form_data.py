import streamlit as st

# This page is for saving form data to a file or database. You can use this page to collect user input and store it for later use.

st.header("Save Form Data")
# Example form to collect user input
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
message = st.text_area("Enter your message")
if st.button("Save Data"):
    # Here you can add code to save the data to a file or database
    # For example, you can save it to a CSV file
    with open("form_data.csv", "a") as f:
        f.write(f"{name},{email},{message}\n")
    st.success("Data saved successfully!")