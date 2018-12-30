# -*- coding:utf-8 -*-

from functools import wraps
from flask import render_template
from flask_login import current_user


def admin_required(func):
    @wraps(func)
    def decorator_function(*args, **kwargs):
        if not current_user.role.is_admin:
            return render_template('error/403.html')
        return func(*args, **kwargs)
    return decorator_function


def manager_required(func):
    @wraps(func)
    def decorator_function(*args, **kwargs):
        if not current_user.is_manager:
            return render_template('error/403.html')
        return func(*args, **kwargs)
    return decorator_function
