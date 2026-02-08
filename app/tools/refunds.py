# a function that will give refund status

def initate_refund(order_id:str) -> str:
    """
    Function to initate refund on the product
    """

    return (
        f"Refund request for order with {order_id} has been initated."
        "You will receive the refund in original payment mode within 5-7 business days!"
    )