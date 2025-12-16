import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    from pathlib import Path
    BASE = Path(__file__).parent
    return pd.read_excel(BASE / "employees_clean.xlsx")

df = load_data()

st.title("Dashboard Employees - Salaries and Departments")
st.subheader("Data Headers")
st.dataframe(df.head())

departments = st.multiselect("Select department: ", df["Department"].unique())

if departments:
    df = df[df["Department"].isin(departments)]

st.subheader("Filtered Data")
st.dataframe(df)