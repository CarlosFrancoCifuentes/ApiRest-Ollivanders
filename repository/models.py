from repository.db_model import db

class Item(db.Model):


    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Inventario %r>' % self.name