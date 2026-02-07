from fastapi import FastAPI
from pydantic import BaseModel
from app.llm.client import call_llm
from app.agents.intent import classify_intent

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
    # calling the intent classifier 
    intent = classify_intent(request.message)
    llm_response = f"Detected Intent : {intent}"
    return ChatResponse(response=llm_response)
