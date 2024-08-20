from watchlist.dao import UserDao


class UserCtrl:
    @staticmethod
    def has_user(id: int) -> bool:
        return UserDao.get_by_id(id) is not None

    @staticmethod
    def has_username(username: str) -> bool:
        return UserDao.get_by_username(username) is not None
