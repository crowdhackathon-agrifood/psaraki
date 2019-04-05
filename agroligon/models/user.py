from flask_login import UserMixin

from agroligon import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Unique user ID
    id = db.Column(db.Integer, primary_key=True)

    # Details from Facebook
    name = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(254), unique=True)
    picture = db.Column(db.Text())
