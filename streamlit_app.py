import streamlit as st
import pandas as pd
st.title("Sales forecastig")
month=st.selectbox("Select month",["festival","Non Festival"])
if "non" in month:month="November"
else:month="October"
st.write(
   str(month)
)
items=pd.read_csv("items.csv")
product=st.selectbox("Product Name ",items["Product"])