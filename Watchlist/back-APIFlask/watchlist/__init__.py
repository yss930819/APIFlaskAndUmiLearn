import pydash
from apiflask import APIFlask, HTTPError

from watchlist.api.hello import hello_bp
from watchlist.extensions import response_handler


def create_app(cfg: dict = None):
    app = APIFlask(__name__, title="Watchlist API", version="1.0.0")

    if not pydash.is_none(cfg):
        app.config.from_object(cfg)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_blueprints(app: APIFlask):
    """
    注册蓝图
    :param app: Flask 的应用实例
    :return:
    """
    PREFIX_V0 = "/api/v0"
    app.register_blueprint(hello_bp, url_prefix=PREFIX_V0 + "/hello")


def register_extensions(app):
    """
    注册 Flask 扩展
    :param app: Flask 的应用实例
    :return:
    """
    response_handler.init_app(app)


def register_commands(app):
    """
    注册 Flask 应用的命令行
    :param app: Flask 的应用实例
    :return:
    """
    pass
