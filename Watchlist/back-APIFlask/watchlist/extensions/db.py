from datetime import datetime

import click
from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(),
                                              onupdate=datetime.now())
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)


db = SQLAlchemy(model_class=Base)


def init_db():
    db.create_all()


@click.command('init_db')
def init_db_cmd():
    init_db()
    click.echo('Initialized the database.')


def drop_db():
    db.drop_all()


@click.command('drop_db')
def drop_db_cmd():
    drop_db()
    click.echo('Drop the database.')


def init_all_db_cmd(app: APIFlask):
    app.cli.add_command(init_db_cmd)
    app.cli.add_command(drop_db_cmd)
