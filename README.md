 Temperature Prediction using NASA CMAPSS Dataset

##  Project Overview

This project predicts **future rotor (engine) temperature** using historical multi-sensor time-series data from the **NASA CMAPSS Turbofan Engine Degradation Dataset**.

The goal is to demonstrate a **complete machine learning workflow** for time-series regression, including data loading, feature engineering, model training, evaluation, visualization, and interpretation.


---

## Problem Statement

Predict the **average rotor temperature at time t** using sensor readings and operating conditions from **time t−1**.

This mirrors real-world **predictive maintenance** and **condition monitoring** tasks used in aerospace and industrial systems.

---

## Dataset

**NASA CMAPSS Turbofan Engine Dataset (FD001)**

Each row represents:

* One engine
* One operating cycle (time step)
* Operational settings
* 21 sensor measurements (temperature, pressure, RPM, etc.)

The dataset captures engine behavior from healthy operation until failure.

---

## Features Used

### Inputs (X)

* Lagged temperature sensor readings:

  * sensor_2 (t−1)
  * sensor_3 (t−1)
  * sensor_4 (t−1)
  * sensor_11 (t−1)
* Average temperature (t−1)
* Operational settings (os_1, os_2, os_3)
* Cycle number (time)

### Target (y)

* Average rotor temperature at time t

---

## Models Implemented

* **Linear Regression** (baseline)
* **Random Forest Regressor**

Models were evaluated using a **time-aware train/test split** (no shuffling).

---

## Evaluation Metric

* **RMSE (Root Mean Squared Error)**

### Results

* Linear Regression RMSE: **1.68 °C**
* Random Forest RMSE: **1.70 °C**

These results indicate highly accurate temperature predictions with strong temporal consistency.

---

## Visualization

* Actual vs Predicted temperature over time
* Residual (prediction error) plots
* Feature importance visualization for Random Forest

---


## Project Structure

* `data/` → Raw NASA dataset
* `src/load_data.py` → Data loading
* `src/features.py` → Feature engineering
* `src/train.py` → Model training & evaluation
* `venv/` → Python virtual environment

---

## Key Learning Outcomes

* Time-series feature engineering using lag variables
* Proper evaluation of temporal data
* Model comparison and interpretation
* Feature importance analysis
* Real-world predictive maintenance modeling

---

## Future Improvements

* Gradient Boosting / XGBoost
* LSTM-based deep learning model
* Rolling window features
* Remaining Useful Life (RUL) prediction

---

## Author

Nodirabegim S.

Machine Learning Project using Real NASA Data

