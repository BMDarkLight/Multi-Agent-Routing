from langchain_openai import ChatOpenAI
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from app.classifier import AgentState

def math_bot_node(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

    word_problem_template = """You are a reasoning agent tasked with solving 
    the user's logic-based questions. Logically arrive at the solution, and be 
    factual. In your answers, clearly detail the steps involved and give the 
    final answer. Provide the response in bullet points. 
    Question {question} Answer"""

    problem_chain = LLMMathChain.from_llm(llm=llm)
    math_tool = Tool.from_function(name="Calculator",
                                func=problem_chain.run,
                                description="Useful for when you need to answer questions about math. This tool is only for math questions.")

    math_assistant_prompt = PromptTemplate(input_variables=["question"],
                            template=word_problem_template)
    word_problem_chain = LLMChain(llm=llm,
                            prompt=math_assistant_prompt)
    word_problem_tool = Tool.from_function(name="Reasoning Tool",
                            func=word_problem_chain.run,
                            description="Useful for when you need to answer logic-based/reasoning questions.",)

    agent = initialize_agent(
        tools=[math_tool, word_problem_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    try:
        answer = agent.invoke({"input": state["question"]})
        output = str(answer["output"]) if "output" in answer else "No output."
    except ValueError as e:
        output = f"Math tool failed to parse the response: {str(e)}"
    
    return {**state, "answer": output}