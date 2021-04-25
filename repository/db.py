from domain.types import AgedBrie, NormalItem
from flask import jsonify
from repository.models import Item
from flask import current_app as app
from repository.db_model import db
import os

class BD:

    def poblar_bd(self):
        inventario = [{"name": "Aged Brie", "sell_in": 2, "quality": 0}, 
        {"name": "Dexterity Vest", "sell_in": 10, "quality": 20},
        {"name": "Elixir Of The Mongoose", "sell_in": 5, "quality": 7},
        {"name": "Sulfuras, Hand of Ragnaros", "sell_in": 0, "quality": 80},
        {"name": "Sulfuras, Hand of Ragnaros", "sell_in": -1, "quality": 80},
        {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 15, "quality": 20},
        {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 49},
        {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 5, "quality": 49}]
        return inventario

    clasesItems = {
            "Sulfuras Hand of Ragnaros": "Sulfuras",
            "Aged Brie": "AgedBrie",
            "Backstage passes to a TAFKAL80ETC concert": "BackstagePasses",
            "Conjured Mana Cake": "Conjured",
            "+5 Dexterity Vest": "Conjured",
            "Normal Item": "NormalItem",
        }

    def crear_objetos(self, item):

        nombre_item = item[0]
        if nombre_item == self.clasesItems[nombre_item]:
            return eval(nombre_item + str(tuple(item)))
        else: 
            return eval(self.clasesItems["Normal Item"] + str(tuple(item)))
    

    @classmethod
    def get_item(cls, name):
        objeto = db.session.query(Item).filter_by(name = name).all()
        return objeto
