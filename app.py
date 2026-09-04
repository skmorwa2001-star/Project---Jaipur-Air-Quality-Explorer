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
