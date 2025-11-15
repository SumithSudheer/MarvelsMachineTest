import streamlit as st
import pandas as pd

st.title("Tourism AI Dashboard")

exp = pd.read_csv("outputs/state_expense.csv")
rating = pd.read_csv("outputs/priority_rating.csv")

st.header("State-wise Expense Summary")
st.dataframe(exp)
st.bar_chart(exp.set_index("state"))

st.header("Priority by Rating")
st.dataframe(rating)
st.bar_chart(rating.set_index("name"))
