from sqlalchemy import Column, Text, Integer
from .database import db


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    