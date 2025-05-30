import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set paths
DATA_PATH = os.path.join("..", "data", "large_sample_transactions_formatted.csv")
MODEL_PATH = os.path.join("..", "models", "iforest_model.pkl")
SCALER_PATH = os.path.join("..", "models", "scaler.pkl")
OUTPUT_CSV = os.path.join("..", "data", "predicted_anomalies.csv")

# Load data
df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])

# Load scaler and model
scaler = joblib.load(SCALER_PATH)
model = joblib.load(MODEL_PATH)

# Select features used during training
features = ["amount"]
X = df[features]
X_scaled = scaler.transform(X)

# Predict anomalies
df["anomaly_score"] = model.decision_function(X_scaled)
df["is_anomaly"] = model.predict(X_scaled)  # 1 = outlier, 0 = inlier

# Save results
df.to_csv(OUTPUT_CSV, index=False)
print(f"Predictions saved to: {OUTPUT_CSV}")

# Plot
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x="timestamp", y="amount", hue="is_anomaly", palette={0: "blue", 1: "red"}, legend="full")
plt.title("Transaction Amounts with Anomaly Detection")
plt.xlabel("Timestamp")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
