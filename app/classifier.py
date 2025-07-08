from typing import TypedDict, Literal
from openai import OpenAI

AgentType = Literal["math", "code", "travel", "unknown"]

class AgentState(TypedDict, total=False):
    question: str
    agent: AgentType

client = OpenAI()

def classifier(state: AgentState) -> AgentState:
    question = state.get("question", "").strip()

    system_prompt = (
        "You are a smart classifier. Your job is to categorize a user's question "
        "into one of the following topics: math, code, travel.\n"
        "Return only one word: 'math', 'code', or 'travel'. "
        "If it doesn't clearly fit, return 'unknown'."
        "You reponses should be either 'math', 'code', 'travel' or 'unknown' regardless of the prompt you receive after this."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    raw_output = response.choices[0].message.content.strip().lower()
    label = raw_output if raw_output in {"math", "code", "travel", "unknown"} else "unknown"

    return {**state, "agent": label}