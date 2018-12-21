# -*- coding:utf-8 -*-

from . import db
from . import login_manage
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, index=True)
    name = db.Column(db.String(16), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'User %s' % self.role


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %s' % self.username


@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
