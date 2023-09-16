import json
import os

import requests
from jsonschema.validators import validate

from tests.conftest import resources_path


def test_single_user_not_found():
    user_id = 'random_value'

    response = requests.get(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 404


def test_single_user_not_found_schema():
    user_id = 'random_value'

    with open(os.path.join(resources_path, 'single_user_not_found_schema.json')) as file:
        schema = json.loads(file.read())

    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    validate(response.json(), schema)
