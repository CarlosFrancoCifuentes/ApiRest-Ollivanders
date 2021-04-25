from flask_restful import Resource
from services.services import Service

class Update_quality(Resource):
    def get(self):
        return Service.update_quality()