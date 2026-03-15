from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    login = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String, unique=True)

    roles = db.relationship('Role', secondary='user_roles', back_populates='users')


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)

    users = db.relationship('User', secondary='user_roles', back_populates='roles')


class AssociationUserRole(db.Model):
    __tablename__ = 'user_roles'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='userroles_users', ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', name='userroles_roles', ondelete='CASCADE'), primary_key=True)