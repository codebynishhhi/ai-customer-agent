
import re

# function to extract the order_id
def extract_order_id(text: str):
    """
    Extracts numeric order IDs from user input.
    Works for:
    - "order id is 1231"
    - "order_id 2891"
    - "my order is 847392"
    """
    match = re.search(r"\b\d{3,}\b", text)
    return match.group() if match else None
