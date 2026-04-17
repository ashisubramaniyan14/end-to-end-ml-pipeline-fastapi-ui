from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.api.schemas import PredictionResponse
from src.features.feature_engineering import add_features


BASE_DIR = Path(__file__).resolve().parent.parent.parent

app = FastAPI(title="End-to-End ML Pipeline API")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

MODEL_PATH = BASE_DIR / "models" / "stock_model.pkl"
PROCESSED_FILE = BASE_DIR / "data" / "processed" / "nvda_processed.csv"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def load_latest_features():
    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed dataset not found: {PROCESSED_FILE}")

    df = pd.read_csv(PROCESSED_FILE)
    df = add_features(df)

    latest_row = df.iloc[-1]
    feature_cols = ["daily_return", "ma_5", "ma_10", "volatility_5", "lag_1", "lag_2"]
    features = latest_row[feature_cols].to_frame().T
    return features


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/health")
def health():
    return {"message": "ML Pipeline API is running"}


@app.get("/predict", response_model=PredictionResponse)
def predict():
    model = load_model()
    features = load_latest_features()

    prediction_label = int(model.predict(features)[0])
    prediction = "UP" if prediction_label == 1 else "DOWN"

    return PredictionResponse(
        symbol="NVDA",
        prediction=prediction,
        prediction_label=prediction_label
    )