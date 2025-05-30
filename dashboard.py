import streamlit as st
import pandas as pd

st.title("Fraud Detection Dashboard")

# Sample data - in real project, this would come from your detector
data = pd.DataFrame([
    {"amount": 120, "status": "Normal"},
    {"amount": 6500, "status": "Fraud"},
    {"amount": 80, "status": "Normal"}
])

st.write("## Recent Transactions")
st.dataframe(data)

st.write("## Fraud Statistics")
st.metric("Total Transactions", len(data))
st.metric("Fraud Detected", sum(data["status"] == "Fraud"))