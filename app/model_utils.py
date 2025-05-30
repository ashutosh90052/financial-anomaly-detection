# app/model_utils.py
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("models/iforest_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_anomalies(data: pd.DataFrame):
    features = ["amount"]  # extend if needed
    data_scaled = scaler.transform(data[features])
    predictions = model.predict(data_scaled)
    data["anomaly"] = predictions
    return data
