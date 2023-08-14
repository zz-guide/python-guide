from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from src.admin.controller import PwdBookController
from src.web.designer.py.pwd_book_table import Ui_Form
from src.web.common.functional import MessageBoxUtil
from src.web.common.widget import TableWidgetFactory
from src.common import VariableCache

mock_table_data = [
    {'id': 1, 'name': '许磊', 'created_at': '2022-11-30 12:12', 'updated_at': '2022-11-30 12:12'},
    {'id': 2, 'name': '张三', 'created_at': '2022-11-29 12:12', 'updated_at': '2022-11-29 12:12'},
    {'id': 3, 'name': '李四', 'created_at': '2022-11-28 12:12', 'updated_at': '2022-11-28 12:12'},
    {'id': 3, 'name': '李四', 'created_at': '2022-11-28 12:12', 'updated_at': '2022-11-28 12:12'},
    {'id': 3, 'name': '李四', 'created_at': '2022-11-28 12:12', 'updated_at': '2022-11-28 12:12'},
    {'id': 3, 'name': '李四', 'created_at': '2022-11-28 12:12', 'updated_at': '2022-11-28 12:12'},
]


class PwdBookTableWidget(QWidget, Ui_Form):
    search_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.setupUi(self)
        params = {
            'rows': [],
            'columns': [
                {'title': 'ID', 'key': 'id'},
                {'title': '账号', 'key': 'username'},
                {'title': '密码', 'key': 'password'},
                {'title': '网址', 'key': 'url'},
                {'title': '备注', 'key': 'remark'},
                {'title': '开始时间', 'key': 'created_at'},
                {'title': '更新时间', 'key': 'updated_at'},
            ],
        }
        self.tableWidget = TableWidgetFactory.create(**params)
        self.layout_table.addWidget(self.tableWidget)
        self.search_signal.connect(self.__search_table)

        self.__search_table()

    def get_url_query_text(self):
        return self.url.text()

    def get_remark_query_text(self):
        return self.remark.text()

    def __search_table(self):
        res = PwdBookController.search_action(url=self.get_url_query_text(), remark=self.get_remark_query_text())
        data = res.get_result()
        self.tableWidget.set_data(data)
        self.tableWidget.rebuild()

    @QtCore.Slot()
    def on_remove_btn_clicked(self):
        _, row = self.tableWidget.get_selected_row()
        if not row:
            MessageBoxUtil.error(self, '请先选择一行数据')
            return

        res = PwdBookController.remove_action(row.get('id'))
        if not res.is_success():
            MessageBoxUtil.error(self, '删除失败')
            return
        else:
            MessageBoxUtil.error(self, '删除成功')
            
        self.__search_table()

    @QtCore.Slot()
    def on_update_btn_clicked(self):
        _, row = self.tableWidget.get_selected_row()
        if not row:
            MessageBoxUtil.error(self, '请先选择一行数据')
            return
        VariableCache.signal_bus.pwd_book_update_signal.emit(row)

    @QtCore.Slot()
    def on_query_btn_clicked(self):
        self.__search_table()

    @QtCore.Slot()
    def on_reset_query_btn_clicked(self):
        print('重置查询条件')
        self.url.clear()
        self.remark.clear()

    @QtCore.Slot()
    def on_create_btn_clicked(self):
        VariableCache.pwd_book_create_widget.show()
