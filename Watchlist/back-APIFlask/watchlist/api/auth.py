from dataclasses import field

from apiflask import APIBlueprint
from marshmallow_dataclass import dataclass

from watchlist.contorl.auth import AuthCtrl
from watchlist.extensions import ResponseHandler


@dataclass
class AuthRequest:
    username: str = field(
        default="",
        metadata={
            "metadata": {
                "title": "用户名",
                "description": "登录时使用",
            },
            "required": True,
        }
    )
    password: str = field(
        default="",
        metadata={
            "metadata": {
                "title": "密码",
                "description": "登录时使用",
            },
            "required": True,
        }
    )


@dataclass
class AuthResponse:
    access_token: str = field(
        default="",
        metadata={
            "metadata": {
                "title": "令牌",
                "description": "登录成功后返回的令牌，在 Header 中增加 ",
            },
        }
    )


auth_bp = APIBlueprint("auth", __name__)


@auth_bp.post("/login")
@auth_bp.input(AuthRequest.Schema)
@auth_bp.output(AuthResponse.Schema)
@auth_bp.doc(
    summary="登录",
    description="用户名 test, 密码：87f77988ccb5aa917c93201ba314fcd4",
)
def login(json_data):
    token = AuthCtrl.login(**json_data.__dict__)
    data = AuthResponse(access_token=token)
    return ResponseHandler.ok_response(data)
