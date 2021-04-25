from flask import Flask
from flask_restful import Resource, Api
from controllers.items import Items
from controllers.inventory import Inventory
from controllers.welcome import WelcomeOllivanders

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(WelcomeOllivanders, "/")
    api.add_resource(Items, "/item/<name>")
    api.add_resource(Inventory, '/inventory')

    return app
