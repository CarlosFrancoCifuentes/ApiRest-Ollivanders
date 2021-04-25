from flask_restful import Resource, Api, reqparse
from services.services import Service

class Sell_in(Resource):
    def get(self):
        args = self.parseRequest()
        objetos = Service.sell_in(args)
        result = {"inventory": []}
        for item_sell_in in objetos:
            result["inventory"].append({"name": item_sell_in.name, "sell_in": item_sell_in.sell_in, "quality": item_sell_in.quality})
        return result

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('sell_in', type=int, required=True,
                            help='introduce una sell_in')
        return parser.parse_args()