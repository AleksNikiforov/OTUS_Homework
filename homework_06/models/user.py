from sqlalchemy import Column, String
from .database import db


class User(db.Model):
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(40), unique=False, nullable=False)
    email = Column(String(40), default=False, nullable=False)
    