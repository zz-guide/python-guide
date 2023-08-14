# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/4 11:33
@Auth ： 仔仔
@File ：main_widget.py
"""
from PySide6.QtWidgets import QMainWindow

from src.common import VariableCache
from src.web.designer.py.main_widget import Ui_MainWindow


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("首页")
        self.layout_main.addWidget(VariableCache.pwd_book_table_widget)
