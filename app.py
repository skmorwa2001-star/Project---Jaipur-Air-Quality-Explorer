import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
  page_title="Jaipur Air Quality Explorer",
  layout='wide'
)

# Load Model

model=joblib.load("gradient_boosting_aqi_model.pkl")

# Title

st.title("Jaipur Air Quality Explorer")
st.subheader("Explore and Estimate Jaipur's Air Quality")

st.write("Enter pollutant values below to estimate the US AQI"
         "using the trained Gradient Boosting Model"
)
st.divider()