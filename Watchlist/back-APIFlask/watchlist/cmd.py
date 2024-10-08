import click
from apiflask import APIFlask
from sqlalchemy.util import md5_hex

from watchlist.dao import User, Movie, UserDao
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


def add_user(name, username, password):
    password = md5_hex(password + username)
    print(password)
    UserDao.create(name, username, password)


@click.command('add_user')
@click.option('-n', '--name', required=True, help='The name of the user.')
@click.option('-u', '--username', required=True, help='The username of the user.')
@click.option('-p', '--password', required=True, help='The password of the user.')
def add_user_cmd(name, username, password):
    try:
        add_user(name, username, password)
    except Exception as e:
        click.echo(f"Add User Failed: {e}")
    else:
        click.echo(f"Add User Success: {name} {username}")


def init_all_db_cmd(app: APIFlask):
    app.cli.add_command(init_db_cmd)
    app.cli.add_command(drop_db_cmd)
    app.cli.add_command(init_data_cmd)
    app.cli.add_command(add_user_cmd)
