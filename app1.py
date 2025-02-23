import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set title
st.title("📊 Advanced Data Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)

    # Display dataframe
    st.subheader("📌 Data Preview")
    st.write(df.head())

    # Select column for analysis
    column = st.selectbox("Select a column to visualize:", df.columns)

    # Plot Histogram
    st.subheader(f"📊 Histogram of {column}")
    fig, ax = plt.subplots()
    df[column].hist(ax=ax, bins=20)
    st.pyplot(fig)

    # Show basic statistics
    st.subheader(f"📈 Summary Statistics for {column}")
    st.write(df[column].describe())

else:
    st.warning("⚠ Please upload a CSV file to proceed.")
