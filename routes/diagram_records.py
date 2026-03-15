from flask import Blueprint, render_template
from flask_security import roles_accepted
from configs.configs import login_required
from database.classes import Record, Civilization
from graphs import


diagram_records = Blueprint('diagram_records', __name__, template_folder='templates')
@diagram_records.route('/diagram/records')
@login_required
@roles_accepted('user')
def diagram_records():
    context = {
        'diagram': ,
    }
    return render_template('main.html', **context)