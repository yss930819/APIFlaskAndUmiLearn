import unittest

from dacite import from_dict

from watchlist import create_app
from watchlist.api.auth import AuthResponse
from watchlist.extensions import BaseResponse


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.client = cls.app.test_client()
        cls.login_url = "api/v0/auth/login"


    def login(self):
        res = self.client.post(self.login_url, json={"username": "test1", "password": "test1"})
        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(AuthResponse, data.data)
        self.headers = {
            "Authorization": f"Bearer {data.data.access_token}"
        }