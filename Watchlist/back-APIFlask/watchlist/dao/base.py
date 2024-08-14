import pydash
from sqlalchemy import select, func

from watchlist.extensions import db


class BaseDao:

    @staticmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @staticmethod
    def get_by_id(cls, _id: int):
        stmt = select(cls).where(cls.id == _id)
        return db.session.execute(stmt).scalars().first()

    @staticmethod
    def get_all(cls):
        stmt = select(cls)
        return db.session.execute(stmt).scalars().all()

    @staticmethod
    def delete(cls, _id: int):
        stmt = select(cls).where(cls.id == _id)
        obj = db.session.execute(stmt).scalar_one_or_none()
        if not pydash.is_none(obj):
            db.session.delete(obj)
            db.session.commit()

    @staticmethod
    def count_all(cls) -> int:
        stmt = select(func.count(cls.id))
        return db.session.scalar(stmt)
