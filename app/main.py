# app/main.py
from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.model_utils import predict_anomalies

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Anomaly Detection API is running."}

@app.post("/predict")
async def detect_anomalies(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result = predict_anomalies(df)
    return result.to_dict(orient="records")
