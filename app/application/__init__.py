
from flask import Blueprint, current_app, session, g

from app.application.models import User

user_bp = Blueprint('user',__name__,url_prefix='/user')
main_bp = Blueprint('main',__name__)


from app.application import user
from app.application import main
@user_bp.before_request
def before_request():
    if current_app.config['USER_ID']in session:
        user_id = session.get(current_app.config['USER_ID'])
        user = User.query.get(user_id)
        if user:
            g.cms_user = user

@main_bp.before_request
def before_request():
    if current_app.config['USER_ID']in session:
        user_id = session.get(current_app.config['USER_ID'])
        user = User.query.get(user_id)
        if user:
            g.cms_user = user
