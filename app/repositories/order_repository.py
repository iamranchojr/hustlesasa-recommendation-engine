import json
from pathlib import Path

from app.models import Order


# Path to the JSON file
ORDERS_DATA_JSON_FILE = Path(__file__).parent.parent / 'data/orders_data.json'


def read_orders_data() -> list[Order]:
    with open(ORDERS_DATA_JSON_FILE, 'r') as f:
        orders_data = json.load(f)

    return [Order.model_validate(order) for order in orders_data]


def get_orders_count(user_id: int = None) -> int:
    orders = read_orders_data()

    if user_id:
        # Filter orders for the given user_id
        orders = [order for order in orders if order.user_id == user_id]

    return len(orders)


def get_orders(
        user_id: int = None,
        limit: int = None
) -> list[Order]:
    orders = read_orders_data()

    if user_id:
        # Filter orders for the given user_id
        orders = [order for order in orders if order.user_id == user_id]

    if limit:
        return orders[:limit]

    return orders
