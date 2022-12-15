from dao.model.director import DirectorSchema
from flask_restx import Resource, Namespace
from implemented import director_service


directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        director = director_service.get_all()
        return directors_schema.dump(director), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_id(did)

        if director:
            return director_schema.dump(director), 200
        else:
            return f'Запись с id {did} не найдена', 404
