import pytest
import json

@pytest.mark.django_db
def test_get_all_owner_must_succeed_with_no_content(client):
    results = client.get("/owner/get/all")
    content = results.content.decode()
    content = json.loads(content)
    status_code = results.status_code
    assert content == []
    assert status_code == 200