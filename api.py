from flask import Flask
from flask_restful import Resource, Api
from controllers.items import Items
from controllers.objetos import Objetos
from repository.bd import BD, db
from controllers.inventory import Inventory
app = Flask(__name__)
api = Api(app)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:3424@localhost/olivanders"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/create')
def create():
    poblar = BD()
    db.drop_all()
    db.create_all()
    with app.app_context():
        poblar.poblar_bd()
    return 'Se ha creado la tabla'

class WelcomeOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivanders'}


api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>', '/item')
api.add_resource(Inventory, '/inventory')
api.add_resource(Objetos, '/objeto/<name>')

if __name__ == '__main__':
    app.run(debug=True)