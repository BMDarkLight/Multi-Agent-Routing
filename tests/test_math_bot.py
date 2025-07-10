import pytest
from unittest.mock import patch, MagicMock
from app.agents.math_bot import math_bot_node
from app.classifier import AgentState

@pytest.mark.parametrize("question,expected_output", [
    ("What is 2 + 2?", "The answer is 4."),
    ("What is the derivative of x^2?", "The derivative of x^2 is 2x."),
])
def test_math_bot_node_returns_expected_answer(question, expected_output):
    state: AgentState = {"question": question}

    with patch("app.agents.math_bot.initialize_agent") as mock_initialize_agent:
        mock_agent = MagicMock()
        mock_agent.invoke.return_value = expected_output
        mock_initialize_agent.return_value = mock_agent

        result_state = math_bot_node(state)

    assert result_state["question"] == question
    assert result_state["answer"] == expected_output