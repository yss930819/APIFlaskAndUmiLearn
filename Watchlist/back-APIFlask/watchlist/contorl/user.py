from watchlist.dao import UserDao


class UserCtrl:

    @staticmethod
    def has_username(username: str) -> bool:
        return UserDao.get_by_username(username) is not None


