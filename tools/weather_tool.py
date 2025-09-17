import os
import requests
from langchain.tools import tool

@tool
def get_weather(location: str) -> str:
    """Fetch current weather for a given location."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    resp = requests.get(url)
    if resp.status_code != 200:
        return "Weather data not available."
    data = resp.json()
    return f"{location}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
