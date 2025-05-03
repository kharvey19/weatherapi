from fastapi import FastAPI, HTTPException
from cache import generate_cache_key, get_cached_weather, cache_weather_data
from weather_service import fetch_weather 
import json

app = FastAPI()

@app.get("/weather")
async def get_weather(location: str, date: str = "today"):
    key = generate_cache_key(location, date)
    cached = get_cached_weather(key)
    if cached:
        return {"source": "cache", "data": json.loads(cached)}
    try:
        data = await fetch_weather(location, date)
        cache_weather_data(key, data)
        return {"source": "api", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
