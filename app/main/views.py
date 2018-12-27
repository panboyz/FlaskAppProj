# -*- coding:utf-8 -*-

from flask import render_template
from .. import db
from . import main
from ..models import User, Role
from flask_login import login_required
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    return render_template('main/index.html')


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    return render_template('main/user.html', username=username)


@main.route('/user/roleManage', methods=['GET'])
@login_required
@admin_required
def role_manage():
    roles = Role.query.filter_by(is_active=1).all()
    return render_template('main/role.html', roles=roles)
