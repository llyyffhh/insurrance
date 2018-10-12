from app.application.models import db
from datetime import datetime
import enum
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    login_name = db.Column(db.String(10),unique=True,nullable=False)
    name = db.Column(db.String(10),nullable=False,unique=True)
    __password = db.Column(db.String(128),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    permission = db.Column(db.String(3),default='操作员')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,raw):
        self.__password = generate_password_hash(raw)

    def check_pwd(self,raw_pwd):
        return check_password_hash(self.__password,raw_pwd)

    def has_permission(self,permission):
        return True if permission == '管理员' else False


