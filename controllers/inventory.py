from services.services import Service
from flask_restful import Resource, Api

class Inventory(Resource):
    def get(self):
        return Service.inventory(), 200