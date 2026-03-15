from flask import Blueprint, render_template
from flask_security import roles_accepted
from configs.configs import login_required
from database.classes import Record
from graphs import create_graph


graph_depending = Blueprint('graph_depending', __name__, template_folder='templates')
@graph_depending.route('/graph/depending')
@login_required
@roles_accepted('user')
def graph_depending():
    context = {
        'graph': create_graph(),
    }
    return render_template('main.html', **context)