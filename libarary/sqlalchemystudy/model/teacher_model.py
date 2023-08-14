# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/7 17:19
@Auth ： 仔仔
@File ：classes_model.py
"""
from sqlalchemy import Column, Date, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import backref, relationship

from .base_model import SqlalchemyBase
from .teacher_classes_model import TeacherClassesModel


class TeacherModel(SqlalchemyBase):
    __tablename__ = 'teacher'
    __table_args__ = {'comment': '教师表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    name = Column(String(30), nullable=False, comment='姓名')
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    data_updated_at = Column(DateTime, nullable=False,
                             server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                             comment='数据更新时间')

    classes = relationship('TeacherClassesModel')

    def __repr__(self):
        return "<TeacherModel(id='%s', name='%s', created_at='%s', updated_at='%s', data_updated_at='%s')>" % (
            self.id,
            self.name,
            self.created_at,
            self.updated_at,
            self.data_updated_at,
        )
