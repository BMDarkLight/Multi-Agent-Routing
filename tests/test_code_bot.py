import pytest
from unittest.mock import patch, MagicMock
from app.agents.code_bot import code_bot_node

@patch("app.agents.code_bot.initialize_agent")
def test_code_bot_node_returns_reasonable_answer(mock_initialize_agent):
    mock_agent = MagicMock()
    mock_agent.invoke.return_value = {
        "output": "You can use a for loop like this in Python: for i in range(10): print(i)"
    }
    mock_initialize_agent.return_value = mock_agent

    state = {"question": "How do I write a for loop in Python?"}
    result = code_bot_node(state)

    answer = result.get("answer", "")
    
    assert isinstance(answer, str)
    assert answer.strip() != ""
    assert "No answer found" not in answer

    loop_keywords = ["for", "range", "in", "print"]
    assert any(word in answer.lower() for word in loop_keywords)