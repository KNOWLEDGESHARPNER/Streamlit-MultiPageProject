import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data for visualization
# Line Chart Data
line_chart_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 250, 300, 350, 400]
}
line_chart_df = pd.DataFrame(line_chart_data)
#display line chart
st.subheader("Sales Over Time(Jan - Jun)")
st.line_chart(line_chart_df.set_index('Month'))

# Bar Chart Data
bar_chart_data = {
    'Chocolates': ['Dairy Milk', 'Bournville', 'Cadbury', 'KitKat'],
    'Values': [100, 200, 150, 300]
}
bar_chart_df = pd.DataFrame(bar_chart_data)
#display bar chart
st.subheader("Sales by Chaocolate Type")
st.bar_chart(bar_chart_df.set_index('Chocolates'))

# Pie Chart Data
pie_chart_data = {
    'Fruits': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Sales_values': [3000, 4000, 2000, 1000]
}
pie_chart_df = pd.DataFrame(pie_chart_data)
#display pie chart
st.subheader("Sales Distribution by Fruit Type")
st.pyplot(pie_chart_df.set_index('Fruits').plot.pie(y='Sales_values', 
        autopct='%1.1f%%', figsize=(5, 5)).get_figure())