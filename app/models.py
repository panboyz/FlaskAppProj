# -*- coding:utf-8 -*-

from datetime import datetime
from . import db
from . import login_manage
from flask_login import UserMixin
from .common.func import current_time
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(32), default='user', unique=True)
    desc = db.Column(db.String(128), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.String(32), default=current_time())
    update_time = db.Column(db.String(32), default=current_time())

    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_role():
        admin_role = Role.query.filter_by(role_name='admin').first()
        # user_role = Role.query.filter_by(role_name='user').first()
        if admin_role is None:
            admin = Role(role_name='admin', desc='superAdministrator', is_admin=1)
            # user = Role(role_name='user', group='user', desc='commonUser', is_admin=0)
            db.session.add(admin)
            # db.session.add(user)
            db.session.commit()

    def __repr__(self):
        return 'Role %s' % self.role


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    group = db.Column(db.String(16))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    is_manager = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.String(32), default=current_time())
    update_time = db.Column(db.String(32), default=current_time())

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def insert_admin():
        user = User.query.filter_by(username='admin').first()
        role = Role.query.filter_by(role_name='admin').first()
        if user is None:
            admin = User(username='admin', password_hash=generate_password_hash('admin'), group='admin', is_manager=1,
                         role_id=role.id)
            db.session.add(admin)
            db.session.commit()

    def __repr__(self):
        return 'User %s' % self.username


@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#
#
# class Project(db.Model):
#     __tablename__ = 'project'
#
#     id = db.Column(db.Integer, primary_key=True)
#     project = db.Column(db.String(32), default='user', unique=True)
#     group = db.Column(db.String(32), default=False)
#     create_time = db.Column(db.DateTime)
#     update_time = db.Column(db.DateTime)
#     is_active = db.Column(db.Boolean, default=True)
#
#     users = db.relationship('User', backref='project', lazy='dynamic')
#
#     def __repr__(self):
#         return 'Project %s' % self.project
