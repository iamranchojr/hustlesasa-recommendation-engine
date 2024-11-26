from fastapi.testclient import TestClient
from fastapi import status

from app.main import app


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
    response = client.get(f'/api/v1/recommend-products?user_id={1}')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    count = len(data)

    assert count == 10
    assert data[0]['id'] == 1
    assert data[0]['name'] == 'Acoustic Guitar'

    assert data[count - 1]['id'] == 50
    assert data[count - 1]['name'] == 'Product 50'


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
