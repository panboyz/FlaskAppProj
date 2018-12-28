# -*- coding:utf-8 -*-

from flask import Blueprint

action = Blueprint('action', __name__)

from . import views, forms
