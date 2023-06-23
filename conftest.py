import pytest
from django.test import Client




@pytest.fixture(scope='function')
def client():
    return Client()

@pytest.fixture
def owner():
    return {
        "username": "testeusername",
        "first_name": "MY TEST",
        "last_name": "Yest",
        "password": "1223hslbHSKN../JS",
        "name": "test"
    }