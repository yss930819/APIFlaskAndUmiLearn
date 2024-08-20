import unittest

from click import password_option
from sqlalchemy.util import md5_hex

from watchlist import create_app
from watchlist.extensions import db
from watchlist.dao import UserDao, User


class UserDaoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        })
        cls.dao = UserDao()

    def setUp(self):
        with self.app.app_context():
            db.create_all()
            user = User(name="Yss", username="yss", password="123456")
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_users(self):
        with self.app.app_context():
            users = self.dao.get_all()
            self.assertIs(len(users), 1)

    def test_get_user_by_id(self):
        with self.app.app_context():
            user = self.dao.get_by_id(1)
            self.assertIsNot(user, None)
            self.assertIs(user.id, 1)
            user = self.dao.get_by_id(4)
            self.assertIsNone(user)

    def test_get_user_by_username(self):
        with self.app.app_context():
            user = self.dao.get_by_username("yss")
            self.assertIsNot(user, None)
            self.assertIs(user.id, 1)

            user = self.dao.get_by_username("test")
            self.assertIsNone(user)

    def test_update_user(self):
        with self.app.app_context():
            user = self.dao.update(1, "test", "test")
            self.assertEqual(user.name, "test")
            self.assertEqual(user.username, "test")

    def test_update_password(self):
        with self.app.app_context():
            user = self.dao.update_password(1, "test")
            self.assertEqual(user.password, md5_hex("test" + "yss"))

    def test_create_user(self):
        with self.app.app_context():
            user = self.dao.create("test", "test", "test")
            self.assertIs(self.dao.count_all(), 2)

            try:
                user = self.dao.create("test", "test", "test")
            except Exception as e:
                self.assertIsNot(e, None)

    def test_delete_user(self):
        with self.app.app_context():
            self.dao.delete(1)
            self.assertIs(self.dao.count_all(), 0)


if __name__ == '__main__':
    unittest.main()
