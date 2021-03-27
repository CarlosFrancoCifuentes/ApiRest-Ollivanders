from flask import Flask
from flask_restful import Resource, Api
from services.services import Service

class Items(Resource):
    def get(self, name):
        return Service.get_item(name), 200
