from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.application.models.user import User
from app.application.models.insurance import Insurance,Raw_data