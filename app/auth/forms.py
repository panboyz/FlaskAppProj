# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'placeholder': u'用户名'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': u'密码'})
    # radio = R
    # submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={'placeholder': u'用户名'})
    password = PasswordField('', validators=[DataRequired()], render_kw={'placeholder': u'密码'})
    verifyPwd = PasswordField('', validators=[DataRequired(), EqualTo('password', '密码不一致')],
                              render_kw={'placeholder': u'确认密码'})
