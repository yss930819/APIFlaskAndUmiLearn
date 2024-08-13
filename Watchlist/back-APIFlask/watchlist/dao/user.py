from sqlalchemy.orm import Mapped, mapped_column

from watchlist.extensions import db


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    name: Mapped[int] = mapped_column(db.String(50), nullable=False, default="")  # 用户名
