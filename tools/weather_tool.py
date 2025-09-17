import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@tool
def get_weather(location: str) -> str:
    """
    Fetch current weather for a given location.
    Input format: "City,Country"
    """
    if not WEATHER_API_KEY:
        return "Weather API key missing."
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
        resp = requests.get(url)
        data = resp.json()
        if data.get("cod") != 200:
            return f"Weather data not available for {location}."
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{location}: {desc.capitalize()}, {temp}°C"
    except Exception as e:
        return f"Error fetching weather: {e}"
