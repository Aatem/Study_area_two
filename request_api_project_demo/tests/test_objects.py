import requests
import pytest
from request_api_project_demo.endpoints.create_object import CreateObject
from request_api_project_demo.endpoints.get_object import GetObject
from request_api_project_demo.endpoints.put_object import PutObgect
from request_api_project_demo.endpoints.delite_object import DelObject


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


def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(id=obj_id)
    get_object_endpoint.check_response_id(object_id=obj_id)
    get_object_endpoint.check_response_is_200()
    

def test_put_object(obj_id):
    put_object_endpoint = PutObgect()
    payload = {
    "name": "123123Apple MacBook Pro 16",
    "data": {
        "year": 2019123123,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "11111 TB"}}
    put_object_endpoint.put_by_id(id=obj_id, payload=payload)
    put_object_endpoint.check_response_name(payload["name"])
    put_object_endpoint.check_response_is_200()

def test_del_object(obj_id):
    del_object_endpoint = DelObject()
    del_object_endpoint.del_by_id(obj_id)
    del_object_endpoint.check_response_is_200()
    del_object_endpoint.check_response_is_404()
