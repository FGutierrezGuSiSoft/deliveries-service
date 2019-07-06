from functools import wraps
import json
import requests
from flask import request

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserService:
    def get_user(self):
        authorization = request.headers.get('Authorization')
        headers = {'Authorization': authorization}
        url = 'http://localhost:5000/user_by_token'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            return 200, User(data.get('id'), data.get('nombre'))
        else:
            print(response.status_code, response.text)
            return response.status_code, None

def get_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response, user = UserService().get_user()
        if response == 200 or response == 201:
            return f(user, *args, **kwargs)
        else:
            return 'Forbidden', 403
    return decorated_function
