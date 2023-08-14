# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/6 19:30
@Auth ： 仔仔
@File ：db_instance.py
"""
from .db_manager import DbManager

manager = DbManager()
session = manager.get_session()
