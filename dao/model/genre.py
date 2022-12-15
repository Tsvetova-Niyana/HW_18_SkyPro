# здесь модель SQLAlchemy для сущности, также могут быть дополнительные
# методы работы с моделью (но не с базой, с базой мы работаем в классе DAO)

from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
