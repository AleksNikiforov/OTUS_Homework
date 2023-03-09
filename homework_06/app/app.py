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



app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(
        debug=False,
    )