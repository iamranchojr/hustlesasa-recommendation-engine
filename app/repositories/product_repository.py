import json
from pathlib import Path

from app.models import Product

# Path to the JSON file
PRODUCTS_DATA_JSON_FILE = Path(__file__).parent.parent / 'data/products_data.json'


def read_products_data() -> list[Product]:
    with open(PRODUCTS_DATA_JSON_FILE, 'r') as f:
        products_data = json.load(f)

    return [Product.model_validate(product) for product in products_data]


def get_products() -> list[Product]:
    return read_products_data()


def get_products_by_ids(
        ids: list[int],
) -> list[Product]:
    products = get_products()
    return [product for product in products if product.id in ids]


def get_products_by_categories(
        categories: list[str],
        product_ids_to_exclude: list[int],
        order_by_popularity_score=False,
        limit: int = None,
) -> list[Product]:
    products = get_products()
    products = [
        product
        for product in products
        if product.category in categories and product.id not in product_ids_to_exclude
    ]

    if order_by_popularity_score:
        products = sorted(
            products,
            key=lambda product: product.popularity_score,
            reverse=True
        )

    if limit:
        return products[:limit]

    return products


def get_products_ordered_by_popularity_score(
        desc=True,
        limit: int = None,
) -> list[Product]:
    products = get_products()
    ordered_products = sorted(
        products,
        key=lambda product: product.popularity_score,
        reverse=desc
    )

    if limit:
        return ordered_products[:limit]

    return ordered_products
