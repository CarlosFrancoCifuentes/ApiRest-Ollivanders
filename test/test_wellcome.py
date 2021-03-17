import pytest

@pytest.mark.wellcome
def test_wellcome(client):
    rv = client.get('/')
    assert b'{"hello": "Ollivanders"}' in rv.data