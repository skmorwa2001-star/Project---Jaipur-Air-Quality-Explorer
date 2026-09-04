import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

FEATURES = [
   "pm10",
   "pm2_5",
   "carbon_monoxide",
   "nitrogen_dioxide",
   "sulphur_dioxide",
   "ozone",
   "aerosol_optical_depth",
   "dust",
   "uv_index",
]

# Page Configuration

st.set_page_config(page_title="Jaipur Air Quality Explorer",page_icon="☁️", layout="wide")

# Model Selection

model_path = Path(__file__).with_name("gradient_boosting_aqi_model.pkl")
model = joblib.load(model_path)

# Title

st.title("☁️Jaipur Air Quality Explorer")
st.subheader("Explore and Estimate Jaipur's Air Quality")
st.write("Enter pollutant values below to estimate the US AQI using the trained Gradient Boosting Model.")
st.divider()

# Input Section

st.header("Air Quality Parameters")
col1, col2, col3 = st.columns(3)

with col1:
   pm10 = st.number_input("PM10", min_value=0.0, value=75.0)
   pm2_5 = st.number_input("PM2.5", min_value=0.0, value=37.0)
   carbon_monoxide = st.number_input("Carbon Monoxide", min_value=0.0, value=443.0)

with col2:
   nitrogen_dioxide = st.number_input("Nitrogen Dioxide", min_value=0.0, value=18.0)
   sulphur_dioxide = st.number_input("Sulphur Dioxide", min_value=0.0, value=8.8)
   ozone = st.number_input("Ozone", min_value=0.0, value=82.0)

with col3:
   aerosol_optical_depth = st.number_input("Aerosol Optical Depth", min_value=0.0, value=0.2)
   dust = st.number_input("Dust", min_value=0.0, value=20.0)
   uv_index = st.number_input("UV Index", min_value=0.0, value=5.0)

st.divider()

if st.button("Estimate US AQI", use_container_width=True):
   input_data = pd.DataFrame(
       {
           "pm10": [pm10],
           "pm2_5": [pm2_5],
           "carbon_monoxide": [carbon_monoxide],
           "nitrogen_dioxide": [nitrogen_dioxide],
           "sulphur_dioxide": [sulphur_dioxide],
           "ozone": [ozone],
           "aerosol_optical_depth": [aerosol_optical_depth],
           "dust": [dust],
           "uv_index": [uv_index],
       },
       columns=FEATURES,
   )

# Prediction

   prediction = model.predict(input_data)[0]

# AQI category
   if prediction <= 50:
       category = "Good 🟢"
       description = "Air is generally clean and safe for normal outdoor activity."
   elif prediction <= 100:
       category = "Moderate 🟡"
       description = "Air is acceptable for most people, though sensitive groups may feel mild impacts."
   elif prediction <= 150:
       category = "Unhealthy for Sensitive Groups 🟠"
       description = "Children, older adults, and people with respiratory issues should reduce prolonged outdoor exertion."
   elif prediction <= 200:
       category = "Unhealthy 🔴"
       description = "Health effects may be noticeable for everyone, especially with prolonged exposure."
   elif prediction <= 300:
       category = "Very Unhealthy 🟣"
       description = "Health warnings may apply; reducing outdoor activity is recommended."
   else:
       category = "Hazardous 🟤"
       description = "Serious health risks are possible; avoid outdoor exposure unless necessary."

   st.success(f"Estimated US AQI: {prediction:,.2f}")
   st.info(f"Air Quality: **{category}**")
   st.caption(description)

st.divider()
st.caption("Jaipur Air Quality Explorer | Machine Learning powered AQI estimation")