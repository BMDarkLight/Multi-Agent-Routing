from langgraph.graph import StateGraph
from app.classifier import classifier_node, AgentState
from app.agents.math_bot import math_bot_node
from app.agents.code_bot import code_bot_node
from app.agents.travel_bot import travel_bot_node

def start_node(state: AgentState) -> AgentState:
    return state

builder = StateGraph(AgentState)

builder.add_node("start", start_node)
builder.add_node("classify", classifier_node)
builder.add_node("math", math_bot_node)
builder.add_node("code", code_bot_node)
builder.add_node("travel", travel_bot_node)

builder.add_edge("start", "classify")

builder.add_conditional_edges(
    "classify",
    lambda state: state["agent"],
    {
        "math": "math",
        "code": "code",
        "travel": "travel",
    }
)

builder.set_entry_point("start")
builder.set_finish_point("classify")

graph = builder.compile()