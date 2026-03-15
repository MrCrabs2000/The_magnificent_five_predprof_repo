from flask import Blueprint, render_template
from flask_security import roles_accepted
from configs.configs import login_required
from database.classes import Civilization
from graphs import


diagram_civilizations = Blueprint('diagram_civilizations', __name__, template_folder='templates')
@diagram_civilizations.route('/diagram/civilizations')
@login_required
@roles_accepted('user')
def diagram_civilizations():
    context = {
        'diagram': ,
    }
    return render_template('main.html', **context)