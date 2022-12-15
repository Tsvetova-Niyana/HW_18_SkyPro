from dao.model.genre import GenreSchema
from flask_restx import Resource, Namespace
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_id(gid)

        if genre:
            return genre_schema.dump(genre), 200
        else:
            return f'Запись с id {gid} не найдена', 404
