from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movies_by_kwargs(self, **kwargs):
        return self.session.filter_by(**kwargs).all()

    def create_movie(self, **kwargs):
        try:
            self.session.query.add(Movie(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def edit_movie_by_id(self, mid, **kwargs):
        try:
            self.session.query.filter(Movie.id == mid).update(kwargs)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def delete_movie_by_id(self, mid):
        try:
            self.session.query.filter(Movie.id == mid).delete()
            self.session.commit()
            return True

        except Exception as e:
            print(e)
            self.session.rollback()
            return False

