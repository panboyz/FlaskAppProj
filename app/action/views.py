# -*- coding:utf-8 -*-

from .. import db
from . import action
from datetime import datetime
from .forms import AddRoleForm, EditRoleForm
from ..models import User, Role
from flask import render_template, request, redirect, url_for, flash, session


@action.route('/user/delete_role/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    role = Role.query.filter_by(id=id).first()
    if not (role.is_active == 1 and role.is_admin == 1):
        try:
            db.session.delete(role)
            db.session.commit()
        except Exception as e:
            print(e)
            flash(u'删除角色异常')
            db.session.rollback()
    else:
        flash('不能删除该角色')
    return redirect(url_for('main.role_manage'))


@action.route('/user/add_role', methods=['GET', 'POST'])
def add_role():
    roleForm = AddRoleForm()
    rolename = roleForm.rolename.data
    group = roleForm.group.data
    desc = roleForm.desc.data
    isadmin = roleForm.isadmin.data
    if isadmin == 2:
        is_admin = 0
    if roleForm.validate_on_submit():
        role = Role.query.filter_by(role_name=rolename).first()
        if role is None:
            role = Role(role_name=rolename, group=group, desc=desc, is_admin=is_admin)
            try:
                db.session.add(role)
                db.session.commit()
                return redirect(url_for('main.role_manage'))
            except Exception as e:
                print(e)
                flash(u'添加用户异常')
                db.session.rollback()
        else:
            flash('角色名已存在')
    return render_template('action/add_role.html', roleForm=roleForm)


@action.route('/user/edit_role/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    editRoleForm = EditRoleForm()
    rolename = editRoleForm.rolename.data
    group = editRoleForm.group.data
    desc = editRoleForm.desc.data
    isadmin = editRoleForm.isadmin.data
    role = Role.query.filter_by(id=id).first()
    if isadmin == 2:
        is_admin = 0
    if editRoleForm.validate_on_submit():
        if role is not None:
            role.role_name = rolename
            role.group = group
            role.desc = desc
            role.is_admin = is_admin
            role.update_time = datetime.now()
            try:
                db.session.add(role)
                db.session.commit()
                return redirect(url_for('main.role_manage'))
            except Exception as e:
                print(e)
                flash(u'编辑用户异常')
                db.session.rollback()
        else:
            flash('角色不存在')
    return render_template('action/edit_role.html', role=role, editRoleForm=editRoleForm)
