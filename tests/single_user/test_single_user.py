import json
import os

import requests
from jsonschema.validators import validate

from tests.conftest import resources_path


def test_single_user_id():
    user_id = 1

    response = requests.get(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id


def test_single_user_schema():
    user_id = 1

    with open(os.path.join(resources_path, 'single_user_schema.json')) as file:
        schema = json.loads(file.read())

    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    validate(response.json(), schema)
