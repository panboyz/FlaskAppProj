# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, url_for, flash, abort, redirect, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from app.main.forms import LoginForm, RegisterForm
from flask_migrate import Migrate
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'flask'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, index=True)
    name = db.Column(db.String(16), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'User %s' % self.role


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, index=True)
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return 'User %s' % self.username


@app.route('/', methods=['GET'])
def index():
    old_name = session.get('username')
    if old_name:
        username = old_name
        return redirect(url_for('user', username=username))
    return redirect(url_for('login'))


@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.query.filter_by(username=username).first()
    olduser = session.get('username')
    if not user or olduser != username:
        return redirect(url_for('login'))
    return render_template('index.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    username = loginform.username.data
    password = loginform.password.data
    if request.method == 'POST' and loginform.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if not user or user.password != password:
            flash('账号/密码错误')
        else:
            session['username'] = username
            return redirect(url_for('user', username=username))
    else:
        if session.get('username'):
            return redirect(url_for('user', username=session.get('username')))
    return render_template('login.html', form=loginform)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if request.method == 'POST':
        username = registerform.username.data
        password = registerform.password.data
        if registerform.validate_on_submit():
            user = User.query.filter_by(username=username).first()
            if not user:
                try:
                    newuser = User(username=username, password=password, role_id=1)
                    db.session.add(newuser)
                    db.session.commit()
                    return redirect(url_for('login'))
                except Exception as e:
                    print(e)
                    db.session.rollback()
            else:
                flash('用户名已存在')
    return render_template('register.html', form=registerform)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session['username'] = None
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
