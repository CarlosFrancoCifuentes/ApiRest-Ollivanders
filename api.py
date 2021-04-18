from flask import Flask
from flask_restful import Resource, Api
from controllers.items import Items
from controllers.inventory import Inventory
from controllers.welcome import WelcomeOllivanders
from repository import db_connect
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
db_connect.init_app(app)

api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>', '/item')
api.add_resource(Inventory, '/inventory')

if __name__ == '__main__':
    app.run(debug=True)