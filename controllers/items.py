from flask import Flask
from flask_restful import Resource, Api, reqparse
from services.services import Service

class Items(Resource):
    def get(self, name):
        return Service.get_item(name), 200

    def post(self):
        args = self.parseRequest()
        Service.post_item(args)
        return 'Item publicado con exito', 201

    def delete(self):
        args = self.parseRequest()
        Service.delete_item(args)
        return 'Item eliminado con exito', 204

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='introduce el nombre')
        parser.add_argument('sell_in', type=int, required=True,
                            help='introduce un sellIn')
        parser.add_argument('quality', type=int, required=True,
                            help='introduce una quality')
        return parser.parse_args()