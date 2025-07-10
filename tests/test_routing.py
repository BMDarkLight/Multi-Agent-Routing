import pytest
from app.classifier import classifier_node, AgentState
from unittest.mock import patch

@pytest.mark.parametrize("question,expected", [
    ("What is the derivative of x^2?", "math"),
    ("How to write a loop in Python?", "code"),
    ("Where should I travel in Europe?", "travel"),
    ("Tell me a bedtime story.", "unknown"),
])
def test_classifier_node(question, expected):
    state: AgentState = {"question": question}

    with patch("app.classifier.llm.invoke") as mock_invoke:
        mock_invoke.return_value.content = expected  # simulate correct classification
        new_state = classifier_node(state)

    assert new_state["agent"] == expected
    assert new_state["question"] == question