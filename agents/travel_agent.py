import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.weather_tool import get_weather
from tools.trends_tool import get_trending_places
from tools.events_tool import get_local_events

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY, temperature=0)

tools = [get_weather, get_trending_places, get_local_events]

agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def plan_trip(user_input: str) -> str:
    return agent.run(user_input)
