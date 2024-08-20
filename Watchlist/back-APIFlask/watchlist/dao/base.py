import pydash
from sqlalchemy import select, func, update

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
        return BaseDao.get_by_filed(cls, 'id', _id)

    @staticmethod
    def get_by_filed(cls, filed: str, value: any):
        stmt = select(cls).where(getattr(cls, filed) == value)
        return db.session.execute(stmt).scalars().first()

    @staticmethod
    def get_all(cls):
        stmt = select(cls)
        return db.session.execute(stmt).scalars().all()

    @staticmethod
    def update(cls, _id: int, **kwargs):
        stmt = update(cls).where(cls.id == _id).values(**kwargs)
        db.session.execute(stmt)
        return db.session.get(cls, _id)


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
