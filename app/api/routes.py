from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import joblib

router = APIRouter()

class InputData(BaseModel):
    values: list[float]

model = joblib.load("app/models/model.pkl")

@router.post("/predict")
def predict(data: InputData):
    arr = np.array(data.values).reshape(1, -1)
    prediction = model.predict(arr)
    return {"anomaly": bool(prediction[0])}
