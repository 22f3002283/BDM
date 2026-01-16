import streamlit as st
import pandas as pd
import pickle
from tensorflow.keras.models import load_model as call
import sklearn
st.title("Sales forecastig")
month=st.selectbox("Select month",["festival","Non Festival"])
if "non" in month:month="November "
else:month="October "
st.write(
str("Select values carefully ")
)
items=pd.read_csv("sales.csv")
product=st.selectbox("Product Name ",items["Product"].unique())
subclass = st.selectbox("Product type ",items["Catagory"].unique())
price=st.number_input("Enter price",min_value=0)
method = st.selectbox("Method ",["Classic","Pure Deep","Hybrid"])
test_dict = {
"Product": [product],
"Catagory": [subclass],
"Month": [month],
"Unit Price of sales": [price]
}
ohc = pickle.load(open("encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
tree_model = pickle.load(open("tree_model.pkl", "rb"))
deep_model = call("deep_model.keras")
test_df = pd.DataFrame(test_dict)
encoded = ohc.transform(test_df[["Product", "Catagory", "Month"]])

test_processed = pd.concat(
[test_df.drop(["Product", "Catagory", "Month"], axis=1), encoded],
axis=1
)

prediction = None

if method == "Classic":
    prediction = tree_model.predict(test_processed)[0]
    if price:prediction = tree_model.predict(test_processed)[0]

elif method == "Pure Deep":
    prediction = deep_model.predict(test_processed)[0][0]*price
    if price:prediction = deep_model.predict(test_processed)[0][0]*price

else:  # Hybrid
    ml_pred = tree_model.predict(test_processed)[0]
    dl_pred = deep_model.predict(test_processed)[0][0]*price
    prediction = (ml_pred + dl_pred) / 2
    if price:
        ml_pred = tree_model.predict(test_processed)[0]
        dl_pred = deep_model.predict(test_processed)[0][0]*price
        prediction = (ml_pred + dl_pred) / 2
st.subheader("Forecasted Revenue:")
if prediction is not None:
st.write(f"₹ {prediction:.2f}")
