import unittest

from watchlist import create_app
from watchlist.extensions import db
from watchlist.dao import MovieDao, Movie


class MovieDaoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.dao = MovieDao()

    def setUp(self):
        with self.app.app_context():
            db.create_all()

            movies = [
                {'title': 'My Neighbor Totoro', 'year': '1988'},
                {'title': 'Dead Poets Society', 'year': '1989'},
                {'title': 'A Perfect World', 'year': '1993'},
            ]
            for movie in movies:
                m = Movie(**movie)
                db.session.add(m)

            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_movie(self):
        with self.app.app_context():
            self.dao.create('My Movie', '2019')
            self.assertEqual(self.dao.count_all(), 4)

    def test_get_all_movies(self):
        with self.app.app_context():
            movies = self.dao.get_all()
            self.assertEqual(len(movies), 3)

    def test_get_movie_by_id(self):
        with self.app.app_context():
            movie = self.dao.get_by_id(1)
            self.assertEqual(movie.title, 'My Neighbor Totoro')
            movie = self.dao.get_by_id(4)
            self.assertIsNone(movie)

    def test_delete_movie(self):
        with self.app.app_context():
            self.dao.delete(1)
            self.assertEqual(self.dao.count_all(), 2)


if __name__ == '__main__':
    unittest.main()
