from datetime import timedelta
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:@127.0.0.1:3306/wechat'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'liyan'
USER_ID = ''
HOST = '0.0.0.0'
PERMANENT_SESSION_LIFETIME = timedelta(days=7)