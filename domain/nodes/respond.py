from services.llm import call_llm

def respond(state):
    res = call_llm(state["input"])
    return {"output": res.content}