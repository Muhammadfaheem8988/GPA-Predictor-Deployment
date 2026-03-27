from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="GPA Prediction App", docs_url=None, redoc_url=None)  # Hide default docs

# Load trained model
model = joblib.load('gpa_model.pkl')

# Serve HTML frontend
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as f:
        return f.read()

# Input schema
class StudentData(BaseModel):
    study_hours: float
    IQ: float
    attendance: float
    sleep_hours: float

# Prediction endpoint
@app.post("/predict_gpa")
def predict_gpa(data: StudentData):
    features = np.array([
        data.study_hours,
        data.IQ,
        data.attendance,
        data.sleep_hours
    ]).reshape(1, -1)

    gpa_pred = np.clip(model.predict(features)[0], 0, 4)  # Ensure GPA stays between 0 and 4
    return {"predicted_GPA": round(float(gpa_pred), 2)}
