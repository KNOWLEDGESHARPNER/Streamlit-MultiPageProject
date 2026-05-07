import streamlit as st
import pandas as pd
import numpy as np

st.header("Data Processing")

# I ineed to add xls file and process it to show the data in a table format. I also need to add some basic data cleaning steps like handling missing values and removing duplicates.

df= pd.read_excel("data/Data sample.xlsx", nrows=5,) 
# Load the Excel file into a DataFrame

df= df.dropna()  # Handle missing values
df= df.drop_duplicates()  # Remove duplicates
st.write(df)  # Display the processed data in a table format