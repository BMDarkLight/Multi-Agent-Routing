from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.agent import graph
from dotenv import load_dotenv
import getpass
import os

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

if "OPENWEATHER_API_KEY" not in os.environ:
    os.environ["OPENWEATHER_API_KEY"] = getpass.getpass("Enter your OpenWeather API key: ")


app = FastAPI()

@app.get('/')
def home_page():
    return HTMLResponse("""<!DOCTYPE HTML>
<html>
    <head>
        <title>Multi-Agent Question Routing System</title>
        <meta charset="UTF-8" />
    </head>
    <body>
        <h1>Multi-Agent Question Routing API</h1>
        <p>Based on FastAPI and working using LangGraph.</p>
        <a href="docs">Swagger Documentation</a>  
</html>
    """)

class Answer(BaseModel):
    agent: str
    answer: str

class Question(BaseModel):
    question: str

@app.post('/ask', response_model=Answer)
def ask_question(q: Question):
    state = {"question": q.question}
    result = graph.invoke(state)
    return Answer(
        agent = result["agent"],
        answer = result.get("answer", "No answer provided")
    )

class Status(BaseModel):
    up: bool

@app.get('/health', response_model=Status)
def service_status() -> Status:
    return Status(
        up = True
    )