from dao.movie import MovieDAO
from dao.model.movie import Movie


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_id(self, mid):
        return self.dao.get_id(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create_movie(self, data):
        movie = Movie(**data)

        return self.dao.create_movie(movie)

    def update_movie(self, data):
        mid = data.get("id")
        movie = self.get_id(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        return self.dao.update_movie(movie)

    def delete(self, mid):
        self.dao.delete_movie(mid)
