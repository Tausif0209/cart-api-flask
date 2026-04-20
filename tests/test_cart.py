import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_add_item(client):
    response = client.post('/cart/add', json={
        "product_name": "TestItem",
        "price": 100,
        "quantity": 2
    })

    assert response.status_code == 201


def test_get_cart(client):
    response = client.get('/cart')
    assert response.status_code == 200


def test_total(client):
    response = client.get('/cart/total')
    data = json.loads(response.data)

    assert "total" in data
  
def test_delete_item(client):
    client.post('/cart/add', json={
        "product_name": "DeleteTest",
        "price": 50,
        "quantity": 1
    })

    response = client.delete('/cart/remove/1')
    assert response.status_code == 200