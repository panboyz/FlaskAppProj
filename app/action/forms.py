# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


class AddRoleForm(FlaskForm):
    rolename = StringField('角色名', validators=[DataRequired()], render_kw={'placeholder': u'角色名'})
    desc = TextAreaField('角色描述', validators=[DataRequired(), Length(max=50, message='不能超过50字')], render_kw={'placeholder': u'角色描述'})
    # isadmin = RadioField(label='是否是管理员',validators=[DataRequired('请选择标签')],choices=[(1, '是'), (2, '否')], coerce=int)
    isadmin = BooleanField('是否管理员')
    submit = SubmitField('提交')


class EditRoleForm(FlaskForm):
    role_name = StringField('角色名', validators=[DataRequired()], render_kw={'placeholder': u'角色名'})
    desc = TextAreaField('角色描述', validators=[DataRequired(), Length(max=50, message='不能超过50字')], render_kw={'placeholder': u'角色描述'})
    # is_admin = RadioField(label='是否是管理员',validators=[DataRequired('请选择标签')],choices=[(1, '是'), (2, '否')], coerce=int)
    is_admin = BooleanField('是否管理员')
    submit = SubmitField('保存')


class EditUserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()], render_kw={'placeholder': u'用户名'})
    group = SelectField('所属组', validators=[DataRequired('请选择标签')],
                        choices=[('中台', '中台'), ('理财', '理财'), ('债转', '债转'), ('机构', '机构'), ('散标', '散标')])
    is_manager = BooleanField('是否组长')
    submit = SubmitField('保存')
