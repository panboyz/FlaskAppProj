# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length


class AddRoleForm(FlaskForm):
    rolename = StringField('角色名', validators=[DataRequired()], render_kw={'placeholder': u'角色名'})
    group = SelectField('所属组',validators=[DataRequired('请选择标签')],choices=[('中台', '中台'), ('理财', '理财'), ('债转', '债转')])
    desc = TextAreaField('角色描述', validators=[DataRequired(), Length(max=50, message='不能超过50字')], render_kw={'placeholder': u'角色描述'})
    isadmin = RadioField(label='是否是管理员',validators=[DataRequired('请选择标签')],choices=[(1, '是'), (2, '否')], coerce=int)
    submit = SubmitField('保存')


class EditRoleForm(FlaskForm):
    rolename = StringField('角色名', validators=[DataRequired()], render_kw={'placeholder': u'角色名'})
    group = SelectField('所属组',validators=[DataRequired('请选择标签')],choices=[('中台', '中台'), ('理财', '理财'), ('债转', '债转')])
    desc = TextAreaField('角色描述', validators=[DataRequired(), Length(max=50, message='不能超过50字')], render_kw={'placeholder': u'角色描述'})
    isadmin = RadioField(label='是否是管理员',validators=[DataRequired('请选择标签')],choices=[(1, '是'), (2, '否')], coerce=int)
    submit = SubmitField('保存')