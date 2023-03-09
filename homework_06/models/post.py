from sqlalchemy import Column, Text, String
from .database import db


class Post(db.Model):
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    