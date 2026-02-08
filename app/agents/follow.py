def get_follow_question(intent : str) -> str:
    if intent == "order_status":
        return "Could you please share your order_id."
    
    if intent == "refund_request":
        return "Please share your order_id so that i can complete the refund request."
    
    if intent == "complaint":
        return "Please share your order_id so that i can rasie a support ticket."
    
    return ""