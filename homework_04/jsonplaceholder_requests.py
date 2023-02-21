import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users_data(url: str = USERS_DATA_URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result: dict = await response.json()
            return result


async def get_posts_data(url: str = POSTS_DATA_URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result: dict = await response.json()
            return result
            