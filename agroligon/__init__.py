from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return 'Hello World'

    return app
