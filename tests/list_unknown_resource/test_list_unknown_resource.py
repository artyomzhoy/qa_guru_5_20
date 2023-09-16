import json
import os

import requests
from jsonschema.validators import validate

from tests.conftest import resources_path


def test_list_unknown_resource_total_pages():
    unknown_resource = 'random_value'
    per_page = 1

    response = requests.get(
        url=f'https://reqres.in/api/{unknown_resource}',
        params={'per_page': per_page})

    assert response.status_code == 200
    assert response.json()['total_pages'] == 12


def test_list_unknown_resource_schema():
    unknown_resource = 'random_value'

    with open(os.path.join(resources_path, 'list_unknown_resource_schema.json')) as file:
        schema = json.loads(file.read())

    response = requests.get(f'https://reqres.in/api/{unknown_resource}')
    validate(response.json(), schema)
