# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/6 19:24
@Auth ： 仔仔
@File ：user_model.py
"""

from sqlalchemy import Column, Date, DateTime, String, text, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship

from .base_model import SqlalchemyBase


class UserModel(SqlalchemyBase):
    __tablename__ = 'user'
    __table_args__ = {'comment': '用户表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    name = Column(String(30), nullable=False, comment='姓名')
    age = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='年龄')
    email = Column(String(50), nullable=False, server_default=text("''"), comment='邮箱')
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    data_updated_at = Column(DateTime, nullable=False,
                             server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                             comment='数据更新时间')
    day = Column(Date, nullable=False, server_default=text("'0000-00-00'"), comment='日期')
    # 逻辑外键，不是数据库的那种强制外键，只需要定义ForeignKey('表名.列名')，然后对应表上定义relationship
    classes_id = Column(INTEGER(11), ForeignKey('classes.id'), nullable=False, server_default=text("'0'"),
                        comment='班级id')

    # relationship位置比较灵活，可以反向配置

    # 第一种 只要一遍配置relationship即可
    # user_history_list1 = relationship("UserHistoryModel")

    # 第二种，两边都要配置 relationship
    # user_history_list2 = relationship("UserHistoryModel", back_populates="user2")

    # 第三种，一这边配置relationship，backref
    # user_history_list3 = relationship("UserHistoryModel", backref="user3")
    # user_history_list = relationship("UserHistoryModel", backref="user")

    def __repr__(self):
        return "<UserModel(id='%s', name='%s', age='%s', classes_id='%s',created_at='%s', updated_at='%s', data_updated_at='%s')>" % (
            self.id,
            self.name,
            self.age,
            self.classes_id,
            self.created_at,
            self.updated_at,
            self.data_updated_at,
        )
