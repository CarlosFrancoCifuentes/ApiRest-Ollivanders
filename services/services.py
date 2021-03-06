from flask_restful import abort, fields, marshal_with
from repository.db_connect import get_db
from repository.db import BD
from repository.models import Item

class Service:
    resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    @staticmethod
    @marshal_with(resource_fields)
    def get_item(name):
        db = get_db()
        if not name:
            abort(404, "Es necesario un nombre de Item")
        items = BD.get_item(name)
        return items

    @staticmethod
    def post_item(args):
        db = get_db()
        item = Item(name = args['name'], sell_in = args['sell_in'], quality = args['quality'])
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete_item(args):
        db = get_db()
        item = db.session.query(Item).filter_by(name = args['name'], sell_in = args['sell_in'], quality = args['quality']).first()
        db.session.delete(item)
        db.session.commit()
        
    @staticmethod
    def inventory():
        db = get_db()
        objetos = db.session.query(Item).all()
        result = {"inventory": []}
        for objeto in objetos:
            result["inventory"].append({"name": objeto.name, "sell_in": objeto.sell_in, "quality": objeto.quality})
        return result

    @staticmethod
    def update_quality():
        db = get_db()
        base = BD()
        for item in db.session.query(Item).all():
            objeto_item = base.crear_objetos([item.name, item.sell_in, item.quality])
            objeto_item.update_quality()
            item.sell_in = objeto_item.sell_in
            item.quality = objeto_item.quality
            db.session.commit()
        return Service.inventory()

    @staticmethod
    def quality(args):
        db = get_db()

        item_quality = db.session.query(Item).filter_by(quality= args['quality'])

        return item_quality

    @staticmethod
    def sell_in(args):
        db = get_db()

        item_sell_in = db.session.query(Item).filter_by(sell_in= args['sell_in'])

        return item_sell_in

