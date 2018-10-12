from flask import Flask
from app.application.models import db
from app.application import user_bp,main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.setting')
    app.config.from_object('config.secure')
    register_buleprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_buleprint(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)

