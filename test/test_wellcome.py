import pytest
from repository.bd import BD
from domain.types import AgedBrie
@pytest.mark.wellcome
def test_wellcome(client):
    rv = client.get("/")
    assert b'{"hello": "Ollivanders"}' in rv.data
