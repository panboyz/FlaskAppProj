# -*- coding:utf-8 -*-

from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(func):
    @wraps(func)
    def decorator_function(*args, **kwargs):
        if not current_user.role.is_admin:
            abort(403)
        return func(*args, **kwargs)
    return decorator_function
