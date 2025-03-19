# test_app.py

import pytest
from app import app  # Flask uygulamanızın ana dosyasındaki app nesnesi

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Ana sayfa testi"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

