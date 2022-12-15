from flask_restx import Resource, Namespace
from flask import request
from implemented import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        if not director_id and not genre_id and not year:
            movies = movie_service.get_all()

        if director_id:
            movies = movie_service.get_by_director(director_id)

        if genre_id:
            movies = movie_service.get_by_genre(genre_id)

        if year:
            movies = movie_service.get_by_year(year)

        return movies_schema.dump(movies), 200

    def post(self):
        reg_json = request.json
        movie_service.create_movie(reg_json)

        return f'Запись с id {reg_json["id"]} добавлена', 201


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movie_service.get_id(mid)

        if movie:
            return movie_schema.dump(movie), 200
        else:
            return f'Запись с id {mid} не найдена', 404

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update_movie(req_json)

        return '', 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return '', 204
