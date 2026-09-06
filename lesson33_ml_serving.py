"""
Lesson 33: MLOps - Serving a Model in Production

Demonstrates core MLOps practices: wrapping a trained model behind a
real API endpoint, structured logging for observability, a health
check endpoint (standard in production systems for load balancers/
monitoring), and basic request/response validation - the operational
concerns that separate a notebook model from a deployed system.
"""

import logging
from datetime import datetime, timezone

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from sklearn.linear_model import LogisticRegression

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ml_serving")

app = FastAPI(title="Student Pass/Fail Prediction Service", version="1.0.0")

MODEL_VERSION = "1.0.0"
_startup_time = datetime.now(timezone.utc)


def train_model() -> LogisticRegression:
    """Train the model once at startup (a real system would load a saved model file)."""
    X = np.array([[1, 40], [2, 45], [3, 55], [4, 60], [5, 70], [6, 75], [7, 85], [8, 90]])
    y = np.array([0, 0, 0, 1, 1, 1, 1, 1])
    model = LogisticRegression()
    model.fit(X, y)
    logger.info(f"Model trained successfully, version {MODEL_VERSION}")
    return model


model = train_model()


class PredictionRequest(BaseModel):
    hours_studied: float
    previous_score: float

    @field_validator("hours_studied")
    @classmethod
    def hours_must_be_reasonable(cls, value: float) -> float:
        if value < 0 or value > 24:
            raise ValueError("hours_studied must be between 0 and 24")
        return value

    @field_validator("previous_score")
    @classmethod
    def score_must_be_valid(cls, value: float) -> float:
        if value < 0 or value > 100:
            raise ValueError("previous_score must be between 0 and 100")
        return value


@app.get("/health")
def health_check():
    """Standard health check endpoint - used by load balancers and monitoring systems."""
    uptime_seconds = (datetime.now(timezone.utc) - _startup_time).total_seconds()
    return {
        "status": "healthy",
        "model_version": MODEL_VERSION,
        "uptime_seconds": round(uptime_seconds, 2),
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    """Predict pass/fail based on hours studied and previous score."""
    logger.info(f"Prediction request: hours={request.hours_studied}, previous_score={request.previous_score}")

    try:
        features = np.array([[request.hours_studied, request.previous_score]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")

    result = "pass" if prediction == 1 else "fail"
    logger.info(f"Prediction result: {result} (probability={probability:.3f})")

    return {
        "prediction": result,
        "probability": round(float(probability), 3),
        "model_version": MODEL_VERSION,
    }
