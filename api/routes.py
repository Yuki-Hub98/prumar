from fastapi import APIRouter
from pydantic import BaseModel
from domain.graph import app as agent_app

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(payload: ChatRequest):
    result = agent_app.invoke({
        "input": payload.message
    })

    return {"response": result["output"]}