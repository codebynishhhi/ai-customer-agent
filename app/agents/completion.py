def is_task_complete(intent:str, memory:str) -> bool:
    """
    Decides whether the agnet has everything it needs to finish the task 
    """

    if intent in ["order_status", "refund_request", "complaint"]:
        return "order_id" in memory
    
    return True
