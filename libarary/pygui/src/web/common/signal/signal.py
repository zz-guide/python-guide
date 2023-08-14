# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 22:41
@Auth ： 仔仔
@File ：signal.py
"""
from PySide6 import QtCore
from PySide6.QtCore import QObject
from src.common import VariableCache


class SignalBus(QObject):
    pwd_book_update_signal = QtCore.Signal(dict)

    def __init__(self):
        super().__init__()
        # 编辑pwd_book表格记录
        self.pwd_book_update_signal.connect(VariableCache.pwd_book_update_widget.update_signal)
