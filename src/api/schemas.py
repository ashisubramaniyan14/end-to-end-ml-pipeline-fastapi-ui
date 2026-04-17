from pydantic import BaseModel


class PredictionResponse(BaseModel):
    symbol: str
    prediction: str
    prediction_label: int