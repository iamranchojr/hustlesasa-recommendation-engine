import random

from app.models import User, Product
from app.repositories import product_repository, order_repository


def recommend_products(user: User = None) -> list[Product]:
    recommend_by_order_history = False

    if user:
        # get user orders count
        order_history_count = order_repository.get_orders_count(
            user_id=user.id
        )

        # we want to order by history only if user has an order count of 5 or more
        recommend_by_order_history = order_history_count >= 5

    if recommend_by_order_history:
        # get user most recent 50 orders
        recent_user_orders = order_repository.get_orders(
            user_id=user.id,
            limit=50
        )

        # extract product ids from order list and randomize them
        order_product_ids = list({item.product_id for order in recent_user_orders for item in order.items})
        random.shuffle(order_product_ids)

        # use the first 10 to get recommended products
        return product_repository.get_products_by_ids(
            ids=order_product_ids[:10],
        )

    # recommend products based on their popularity
    return product_repository.get_products_ordered_by_popularity_score(
        limit=10
    )
