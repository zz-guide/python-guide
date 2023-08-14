from typing import Optional

from src.admin.common.model.pwd_book import PwdBook


class PwdBookService:
    @staticmethod
    def get_by_username(username: str, *fields) -> Optional[PwdBook]:
        if not username:
            return None

        return PwdBook.select(*fields).where(PwdBook.username == username).get_or_none()

    @staticmethod
    def get_by_id(_id: str, *fields) -> Optional[PwdBook]:
        if not _id:
            return None

        return PwdBook.select(*fields).where(PwdBook.id == _id).get_or_none()
