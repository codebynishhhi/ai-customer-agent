# import all intent prompt templates
from app.prompts.template import (
    ORDER_STATUS_PROMPT,
    REFUND_PROMPT,
    POLICY_PROMPT,
    COMPLAINT_PROMPT,
    CHITCHAT_PROMPT,
)

from app.llm.client import call_llm

def route_intent(intent:str, user_message:str) -> str:
    if intent == "order_status":
        prompt = ORDER_STATUS_PROMPT.format(message = user_message)
    elif intent == "refund_request":
        prompt = REFUND_PROMPT.format(message = user_message)
    elif intent == "policy_question":
        prompt = POLICY_PROMPT.format(message=user_message)

    elif intent == "complaint":
        prompt = COMPLAINT_PROMPT.format(message=user_message)

    elif intent == "chitchat":
        prompt = CHITCHAT_PROMPT.format(message=user_message)

    else:
        return "I'm not sure how to help with that. Could you rephrase?"

    return call_llm(prompt=prompt)