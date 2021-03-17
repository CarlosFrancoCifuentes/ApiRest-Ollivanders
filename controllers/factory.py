from flask import Flask
from flask_restful import Resource, Api
def create_app():
    app = Flask(__name__)
    api = Api(app)

    class WelcomeOllivanders(Resource):
        def get(self):
            return {'hello': 'Ollivanders'}

    api.add_resource(WelcomeOllivanders, '/')

    return app