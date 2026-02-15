"""from fastapi import FastAPI
from pydantic import BaseModel
from model import recommend_schemes

app = FastAPI()

class UserProfile(BaseModel):
    age: int
    gender: str
    income: int
    state: str
    category: str

@app.get("/")
def home():
    return {"message": "Bharat AI Saathi Backend Running 🇮🇳"}

@app.post("/recommend")
def get_recommendations(user: UserProfile):
    result = recommend_schemes(user.dict())
    return {"recommended_schemes": result}


import pandas as pd

df = pd.read_csv("D:\updated_data.csv")

print(df.head())"""

import pandas as pd

df = pd.read_csv("../dataset/schemes.csv")

print(df.head())
