from flask import Flask
from flask_restful import Resource, Api
from controllers.items import Items
from controllers.objetos import Objetos
app = Flask(__name__)
api = Api(app)

class WelcomeOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivanders'}

api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>')
api.add_resource(Objetos, '/objeto/<name>')

if __name__ == '__main__':
    app.run(debug=True)