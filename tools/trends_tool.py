from langchain.tools import tool

@tool
def get_trending_places(preference: str) -> str:
    """
    Return a few trending destinations based on user preference.
    Mock implementation, no API needed.
    """
    pref = preference.lower()
    if "beach" in pref:
        return "Bali, Indonesia; Goa, India; Phuket, Thailand"
    if "mountain" in pref:
        return "Manali, India; Swiss Alps, Switzerland; Bhutan"
    if "city" in pref:
        return "Barcelona, Spain; Lisbon, Portugal; Singapore"
    return "Bali, Indonesia; Barcelona, Spain; Kerala, India"
