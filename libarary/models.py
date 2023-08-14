# coding: utf-8
from sqlalchemy import Column, Date, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT(20), primary_key=True, comment='主键ID')
    name = Column(String(30), nullable=False, comment='姓名')
    age = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='年龄')
    email = Column(String(50), nullable=False, server_default=text("''"), comment='邮箱')
    ids = Column(String(100), nullable=False, server_default=text("''"), comment='ids,逗号分隔')
    link_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='连接id')
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    data_updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='数据更新时间')
    day = Column(Date, nullable=False, server_default=text("'0000-00-00'"), comment='日期')
