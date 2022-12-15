from flask import Flask
from flask_restx import Api
from setup_db import db

from config import Config
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import directors_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()

    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(directors_ns)


app = create_app(Config())
app.debug = True
register_extensions(app)

if __name__ == '__main__':
    app.run()
