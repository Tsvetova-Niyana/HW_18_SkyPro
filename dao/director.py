# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_id(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()
