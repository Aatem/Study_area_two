import requests
import pytest
import allure



@pytest.fixture()
def obj_id():
    payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response['id']}')

@allure.feature('object')
@allure.story('create')
def test_create_object():
    payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    assert response['name'] == payload['name']

@allure.feature('object')
@allure.story('get')
def test_get_object(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id

def test_put_object(obj_id):
    payload = {
    "name": "123123Apple MacBook Pro 16",
    "data": {
        "year": 2019123123,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "11111 TB"}}
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload).json()
    assert response['name'] == payload['name']

def test_del_object(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404