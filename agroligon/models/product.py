from agroligon import db
from agroligon.models.user import User


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    quantity = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=db.func.now())

    producer = db.relationship(User, backref='products')
