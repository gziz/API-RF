from fastapi import FastAPI
import ml
from typing import List
from pydantic import BaseModel
import pickle

app = FastAPI()

class DataBody(BaseModel):
    records: List[float]


@app.get('/')
def index():
    return {'Hello': 'There'}


@app.post('/correct')
async def correct(data: DataBody):
    
    records = data.records
    records = [[x] for x in records]

    preds = ml.predict_rf(records)
    return {'predictions:': preds}



