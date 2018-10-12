from .Base import BaseForm
from wtforms.validators import Length,DataRequired
from wtforms import StringField,ValidationError


class AddDataForm(BaseForm):
    name = StringField(validators=[Length(min=2,max=4,message='姓名长度有误')])
    num = StringField(validators=[Length(min=18,max=18,message='身份证号长度有误')])
    money = StringField(validators=[Length(min=2,max=3,message='金额输入有误')])
    tel = StringField()
    low = StringField(validators=[DataRequired()])
class EditForm(AddDataForm):
    raw_name = StringField()
    raw_num = StringField()
    raw_money = StringField()
    raw_tel = StringField()
    raw_low = StringField(validators=[DataRequired()])
