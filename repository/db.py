from domain.types import AgedBrie, NormalItem
from flask import jsonify
from repository.models import Item
from flask import current_app as app
from repository.db_model import db
import os

class BD:

    def poblar_bd(self):
        aged_brie = Item(name = "Aged Brie", sell_in = 2, quality = 0)
        dexterity_vest = Item(name = "Dexterity Vest", sell_in = 10, quality = 20)
        elixir_of_the_mongoose = Item(name = "Elixir Of The Mongoose", sell_in = 5, quality = 7)
        sulfuras1 = Item(name = "Sulfuras, Hand of Ragnaros", sell_in = 0, quality = 80)
        sulfuras2 = Item(name = "Sulfuras, Hand of Ragnaros", sell_in = -1, quality = 80)
        back_stage1 = Item(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 15, quality = 20)
        back_stage2 = Item(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 10, quality = 49)
        back_stage3 = Item(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 5, quality = 49)
        
        db.session.add(aged_brie)
        db.session.add(dexterity_vest)
        db.session.add(elixir_of_the_mongoose)
        db.session.add(sulfuras1)
        db.session.add(sulfuras2)
        db.session.add(back_stage1)
        db.session.add(back_stage2)
        db.session.add(back_stage3)

        db.session.commit()
    

    @classmethod
    def get_item(cls, name):
        objeto = db.session.query(Item).filter_by(name = name).all()
        return objeto

    @classmethod
    def get_objeto(cls, name):
        items = cls.objetos
        return [item for item in items if item.name == name][0]
