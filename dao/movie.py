# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, mid):
        movie = self.get_id(mid)

        self.session.delete(movie)
        self.session.commit()

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie
