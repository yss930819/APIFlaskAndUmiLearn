import pydash
from apiflask import APIFlask, HTTPError


def create_app(cfg: dict = None):
    app = APIFlask(__name__, title="Watchlist API", version="1.0.0")

    if not pydash.is_none(cfg):
        app.config.from_object(cfg)

    return app


def register_blueprints(app):
    """
    注册蓝图
    :param app: Flask 的应用实例
    :return:
    """
    pass


def register_extensions(app):
    """
    注册 Flask 扩展
    :param app: Flask 的应用实例
    :return:
    """
    pass


def register_commands(app):
    """
    注册 Flask 应用的命令行
    :param app: Flask 的应用实例
    :return:
    """
    pass
