# Session & conversation memory
# Simple in-memory session store
# session_id -> memory dict

SESSION_MEMORY = {}

def get_memory(session_id:str) -> dict:
    return SESSION_MEMORY.get(session_id, {})

def update_memory(session_id:str, new_data:dict) -> dict:
    if session_id not in SESSION_MEMORY:
        SESSION_MEMORY[session_id] = {}

    SESSION_MEMORY[session_id].update(new_data)
