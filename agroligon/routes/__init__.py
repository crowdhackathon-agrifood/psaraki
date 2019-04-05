# Initializes all blueprints

def init_routes(app):
    from agroligon.routes import home

    # Register '/' handler
    app.register_blueprint(home.blueprint)
