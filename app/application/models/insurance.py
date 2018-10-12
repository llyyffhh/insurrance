from app.application.models import db
from datetime import date
from functools import reduce
class Insurance(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    num_id = db.Column(db.String(20),nullable=True,unique=True)
    name = db.Column(db.String(10),nullable=True)
    money = db.Column(db.String(10),nullable=True)
    telephone = db.Column(db.String(16))
    low = db.Column(db.Integer,default=0)
    new = db.Column(db.Integer,default=0)
    join_time = db.Column(db.DateTime,default=date.today)

    @staticmethod
    def age(year):
        this_year = int(str(date.today()).split('-')[0])
        age = str(this_year - int(year))
        return age if int(age) > 0 else '新生儿'

    @classmethod
    def today_data(cls):
        today = date.today()
        total_list = db.session.query(cls.money).all()
        total_list = [x[0] for x in total_list]
        total_list = list(map(lambda x:int(x),total_list))
        person = str(len(db.session.query(cls.num_id).all()))
        total_money = reduce(lambda x,y:x+y,total_list)
        limit = cls.query.filter_by(join_time=today).all()
        data = {}
        if limit:
            today_list = [x.money for x in limit]
            today_list = list(map(lambda x:int(x),today_list))
            result = reduce(lambda x,y:x+y ,today_list)
            data['moneys'] = result
        else:
            data['moneys'] = ''
        data['len'] = str(len(limit)) or ''
        data['total'] = total_money or ''
        data['person'] = person or ''
        return data




    @classmethod
    def history_data(cls,num,name,date):
        if date and num:
            result = db.session.query(cls).filter(cls.num_id==num,cls.join_time==date).all()
        elif date and name:
            result = db.session.query(cls).filter(cls.name==name,cls.join_time==date).all()
        elif num:
            result = db.session.query(cls).filter(cls.num_id==num).all()
        elif name:
            result = db.session.query(cls).filter(cls.name==name).all()
        elif date:
            result = db.session.query(cls).filter(cls.join_time==date).all()
        else:
            return []
        return result



class Raw_data(db.Model):
    __tablename__ = 'raw_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_id = db.Column(db.String(20), nullable=True, unique=True)
    name = db.Column(db.String(10), nullable=True)
    telephone = db.Column(db.String(16))
    low = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer,default=0)

    @staticmethod
    def age(year):
        this_year = int(str(date.today()).split('-')[0])
        age = str(this_year - int(year))
        return age if int(age) > 0 else '新生儿'






