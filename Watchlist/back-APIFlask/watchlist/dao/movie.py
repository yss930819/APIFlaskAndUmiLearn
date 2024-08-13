from sqlalchemy.orm import Mapped, mapped_column

from watchlist.extensions import db


class Movie(db.Model):  # 表名将会是 movie（自动生成，小写处理）
    title: Mapped[int] = mapped_column(db.String(50), nullable=False, default="")  # 电影标题
    year: Mapped[str] = mapped_column(db.String(10), nullable=False, default="")  # 年份
