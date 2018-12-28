# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class AddRoleForm(FlaskForm):
    rolename = StringField('角色名', validators=[DataRequired()], render_kw={'placeholder': u'角色名'})
    group = SelectField('所属组',validators=[DataRequired('请选择标签')],choices=[(1, '中台'), (2, '理财'), (3, '债转')],coerce=int)
    desc = TextAreaField('角色描述', validators=[DataRequired()], render_kw={'placeholder': u'角色描述'})
    isadmin = RadioField('是否是管理员',validators=[DataRequired('请选择标签')],choices=[(1, '是'), (2, '否')],coerce=int)
    submit = SubmitField('保存')
