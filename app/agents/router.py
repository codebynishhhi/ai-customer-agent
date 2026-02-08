# import all intent prompt templates
from app.prompts.template import (
    ORDER_STATUS_PROMPT,
    COMPLAINT_PROMPT,
    CHITCHAT_PROMPT,
)
from app.llm.client import call_llm
from app.memory.session import update_memory, get_memory
from app.memory.extract import extract_order_id
from app.rag.retriever import retrieve_relevant_docs
from app.tools.orders import get_order_status
from app.tools.refunds import initate_refund
from app.tools.tickets import create_support_ticket


def route_intent(intent: str, user_message: str, session_id: str) -> str:
    memory = get_memory(session_id)

    # -------- TOOLS (assume memory is valid) --------
    if intent == "order_status":
        return get_order_status(memory["order_id"])

    if intent == "refund_request":
        return initate_refund(memory["order_id"])

    if intent == "complaint":
        return create_support_ticket(memory["order_id"])

    # -------- RAG --------
    if intent == "policy_question":
        docs = retrieve_relevant_docs(user_message)

        if not docs:
            return "I couldn’t find a relevant policy. Could you clarify your question?"

        context = "\n".join(doc["text"] for doc in docs)

        prompt = f"""
            Use ONLY the following company documents to answer.

            Documents:
            {context}

            User message:
            \"\"\"{user_message}\"\"\"
        """
        return call_llm(prompt)

    # -------- CHAT --------
    if intent == "chitchat":
        return call_llm(CHITCHAT_PROMPT.format(message=user_message))

    return "I'm not sure how to help with that."