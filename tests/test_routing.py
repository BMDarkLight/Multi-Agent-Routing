import pytest
from app.classifier import classifier_node

@pytest.mark.parametrize("question,expected_agent", [
    ("What is 2 + 2?", "math"),
    ("How do I write a loop in Python?", "code"),
    ("What's the best place to visit in Italy?", "travel"),
    ("I had a weird dream about robots", "unknown"),
    ("Can you help me with calculus homework?", "math"),
    ("How to sort a list in JavaScript?", "code"),
    ("Is Japan a good travel destination in spring?", "travel"),
])
def test_classifier_node(question, expected_agent):
    state = {"question": question}
    result = classifier_node(state)
    assert result["agent"] == expected_agent