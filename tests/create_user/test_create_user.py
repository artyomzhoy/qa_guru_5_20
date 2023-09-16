import json
import os

import requests
from jsonschema.validators import validate

from tests.conftest import resources_path


def test_create_user():
    name = 'morpheus'
    job = 'leader'

    response = requests.post('https://reqres.in/api/users/',
                             {'name': name, 'job': job})

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_create_user_schema():
    name = 'morpheus'
    job = 'leader'

    with open(os.path.join(resources_path, 'create_user_schema.json')) as file:
        schema = json.loads(file.read())

    response = requests.post('https://reqres.in/api/users/',
                             {'name': name, 'job': job})
    validate(response.json(), schema)

