import streamlit as st
import pandas as pd
import os

st.header("Data Processing")

# 1. File Uploader - This allows you to "add" the file to the app
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Load the Excel file
    # We use a try-except block to catch potential engine errors (like missing openpyxl)
    try:
        # read_excel requires the 'openpyxl' library installed in your requirements.txt
        df = pd.read_excel(uploaded_file)
        
        st.subheader("Original Data (Preview)")
        st.write(df.head())

        # 2. Basic Data Cleaning Steps
        st.markdown("---")
        st.subheader("Cleaning Tools")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Handle Missing Values"):
                df = df.dropna()
                st.success("Dropped rows with missing values!")

        with col2:
            if st.button("Remove Duplicates"):
                df = df.drop_duplicates()
                st.success("Duplicate rows removed!")

        # 3. Display Processed Data in Table Format
        st.subheader("Final Processed Data")
        st.dataframe(df) # st.dataframe provides a searchable/sortable table

        # Optional: Add a download button for the cleaned data
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Data as CSV",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.info("Make sure 'openpyxl' is added to your requirements.txt file.")

else:
    st.info("👆 Please upload an Excel file (.xlsx or .xls) to start processing.")
    
    # FIX for your specific FileNotFoundError: 
    # If you want to load a specific file already in your repo as a default:
    # Use an absolute path logic:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Adjust path to go up one level from 'pages' then into 'data'
    sample_path = os.path.join(current_dir, "..", "data", "Data sample.xlsx")
    
    if os.path.exists(sample_path):
        if st.checkbox("Load Sample File from Repository"):
            df_sample = pd.read_excel(sample_path)
            st.write("Loaded sample file successfully!")
            st.dataframe(df_sample)