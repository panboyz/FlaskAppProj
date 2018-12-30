# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'placeholder': u'用户名'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': u'密码'})


class RegisterForm(FlaskForm):
    username = StringField('', validators=[DataRequired()], render_kw={'placeholder': u'用户名'})
    password = PasswordField('', validators=[DataRequired()], render_kw={'placeholder': u'密码'})
    verifyPwd = PasswordField('', validators=[DataRequired(), EqualTo('password', '密码不一致')],
                              render_kw={'placeholder': u'确认密码'})
    group = SelectField('所属组', validators=[DataRequired('请选择标签')], choices=[('中台', '中台'), ('理财', '理财'), ('债转', '债转'), ('机构', '机构'), ('散标', '散标')])
