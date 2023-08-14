from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from src.common import VariableCache
from src.web.designer.py.pwd_book_create import Ui_Form
from src.admin.controller.pwd_book import PwdBookController
from src.web.common.functional import MessageBoxUtil


class PwdBookCreateWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("创建密码本")

    @QtCore.Slot()
    def on_reset_btn_clicked(self):
        self.reset_text()

    @QtCore.Slot()
    def on_submit_btn_clicked(self):
        username = self.username.text()
        password = self.password.text()
        url = self.url.text()
        remark = self.remark.toPlainText()
        if not username:
            MessageBoxUtil.error(self, '账号必填')
            return
        if not password:
            MessageBoxUtil.error(self, '密码必填')
            return
        if not url:
            MessageBoxUtil.error(self, '网址必填')
            return

        data = {'username': username, 'password': password, 'url': url, 'remark': remark}
        res = PwdBookController.create_action(**data)
        if not res.is_success():
            MessageBoxUtil.error(self, res.get_msg())
            return
        else:
            MessageBoxUtil.info(self, '创建成功')

        self.close()
        VariableCache.pwd_book_table_widget.search_signal.emit()

    def close(self):
        self.reset_text()
        super().close()

    def reset_text(self):
        self.username.clear()
        self.url.clear()
        self.password.clear()
        self.remark.clear()
