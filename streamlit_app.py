import streamlit as st

st.title("Sales forecastig")
x=st.selectbox("What do ou like",["Cat","Dog"])
st.write(
   str(x)
)