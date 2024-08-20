"""
项目使用的扩展
"""
from flask_cors import CORS
from apiflask import HTTPTokenAuth
from flask_jwt_extended import JWTManager

from .response import ResponseHandler, ErrorData, BaseResponse
from .db import db

response_handler = ResponseHandler()  # 响应数据处理

cors = CORS()

auth = HTTPTokenAuth()

jwt = JWTManager()