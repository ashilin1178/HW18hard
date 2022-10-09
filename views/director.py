# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета
# service

# Пример
from flask_restx import Resource, Namespace
from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
        выводит список всех режисеров
        :return:
        """
        result = director_service.get_directors()
        return directors_schema.dump(result), 200


@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did):
        """
        выводит режисера по его id
        :param did:
        :return:
        """

        result = director_service.get_director_by_id(did)
        return director_schema.dump(result), 200
