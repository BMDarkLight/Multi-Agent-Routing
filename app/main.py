from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import agents
import classifier

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
@app.post('/ask', response_model=Answer)
def ask_question(question: str):
    return 

class Status(BaseModel):
    up: bool

@app.get('/health', response_model=Status)
def service_status() -> Status:
    return Status(
        up = True
    )