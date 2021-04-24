import pytest

def test_app_boot(client):
    response = client.get('/');
    assert response.data == b"Hello, World!"