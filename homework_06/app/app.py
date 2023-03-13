"""
создайте docker-compose файл, настройте там связь базы данных и веб-приложения
добавьте в свой проект модели. Это могут быть те же модели, что были использованы для сохранения данных с открытого API, это может быть и что-то новое
добавьте возможность создавать новые записи
создайте страницу, на которой эти записи выводятся
база данных должна быть в отдельном контейнере
Flask приложение должно запускаться не в debug режиме, а в production-ready (uwsgi/gunicorn, nginx, Flask)
"""
import os
from flask import Flask, render_template
from models import Post, User, db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
from views.forms import PostForm, UserForm
from http import HTTPStatus
from werkzeug.exceptions import NotFound
from request_data import get_users_data, get_posts_data



config_name = os.getenv("CONFIG_NAME", "ProductionConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
db.init_app(app)

csrf = CSRFProtect(app)


@app.get("/getdata/")
def get_data():
    # first of all create table in db
    with app.app_context():
        db.create_all()
    # then get dat from remote site
    users_data = get_users_data()
    posts_data = get_posts_data()
    # then put data to db
    for user in users_data:
        user = User(
            name = user.get('name'),
            username = user.get('username'),
            email = user.get('email')
        )
        db.session.add(user)
    db.session.commit()
    for post in posts_data:
        post = Post(
            title = post.get('title'),
            body = post.get('body'),
        )
        db.session.add(post)
    db.session.commit()    
    return render_template("getdata.html")


@app.get("/")
def index_view():
    return render_template("index.html")


@app.get("/about/")
def about_view():
    return render_template("about.html")


@app.get("/list_of_posts", endpoint = 'list_of_posts')
def get_posts_list():
    posts = db.session.query(Post).order_by(Post.id).all()
    return render_template(
        "list_of_posts.html",
        posts=posts,
    )


@app.get("/list_of_users", endpoint = 'list_of_users')
def get_users_list():
    users = db.session.query(User).order_by(User.id).all() 
    return render_template(
        "list_of_users.html",
        users=users,
    )


@app.get("/delete_posts", endpoint = 'delete_posts')
def delete_posts():
    try:
        db.session.query(Post).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return render_template("delete_posts.html")


@app.get("/delete_users", endpoint = 'delete_users')
def delete_users():
    try:
        db.session.query(User).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return render_template("delete_users.html")


@app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("create_post.html", form=form)

    if not form.validate_on_submit():
        return (
            render_template("create_post.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    post = Post(
        title=form.data["title"],
        body=form.data["body"],
    )
    db.session.add(post)
    db.session.commit()
    flash(f"Post {post.title} was created!", category="success")
    url = url_for("list_of_posts")
    return redirect(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")