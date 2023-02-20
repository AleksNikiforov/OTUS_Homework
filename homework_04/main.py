import asyncio
from logger import log
from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
#from base import async_engine, async_session, Base
from models import User, Post, async_engine, Session, Base
from jsonplaceholder_requests import get_users_data, get_posts_data


async def create_tables():
  log.info("Starting create tables")
  async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.drop_all)
      await conn.run_sync(Base.metadata.create_all)
      log.info("Tables created")


async def create_user(session: AsyncSession, name: str, username: str, email: str):
  log.info("Starting create user %s", name)
  user = User(name=name, username=username, email=email)
  session.add(user)
  await session.commit()
  log.info("Created user %s", name)

    
async def create_post(session: AsyncSession, user_id: int, title: str, body: str):
  log.info("Starting create post %s", user_id)
  post = Post(user_id=user_id, title=title, body=body)
  session.add(post)
  await session.commit()
  log.info("Created post %s", title)


async def async_main():
  log.info("Starting collect users_data and posts_data")
  users_data, posts_data = await asyncio.gather(
        get_users_data(),
        get_posts_data(),
    )
  log.info("Collected users_data and posts_data")
  log.info("Starting add users_data and posts_data to DB")
  async with Session() as session:
        for user_data in users_data:
          await create_user(session, user_data['name'], user_data['username'], user_data['email'])
        for post_data in posts_data:
          await create_post(session, post_data['userId'], post_data['title'], post_data['body'])


async def main():
  await create_tables()
  await async_main()


if __name__ == "__main__":
  asyncio.run(main())
