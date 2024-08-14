from sqlalchemy.orm import Mapped, mapped_column

from watchlist.dao.base import BaseDao
from watchlist.extensions import db


class Movie(db.Model):  # 表名将会是 movie（自动生成，小写处理）
    title: Mapped[int] = mapped_column(db.String(50), nullable=False, default="")  # 电影标题
    year: Mapped[str] = mapped_column(db.String(10), nullable=False, default="")  # 年份


class MovieDao:

    @staticmethod
    def create(title: str, year: str) -> Movie:
        return BaseDao.create(Movie, title=title, year=year)

    @staticmethod
    def get_by_id(_id: int) -> Movie:
        return BaseDao.get_by_id(Movie, _id)

    @staticmethod
    def get_all() -> list[Movie]:
        return BaseDao.get_all(Movie)

    @staticmethod
    def delete(_id: int) -> None:
        BaseDao.delete(Movie, _id)

    @staticmethod
    def count_all() -> int:
        return BaseDao.count_all(Movie)
