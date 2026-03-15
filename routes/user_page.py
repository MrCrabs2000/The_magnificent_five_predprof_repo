from flask import Blueprint, render_template, request
from flask_security import roles_accepted, current_user
from database.classes import db
from configs.configs import login_required
from model import load_data


user_page = Blueprint('user_page', __name__, template_folder='templates')
@user_page.route('/user/main')
@login_required
@roles_accepted('user')
def user_page():
    try:
        context = {
            'data': load_data(),
        }

        return render_template('user/upload.html', **context)

    finally:
        db.session.close()