from agroligon import db
from agroligon.models.region import Region


class Municipality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    region_id = db.Column(db.Integer, db.ForeignKey(Region.id), nullable=False)
    region = db.relationship(Region, backref='municipalities')
