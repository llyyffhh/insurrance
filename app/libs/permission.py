from functools import wraps
from flask import redirect, url_for,g


def permission_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user = g.cms_user
        if user.has_permission(user.permission):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('main.index'))
    return inner


