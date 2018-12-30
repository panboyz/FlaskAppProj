# -*- coding:utf-8 -*-

from .. import db
from . import auth
from ..models import User, Role
from .forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for, flash, session


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = User.query.filter_by(username=register_form.username.data).first()
        role = Role.query.filter_by(role_name='user').first()
        if not user:
            try:
                newuser = User(username=register_form.username.data, group=register_form.group.data, role_id=role.id)
                newuser.password = register_form.password.data
                db.session.add(newuser)
                db.session.commit()
                return redirect(url_for('.login'))
            except Exception as e:
                print(e)
                db.session.rollback()
        else:
            flash('用户名已存在')
    return render_template('auth/register.html', form=register_form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page is None or not next_page.startswith('/'):
                next_page = url_for('main.user', username=user.username)
            return redirect(next_page)
        flash('账号/密码错误')
    else:
        if session.get('username'):
            return redirect(url_for('main.user', username=session.get('username')))
    return render_template('auth/login.html', form=login_form)


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('.login'))
