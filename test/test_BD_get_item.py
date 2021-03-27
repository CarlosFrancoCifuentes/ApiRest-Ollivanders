import pytest
from repository.bd import BD
from domain.types import AgedBrie
@pytest.mark.db
def test_get_item():
    item = ["Aged Brie", 2, 0]
    assert item == BD.get_item("Aged Brie")
