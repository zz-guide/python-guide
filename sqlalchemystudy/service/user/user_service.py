# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/6 19:25
@Auth ： 仔仔
@File ：user_service.py
"""
from sqlalchemy import and_, or_, func

from sqlalchemystudy.db import session
from sqlalchemystudy.model.user_model import UserModel


class UserService:
    @staticmethod
    def insert():
        data = [
            {'name': '许磊', 'age': 22},
            {'name': '张三', 'age': 23},
            {'name': '李四', 'age': 24},
        ]

        models = []
        for key, value in enumerate(data):
            print(key, value, type(key), type(value))
            user = UserModel(**value)
            print(user)
            models.append(user)

        session.add_all(models)
        session.commit()
        session.close()

    @staticmethod
    def update():
        # 1.将要更新的字段设置为update参数
        # 2.直接设置model属性，然后commit
        user = session.query(UserModel).filter(UserModel.id == 1).update({UserModel.name: "ben"})
        print(user)
        session.commit()
        session.close()

    @staticmethod
    def get_all():
        users = session.query(UserModel).order_by(UserModel.created_at.desc()).all()
        if not users:
            return []
        return users

    @staticmethod
    def page_search():
        # 结论：可以连续使用多个filter
        # 结论：可以使用and_和or_进行where的拼接
        # _where = [UserModel.name == '许磊', UserModel.age == 23]
        # _where = [and_(UserModel.name == '许磊', UserModel.age == 23),
        #           or_(UserModel.name == '许磊', UserModel.age == 23)]
        users = session.query(UserModel).filter(UserModel.name == '许磊').filter(UserModel.age == 22).all()
        # users = session.query(UserModel).filter(*_where).all()
        if not users:
            return []
        return users

    @staticmethod
    def get_count_id():
        # 聚合函数
        # from sqlalchemy import func, extract
        # count
        # result = session.query(YtTest.name, func.count(YtTest.id)).group_by(YtTest.name).all()
        # sum
        # result = session.query(YtTest.name, func.sum(YtTest.id)).group_by(YtTest.name).all()
        # max
        # result = session.query(YtTest.name, func.max(YtTest.id)).group_by(YtTest.name).all()
        # min
        # result = session.query(YtTest.name, func.min(YtTest.id)).group_by(YtTest.name).all()
        # having

        # 结果：[(2,), (2,), (2,)]
        return session.query(func.count(UserModel.id)).group_by(UserModel.name).all()

    @staticmethod
    def get_count():
        return session.query(UserModel).count()

    @staticmethod
    def get_name_like(name: str):
        if not name:
            return []
        # like, not like
        users = session.query(UserModel).filter(UserModel.name.like(f'%{name}%')).all()
        if not users:
            return []

        return users

    @staticmethod
    def get_by_id(_id: int):
        if not _id:
            return None
        user = session.query(UserModel).filter(UserModel.id == _id).one_or_none()
        return user

    @staticmethod
    def get_by_ids(ids: [] = None):
        if not ids:
            return []
        return session.query(UserModel).filter(UserModel.id.in_(ids)).all()

    @staticmethod
    def delete_by_id(_id: int) -> bool:
        if not _id:
            return False

        # 先查询后删除,返回结果是受影响行数
        session.query(UserModel).filter(UserModel.id == _id).delete()
        session.commit()
        session.close()
        return True
