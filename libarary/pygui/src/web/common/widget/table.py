from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, QHeaderView


class TableWidget(QTableWidget):
    def __init__(self, **kwargs):
        super().__init__()
        self.__columns = kwargs.get('columns', [])  # 表格列配置项
        self.__rows = kwargs.get('rows', [])  # 表格行配置项
        self.__data = kwargs.get('data', [])  # 表格数据

        self.__column_names = []  # 列名list
        self.__column_data_keys = []  # 列 key list
        self.__column_count = 0
        self.__row_count = 20

        # 表格样式配置项
        self.__set_style_config()
        self.__parse()

    def __set_style_config(self):
        # 是否需要显示网格
        self.setShowGrid(True)
        # self.setSelectionMode(QAbstractItemView.SingleSelection)
        # 把表格填满窗口
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 设置表格禁止编辑
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # 设置整行选择
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        # 设置选中模式为单行
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

    def set_columns(self, columns=None):
        if not columns:
            columns = []

        self.__columns = columns

    def set_rows(self, rows=None):
        if not rows:
            rows = []

        self.__rows = rows

    def set_data(self, data=None):
        if not data:
            data = []
        self.__data = data

    def rebuild(self):
        self.__parse()

    def __parse(self):
        self.__parse_columns()
        self.__parse_rows()
        self.__parse_data()

    def __parse_rows(self):
        if not (self.__row_count > 0):
            self.__row_count = len(self.__rows)

        self.__setRows()

    def __parse_data(self):
        if not self.__data:
            return

        self.clearContents()
        for row, item in enumerate(self.__data):
            if type(item) is not dict:
                raise Exception('数据项必须为字典')

            for col, key in enumerate(self.__column_data_keys):
                # print(row, col, key, item)

                # todo::注意,表格数据必须是一个字符串或者icon，其他类型不显示
                _text = item.get(key)
                cell_item = QTableWidgetItem(str(_text))
                # 设置单元格的对齐方式
                cell_item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.setItem(row, col, cell_item)

    def __parse_columns(self):
        column_names = []
        column_data_keys = []
        for item in self.__columns:
            if type(item) is not dict:
                raise Exception('列的数据项必须为字典')

            title = item.get('title')
            if not title:
                raise Exception('列名不能为空')

            key = item.get('key')
            if not key:
                raise Exception('列的数据项key不能为空')

            column_names.append(title)
            column_data_keys.append(key)

        self.__column_names = column_names
        self.__column_count = len(column_names)
        self.__column_data_keys = column_data_keys

        self.__setColumns()

    def __setColumns(self):
        """
        设置表格的列名+列的数量
        顺序不能反，如果先设置了数量，会默认显示1，,2，,3。。。。
        """

        self.clear()
        self.setColumnCount(self.__column_count)
        self.setHorizontalHeaderLabels(self.__column_names)

    def __setRows(self):
        """
        设置表格的行名+初始化行的数量
        """
        self.setRowCount(self.__row_count)
        self.setVerticalHeaderLabels(self.__rows)

    def get_selected_row(self) -> (int, Optional[dict]):
        row_select = self.selectedItems()
        if not row_select:
            return -1, None

        rowIndex = row_select[0].row()
        row = self.__data[rowIndex]
        return rowIndex, row


class TableWidgetFactory:
    @classmethod
    def create(cls, **kwargs) -> TableWidget:
        _widget = TableWidget(**kwargs)
        return _widget
