from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
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


def unknown_node(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    response = llm([HumanMessage(content="You are backup agentic assistant, You answer the question after the system detected that it isn't a math problem, code question or in need of a travel advice. You answer comes after the sentence 'The question wasn't related to code, math or travel.'. Question :" + state["question"])])
    return {
        **state,
        "answer": "The question wasn't related to code, math or travel. " + response.content
    }

builder.add_node("unknown", unknown_node)

builder.add_edge("start", "classify")

builder.add_conditional_edges(
    "classify",
    lambda state: state["agent"],
    {
        "math": "math",
        "code": "code",
        "travel": "travel",
        "unknown": "unknown"
    }
)

builder.set_entry_point("start")

builder.set_finish_point("math")
builder.set_finish_point("code")
builder.set_finish_point("travel") 

graph = builder.compile()