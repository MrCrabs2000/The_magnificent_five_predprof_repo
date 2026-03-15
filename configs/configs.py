from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask import Flask, redirect
from werkzeug.security import generate_password_hash
import uuid
from functools import wraps
import os
from locale import setlocale, Error, LC_ALL

from database.classes import User, Role, db
from utils.generation_password import generate_password_for_user


try:
    setlocale(LC_ALL, 'ru_RU.utf8')
except Error:
    try:
        setlocale(LC_ALL, 'rus_rus')
    except Error:
        print("Выбранная локализация недоступна. Используется локализация по умолчанию.")


app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
app.template_folder = TEMPLATE_DIR

app.static_folder = os.path.join(BASE_DIR, '..', 'static')

DB_DIR = os.path.join(BASE_DIR, '..', 'db')
DB_PATH = os.path.join(DB_DIR, 'database.db')


if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR, exist_ok=True)


app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SECURITY_PASSWORD_SALT'] = 'salt-for-password-hashing'
app.config['SECURITY_LOGIN_URL'] = '/logining'
app.config['SECURITY_REGISTER_URL'] = '/registration'
app.config['SECURITY_REGISTERABLE'] = False
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False



db.init_app(app)


@app.before_request
def start_db():
    with app.app_context():
        db.create_all()
        if not Role.query.first():
            admin_role = Role(name='admin')
            user_role = Role(name='user')
            db.session.add(admin_role)
            db.session.add(user_role)
            db.session.commit()
    admin_role = Role.query.filter_by(name='admin').first()

    try:
        admin = User.query.filter_by(login='Admin').first()

        if not admin:
            password = generate_password_for_user()
            print(f"Admin password: {password}")

            passwordHash = generate_password_hash(password)

            main_admin = User(
                login='Admin',
                password=passwordHash,
                active=True,
                fs_uniquifier=str(uuid.uuid4()),
            )

            db.session.add(main_admin)

            if admin_role:
                main_admin.roles.append(admin_role)
            else:
                admin_role = Role(name='admin')
                db.session.add(admin_role)
                main_admin.roles.append(admin_role)

        db.session.commit()
    except Exception:
        db.session.rollback()
    finally:
        db.session.close()

    app.before_first_request = True


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function