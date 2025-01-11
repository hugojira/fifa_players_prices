# Import the required libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle

app = FastAPI()

# The features for the model
class player_features(BaseModel):
    age : int
    height_cm :float
    weak_foot : int
    international_reputation : int
    potential : float
    pace : float
    shooting : float
    passing : float
    dribbling : float
    defending : float
    physic : float

# Loading the trained model
with open("./model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

@app.get("/")
async def root():
    return {"message": "Welcome to the fifa players predict prices API, by Hugo Valenzuela"}

@app.post('/prediction' )
async def predict_price(data: player_features):
    new_input = pd.DataFrame(np.array([[data.age,
                           data.height_cm,
                           data.weak_foot,
                           data.international_reputation,
                           data.potential,
                           data.pace,
                           data.shooting,
                           data.passing,
                           data.dribbling,
                           data.defending,
                           data.physic]]),
                columns=['age', 'height_cm', 'weak_foot', 'international_reputation', 'potential',
                         'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'])
    # prices are log values so we need to apply exp
    pred = loaded_model.predict(new_input)[0]

    return {'Prediction':  np.exp(pred)}