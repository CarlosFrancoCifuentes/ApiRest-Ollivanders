from flask import Flask
from flask_restful import Resource, Api
from services.services import Service

class Objetos(Resource):
    def get(self, name):
        return Service.get_objeto(name), 200
