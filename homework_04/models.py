from sqlalchemy import Column, Text, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from base import Base


class User(Base):
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(40), default=False, nullable=False)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    user_id = Column(Integer, nullable=False, unique=False)
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    user_id_this_post = Column(Integer, ForeignKey("blog_users.id"), nullable=True, unique=False)
    user = relationship("User", back_populates="posts")



