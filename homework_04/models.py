from sqlalchemy import Column, Text, String
from sqlalchemy.orm import relationship
from base import Base

"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user

- доработайте модуль `models`:
    - создайте асинхронный алхимичный `engine` (при помощи `create_async_engine`)
    - добавьте `declarative base`
    - создайте объект `Session` на основе класса `AsyncSession`
    - добавьте модели `User` и `Post`, объявите поля:
        - для модели `User` обязательными являются `name`, `username`, `email`
        - для модели `Post` обязательными являются `user_id`, `title`, `body`
        - создайте связи `relationship` между моделями: `User.posts` и `Post.user`
"""



class User(Base):
    name = Column(String(20), unique=False, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(40), default=False, nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    user_id = Column(String(100), nullable=False, default="", server_default="")
    title = Column(Text, nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts")



