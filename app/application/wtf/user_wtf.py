from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,DataRequired,Length,EqualTo,ValidationError

from app.application import User
from app.application.wtf.Base import BaseForm


class LoginForm(BaseForm):
    login_name = StringField(validators=[DataRequired(message='登录名不能为空'),Length(min=3,max=10,message='登录名必须为3-6位')])
    password = StringField(validators=[Length(min=6,max=16,message='密码必须为6-16位之间')])
    remember = IntegerField()

class ResetPwdForm(BaseForm):
    old_pwd = StringField(validators=[Length(min=6,max=16,message='密码必须为6-16位')])
    new_pwd = StringField(validators=[Length(min=6,max=16,message='密码必须为6-16位')])
    new_pwd2 = StringField(validators=[EqualTo('new_pwd',message='两次输入密码不一致')])

class AddUserForm(BaseForm):
    login_name = StringField(validators=[DataRequired(message='登录名不能为空'),Length(min=3,max=10,message='登录名必须为3-6位')])
    name = StringField(validators=[DataRequired('姓名不能为空')])

    def validate_login_name(self,field):
        login_name = field.data
        user = User.query.filter_by(login_name=login_name).first()
        if not user:
            return True
        else:
            raise ValidationError(message='登录名已存在,换一个试试！')

    def validate_name(self,field):
        name = field.data
        user = User.query.filter_by(name=name).first()
        if not user:
            return True
        else:
            raise ValidationError(message='用户名已存在,换一个试试！')



