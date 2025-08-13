from fastapi import FastAPI
import requests
import dotenv
import os
import redis
import json

dotenv.load_dotenv()
key = os.getenv("API_KEY")
app = FastAPI()

redis_client = redis.Redis(host = "localhost", port = 6379, db = 0)

@app.get("/")
def root():
    return {"message":"Backend of Weather API"}

@app.get("/weather/{city}")
def get_weather(city: str):
    cached_data = redis_client.get(city)
    if cached_data:
        print("Cache hit")
        return json.loads(cached_data)
    else:
        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={key}&contentType=json")

        if response.status_code == 200:
            data = response.json()
            redis_client.set(city, json.dumps(data), ex = 3600)
            return data
        else:
            return {"error": "Failed to fetch weather data"}



