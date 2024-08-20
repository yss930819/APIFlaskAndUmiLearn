from watchlist.dao import MovieDao


class MovieCtrl:

    @staticmethod
    def has_movie(id: int) -> bool:
        return MovieDao.get_by_id(id) is not None