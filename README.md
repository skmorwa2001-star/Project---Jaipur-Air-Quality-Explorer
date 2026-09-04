# 🌫️ Jaipur Air Quality Explorer

A Machine Learning project for exploring historical air-quality data
from Jaipur and estimating **US AQI (Air Quality Index)** from pollutant
and environmental measurements.

## 📌 Overview

This project demonstrates an end-to-end workflow:

**Data → Cleaning → EDA → Visualization → Model Training → Model
Comparison → Model Saving → Streamlit App**

> **Important:** The current model performs AQI **estimation** from
> supplied measurements. It is not a future AQI forecasting model.

## 🎯 Objectives

-   Clean historical Jaipur air-quality data
-   Analyze pollutant and AQI relationships
-   Study AQI trends and seasonal variation
-   Detect and analyze outliers
-   Compare regression models
-   Identify important predictive features
-   Build an interactive Streamlit AQI estimator

## 🗂️ Project Structure

``` text
Project- Jaipur Air explorer/
│
├── jaipur-in-1269515/
│   ├── air_quality_historical.csv
│   ├── city_info.csv
│   ├── data_dictionary.csv
│   └── dataset-metadata.json
│
├── data_cleaning.ipynb
├── gradient_boosting_aqi_model.pkl
├── app.py
└── README.md
```

## 📚 Dataset

-   **Title:** Dataset: Air Quality Dataset for Jaipur
-   **Dataset ID:** `nitirajkulkarni/jaipur-in-1269515`
-   **Coverage:** 2022-08-01 to 2026-02-18
-   **License:** CC0-1.0

## 🧾 Dataset Columns

  Column                    Description
  ------------------------- ------------------------------
  `date`                    Observation date/time
  `pm10`                    PM10 measurement
  `pm2_5`                   PM2.5 measurement
  `carbon_monoxide`         Carbon monoxide measurement
  `nitrogen_dioxide`        Nitrogen dioxide measurement
  `sulphur_dioxide`         Sulphur dioxide measurement
  `ozone`                   Ozone measurement
  `aerosol_optical_depth`   Aerosol optical depth
  `dust`                    Dust measurement
  `uv_index`                UV index
  `us_aqi`                  **Target variable**
  `european_aqi`            European AQI

# 🧹 Data Cleaning

Data cleaning was performed in `data_cleaning.ipynb`.

### Steps

1.  Load the CSV using Pandas
2.  Inspect shape, columns and data types
3.  Convert `date` to datetime
4.  Check missing values
5.  Check duplicate rows
6.  Remove incomplete rows for the modeling dataset
7.  Verify the cleaned data
8.  Generate descriptive statistics
9.  Analyze outliers
10. Analyze correlations
11. Create visualizations

After cleaning, the working DataFrame contained **1294 rows and 12
columns**.

# 🔎 Exploratory Data Analysis

## PM2.5 vs US AQI

The PM2.5--US AQI correlation was approximately **0.91**, indicating a
strong positive relationship in this dataset.

## Important correlations

  Relationship                Approx. correlation
  ------------------------- ---------------------
  PM2.5 ↔ US AQI                             0.91
  PM10 ↔ US AQI                              0.53
  PM2.5 ↔ Carbon Monoxide                    0.78
  Carbon Monoxide ↔ SO₂                      0.81
  PM10 ↔ Dust                                0.85
  US AQI ↔ European AQI                      0.82

Correlation indicates statistical association, not causation.

## Visualizations

-   US AQI trend over time
-   Seasonal average US AQI
-   PM2.5 vs US AQI scatter plot
-   Correlation heatmap
-   Outlier box plots
-   Actual vs predicted AQI plot
-   Gradient Boosting feature-importance plot

## 🌦️ Seasonal Analysis

Average US AQI was compared across **Monsoon, Post-Monsoon, Summer and
Winter**, showing noticeable seasonal variation in the historical
dataset.

## 📦 Outlier Analysis

Box plots showed high-value observations in several variables, including
PM10, PM2.5, carbon monoxide, ozone, dust and US AQI. Extreme
observations were analyzed rather than automatically assuming that every
extreme value was an error.

# 🤖 Machine Learning

## Target

``` text
us_aqi
```

This is a **regression problem** because US AQI is a continuous
numerical target.

## Features

``` text
pm10
pm2_5
carbon_monoxide
nitrogen_dioxide
sulphur_dioxide
ozone
aerosol_optical_depth
dust
uv_index
```

The `date` column was not directly used as a model feature.

## ✂️ Train/Test Split

``` python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Approximately 80% of observations were used for training and 20% for
testing.

# 🧪 Model Comparison

Three regression models were evaluated.

  ------------------------------------------------------------------------
  Model                 MAE ↓          MSE ↓         RMSE ↓           R² ↑
  ------------ -------------- -------------- -------------- --------------
  Linear                 9.17         154.78          12.44          0.850
  Regression                                                

  Random                 7.82         116.42          10.79          0.887
  Forest                                                    

  **Gradient         **7.64**     **108.92**      **10.44**      **0.894**
  Boosting**                                                
  ------------------------------------------------------------------------

## 🏆 Best Model: Gradient Boosting Regressor

Configuration:

``` python
GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
```

### Performance

-   **MAE = 7.64**
-   **MSE = 108.92**
-   **RMSE = 10.44**
-   **R² = 0.894**

### Interpretation

-   **MAE 7.64:** average absolute prediction error is about 7.6 AQI
    points on this test set.
-   **RMSE 10.44:** larger errors receive greater penalty.
-   **R² 0.894:** about 89.4% of target variance is explained on this
    test set.

These results are specific to the current train/test split and are not a
guarantee of real-world performance.

# 📈 Actual vs Predicted

The Actual vs Predicted plot compares:

-   X-axis → Actual US AQI
-   Y-axis → Predicted US AQI

The points show a strong upward pattern, indicating that the model
captures the overall relationship reasonably well.

A perfect model would place every point on:

``` text
Predicted AQI = Actual AQI
```

# ⭐ Feature Importance

Gradient Boosting feature importance showed **PM2.5 as the dominant
feature** in the trained model.

This is consistent with the strong PM2.5--US AQI relationship found
during EDA.

> Feature importance is model-specific and does **not** prove causation.

# 💾 Saved Model

The final model was saved as:

``` text
gradient_boosting_aqi_model.pkl
```

Example:

``` python
import joblib

joblib.dump(gb, "gradient_boosting_aqi_model.pkl")
```

# 🌐 Streamlit Application

`app.py` loads the saved Gradient Boosting model.

Users can enter:

-   PM10
-   PM2.5
-   Carbon Monoxide
-   Nitrogen Dioxide
-   Sulphur Dioxide
-   Ozone
-   Aerosol Optical Depth
-   Dust
-   UV Index

The app then estimates US AQI and displays an AQI category.

# ▶️ How to Run

## 1. Open the project

Open the project folder in VS Code.

Make sure these files are available:

``` text
app.py
gradient_boosting_aqi_model.pkl
```

## 2. Install dependencies

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

## 3. Run the app

``` bash
streamlit run app.py
```

If Streamlit is not recognized:

``` bash
python -m streamlit run app.py
```

The app normally opens at:

``` text
http://localhost:8501
```

## ⚠️ Model Loading Error

If a `ModuleNotFoundError` appears while loading the `.pkl` file, check
the Python and Scikit-learn environments:

``` bash
python --version
```

``` bash
python -c "import sklearn; print(sklearn.__version__)"
```

Use the same Python environment and compatible package versions used to
train and save the model.

For Anaconda, for example:

``` bash
C:\Users\<username>\anaconda3\python.exe -m streamlit run app.py
```

# 🧰 Technologies Used

  Technology         Purpose
  ------------------ ---------------------------
  Python             Programming
  Pandas             Data manipulation
  NumPy              Numerical operations
  Matplotlib         Visualization
  Seaborn            Statistical visualization
  Scikit-learn       Machine learning
  Joblib             Model saving/loading
  Jupyter Notebook   Analysis
  Streamlit          Web application
  Git/GitHub         Version control

# 📌 Limitations

1.  The current model estimates AQI from supplied measurements; it does
    not forecast future AQI.
2.  Performance depends on the dataset and train/test split.
3.  Historical observations may not represent current real-time
    conditions.
4.  The model is not an official AQI monitoring service.
5.  Feature importance should not be interpreted as causal influence.
6.  Real-world deployment should validate predictions against reliable
    current monitoring data.

# 🚀 Future Improvements

-   Add real-time AQI data
-   Add Jaipur location/station comparison
-   Add interactive date filters
-   Add live pollutant charts
-   Build future AQI forecasting using lag/time-series features
-   Try XGBoost or LightGBM
-   Add SHAP explainability
-   Add AQI threshold alerts
-   Add downloadable reports
-   Deploy the Streamlit application online

# 🎓 Learning Outcomes

This project provides practical experience with:

-   Data loading and cleaning
-   Missing-value handling
-   Duplicate checking
-   Datetime processing
-   Descriptive statistics
-   Outlier analysis
-   Correlation analysis
-   Data visualization
-   Feature/target selection
-   Train/test splitting
-   Regression
-   Model evaluation
-   Model comparison
-   Feature importance
-   Model serialization
-   Streamlit development

# 📜 Disclaimer

This project is intended for **educational, analytical and demonstration
purposes**.

The estimated AQI should not be treated as an official real-time
air-quality measurement or as medical/environmental advice. For
health-related decisions, use current information from appropriate
authoritative air-quality monitoring sources.

# 👨‍💻 Author

**Sunil Kumar**\
B.Tech --- Artificial Intelligence\
Rajasthan Technical University (RTU)

# ⭐ Project Workflow

``` text
Historical Jaipur Air Quality Data
              ↓
         Data Cleaning
              ↓
              EDA
              ↓
       Data Visualization
              ↓
       Feature Selection
              ↓
       Train/Test Split
              ↓
       Model Training
              ↓
 ┌────────────┼────────────┐
 ↓            ↓            ↓
Linear      Random      Gradient
Regression  Forest      Boosting
 └────────────┼────────────┘
              ↓
       Model Comparison
              ↓
   Gradient Boosting Selected
              ↓
         Save Model
              ↓
       Streamlit Application
              ↓
       Interactive AQI
          Estimation
```

## 🏆 Final Result

``` text
Best Model: Gradient Boosting Regressor

MAE  = 7.64
RMSE = 10.44
R²   = 0.894
```

**Jaipur Air Quality Explorer --- turning air-quality data into
understandable insights. 🌫️📊🤖**
