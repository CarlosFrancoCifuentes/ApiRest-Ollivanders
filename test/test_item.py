import pytest

@pytest.mark.item
def test_item(client):
    rv = client.get('/item/Aged Brie')
    assert {'name': 'Aged Brie', 'quality': 0, 'sell_in': 2} == rv.get_json()