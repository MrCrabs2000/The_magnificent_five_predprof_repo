from flask_security import login_user
from werkzeug.security import check_password_hash
from flask import Blueprint, request, render_template, redirect

from database.classes import db, User



login_page = Blueprint('login_page', __name__, template_folder='templates')
@login_page.route('/login', methods=['GET', 'POST'])
def loginpage():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not all([login, password]):
        return redirect('/')
    
    user = db.session.query(User).filter_by(login=login).first()

    if not user or not check_password_hash(user.password, password):
        return redirect('/')
    
    login_user(user)

    return redirect('/')