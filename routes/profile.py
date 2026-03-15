from flask import Blueprint, render_template
from flask_security import current_user
from database.classes import db, User
from configs.configs import login_required
from flask_security import roles_accepted



profile_page = Blueprint('profile_page', __name__, template_folder='templates')
@profile_page.route('/profile')
@roles_accepted('user')
@login_required
def profilepage():
    info = db.session.query(User).filter_by(id=current_user.id).first()

    context = {
        'name': current_user.name,
        'surname': current_user.surname,
        'login': current_user.login,
        'role': info.roles.name,
    }


    db.session.close()

    return render_template('user/profile.html', **context)