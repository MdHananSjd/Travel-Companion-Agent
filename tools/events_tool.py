import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")

@tool
def get_local_events(location: str) -> str:
    """
    Fetch events for a location.
    Input format: "City,Country"
    """
    if not EVENTBRITE_API_KEY:
        return "Event API key missing."
    try:
        # Eventbrite API example (free public events)
        url = f"https://www.eventbriteapi.com/v3/events/search/?location.address={location}&token={EVENTBRITE_API_KEY}&sort_by=date"
        resp = requests.get(url)
        data = resp.json()
        events = data.get("events", [])
        if not events:
            return f"No events found for {location}."
        names = [event["name"]["text"] for event in events[:3]]  # show top 3
        return "Upcoming events: " + ", ".join(names)
    except Exception as e:
        return f"Error fetching events: {e}"
