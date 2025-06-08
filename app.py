import streamlit as st
import pandas as pd

st.set_page_config(page_title="Colab App", layout="wide")

st.title("My First Streamlit Web App")
st.header("Streamlit Demo on Google Colab")
st.write("This app is running live from a Google Colab notebook.")

st.sidebar.header("User Input Section")
name = st.sidebar.text_input("Enter your name:")
if name:
    st.write(f"### Welcome, {name}!")

age = st.sidebar.slider("Select your age", 0, 100, 25)
st.sidebar.write(f"Your selected age: **{age}**")

if st.checkbox("Do you want to see a sample DataFrame?"):
    st.subheader("Sample Data")
    chart_data = pd.DataFrame({
        'Serial': range(1, 6),
        'Value': [20, 55, 60, 35, 80]
    })
    st.dataframe(chart_data)
    st.line_chart(chart_data.set_index('Serial'))
