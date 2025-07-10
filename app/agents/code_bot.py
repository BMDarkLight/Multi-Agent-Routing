from langchain_community.llms import OpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from app.classifier import AgentState

def code_bot_node(state: AgentState) -> AgentState:
    search = Tool(
        name="GeneralInternetSearch",
        func=DuckDuckGoSearchRun().run,
        description="Searches the internet for answers to general Python programming questions when python.org and forums do not have the answer."
    )

    llm = OpenAI(temperature=0)
    tools = [search]
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={
            "prefix": (
                "You are a helpful assistant that answers Python programming questions "
                "You search python.org for answers in the first place, You usually do this when the question is about the syntax of the code or the way python itself behaves not the libraries used,"
                "Then you try to search forums like Quora, Reddit and Stack Overflow for similar problems people have had in the past and provide ways to fix the problem provided,"
                "Then if there was no answer satisfying the question, you try to search the internet globally"
            )
        }
    )

    answer = agent.invoke({"input": state["question"]})
    
    return {**state, "answer": str(answer)}