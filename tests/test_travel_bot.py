import pytest
from unittest.mock import patch, MagicMock
from app.agents.travel_bot import travel_bot_node
from app.classifier import AgentState

@pytest.mark.parametrize("question,expected_answer", [
    ("What should I do in Paris?", "Visit the Eiffel Tower."),
    ("Tell me about Kyoto", "Kyoto has many temples."),
])
def test_travel_bot_node(question, expected_answer):
    state: AgentState = {"question": question}

    with patch("app.agents.travel_bot.initialize_agent") as mock_initialize_agent:
        mock_agent = MagicMock()
        mock_agent.invoke.return_value = expected_answer
        mock_initialize_agent.return_value = mock_agent

        new_state = travel_bot_node(state)

    assert new_state["question"] == question
    assert new_state["answer"] == expected_answer