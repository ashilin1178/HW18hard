from typing import List

from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> List[MovieDAO]:
        return self.movie_dao.get_all_movies()

    def get_movie_by_id(self, mid):
        return self.movie_dao.get_movie_by_id(mid)

    def create_movie(self, **kwargs):
        return self.movie_dao.create_movie(**kwargs)

    def edit_movie(self, mid, **kwargs):
        return self.movie_dao.edit_movie_by_id(mid, **kwargs)

