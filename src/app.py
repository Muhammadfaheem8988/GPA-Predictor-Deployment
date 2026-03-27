from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import numpy as np
from pathlib import Path

app = FastAPI(title="GPA Prediction App", docs_url=None, redoc_url=None)

# repo root (…/GPA-Predictor-Deployment)
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "gpa_model.pkl"
HTML_PATH = BASE_DIR / "templates" / "index.html"

# Load trained model (from models/)
model = joblib.load(MODEL_PATH)

# Serve HTML frontend (from templates/)
@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PATH.read_text(encoding="utf-8")


class StudentData(BaseModel):
    study_hours: float
    IQ: float
    attendance: float
    sleep_hours: float


@app.post("/predict_gpa")
def predict_gpa(data: StudentData):
    features = np.array(
        [data.study_hours, data.IQ, data.attendance, data.sleep_hours]
    ).reshape(1, -1)

    gpa_pred = np.clip(model.predict(features)[0], 0, 4)
    return {"predicted_GPA": round(float(gpa_pred), 2)}
