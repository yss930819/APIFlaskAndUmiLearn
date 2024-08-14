import dataclasses

import pydash
from apiflask import APIFlask, abort

from dataclasses import field
from typing import Union

from marshmallow_dataclass import dataclass


@dataclass
class BaseResponse:
    code: int = field(
        default=0,
        metadata={
            "metadata": {
                "title": "状态码",
                "description": "0 成功，非 0 失败",
            }

        }
    )
    data: Union[dict, list] = field(
        default_factory=dict,
        metadata={
            "metadata": {
                "title": "返回数据",
                "description": "成功时返回数据，失败时返回为故障详情",
            }

        })
    message: str = field(
        default="",
        metadata={
            "metadata": {
                "title": "返回消息",
                "description": "错误时返回错误提示消息",
            }
        })


@dataclasses.dataclass
class ErrorData:
    code: int = -1
    message: str = ""
    status_code: int = 400
    detail: Union[None, dict] = None


class ResponseHandler:
    NAME = "ys-response"

    error_schema = {
        "properties": {
        },
        "type": "object"
    }

    def __init__(self, app: APIFlask = None):
        self.app = app

        if not pydash.is_none(app):
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        # 设置基础返回 schema
        self.app.config["BASE_RESPONSE_SCHEMA"] = BaseResponse.Schema

        # 设置error处理器
        self.app.error_processor(self.error_processor)
        # 设置 error 的 schema
        self.app.config['VALIDATION_ERROR_SCHEMA'] = self.error_schema
        self.app.config['HTTP_ERROR_SCHEMA'] = self.error_schema

        self.app.extensions[self.NAME] = self

    @staticmethod
    def error_processor(error):
        res = BaseResponse()
        res.code = -1

        if not pydash.is_none(error.extra_data) and "code" in error.extra_data:
            res.code = error.extra_data["code"]

        res.message = error.message
        res.data = error.detail

        return res.__dict__, error.status_code, error.headers

    @staticmethod
    def ok_response(data, message=""):
        """
        成功响应

        :param data: 成功后的数据
        :param message: 可添加成功消息，比如删除时提示删除成功。
        :return: 基于 BaseResponse 的数据
        """
        res = BaseResponse()
        res.code = 0
        res.data = data
        res.message = message
        return res.__dict__

    @staticmethod
    def error_response(code: int, message: str, status_code: int = 400, detail=None):
        """
        错误响应

        :param code: 异常码
        :param message: 错误信息
        :param status_code: HTTP 状态码 默认 400
        :param detail: 错误详情 可以不传递
        """
        abort(status_code, message=message, detail=detail, extra_data={"code": code})
