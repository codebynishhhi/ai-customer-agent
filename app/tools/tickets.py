# External actions (ticket create / lookup)
import uuid
def create_support_ticket(order_id:str) -> str:
    """
    Function to create supoort tickets for user query
    """
    ticket_id = f"TICK-{uuid.uuid4().hex[:8].upper()}"
    return (
        f"Ticket has been created for your query with ticket id - {ticket_id}"
    )