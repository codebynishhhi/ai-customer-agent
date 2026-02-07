# Decision-making logic, intent classifier agent, routing
from typing import Literal
from app.llm.client import call_llm

# Allowed intents
Intent = Literal[
    "order_status",
    "refund_status",
    "refund_request",
    "policy_question",
    "complaints",
    "chitchat",
    "unknown"
]

# intent classifier prompt 
INTENT_PROMPT_TEMPLATE = """
You are an intent classfication agent for a customer supoort system.

Classify the user's message into one of the following intents:
- order_status
- refund_request
- policy_question
- complaint
- chitchat
- unknown

Rules:
- Respond only with the intent name 
- DO NOT add punctuations
- DO NOT explain the selection of the intent

User message : \"\"\"{user_message}\"\"\"
"""

def classify_intent(user_prompt :str) -> str:
    prompt = INTENT_PROMPT_TEMPLATE.format(user_message = user_prompt)
    intent = call_llm(prompt, max_tokens=300).lower().strip()
    allowed_intents = {
        "order_status",
        "refund_request",
        "policy_question",
        "complaint",
        "chitchat",
        "unknown",
    }

    if intent not in allowed_intents:
        return "Unknow intent detected!"
    
    return intent
