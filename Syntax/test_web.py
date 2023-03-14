import pytest
import json

from web import app as alex_app  # importing web app from file
from web import app  # importing web app from file

def test_my_endpoint2():
    client = app.test_client()
    response = client.get('/my-endpoint')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'













@pytest.fixture
def app():
    yield alex_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_func(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'{"hi":"alex"}\n'


def test_my_endpoint():
    with app.test_client() as client:
        response = client.get('/my-endpoint')
        assert response.status_code == 200
        assert response.data == 'hello world'

def test_my_endpoint2():
    client = app.test_client()
    response = client.get('/my-endpoint')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
