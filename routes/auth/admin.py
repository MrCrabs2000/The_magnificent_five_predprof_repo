from flask_security import login_user, current_user
from flask import Blueprint, request, render_template, redirect
from flask_security import roles_required
import uuid
from werkzeug.security import generate_password_hash

from database.classes import db, User, Role


admin_page = Blueprint('admin_page', __name__, template_folder='templates')


@admin_page.route('/create_user', methods=['GET', 'POST'])
@roles_required('admin')
def create_user():
    if request.method == 'GET':
        return render_template('auth/admin.html')

    login = request.form.get('login')
    password = request.form.get('password')
    name = request.form.get('name')
    surname = request.form.get('surname')

    role = db.session.query(Role).filter_by(name='user').first()
    user = db.session.query(User).filter_by(login=login).first()

    if not all([login, password, name, surname]) or len(password) < 6 or user:
        return redirect('/')

    fs_uniquifier = str(uuid.uuid4())

    new_user = User(login=login, name=name, surname=surname, password=generate_password_hash(password), active=True,
                    fs_uniquifier=fs_uniquifier)

    if role:
        new_user.roles.append(role)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

