from flask import current_app as app
from repository.db_model import db
from flask import g
from repository.db import BD
import click
from flask.cli import with_appcontext
from repository.models import Item

def get_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:3424@localhost/olivanders"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if "db" not in g:
        db.init_app(app)
        g.db = db
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.session.close()

def init_db():
    db = get_db()
    poblar = BD()
    inventario = poblar.poblar_bd()
    db.create_all()
    for item in inventario:
        item_añadido = Item(name=item["name"], sell_in=item["sell_in"], quality=item["quality"])
        db.session.add(item_añadido)
        db.session.commit()

@click.command('init_db_command')
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Creada Base de datos")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)