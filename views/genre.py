from flask_restx import Resource, Namespace
from dao.model.schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        выводит список всех жанров
        :return:
        """
        result = genre_service.get_genres()
        return genres_schema.dump(result), 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        """
        выводит жанр по его id
        :param gid:
        :return:
        """

        result = genre_service.get_genre_by_id(gid)
        return genre_schema.dump(result), 200
