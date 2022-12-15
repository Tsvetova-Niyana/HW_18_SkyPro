from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_id(self, did):
        return self.dao.get_id(did)

    def get_all(self):
        return self.dao.get_all()
