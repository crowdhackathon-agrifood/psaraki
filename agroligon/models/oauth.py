from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from agroligon import db
from agroligon.models.user import User


class OAuth(db.Model, OAuthConsumerMixin):
    __tablename__ = 'oauth'

    # The Facebook user ID
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)

    # The Agroligon user ID
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    # The User model association
    user = db.relationship(User)
