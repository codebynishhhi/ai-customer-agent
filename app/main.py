from fastapi import FastAPI
from pydantic import BaseModel
from app.llm.client import call_llm

app = FastAPI(title="AI Customer Support Agent")

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # placeholder response
    # return ChatResponse(response="Agent is alive")
    llm_response = call_llm("Whats today's tech market news in 200 characters.")
    return ChatResponse(response=llm_response)
