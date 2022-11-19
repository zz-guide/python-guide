from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# 创建一个SQLORM基类，之后创建的表必须得继承它
Base = declarative_base()


# 创建Users表
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, default=None, primary_key=True)
    name = Column(String(20), default=None, nullable=False)
    age = Column(Integer, default=None, nullable=False)

    # alter table user alter column ids set default '' 修改数据库列默认值
    def __repr__(self):
        return f"User: name: {self.name},age: {self.age}"
