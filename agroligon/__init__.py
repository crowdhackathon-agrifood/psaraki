from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    from agroligon import routes
    routes.init_routes(app)

    return app
