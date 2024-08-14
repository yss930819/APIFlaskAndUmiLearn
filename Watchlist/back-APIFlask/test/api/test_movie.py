import unittest

from watchlist import create_app
from watchlist.extensions import db


class MovieApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.client = cls.app.test_client()
        cls.base_url = "api/v0/movie/"

    def setUp(self):
        with self.app.app_context():
            db.create_all()

            db.session.add(User(id=1, name="Test1"))
            db.session.add(User(id=10, name="Test2"))

            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()



if __name__ == '__main__':
    unittest.main()
