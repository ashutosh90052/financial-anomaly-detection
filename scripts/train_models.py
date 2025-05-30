# scripts/train_models.py

import pandas as pd
import joblib
from pyod.models.iforest import IForest
from sklearn.preprocessing import StandardScaler
import os

# Set paths
DATA_PATH = os.path.join("..", "data", "large_sample_transactions_formatted.csv")
MODEL_DIR = os.path.join("..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "iforest_model.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

# Create models directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])

# Feature selection
features = ["amount"]
X = df[features].copy()

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model training
model = IForest(contamination=0.01, random_state=42)
model.fit(X_scaled)

# Save model and scaler
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print(f"Model saved to: {MODEL_PATH}")
print(f"Scaler saved to: {SCALER_PATH}")
