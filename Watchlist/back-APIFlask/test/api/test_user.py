import unittest

from dacite import from_dict

from watchlist import create_app, db
from watchlist.api.user import UserResponse
from watchlist.dao import User
from watchlist.extensions import BaseResponse


class UserApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        cls.client = cls.app.test_client()
        cls.base_url = "api/v0/user"

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

    def test_app_exist(self):
        """
        测试程序实例是否存在
        :return:
        """
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        """
        测试程序是否处于测试模式
        :return:
        """
        self.assertTrue(self.app.config['TESTING'])

    def test_get_users(self):
        res = self.client.get(self.base_url)
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(len(data.data), 2)

    def test_get_user(self):
        # 获取存在的用户
        res = self.client.get(self.base_url + "/1")
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(UserResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 1)
        self.assertEqual(data.data.name, "Test1")

        # 获取不存在的用户
        res = self.client.get(self.base_url + "/100")
        self.assertEqual(res.status_code, 404)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1000)
        self.assertEqual(data.message, "用户不存在！")
        self.assertEqual(data.data, {})

    def test_create_user(self):
        # 正常输入
        res = self.client.post(self.base_url, json={"name": "Test3"})
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(UserResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 11)
        self.assertEqual(data.data.name, "Test3")

        #

    def test_delete(self):
        res = self.client.delete(self.base_url + "/1")
        self.assertEqual(res.status_code, 200)
        data = from_dict(BaseResponse, res.get_json())

        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "删除成功！")
        self.assertEqual(data.data, {})


if __name__ == '__main__':
    unittest.main()
