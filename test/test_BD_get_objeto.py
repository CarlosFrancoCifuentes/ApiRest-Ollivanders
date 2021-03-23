import pytest
from repository.bd import BD
from domain.types import NormalItem

@pytest.mark.db
def test_bd_get_objeto():
    item = NormalItem("Aged Brie", 2, 0)
    assert item == BD.get_objeto("Aged Brie")