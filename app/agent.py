from langgraph.graph import StateGraph
from app.classifier import classifier, AgentState
#from app.agents.math_bot import math_bot_node
#from app.agents.code_bot import code_bot_node
#from app.agents.travel_bot import travel_bot_node

builder = StateGraph(AgentState)

builder.add_node("classify", classifier)
#builder.add_node("math", math_bot)
#builder.add_node("code", code_bot)
#builder.add_node("travel", travel_bot)

builder.add_conditional_edges(
    "classify",
    lambda state: state["agent"],
    {
        "math": "math",
        "code": "code",
        "travel": "travel",
    }
)