from werkzeug.security import generate_password_hash
from database.classes import db, User, Role
import uuid


def create_initial_admin(app, login_admin='admin', password_admin='password'):
    with app.app_context():
        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(name='admin')
            db.session.add(admin_role)
            db.session.commit()

        user_role = Role.query.filter_by(name='user').first()
        if not user_role:
            user_role = Role(name='user')
            db.session.add(user_role)
            db.session.commit()

        if not User.query.filter_by(login='admin').first():
            new_admin = User(
                name='Admin',
                surname='Admin',
                login=login_admin,
                password=generate_password_hash(password_admin),
                role=admin_role,
                active=True,
                fs_uniquifier=str(uuid.uuid4())
            )
            new_admin.roles.append(admin_role)
            db.session.add(new_admin)
            db.session.commit()