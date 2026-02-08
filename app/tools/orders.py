
def get_order_status(order_id:str) -> str:
    """
    Simulated order status
    """

    fake_db_data = {
        "1231": "Order out for delivery",
        "2891": "Order delivered",
        "5432": "Order cancelled ",
        "8971": "Order delayed by 2hrs , bad weather"
    }

    return fake_db_data.get(order_id, "Order id not found. Please verify and try again!")