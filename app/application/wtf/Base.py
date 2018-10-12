
from wtforms import Form

class BaseForm(Form):
    @property
    def get_error(self):
        msg = self.errors.popitem()[1][0]
        return msg