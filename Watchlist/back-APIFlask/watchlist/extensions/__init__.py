"""
项目使用的扩展
"""
from .response import ResponseHandler
from .db import db, init_all_db_cmd

response_handler = ResponseHandler()  # 响应数据处理