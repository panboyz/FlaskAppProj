# -*- coding:utf-8 -*-

from .. import db
from . import action
from .forms import AddRoleForm
from ..models import User, Role
from flask import render_template, request, redirect, url_for, flash, session


@action.route('/delete_role/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    role = Role.query.filter_by(id=id).first()
    if role.is_active == 1 and role.is_admin == 1:
        flash('不能删除该角色')
    try:
        db.session.delete(role)
        db.session.commit()
    except Exception as e:
        print(e)
        flash(u'删除角色异常')
        db.session.rollback()
    return redirect(url_for('main.role_manage'))


@action.route('/user/add_role', methods=['GET', 'POST'])
def add_role():
    roleForm = AddRoleForm()
    return render_template('action/add_role.html', roleForm=roleForm)