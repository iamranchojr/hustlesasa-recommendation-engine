from fastapi.testclient import TestClient
from fastapi import status

from app.main import app


client = TestClient(app)


def test_index():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'Welcome to Hustlesasa Recommendation Engine v1.0'
    }
