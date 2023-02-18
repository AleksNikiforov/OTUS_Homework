import asyncio
from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from base import async_engine, async_session, Base
from models import User, Post
"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# async def create_user(session: AsyncSession, username: str, is_staff=False) -> User:
#     user = User(username=username, is_staff=is_staff)
#     session.add(user)
#     await session.commit()
#     print("created user", user)
#     return user


# async def create_posts(session: AsyncSession, author: Author, *titles: str) -> list[Post]:
#     posts = [Post(author=author, title=title) for title in titles]
#     session.add_all(posts)
#     await session.commit()
#     print(posts)
#     return posts


async def async_main():
    create_tables()
'''
(
users_data: List[dict]
posts_data: List[dict]
users_data, posts_data = await asyncio.gather(
                  fetch_users_data(),
                  fetch_posts_data(),
)
'''


def main():
  pass
  #await async_main()


if __name__ == "__main__":
  asyncio.run(create_tables())
  #asyncio.run(main())

