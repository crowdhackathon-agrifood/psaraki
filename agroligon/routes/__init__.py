from agroligon.routes import home, login_fb, auth


# Initializes all blueprints

def init_routes(app):
    # Register '/' handler
    app.register_blueprint(home.blueprint)

    # Register '/login/facebook'
    app.register_blueprint(login_fb.blueprint, url_prefix='/login')

    # Register '/logout'
    app.register_blueprint(auth.blueprint)
