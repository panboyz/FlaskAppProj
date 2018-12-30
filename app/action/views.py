# -*- coding:utf-8 -*-

from .. import db
from . import action
from ..models import User, Role
from ..common.func import current_time
from .forms import AddRoleForm, EditRoleForm, EditUserForm
from ..decorators import admin_required, manager_required
from flask_login import current_user
from flask import render_template, redirect, url_for, flash, session


@action.route('/role/add_role', methods=['GET', 'POST'])
@admin_required
def add_role():
    roleForm = AddRoleForm()
    rolename = roleForm.rolename.data
    desc = roleForm.desc.data
    isadmin = roleForm.isadmin.data
    if roleForm.validate_on_submit():
        role = Role.query.filter_by(role_name=rolename).first()
        if role is None:
            role = Role(role_name=rolename, desc=desc, is_admin=isadmin)
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


@action.route('/role/edit_role/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_role(id):
    editRoleForm = EditRoleForm()
    role_name = editRoleForm.role_name.data
    desc = editRoleForm.desc.data
    is_admin = editRoleForm.is_admin.data
    role = Role.query.filter_by(id=id).first()
    if is_admin == 2:
        is_admin = 0
    if role.role_name != 'admin':
        if editRoleForm.validate_on_submit():
            role.role_name = role_name
            role.desc = desc
            role.is_admin = is_admin
            role.update_time = current_time()
            try:
                db.session.add(role)
                db.session.commit()
                return redirect(url_for('main.role_manage'))
            except Exception as e:
                print(e)
                flash(u'编辑用户异常')
                db.session.rollback()
    else:
        flash(u'不允许编辑该角色')
        return redirect(url_for('main.role_manage'))
    editRoleForm.role_name.data = role.role_name
    editRoleForm.desc.data = role.desc
    editRoleForm.is_admin.data = role.is_admin
    return render_template('action/edit_role.html', editRoleForm=editRoleForm)


@action.route('/role/delete_role/<int:id>', methods=['GET', 'POST'])
@admin_required
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


@action.route('/user/edit_user/<int:id>', methods=['GET', 'POST'])
@manager_required
def edit_user(id):
    editUserForm = EditUserForm()
    username = editUserForm.username.data
    group = editUserForm.group.data
    is_manager = editUserForm.is_manager.data
    user = User.query.filter_by(id=id).first()
    if is_manager == 2:
        is_manager = 0
    if user.username != 'admin':
        if editUserForm.validate_on_submit():
            user.username = username
            user.group = group
            user.is_manager = is_manager
            user.update_time = current_time()
            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.user_manage'))
            except Exception as e:
                print(e)
                flash(u'编辑用户异常')
                db.session.rollback()
    else:
        flash(u'不允许编辑该角色')
        return redirect(url_for('main.user_manage'))
    editUserForm.username.data = user.username
    editUserForm.group.data = user.group
    editUserForm.is_manager.data = user.is_manager
    return render_template('action/edit_user.html', editUserForm=editUserForm)


@action.route('/user/delete_user/<int:id>', methods=['GET', 'POST'])
@manager_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if current_user.role.is_admin == 1 and user.username != 'admin' or (
            current_user.is_manager == 1 and user.is_manager != 1 and user.group == current_user.group):
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            print(e)
            flash(u'删除角色异常')
            db.session.rollback()
    else:
        flash('无权限删除')
    return redirect(url_for('main.user_manage'))
