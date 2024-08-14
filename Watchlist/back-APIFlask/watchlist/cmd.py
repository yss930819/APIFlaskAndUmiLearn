import click
from apiflask import APIFlask

from watchlist.dao import User, Movie
from watchlist.extensions import db


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


def init_data():
    """
    生成初始化数据
    :return:
    """

    # 增加用户
    name = "Yss"
    user = User(name=name)
    db.session.add(user)

    # 增加电影信息
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    # 提交到数据库
    db.session.commit()


@click.command('init_data')
def init_data_cmd():
    init_data()
    click.echo("Insert Data Success")


def init_all_db_cmd(app: APIFlask):
    app.cli.add_command(init_db_cmd)
    app.cli.add_command(drop_db_cmd)
    app.cli.add_command(init_data_cmd)
