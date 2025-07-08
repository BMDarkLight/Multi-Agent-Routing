from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from app.classifier import AgentState
import requests
from dotenv import load_dotenv
import os

load_dotenv()

search = DuckDuckGoSearchRun()
wikipedia = WikipediaAPIWrapper()

def get_weather(place: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The current weather in {place} is {weather} with a temperature of {temp}°C."
    else:
        return "Weather information is not available at the moment."

def travel_bot_node(state: AgentState) -> AgentState:

    weather_tool = Tool(
        name="Weather",
        func=get_weather,
        description="Provides live weather information for a given place."
    )

    search_tool = Tool(
        name="Search",
        func=search.run,
        description="Searches the internet for attractions and travel insights about a place."
    )

    wikipedia_tool = Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Fetches history and culture information about a place from Wikipedia."
    )

    tools = [search_tool, wikipedia_tool, weather_tool]

    llm = OpenAI(temperature=0)

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True,
        agent_kwargs={
            "prefix": (
                "You are a travel advisor. "
                "Your task is to provide comprehensive travel advice about a place, "
                "including top attractions, insights about the place, its history and culture, "
                "and current weather information."
                "Include top attractions (from internet search), "
                "insights about the place, its history and culture (from Wikipedia), "
                "and the current weather (from live weather info)."
            )
        }
    )

    answer = agent.invoke({"input": state["question"]})

    return {**state, "answer": str(answer)}