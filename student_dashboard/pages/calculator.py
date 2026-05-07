import streamlit as st

# Calculator Page

st.title("Simple Calculator")
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)    
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])  
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero.")
            result = None
    if result is not None:
        st.success(f"The result of {operation}ing {num1} and {num2} is: {result}")