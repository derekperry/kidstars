from __future__ import absolute_import

from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_security import current_user

db = SQLAlchemy()

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class UsersChildrenAssociation(db.Model):
    __tablename__ = 'users_to_children'
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key=True)
    child_id = db.Column(db.Integer(), db.ForeignKey('child.id'), primary_key=True)
    view_only = db.Column(db.Boolean(), default=False)
    sort_order = db.Column(db.Integer())
    child = db.relationship('Child', back_populates='users')
    user = db.relationship('User', back_populates='children')


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    children = db.relationship('UsersChildrenAssociation', back_populates='user')

    def __repr__(self):
        return '<User ID: {0} - {1}>'.format(self.id, self.username)

    @property
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def as_dict(self):
        # need to update for not columnar property
        props = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return props


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    birth_date = db.Column(db.Date())
    image_url = db.Column(db.String(512), nullable=True)
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'))
    users = db.relationship('UsersChildrenAssociation', back_populates='child')

    def __init__(self):
        self.created_on = date.today()
        self.created_by = current_user.id

