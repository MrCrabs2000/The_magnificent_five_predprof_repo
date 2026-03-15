from flask import Blueprint, render_template
from flask_security import roles_accepted
from configs.configs import login_required
from database.classes import Record, Civilization
from graph import civilization_records_chart


diagram_civilization_records = Blueprint('diagram_civilization_records', __name__, template_folder='templates')
@diagram_civilization_records.route('/diagram/civilization_records')
@login_required
@roles_accepted('user')
def diagram_civilization_records():

    context = {
        'diagram': civilization_records_chart(data),
    }
    return render_template('main.html', **context)