import unittest

from dacite import from_dict

from watchlist import create_app
from watchlist.api.movie import MovieResponse
from watchlist.dao import Movie
from watchlist.extensions import db, BaseResponse


class MovieApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.client = cls.app.test_client()
        cls.base_url = "api/v0/movie"

    def setUp(self):
        with self.app.app_context():
            db.create_all()

            db.session.add(Movie(id=1, title="Movie 1", year="1993"))
            db.session.add(Movie(id=2, title="Movie 2", year="1994"))
            db.session.add(Movie(id=3, title="Movie 3", year="1995"))
            db.session.add(Movie(id=4, title="Movie 4", year="1996"))
            db.session.add(Movie(id=5, title="Movie 5", year="1997"))
            db.session.add(Movie(id=6, title="Movie 6", year="1998"))
            db.session.add(Movie(id=7, title="Movie 7", year="1999"))
            db.session.add(Movie(id=8, title="Movie 8", year="2000"))
            db.session.add(Movie(id=9, title="Movie 9", year="2001"))
            db.session.add(Movie(id=10, title="Movie 10", year="2002"))

            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_movies(self):
        res = self.client.get(self.base_url)
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(len(data.data), 10)

    def test_get_movie(self):
        res = self.client.get(self.base_url + "/1")
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(MovieResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 1)
        self.assertEqual(data.data.title, "Movie 1")
        self.assertEqual(data.data.year, "1993")

        res = self.client.get(self.base_url + "/100")
        self.assertEqual(res.status_code, 404)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1000)
        self.assertEqual(data.message, "电影不存在")

    def test_create_movie(self):
        res = self.client.post(self.base_url, json={
            "title": "Movie 11",
            "year": "2003"
        })
        self.assertEqual(res.status_code, 200)
        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(MovieResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 11)
        self.assertEqual(data.data.title, "Movie 11")
        self.assertEqual(data.data.year, "2003")


    def test_delete_movie(self):
        res = self.client.delete(self.base_url + "/1")
        self.assertEqual(res.status_code, 200)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "删除成功")


if __name__ == '__main__':
    unittest.main()
