from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message":
        "Water Quality Monitoring System Running"
    }

@app.get("/dashboard")
def dashboard():

    try:

        with open("data.json", "r") as file:

            data = json.load(file)

        return data

    except:

        return {
            "temperature": 0,
            "ph": 0,
            "turbidity": 0,
            "tds": 0,
            "water_level": 0,
            "status": "WAITING",
            "timestamp": "--"
        }