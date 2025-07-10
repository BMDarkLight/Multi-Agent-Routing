import pytest
from httpx import AsyncClient
from app.main import app
from unittest.mock import patch

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": True}

@pytest.mark.asyncio
@patch("app.main.graph.invoke")
async def test_ask_question(mock_invoke):
    mock_invoke.return_value = {
        "agent": "math",
        "answer": "The derivative of x^2 is 2x."
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/ask", json={"question": "What is the derivative of x^2?"})

    assert res.status_code == 200
    data = res.json()
    assert data["agent"] == "math"
    assert "2x" in data["answer"]