import requests
import json

def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x)

def get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)

def post_new_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1,
        "id": 101
    })
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data = body,
        headers = headers
    )
    print(response.json())
    print(response.status_code)

def update_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo1",
        "body": "bar2",
        "userId": 1,
        "id": 101
    })
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        data = body,
        headers = headers
    )
    print(response.json())

def patch_post():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "foo111",
        "userId": 1,
        "id": 101
    })
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        data = body,
        headers = headers
    )
    print(response.json())

def delite_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.text)
    print(response.status_code)

delite_post()