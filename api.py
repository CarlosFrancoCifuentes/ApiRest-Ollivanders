from flask import Flask
from flask_restful import Resource, Api
from controllers.items import Items
from controllers.objetos import Objetos
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:3424@localhost/olivanders"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Inventario(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
db.create_all()

class WelcomeOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivanders'}

api.add_resource(WelcomeOllivanders, '/')
api.add_resource(Items, '/item/<name>')
api.add_resource(Objetos, '/objeto/<name>')

if __name__ == '__main__':
    app.run(debug=True)