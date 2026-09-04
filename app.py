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

# Input Section

st.header("Air Quality Parameters")

col1,col2,col3 = st.columns(3)

with col1:
    pm10 = st.number_input(
        "PM10",
        min_value=0.0,
        value=75.0
    )

    pm2_5= st.number_input(
        "PM2.5",
        min_value=0.0,
        value=37.0
    )

    carbon_monoxide= st.number_input(
        "Carbon Monoxide",
        min_value=0.0,
        value=443.0
    )

with col2:
    nitrogen_dioxide= st.number_input(
        "Nitrogen Dioxide",
        min_value=0.0,
        value=18.0
    )    

    sulphur_dioxide= st.number_input(
        "Sulphur Dioxide",
        min_value=0.0,
        value=8.8
    )

    ozone= st.number_input(
        "Ozone",
        min_value=0.0,
        value=82.0
    )

with col3:
    aersol_optical_depth= st.number_input(
        "Aersol Optical Depth",
        min_value=0.0,
        value=0.2
    )    

    dust= st.number_input(
        "Dust",
        min_value=0.0,
        value=20.0
    )

    uv_index=st.number_input(
        "UV Index",
        min_value=0.0,
        value=5.0
    )