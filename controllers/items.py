from flask import Flask, jsonify, g
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from services.services import Service
from repository.bd import BD, Inventario


class Items(Resource):
    resource_fields = {
        "response": fields.String
    }
    def get(self, name):
        return {"items": Service.get_item(name)}, 200

    @marshal_with(resource_fields)
    def post(self):
        args = self.parseRequest()
        Service.post_item(args)
        return {'response': 'Item publicado con exito'}, 201

    @marshal_with(resource_fields)
    def delete(self):
        response = ""
        args = self.parseRequest()
        item = g.db.session.query(Inventario).filter_by(name = args['name'], sell_in = args['sell_in'], quality = args['quality']).first()
        if not item:
            response = 'El item no existe'
        else:
            Service.delete_item(args)
            response = 'Item eliminado con exito'
        return {'response': response},200
        

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='introduce el nombre')
        parser.add_argument('sell_in', type=int, required=True,
                            help='introduce un sellIn')
        parser.add_argument('quality', type=int, required=True,
                            help='introduce una quality')
        return parser.parse_args()