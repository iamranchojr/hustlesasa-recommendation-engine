from fastapi.testclient import TestClient
from fastapi import status

from app.main import app
from app.repositories import order_repository, product_repository

client = TestClient(app)


def test_recommend_products__anonymous_user():
    response = client.get('/api/v1/recommend-products')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 49
    assert data[0]['name'] == 'Product 49'

    assert data[count - 1]['id'] == 1
    assert data[count - 1]['name'] == 'Acoustic Guitar'


def test_recommend_products__by_order_history__case_of_orders_gte_5__authenticated_user():
    user_id = 1
    response = client.get(f'/api/v1/recommend-products?user_id={1}')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 48
    assert data[0]['name'] == 'Product 48'

    assert data[count - 1]['id'] == 5
    assert data[count - 1]['name'] == 'Vocal Microphone'

    # get user most recent 50 orders
    recent_user_orders = order_repository.get_orders(
        user_id=user_id,
        limit=50
    )

    # extract product ids from order list and get categories of those products
    order_product_ids = list({item.product_id for order in recent_user_orders for item in order.items})
    order_product_categories = list({
        product.category for product in product_repository.get_products_by_ids(list(order_product_ids))
    })

    # Validate that recommended products do not include IDs from the user's order history
    recommended_product_ids = [product['id'] for product in data]
    assert not any(product_id in order_product_ids for product_id in recommended_product_ids), (
        "Recommended products should not include IDs already purchased by the user."
    )

    # Validate that recommended products belong to categories in the user's order history
    recommended_product_categories = [product['category'] for product in data]
    assert all(category in order_product_categories for category in recommended_product_categories), (
        "All recommended products should belong to categories in the user's order history."
    )


def test_recommend_products__by_popularity_score__case_of_orders_lt_5__authenticated_user():
    response = client.get(f'/api/v1/recommend-products?user_id={2}')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 49
    assert data[0]['name'] == 'Product 49'

    assert data[count - 1]['id'] == 1
    assert data[count - 1]['name'] == 'Acoustic Guitar'


def test_recommend_products__by_popularity_score__case_of_no_orders__authenticated_user():
    response = client.get(f'/api/v1/recommend-products?user_id={3}')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 49
    assert data[0]['name'] == 'Product 49'

    assert data[count - 1]['id'] == 1
    assert data[count - 1]['name'] == 'Acoustic Guitar'


def test_recommend_products__by_popularity_score__case_of_non_existent_user__authenticated_user():
    response = client.get(f'/api/v1/recommend-products?user_id={3}')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 49
    assert data[0]['name'] == 'Product 49'

    assert data[count - 1]['id'] == 1
    assert data[count - 1]['name'] == 'Acoustic Guitar'
