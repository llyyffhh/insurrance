from datetime import datetime

from ..models.insurance import Raw_data
from ..models.insurance import Insurance
class QueryModel:
    def __init__(self):
        self.total = ''
        self.rows = []

    def is_low(self,raw):
        return '是' if raw == 1 else '否'

    def state(self,raw):
        return '已缴费' if raw == 1 else '未缴费'

    def single_data(self,index,raw_data):
        data = {
            'Id' : str(index+1),
            'name': raw_data.name,
            'num': raw_data.num_id,
            'tel': raw_data.telephone,
            'age': Raw_data.age(raw_data.num_id[6:10]),
            'low': self.is_low(raw_data.low),
            'state':self.state(raw_data.state)
        }
        return data


    def api(self,data):
        if not data:
            return {'total':self.total,'rows':self.rows}
        else:
            rows = [self.single_data(index=x,raw_data=y) for x,y in enumerate(data)]
            result = {
                'total': str(len(rows)),
                'rows' : rows
            }
            return result
    @staticmethod
    def low(data):
        return '1' if data == '是' else '0'

class todayModel:
    def __init__(self):
        self.total = ''
        self.rows = []

    def is_low(self,raw):
        return '是' if raw == 1 else '否'

    def new(self,raw):
        return '是' if raw == 1 else '否'

    def single_data(self,index,raw_data):
        data = {
            'id' : str(index+1),
            'name': raw_data.name,
            'num': raw_data.num_id,
            'tel': raw_data.telephone,
            'money':raw_data.money,
            'age': Insurance.age(raw_data.num_id[6:10]),
            'low': self.is_low(raw_data.low),
            'new':self.new(raw_data.new)
        }
        return data


    def api(self,data):
        if not data:
            return {'total':self.total,'rows':self.rows}
        else:
            rows = [self.single_data(index=x,raw_data=y) for x,y in enumerate(data)]
            result = {
                'total': str(len(rows)),
                'rows' : rows
            }
            return result

class historyModel(todayModel):
    def single_data(self,index,raw_data):
        data = {
            'id' : str(index+1),
            'name': raw_data.name,
            'num': raw_data.num_id,
            'tel': raw_data.telephone,
            'money':raw_data.money,
            'age': Insurance.age(raw_data.num_id[6:10]),
            'low': self.is_low(raw_data.low),
            'new':self.new(raw_data.new),
            'join_time':self.date_to_str(raw_data.join_time)
        }
        return  data

    def date_to_str(self,date):
        return str(date).split(' ')[0]


