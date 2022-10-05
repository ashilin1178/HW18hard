from flask import request
from flask_restx import Resource, Namespace
from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        """
        выводит список всех фильмов
        :return:
        """
        args = request.args
        if len(args) > 0:
            result = movie_service.get_movie_by_kwargs(**args)
            return movies_schema.dump(result), 200
        result = movie_service.get_movies()
        return movies_schema.dump(result), 200

    def post(self):
        """
        добавляет фильм в базу
        :return:
        """
        req = request.json
        if movie_service.create_movie(**req):
            return "фильм добавлен", 201
        else:
            return "ошибка добавления фильма"

@movie_ns.route('/<int:mid>')
class GenresView(Resource):
    def get(self, mid):
        """
        выводит фильм по его id
        :param mid:
        :return:
        """

        result = movie_service.get_movie_by_id(mid)
        return movies_schema.dump(result), 200

    def put(self, mid):
        """
        обновляет данные фильма
        :param mid:
        :return:
        """
        req = request.json
        if movie_service.edit_movie(mid, **req):
            return "фильм обновился", 204
        else:
            return "ошибка обновления", 404

    def delete(self, mid):
        if movie_service.delete_movie(mid):
            return "фильм успешно удален", 204

        else:
            return "ошибка удаления фильма", 404

