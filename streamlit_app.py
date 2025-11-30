import streamlit as st
import pandas as pd
st.title("Sales forecastig")
month=st.selectbox("Select month",["festival","Non Festival"])
if "non" in month:month="November"
else:month="October"
st.write(
   str("Select values carefully ")
)
items=pd.read_csv("sales.csv")
product=st.selectbox("Product Name ",items["Product"].unique())
subclass = st.selectbox("Product type ",items["Catagory"].unique())
price=st.number_input("Enter price",min_value=0)