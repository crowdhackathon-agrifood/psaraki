from flask import flash
from flask_dance.consumer import oauth_authorized
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_login import current_user, login_user
from sqlalchemy.orm.exc import NoResultFound

from agroligon import db
from agroligon.models.oauth import OAuth
from agroligon.models.user import User

blueprint = make_facebook_blueprint(
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
    scope='email',
    redirect_to='home.producer'
)


@oauth_authorized.connect_via(blueprint)
def facebook_logged_in(blueprint, token):
    if not token:
        flash('Failed to log in.', category='error')
        return False

    resp = blueprint.session.get(
        '/me?fields=id,name,email,picture'
    )

    if not resp.ok:
        flash('Failed to fetch user info.')
        return False

    info = resp.json()
    fb_user_id = info['id']

    query = OAuth.query.filter_by(
        provider=blueprint.name,
        provider_user_id=fb_user_id,
    )

    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=fb_user_id,
            token=token
        )

    if oauth.user:
        login_user(oauth.user)
    else:
        user = User(
            name=info['name'],
            email=info['email'],
            picture=info['picture']['data']['url']
        )

        oauth.user = user

        db.session.add_all([user, oauth])
        db.session.commit()

        login_user(user)

    return False
