"""
项目数据库操作
"""
from .movie import Movie, MovieDao
from .user import User, UserDao

__all__ = ['Movie', 'User', "MovieDao", "UserDao"]
