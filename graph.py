from datetime import datetime
import json

from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage
from langgraph.graph import StateGraph, MessagesState, START, END

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

def llm_node(state: MessagesState):
    response: AIMessage = llm.invoke(state["messages"])
    return {"messages": [response]}


def time_node(state: MessagesState):
    current_time = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    content = json.dumps({"utc": current_time})
    return {"messages": [AIMessage(content=content)]}


def route(state: MessagesState):
    last = state["messages"][-1]
    if hasattr(last, "content") and "time" in last.content.lower():
        return "time_node"
    else:
        return "llm_node"


builder = StateGraph(MessagesState)
builder.add_node("llm_node", llm_node)
builder.add_node("time_node", time_node)
builder.add_conditional_edges(START, route, ["time_node", "llm_node"])
builder.add_edge("time_node", END)
builder.add_edge("llm_node", END)

graph = builder.compile()
