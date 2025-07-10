import pytest
from unittest.mock import patch, MagicMock
from app.agents.code_bot import code_bot_node
from app.classifier import AgentState

@pytest.mark.parametrize("question,expected_answer", [
    ("How do I write a function in Python?", "You can define a function using `def`."),
    ("How to fix a TypeError in Python?", "Check the variable types and use casting."),
])
def test_code_bot_node(question, expected_answer):
    state: AgentState = {"question": question}

    with patch("app.agents.code_bot.initialize_agent") as mock_initialize_agent:
        mock_agent = MagicMock()
        mock_agent.invoke.return_value = expected_answer
        mock_initialize_agent.return_value = mock_agent

        result_state = code_bot_node(state)

    assert result_state["question"] == question
    assert result_state["answer"] == expected_answer