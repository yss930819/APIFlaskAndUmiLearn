from http import HTTPStatus
from os import abort
from typing import Union

from flask_jwt_extended import create_access_token, get_jwt_identity, current_user

from watchlist.extensions import auth, jwt, ResponseHandler
from watchlist.dao import UserDao


class AuthCtrl:

    @staticmethod
    def login(username: str, password: str) -> Union[str, None]:
        """
        登陆逻辑
        判断 username 和 password 后
        :param username:
        :param password:
        :return:
        """
        user = UserDao.get_by_username(username)
        if user is None:
            return None
        if not user.check_password(password):
            return None
        return create_access_token(identity=user.id)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        """
        jwt 插件获取当前用户
        :param jwt_data:
        :return:
        """
        identity = jwt_data["sub"]
        return UserDao.get_by_id(identity)

    @jwt.unauthorized_loader
    def unauthorized_callback(error_string: str):
        """
        jwt 插件未授权回调
        :param error:
        :return:
        """
        return ResponseHandler.response(-10, error_string, {}, HTTPStatus.UNAUTHORIZED)

    @jwt.invalid_token_loader
    def invalid_token_callback(error_string: str):
        """
        jwt 插件无效回调
        :param error:
        :return:
        """
        return ResponseHandler.response(-11, error_string, {}, HTTPStatus.UNPROCESSABLE_ENTITY)

    @jwt.expired_token_loader
    def expired_token_callback(_expired_jwt_header: dict, _expired_jwt_data: dict):
        """
        jwt 插件过期回调
        :param _expired_jwt_data:
        :return:
        """
        return ResponseHandler.response(-12, "令牌已过期", {}, HTTPStatus.UNAUTHORIZED)

    @jwt.user_lookup_error_loader
    def user_lookup_error_callback(_jwt_header, jwt_data):
        """
        jwt 插件获取当前用户失败回调
        :param jwt_data:
        :return:
        """
        return ResponseHandler.response(-13, "用户不存在", {}, HTTPStatus.UNAUTHORIZED)

    @auth.verify_token
    def verify_token(token: str) -> bool:
        """
        auth 校验 token 的函数
        通过 jwt 的 current_user 直接判断登陆是否成功，无需再解析 token
        :return:
        """
        if not current_user:
            return False
        return True
