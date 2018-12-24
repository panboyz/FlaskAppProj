# -*- coding:utf-8 -*-

from flask import render_template
from .. import db
from . import main
from ..models import User
from flask_login import login_required
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    return render_template('index.html')


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    # user = User.query.filter_by(username=username).first()
    # olduser = session.get('username')
    # if not user or olduser != username:
    #     return redirect(url_for('auth.login'))
    return render_template('user.html', username=username)
