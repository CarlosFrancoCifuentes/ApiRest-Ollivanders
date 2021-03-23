import pytest

@pytest.mark.item
def test_aged_brie(client):
    rv = client.get('/item/Aged Brie')
    assert {'name': 'Aged Brie', 'quality': 0, 'sell_in': 2} == rv.get_json()
    
@pytest.mark.item
def test_normal_item(client):
    rv = client.get('/item/Elixir of the Mongoose')
    assert {'name': 'Elixir of the Mongoose', 'quality': 7, 'sell_in': 5} == rv.get_json()