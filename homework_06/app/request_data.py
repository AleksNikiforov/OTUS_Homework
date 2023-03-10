import requests

USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts"


session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100)


def get_users_data(url: str = USERS_DATA_URL):
    session.mount('http://', adapter)
    response = session.get(USERS_DATA_URL)
    return response.json()


def get_posts_data(url: str = POSTS_DATA_URL):
    session.mount('http://', adapter)
    response = session.get(POSTS_DATA_URL)
    return response.json()
