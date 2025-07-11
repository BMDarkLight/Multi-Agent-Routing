import unittest
from unittest.mock import patch, MagicMock
from app.agents.math_bot import math_bot_node

class TestMathBot(unittest.TestCase):
    
    @patch("app.agents.math_bot.initialize_agent")
    def test_math_bot_node_returns_reasonable_answer(self, mock_initialize_agent):
        mock_agent = MagicMock()
        mock_agent.invoke.return_value = {
            "output": "• Step 1: Identify known values\n• Step 2: Use the formula a^2 + b^2 = c^2\n• Final answer: 13"
        }
        mock_initialize_agent.return_value = mock_agent

        state = {"question": "What is the hypotenuse of a triangle with sides 5 and 12?"}
        result = math_bot_node(state)
        answer = result.get("answer", "")

        self.assertIsInstance(answer, str)
        self.assertTrue(answer.strip())
        self.assertNotIn("No answer", answer)
        self.assertIn("step", answer.lower())
        self.assertIn("answer", answer.lower())

    @patch("app.agents.math_bot.initialize_agent")
    def test_math_bot_node_handles_non_math_input(self, mock_initialize_agent):
        mock_agent = MagicMock()
        mock_agent.invoke.return_value = {
            "output": "I'm not sure what you meant, but I think you're asking about a mathematical relationship. Here's my interpretation..."
        }
        mock_initialize_agent.return_value = mock_agent

        state = {"question": "The cat ran across the road twice"}
        result = math_bot_node(state)
        answer = result.get("answer", "")

        self.assertIn("interpretation", answer.lower())
        self.assertIsInstance(answer, str)
        self.assertTrue(len(answer.strip()) > 0)