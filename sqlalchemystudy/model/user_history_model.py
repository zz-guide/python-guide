# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/7 17:26
@Auth ： 仔仔
@File ：user_history_model.py
"""

from sqlalchemy import Column, Date, DateTime, String, text, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship, backref

from .base_model import SqlalchemyBase


class UserHistoryModel(SqlalchemyBase):
    __tablename__ = 'user_history'
    __table_args__ = {'comment': '用户历史表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    name = Column(String(30), nullable=False, comment='姓名')
    user_id = Column(BIGINT(20), ForeignKey('user.id'), default=0, nullable=False, server_default=text("'0'"),
                     comment='用户id')
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    data_updated_at = Column(DateTime, nullable=False,
                             server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                             comment='数据更新时间')

    user = relationship('UserModel', backref=backref('user_history_list', uselist=True), cascade='')

    # user2 = relationship("UserModel", back_populates="user_history_list2")

    def __repr__(self):
        return "<UserHistoryModel(id='%s', name='%s', user_id='%s',created_at='%s', updated_at='%s', data_updated_at='%s')>" % (
            self.id,
            self.name,
            self.user_id,
            self.created_at,
            self.updated_at,
            self.data_updated_at,
        )
