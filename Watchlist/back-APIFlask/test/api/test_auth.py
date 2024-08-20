import unittest
from http import HTTPStatus

from dacite import from_dict

from watchlist import create_app
from watchlist.api.auth import AuthResponse
from watchlist.dao import User
from watchlist.extensions import db, BaseResponse


class AuthApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.client = cls.app.test_client()
        cls.base_url = "api/v0/auth/login"

    def setUp(self):
        with self.app.app_context():
            db.create_all()

            db.session.add(User(id=1, name="Test1", username="test1", password=User.hash_password("test1", "test1")))

            db.session.commit()

    def test_login(self):
        # 存在
        res = self.client.post(self.base_url, json={"username": "test1", "password": "test1"})
        self.assertEqual(res.status_code, HTTPStatus.OK)
        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(AuthResponse, data.data)
        self.assertIsNotNone(data.data.access_token)

        # 不存在
        res = self.client.post(self.base_url, json={"username": "test2", "password": "test2"})
        self.assertEqual(res.status_code, HTTPStatus.UNAUTHORIZED)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.message, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main()
