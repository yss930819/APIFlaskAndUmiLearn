from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.util import md5_hex
from sqlalchemy import select, update

from watchlist.dao.base import BaseDao
from watchlist.extensions import db


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    name: Mapped[str] = mapped_column(db.String(50), nullable=False, default="")  # 用户姓名
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, default="", unique=True)  # 用户名
    password: Mapped[str] = mapped_column(db.String(50), nullable=False, default="")

    def check_password(self, password):
        return self.password.__eq__(md5_hex(password + self.username))

    @staticmethod
    def hash_password(username: str, password: str):
        return md5_hex(password + username)


class UserDao:
    @staticmethod
    def create(name: str, username: str, password: str) -> User:
        password = User.hash_password(username, password)
        return BaseDao.create(User, name=name, username=username, password=password)

    @staticmethod
    def get_by_id(Id: int) -> User:
        return BaseDao.get_by_id(User, Id)

    @staticmethod
    def get_by_username(username: str) -> User:
        return BaseDao.get_by_filed(User, "username", username)

    @staticmethod
    def get_all() -> list[User]:
        return BaseDao.get_all(User)

    @staticmethod
    def update(_id: int, name: str, username: str) -> User:
        return BaseDao.update(User, _id, name=name, username=username)

    @staticmethod
    def update_password(_id: int, password: str) -> User:
        stmt = select(User).where(User.id == _id)
        obj = db.session.execute(stmt).scalars().first()
        obj.password = obj.hash_password(obj.username, password)
        db.session.commit()
        return obj

    @staticmethod
    def delete(_id: int) -> None:
        BaseDao.delete(User, _id)

    @staticmethod
    def count_all() -> int:
        return BaseDao.count_all(User)
