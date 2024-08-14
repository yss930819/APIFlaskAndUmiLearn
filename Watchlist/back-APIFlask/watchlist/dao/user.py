from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column

from watchlist.dao.base import BaseDao
from watchlist.extensions import db


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    name: Mapped[str] = mapped_column(db.String(50), nullable=False, default="")  # 用户名


class UserDao:
    @staticmethod
    def create(name: str) -> User:
        return BaseDao.create(User, name=name)

    @staticmethod
    def get_by_id(Id: int) -> User:
        return BaseDao.get_by_id(User, Id)

    @staticmethod
    def get_all() -> list[User]:
        return BaseDao.get_all(User)

    @staticmethod
    def delete(_id: int) -> None:
        BaseDao.delete(User, _id)

    @staticmethod
    def count_all() -> int:
        return BaseDao.count_all(User)
