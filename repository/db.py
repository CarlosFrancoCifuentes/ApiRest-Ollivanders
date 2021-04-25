from domain.types import *
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
        {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 10, "quality": 30},
        {"name": "Backstage passes to a TAFKAL80ETC concert", "sell_in": 5, "quality": 30}]
        return inventario



    def crear_objetos(self, item):
        dictClassesItems = {
            "Sulfuras, Hand of Ragnaros": "Sulfuras",
            "Aged Brie": "AgedBrie",
            "Backstage passes to a TAFKAL80ETC concert": "Backstage",
            "Conjured mana cake": "ConjuredItem",
            "Normal Item": "NormalItem",
        }
        try:
            nombre_item = item[0]
            classItem = dictClassesItems[nombre_item]
        except KeyError:
            classItem = dictClassesItems["Normal Item"]

        return eval(classItem + str(tuple(item)))
    

    @classmethod
    def get_item(cls, name):
        objeto = db.session.query(Item).filter_by(name = name).all()
        return objeto
