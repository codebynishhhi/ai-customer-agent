import re 

def extract_order_id(message: str):
    match = re.search(r"\b\d{5,}\b", message)
    if match:
        return match.group()
    return None