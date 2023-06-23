import pytest
import json
    
    

@pytest.mark.django_db
def test_must_create_one_user(client, owner):
    results = client.post("/owner/create", data=owner)
    content = results.content.decode()
    content = json.loads(content)
    assert results.status_code == 201
    assert content["username"] == owner["username"]
    assert content["is_staff"] == False
