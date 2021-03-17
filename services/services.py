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
        return items