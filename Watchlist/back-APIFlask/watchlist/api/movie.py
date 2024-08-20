from dataclasses import field

import pydash
from apiflask import APIBlueprint
from flask_jwt_extended import jwt_required
from marshmallow.validate import Length
from marshmallow_dataclass import dataclass

from watchlist.dao import MovieDao
from watchlist.extensions import ResponseHandler, ErrorData, auth


@dataclass
class MovieRequest:
    title: str = field(
        default="Name",
        metadata={
            "metadata": {
                "title": "电影名",
            },
            "required": True,
            "validate": Length(min=1, max=50),
        }
    )
    year: str = field(
        default=0,
        metadata={
            "metadata": {
                "title": "年份",
            },
            "required": True,
            "validate": Length(min=1, max=4),
        }
    )


@dataclass
class MovieResponse:
    id: int = field(
        default=0,
        metadata={
            "metadata": {
                "title": "电影ID",
            },
        }
    )
    title: str = field(
        default="Name",
        metadata={
            "metadata": {
                "title": "电影名"
            }
        }
    )
    year: str = field(
        default=0,
        metadata={
            "metadata": {
                "title": "年份"
            }
        }
    )


movie_bp = APIBlueprint("movie", __name__)
ERROR_NOT_FOUND = ErrorData(code=-1000, message="电影不存在", status_code=404)


@movie_bp.get("")
@movie_bp.output(MovieResponse.Schema(many=True))
def get_movies():
    movies = MovieDao.get_all()
    return ResponseHandler.ok_response(movies)


@movie_bp.get("/<int:_id>")
@movie_bp.output(MovieResponse.Schema())
@jwt_required()
@movie_bp.auth_required(auth)
def get_movie(_id: int):
    movie = MovieDao.get_by_id(_id)
    if pydash.is_none(movie):
        ResponseHandler.error_response(**ERROR_NOT_FOUND.__dict__)
    return ResponseHandler.ok_response(movie)


@movie_bp.post("")
@movie_bp.input(MovieRequest.Schema())
@movie_bp.output(MovieResponse.Schema())
@jwt_required()
@movie_bp.auth_required(auth)
def create_movie(json_data: MovieRequest):
    movie = MovieDao.create(**json_data.__dict__)
    return ResponseHandler.ok_response(movie)


@movie_bp.delete("/<int:_id>")
@movie_bp.output({})
@jwt_required()
@movie_bp.auth_required(auth)
def delete_movie(_id: int):
    MovieDao.delete(_id)
    return ResponseHandler.ok_response({}, "删除成功")
