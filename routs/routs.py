from routs.auth.login import login_page
from routs.auth.admin import admin_page


def register_all_blueprints(app):
    app.register_blueprint(login_page)
    app.register_blueprint(admin_page)
