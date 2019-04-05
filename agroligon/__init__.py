import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # Create Flask application
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration file from instance/ folder
    app.config.from_pyfile('config.py')

    # We enable insecure transport for OAuth so we can
    # connect with Facebook without errors about HTTPS on localhost
    if app.debug:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Setup database SQLite3 file location
    db_prefix = 'sqlite:///'
    db_suffix = app.config['DB_FILE_NAME']
    db_file_loc = f'{db_prefix}{app.instance_path}/{db_suffix}'

    # Initialize SQLAlchemy ORM
    app.config['SQLALCHEMY_DATABASE_URI'] = db_file_loc
    db.init_app(app)

    # Initialize all models
    from agroligon import models

    # Register custom commands
    from agroligon import commands
    commands.init_commands(app)

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)

    from agroligon.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register all app routes
    from agroligon import routes
    routes.init_routes(app)

    return app
