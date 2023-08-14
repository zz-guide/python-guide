# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/6 19:25
@Auth ： 仔仔
@File ：user_service.py
"""
from sqlalchemy import and_, or_, func

from sqlalchemystudy.db import session
from sqlalchemystudy.model.classes_model import ClassesModel
from sqlalchemystudy.model.teacher_classes_model import TeacherClassesModel
from sqlalchemystudy.model.user_history_model import UserHistoryModel
from sqlalchemystudy.model.user_model import UserModel
from sqlalchemystudy.model.teacher_model import TeacherModel


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
        print(1212)
        # 1.将要更新的字段设置为update参数
        # 2.直接设置model属性，然后commit
        # user = session.query(UserModel).filter(UserModel.id == 1).update({UserModel.name: "ben"})
        # print(user)
        # session.commit()
        # session.close()

        user = UserService.get_by_id(7)
        print(user)
        user.name = '我问问'
        session.commit()

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

    @staticmethod
    def one_2_one():
        user = session.query(UserModel).filter(UserModel.id == 7).one_or_none()
        print('用户信息:', user)
        print('班级信息:', user.classes, type(user.classes))
        print('班级信息222:', user.classes.users, type(user.classes.users))

    @staticmethod
    def one_2_many():
        # user_history = session.query(UserHistoryModel).filter(UserHistoryModel.user_id == 7).one_or_none()
        # print('用户历史信息:', user_history)
        # print('用户信息:', user_history.user)
        user = session.query(UserModel).filter(UserModel.id == 7).one_or_none()
        print('用户信息:', user)
        print('用户历史信息:', user.user_history_list2)
        ## 发现了一个奇怪的现象，只有用到了关联属性才会去查表，不知道底层是怎么做的。。。跟lazy属性有关
        # print('用户历史信息:', user.user_history_list, type(user.user_history_list))
        # print('用户历史信息2:', user.user_history_list[0], type(user.user_history_list[0].user))

    @staticmethod
    def many_2_many():
        # teacher = session.query(TeacherModel).filter(TeacherModel.id == 1).one_or_none()
        # print('老师信息:', teacher)
        # print('班级信息:', teacher.classes, type(teacher.classes))

        classes_info = session.query(ClassesModel).filter(ClassesModel.id == 1).one_or_none()
        print('班级信息:', classes_info)
        print('老师信息:', classes_info.teachers, type(classes_info.teachers))

    @staticmethod
    def many_2_many2():
        association_info = session.query(TeacherClassesModel).filter(TeacherClassesModel.id == 1).one_or_none()
        print('中间表信息:', association_info)
        print('老师信息:', association_info.teachers, type(association_info.teachers))
        print('班级信息:', association_info.classes, type(association_info.teachers))

    @staticmethod
    def relation_delete():
        # 尝试关联关系删除
        res = session.query(UserModel).filter(UserModel.id == 7).one_or_none()
        session.delete(res)
        session.commit()

    @staticmethod
    def join():
        # INNER JOIN
        # LEFT OUTER JOIN
        res = session.query(UserModel, UserHistoryModel).outerjoin(UserHistoryModel).filter(UserModel.id == 7).all()
        for item in res:
            print('item:', item)

        pass

    @staticmethod
    def sub_query():
        pass
