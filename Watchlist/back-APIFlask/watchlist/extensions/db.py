from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, default=None)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(),
                                              onupdate=datetime.now())
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)


db = SQLAlchemy(model_class=Base)
