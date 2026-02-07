from fastapi import FastAPI
from pydantic import BaseModel

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
    return ChatResponse(response="Agent is alive")
