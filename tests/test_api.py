import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Multi-Agent Question Routing API" in response.text

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": True}

@pytest.mark.parametrize("question", [
    "What is 2 + 2?",
    "How do I write a for loop in Python?",
    "Where should I travel in summer?"
])
def test_ask_question(question):
    response = client.post("/ask", json={"question": question})
    assert response.status_code == 200
    json_response = response.json()
    assert "agent" in json_response
    assert "answer" in json_response
    assert isinstance(json_response["answer"], str)
    assert json_response["answer"] != "No answer provided"