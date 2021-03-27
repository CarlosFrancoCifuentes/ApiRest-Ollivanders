from flask_restful import abort
from repository.bd import BD


class Service:
    @staticmethod
    def get_item(name):
        if not name:
            abort(404, "Es necesario un nombre de Item")
        items = BD.get_item(name)

        if not items:
            abort(404, "No existe ningún item {}".format(name))
        return {"name": items[0], "sell_in": items[1], "quality": items[2]}

    @staticmethod
    def get_objeto(name):
        if not name:
            abort(404, "Es necesario un nombre de Objeto")
        items = BD.get_objeto(name)

        if not items:
            abort(404, "No existe ningún item {}".format(name))
        return {"name": items.name, "sell_in": items.sell_in, "quality": items.quality}
