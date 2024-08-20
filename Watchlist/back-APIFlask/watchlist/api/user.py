from dataclasses import field

import pydash
from apiflask import APIBlueprint
from flask_jwt_extended import jwt_required
from marshmallow.validate import Length
from marshmallow_dataclass import dataclass

from watchlist.dao import UserDao
from watchlist.extensions import ResponseHandler, auth
from watchlist.extensions.response import ErrorData


@dataclass
class UserRequest:
    name: str = field(
        default="Name",
        metadata={
            "metadata": {
                "title": "用户名",
                "description": "创建用户时使用",
            },
            "required": True,
            "validate": Length(min=1, max=10),
        }
    )
    username: str = field(
        default="Username",
        metadata={
            "metadata": {
                "title": "用户名",
                "description": "创建用户时使用",
            },
            "required": True,
            "validate": Length(min=1, max=10),
        }
    )
    password: str = field(
        default="Password",
        metadata={
            "metadata": {
                "title": "密码",
                "description": "创建用户时使用",
            },
            "required": True,
            "validate": Length(max=50),
        }
    )


@dataclass
class UserResponse:
    id: int = field(
        default=0,
        metadata={
            "metadata": {
                "title": "用户ID",
            },
        }
    )
    name: str = field(
        default="Name",
        metadata={
            "metadata": {
                "title": "用户名"
            }
        }
    )


user_bp = APIBlueprint("user", __name__)

ERROR_NOT_FOUND = ErrorData(code=-1000, message="用户不存在！", status_code=404)


@user_bp.get("/<int:_id>")
@user_bp.output(UserResponse.Schema())
@jwt_required()
@user_bp.auth_required(auth)
def get_user(_id: int):
    user = UserDao.get_by_id(_id)
    if pydash.is_none(user):
        ResponseHandler.error_response(**ERROR_NOT_FOUND.__dict__)
    return ResponseHandler.ok_response(user)


@user_bp.get("")
@user_bp.output(UserResponse.Schema(many=True))
@jwt_required()
@user_bp.auth_required(auth)
def get_users():
    users = UserDao.get_all()
    return ResponseHandler.ok_response(users)


@user_bp.post("")
@user_bp.input(UserRequest.Schema())
@user_bp.output(UserResponse.Schema())
@jwt_required()
@user_bp.auth_required(auth)
def create_user(json_data: UserRequest):
    user = UserDao.create(**json_data.__dict__)
    return ResponseHandler.ok_response(user)


@user_bp.delete("/<int:_id>")
@user_bp.output({})
@jwt_required()
@user_bp.auth_required(auth)
def delete_user(_id: int):
    UserDao.delete(_id)
    return ResponseHandler.ok_response({}, "删除成功！")
