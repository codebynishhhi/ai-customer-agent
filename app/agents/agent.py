# This is the agent brain loop

from app.agents.intent import classify_intent
from app.agents.router import route_intent
from app.agents.completion import is_task_complete
from app.agents.follow import get_follow_question
from app.memory.session import get_memory, update_memory
from app.memory.extract import extract_order_id


def run_agent(session_id: str, user_message: str) -> str:
    memory = get_memory(session_id)
    # 1️⃣ Classify intent
    intent = classify_intent(user_message)

    # Fallback - if intent not clear use previous intent stored in memory 
    if intent in ["unknown", "chitchat"] and "last_intent" in memory:
        intent = memory["last_intent"]

    print("intent ans", intent)

    # 2️⃣ Extract  order_id & store memory FIRST
    order_id = extract_order_id(user_message)
    if order_id:
        update_memory(session_id, {"order_id": order_id})

    print(order_id, "nishi order id")
    # update the intent in memory 
    update_memory(session_id, {"last_intent": intent})

    # 3️⃣ Fetch updated memory
    memory = get_memory(session_id)

    print("nishi memory", memory)
    # 4️⃣ Check task completion
    if not is_task_complete(intent, memory):
        return get_follow_question(intent)

    # 5️⃣ Route + execute
    return route_intent(intent, user_message, session_id)