from domain.types import AgedBrie, NormalItem
from repository.models import Inventario, db
from sqlalchemy import create_engine
from flask import jsonify

class BD:
    
    def poblar_bd(self):
        aged_brie = Inventario(name = "Aged Brie", sell_in = 2, quality = 0)
        dexterity_vest = Inventario(name = "Dexterity Vest", sell_in = 10, quality = 20)
        elixir_of_the_mongoose = Inventario(name = "Elixir Of The Mongoose", sell_in = 5, quality = 7)
        sulfuras1 = Inventario(name = "Sulfuras, Hand of Ragnaros", sell_in = 0, quality = 80)
        sulfuras2 = Inventario(name = "Sulfuras, Hand of Ragnaros", sell_in = -1, quality = 80)
        back_stage1 = Inventario(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 15, quality = 20)
        back_stage2 = Inventario(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 10, quality = 49)
        back_stage3 = Inventario(name = "Backstage passes to a TAFKAL80ETC concert", sell_in = 5, quality = 49)
        
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
        objeto = db.session.query(Inventario).filter_by(name = name).all()
        return objeto

    @classmethod
    def get_objeto(cls, name):
        items = cls.objetos
        return [item for item in items if item.name == name][0]
