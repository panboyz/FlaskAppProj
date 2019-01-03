# -*- coding:utf-8 -*-

from flask import render_template
from .. import db
from . import main
from ..models import User, Role, Group
from flask_login import login_required
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('main/index.html')


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    return render_template('main/home.html', username=username)


@main.route('/invest/roleManage', methods=['GET'])
@login_required
@admin_required
def role_manage():
    roles = Role.query.filter_by(is_active=1).all()
    return render_template('main/role.html', roles=roles)


@main.route('/invest/userManage', methods=['GET'])
@login_required
def user_manage():
    users = User.query.filter_by(is_active=1).all()
    return render_template('main/user.html', users=users)


@main.route('/invest/groupManage', methods=['GET'])
@login_required
def group_manage():
    groups = Group.query.filter_by(is_active=1).all()
    return render_template('main/group.html', groups=groups)