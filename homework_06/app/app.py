"""
создайте docker-compose файл, настройте там связь базы данных и веб-приложения
добавьте в свой проект модели. Это могут быть те же модели, что были использованы для сохранения данных с открытого API, это может быть и что-то новое
добавьте возможность создавать новые записи
создайте страницу, на которой эти записи выводятся
база данных должна быть в отдельном контейнере
Flask приложение должно запускаться не в debug режиме, а в production-ready (uwsgi/gunicorn, nginx, Flask)
"""

from flask import Flask, render_template
from async_db import async_get_data

from models import Post, User
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
db.init_app(app)



@app.get("/")
def index_view():
    return render_template("index.html")


@app.get("/about/")
def about_view():
    return render_template("about.html")


@app.get("/getdata/")
async def get_data():
    await async_get_data()
    return render_template("getdata.html")


@app.get("/list_of_posts", endpoint = 'list_of_posts')
def get_posts_list():
    posts = db.session.query(Post).all()
    return render_template(
        "list_of_posts.html",
        posts=posts,
    )


@app.get("/list_of_users", endpoint = 'list_of_users')
def get_products_list():
    users = db.session.query(User).all() 
    return render_template(
        "list_of_users.html",
        users=users,
    )


if __name__ == "__main__":
    app.run(
        debug=False,
    )