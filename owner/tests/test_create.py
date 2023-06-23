import pytest
import json



@pytest.fixture
def owner():
    return {
        "username": "test",
        "password": "test",
        "name": "test"
    }
    
    
    
@pytest.mark.django_db
def test_must_create_one_user(client, owner):
    results = client.post("/owner/create", data=owner)
    content = results.content.decode()
    content = json.loads(content)
    status_code = results.status_code
    assert content == []
    assert status_code == 200