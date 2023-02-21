import asyncio
from logger import log
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from models import User, Post, async_engine, Session, Base
from jsonplaceholder_requests import get_users_data, get_posts_data


async def create_tables():
  async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
      log.info("Tables created")


async def drop_tables():
  async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.drop_all)
      log.info("Tables deleted")


async def create_user(session: AsyncSession, name: str, username: str, email: str):
  user = User(name=name, username=username, email=email)
  session.add(user)
  log.info("Created user %s", name)

    
async def create_post(session: AsyncSession, user_id: int, title: str, body: str):
  post = Post(user_id=user_id, title=title, body=body)
  session.add(post)
  log.info("Created post %s", title)


async def async_main():
  await create_tables()
  users_data, posts_data = await asyncio.gather(
        get_users_data(),
        get_posts_data(),
    )
  log.info("Collected users_data and posts_data")
  log.info("Starting add users_data and posts_data to DB")
  async with Session() as session:
        for user in users_data:
          await create_user(session=session, name=user.get('name'), username=user.get('username'), email=user.get('email'))
        await session.commit()
        for post in posts_data:
          await create_post(session=session, user_id=post.get('userId'), title=post.get('title'), body=post.get('body'))
        await session.commit()


async def main():
  await async_main()


if __name__ == "__main__":
  asyncio.run(main())
