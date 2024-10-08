import os
from pathlib import Path

import pydash
from apiflask import APIFlask, HTTPError

from watchlist.api import blueprints
from watchlist.api.hello import hello_bp
from watchlist.cmd import init_all_db_cmd
from watchlist.extensions import response_handler, db, cors, jwt, auth
import watchlist.dao as dao


def create_app(cfg: dict = None):
    app = APIFlask(__name__, title="Watchlist API", version="1.0.0")

    init_default_config(app)
    if not pydash.is_none(cfg):
        app.config.update(**cfg)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def init_default_config(app: APIFlask):
    """
    请在此添加应用的默认配置
    """
    _root = Path(app.root_path)

    # # 数据库配置
    _db_path = (_root / "_data/data.db")
    # # 创建数据库文件夹
    if not _db_path.parent.exists():
        _db_path.parent.mkdir(parents=True, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + _db_path.__str__()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

    # JWT 配置
    app.config["JWT_SECRET_KEY"] = "secret"


def register_blueprints(app: APIFlask):
    """
    注册蓝图
    :param app: Flask 的应用实例
    :return:
    """
    PREFIX_V0 = "/api/v0"
    for bp in blueprints:
        app.register_blueprint(bp, url_prefix=PREFIX_V0 + "/" + bp.name)


def register_extensions(app):
    """
    注册 Flask 扩展
    :param app: Flask 的应用实例
    :return:
    """
    response_handler.init_app(app)
    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)


def register_commands(app):
    """
    注册 Flask 应用的命令行
    :param app: Flask 的应用实例
    :return:
    """
    init_all_db_cmd(app)
