# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/7 17:19
@Auth ： 仔仔
@File ：classes_model.py
"""
from sqlalchemy import Column, Date, DateTime, String, text, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship

from .base_model import SqlalchemyBase


class TeacherClassesModel(SqlalchemyBase):
    __tablename__ = 'teacher_classes'
    __table_args__ = {'comment': '老师和班级关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    teacher_id = Column(INTEGER(30), ForeignKey("teacher.id"), nullable=False, server_default=text("'0'"),
                        comment='老师id')
    classes_id = Column(INTEGER(30), ForeignKey("classes.id"), nullable=False, server_default=text("'0'"),
                        comment='班级id')
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    data_updated_at = Column(DateTime, nullable=False,
                             server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                             comment='数据更新时间')

    # teacher = relationship("TeacherModel", backref="a1", uselist=False)
    # classes = relationship("ClassesModel", backref="a2", uselist=False)

    def __repr__(self):
        return "<TeacherClassesModel(id='%s', teacher_id='%s', classes_id='%s', created_at='%s', updated_at='%s', data_updated_at='%s')>" % (
            self.id,
            self.teacher_id,
            self.classes_id,
            self.created_at,
            self.updated_at,
            self.data_updated_at,
        )
