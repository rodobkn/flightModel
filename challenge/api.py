import fastapi
import os
import pandas as pd
import xgboost as xgb
from typing import List, Dict
from pydantic import BaseModel

app = fastapi.FastAPI()

def get_model_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "main_model.model")

loadedModel = xgb.XGBClassifier()
loadedModel.load_model(get_model_path())

class PredictionOutput(BaseModel):
    predict: List[int]

class FlightInput(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

class FlightsInput(BaseModel):
    flights: List[FlightInput]

def process_input(data: List[FlightInput]) -> pd.DataFrame:
    features = []
    for flight in data:
        feature = {}
        feature["OPERA_Latin American Wings"] = 1 if flight.OPERA == "Latin American Wings" else 0
        feature["MES_7"] = 1 if flight.MES == 7 else 0
        feature["MES_10"] = 1 if flight.MES == 10 else 0
        feature["OPERA_Grupo LATAM"] = 1 if flight.OPERA == "Grupo LATAM" else 0
        feature["MES_12"] = 1 if flight.MES == 12 else 0
        feature["TIPOVUELO_I"] = 1 if flight.TIPOVUELO == "I" else 0
        feature["MES_4"] = 1 if flight.MES == 4 else 0
        feature["MES_11"] = 1 if flight.MES == 11 else 0
        feature["OPERA_Sky Airline"] = 1 if flight.OPERA == "Sky Airline" else 0
        feature["OPERA_Copa Air"] = 1 if flight.OPERA == "Copa Air" else 0
        features.append(feature)

    return pd.DataFrame(features)

def valid_input(data: List[FlightInput]) -> bool:
    for flight in data:
        if not (1 <= flight.MES <= 12):
            return False
        
        if flight.TIPOVUELO not in ["N", "I"]:
            return False
    return True

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict(data: FlightsInput) -> PredictionOutput:
    """
    Predict delays for a list of flights.
    """
    input_data = data.flights
    
    if not valid_input(input_data):
        raise fastapi.exceptions.HTTPException(status_code=400, detail="Invalid input data")
    
    processed_input = process_input(input_data)
    predictions = loadedModel.predict(processed_input)
    
    return {"predict": predictions.tolist()}
