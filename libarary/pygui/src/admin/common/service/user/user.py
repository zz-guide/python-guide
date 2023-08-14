from typing import Optional

from src.admin.common.model import User


class UserService:

    @staticmethod
    def get_by_username(username: str, *fields) -> Optional[User]:
        if not username:
            return None

        return User.select(*fields).where(User.username == username).get_or_none()
