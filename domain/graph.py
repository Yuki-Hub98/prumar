from langgraph.graph import StateGraph
from domain.state import AgentState

from domain.nodes.think import think
from domain.nodes.respond import respond
from domain.nodes.calculate import calculate

def router(state: AgentState):
    if "calcular" in state["decision"]:
        return "calculate"
    return "respond"

graph = StateGraph(AgentState)

graph.add_node("think", think)
graph.add_node("respond", respond)
graph.add_node("calculate", calculate)

graph.set_entry_point("think")

graph.add_conditional_edges(
    "think",
    router,
    {
        "respond": "respond",
        "calculate": "calculate",
    }
)

graph.set_finish_point("respond")
graph.set_finish_point("calculate")

app = graph.compile()