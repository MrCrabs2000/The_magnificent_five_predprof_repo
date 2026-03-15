from routes.auth.login import login_page
from routes.profile import profile_page
from routes.user_page import user_page
from routes.graph_depending import graph_depending
from routes.diagram_civilization_records import diagram_civilization_records
from routes.diagram_records import diagram_records
from routes.diagram_civilizations import diagram_civilizations


def register_all_blueprints(app):
    app.register_blueprint(login_page)
    app.register_blueprint(profile_page)
    app.register_blueprint(user_page)
    app.register_blueprint(graph_depending)
    app.register_blueprint(diagram_civilization_records)
    app.register_blueprint(diagram_records)
    app.register_blueprint(diagram_civilizations)