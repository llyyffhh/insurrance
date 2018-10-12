from functools import wraps
from flask import session, redirect, current_app, url_for


def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if current_app.config['USER_ID'] in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('user.login'))
    return inner

