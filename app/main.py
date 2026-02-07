from fastapi import FastAPI
from pydantic import BaseModel
from app.llm.client import call_llm
from app.agents.intent import classify_intent
from app.agents.router import route_intent

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
    response = route_intent(intent, request.message)
    llm_response = f"Detected Intent : {intent}"
    print(llm_response, "Intent of query")
    return ChatResponse(response=response)
