from langgraph.graph import StateGraph, START, END
from .llm_setup import llm_chain
from .context_manager import trim_messages
from .calendar_toolkit import calendar_tools

def booking_node(state):
    msgs = trim_messages(state["messages"])
    resp = llm_chain.invoke({"messages": msgs})
    return {"messages": [resp]}

graph_builder = StateGraph({"messages": list})
graph_builder.add_node("booking", booking_node)
# integrate calendar tools at relevant point
# e.g. calendar availability and book nodes
graph_builder.add_edge(START, "booking")
graph_builder.add_edge("booking", END)
graph = graph_builder.compile()
