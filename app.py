import streamlit as st
import numpy as np
import joblib

# Custom CSS for styling the app
st.markdown("""
    <style>
    /* Background for the app */
    .stApp {
        background-color: #f0f4f7;
    }

    /* Title styling */
    .title h1 {
        font-size: 48px;
        font-weight: bold;
        color: #009688;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Subtle box shadow for input widgets */
    .stNumberInput, .stSelectbox {
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        border-radius: 8px;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton button {
        background-color: #009688;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .stButton button:hover {
        background-color: #00796b;
    }

    /* Text area styling for results */
    .stTextArea {
        font-size: 18px;
        color: #424242;
        border: 1px solid #bdbdbd;
        padding: 20px;
        border-radius: 10px;
        background-color: #e0f7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model (make sure the model is correctly loaded from the path)
model = joblib.load("stock_logi.pkl")

# Title with custom styling
st.markdown("<div class='title'><h1>Stock Price Prediction</h1></div>", unsafe_allow_html=True)

# Image (replace with correct image file path)
st.image("stock.jpg", caption="Stock Price Prediction", use_container_width=True)

# User inputs with section header
st.header("Please enter the stock data to predict stock price movement:")

# User inputs for stock data (Price, Adj Close, Close, High, Low, Open)
price = st.number_input("Enter Price", min_value=0.0, max_value=1000.0, step=0.1)
adj_close = st.number_input("Enter Adjusted Close", min_value=0.0, max_value=1000.0, step=0.1)
close = st.number_input("Enter Close", min_value=0.0, max_value=1000.0, step=0.1)
high = st.number_input("Enter High", min_value=0.0, max_value=1000.0, step=0.1)
low = st.number_input("Enter Low", min_value=0.0, max_value=1000.0, step=0.1)
open_value = st.number_input("Enter Open", min_value=0, max_value=100000000, step=1)

# Prepare input features (Removed 'Volume' to match the model's expected input)
input_features = [[price, adj_close, close, high, low, open_value]]

# Prediction with a button
if st.button("Predict Stock Price Movement"):
    prediction = model.predict(input_features)

    # Display prediction result as 'Increase' or 'Decrease' with color
    if prediction == 0:
        st.markdown("<h2 style='color: green;'>The stock price is predicted to INCREASE.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color: red;'>The stock price is predicted to DECREASE.</h2>", unsafe_allow_html=True)
