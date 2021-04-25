from flask_restful import Resource, Api, reqparse
from services.services import Service

class Quality(Resource):
    def get(self):
        args = self.parseRequest()
        objetos = Service.quality(args)
        result = {"inventory": []}
        for item_quality in objetos:
            result["inventory"].append({"name": item_quality.name, "sell_in": item_quality.sell_in, "quality": item_quality.quality})
        return result

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='introduce el nombre')
        parser.add_argument('sell_in', type=int, required=True,
                            help='introduce un sellIn')
        parser.add_argument('quality', type=int, required=True,
                            help='introduce una quality')
        return parser.parse_args()