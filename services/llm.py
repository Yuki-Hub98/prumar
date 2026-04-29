from langchain_community.chat_models import ChatOllama
import os

ollama_url = os.getenv("OLLAMA_BASE_URL")
llm = ChatOllama(
    model="llama3",
    base_url=ollama_url,
    temperature=0
)

def call_llm(prompt: str):
    response = llm.invoke(prompt)
    return response.content
