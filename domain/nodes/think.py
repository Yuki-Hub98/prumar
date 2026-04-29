from services.llm import call_llm

def think(state):
    prompt = f"""
    Classifique a tarefa:
    - responder
    - calcular

    Entrada: {state['input']}
    """

    res = call_llm(prompt)

    return {"decision": res.content.lower()}