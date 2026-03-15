from routes.auth.login import login_page


def register_all_blueprints(app):
    app.register_blueprint(login_page)
