# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/6 19:22
@Auth ： 仔仔
@File ：base_model.py
"""
from sqlalchemy.orm import declarative_base

# 创建一个SQLORM基类，之后创建的表必须得继承它
SqlalchemyBase = declarative_base()
