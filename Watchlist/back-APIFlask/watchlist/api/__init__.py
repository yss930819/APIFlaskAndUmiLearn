"""
项目提供的 API 接口
负责返回数据和校验数据
"""
from typing import List

from apiflask import APIBlueprint

from .hello import hello_bp

blueprints: List[APIBlueprint] = [
    hello_bp
]
