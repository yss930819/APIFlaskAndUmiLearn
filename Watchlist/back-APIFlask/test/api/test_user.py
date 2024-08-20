import unittest
from http import HTTPStatus

from dacite import from_dict
from sqlalchemy.util import md5_hex

from test.api.test_base import BaseTestCase
from watchlist import create_app, db
from watchlist.api.auth import AuthResponse
from watchlist.api.user import UserResponse
from watchlist.dao import User
from watchlist.extensions import BaseResponse


class UserApiTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.base_url = "api/v0/user"

    def setUp(self):
        with self.app.app_context():
            db.create_all()

            db.session.add(User(id=1, name="Test1", username="test1", password=User.hash_password("test1", "test1")))
            db.session.add(User(id=10, name="Test2", username="test2", password=User.hash_password("test2", "test2")))

            db.session.commit()

            self.login()

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
        res = self.client.get(self.base_url, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.OK)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(len(data.data), 2)

    def test_get_user(self):
        # 获取存在的用户
        res = self.client.get(self.base_url + "/1", headers=self.headers)
        self.assertEqual(res.status_code, 200)

        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(UserResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 1)
        self.assertEqual(data.data.name, "Test1")

        # 获取不存在的用户
        res = self.client.get(self.base_url + "/100", headers=self.headers)
        self.assertEqual(res.status_code, 404)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1000)
        self.assertEqual(data.message, "用户不存在！")
        self.assertEqual(data.data, {})

    def test_create_user(self):
        # 正常输入
        res = self.client.post(self.base_url, json={"name": "Test3", "username": "test3", "password": "test3"},
                               headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.OK)

        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(UserResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 11)
        self.assertEqual(data.data.name, "Test3")

        # 异常 name 为空
        res = self.client.post(self.base_url, json={"name": ""}, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1)
        self.assertEqual(data.message, "Validation error")

        # 异常长度超出限制
        res = self.client.post(self.base_url, json={"name": "12345678901234567890"}, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1)
        self.assertEqual(data.message, "Validation error")

        # 用户名重复
        res = self.client.post(self.base_url, json={"name": "Test1", "username": "test1", "password": "test1"},
                               headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.BAD_REQUEST)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1001)
        self.assertEqual(data.message, "用户名已存在！")
        self.assertEqual(data.data, {})

    def test_update(self):
        res = self.client.put(self.base_url + "/1", json={"name": "Test1_up",
                                                          "username": "test1_up",
                                                          }, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        data = from_dict(BaseResponse, res.get_json())
        data.data = from_dict(UserResponse, data.data)
        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "")
        self.assertEqual(data.data.id, 1)
        self.assertEqual(data.data.name, "Test1_up")
        self.assertEqual(data.data.username, "test1_up")

        # 更新不存在的用户
        res = self.client.put(self.base_url + "/100", json={"name": "Test1_up",
                                                            "username": "test1_up",
                                                            }, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.NOT_FOUND)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1000)
        self.assertEqual(data.message, "用户不存在！")
        self.assertEqual(data.data, {})


    def test_update_password(self):
        res = self.client.put(self.base_url + "/1/password", json={"password": "test1_update"}, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        data = from_dict(BaseResponse, res.get_json())

        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "更新密码成功！")

        # 更新不存在的用户
        res = self.client.put(self.base_url + "/100/password", json={"password": "test1_update"}, headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.NOT_FOUND)
        data = from_dict(BaseResponse, res.get_json())
        self.assertEqual(data.code, -1000)
        self.assertEqual(data.message, "用户不存在！")
        self.assertEqual(data.data, {})

    def test_delete(self):
        res = self.client.delete(self.base_url + "/1", headers=self.headers)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        data = from_dict(BaseResponse, res.get_json())

        self.assertEqual(data.code, 0)
        self.assertEqual(data.message, "删除成功！")
        self.assertEqual(data.data, {})


if __name__ == '__main__':
    unittest.main()
