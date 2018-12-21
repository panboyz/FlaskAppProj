# -*- coding:utf-8 -*-

from flask import render_template, request, url_for, flash, redirect, session
from .. import db
from . import main
from ..models import User
from flask_login import login_required


@main.route('/', methods=['GET'])
def index():
    old_name = session.get('username')
    if old_name:
        username = old_name
        return redirect(url_for('.user', username=username))
    return redirect(url_for('auth.login'))


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    olduser = session.get('username')
    if not user or olduser != username:
        return redirect(url_for('auth.login'))
    return render_template('index.html', username=username)


@main.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session['username'] = None
    return redirect(url_for('auth.login'))
