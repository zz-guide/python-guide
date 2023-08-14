from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from src.common import VariableCache
from src.web.designer.py.pwd_book_update import Ui_Form
from src.admin.controller.pwd_book import PwdBookController
from src.web.common.functional import MessageBoxUtil


class PwdBookUpdateWidget(QWidget, Ui_Form):
    update_signal = QtCore.Signal(dict)

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.setupUi(self)
        self.setWindowTitle("编辑密码本")

        self.__form_data = {}
        self.update_signal.connect(self.__open_update)

    @QtCore.Slot()
    def on_reset_btn_clicked(self):
        self.__reset()

    @QtCore.Slot()
    def on_submit_btn_clicked(self):
        data = self.__get_form_data()
        if not data.get('username'):
            MessageBoxUtil.error(self, '账号必填')
            return

        if not data.get('password'):
            MessageBoxUtil.error(self, '密码必填')
            return

        if not data.get('url'):
            MessageBoxUtil.error(self, '网址必填')
            return

        res = PwdBookController.update_action(**data)
        if not res.is_success():
            MessageBoxUtil.error(self, res.get_msg())
            return
        else:
            MessageBoxUtil.info(self, '修改成功')

        self.__close()
        VariableCache.pwd_book_table_widget.search_signal.emit()

    @QtCore.Slot(dict)
    def __open_update(self, val):
        self.__reset()
        self.__set_form_data(**val)
        self.show()

    def __get_form_data(self) -> dict:
        url = self.url.text()
        username = self.username.text()
        password = self.password.text()
        remark = self.remark.toPlainText()
        data = {
            'id': self.__form_data.get('id'),
            'username': username,
            'password': password,
            'url': url,
            'remark': remark,
        }
        return data

    def __set_form_data(self, **kwargs):
        self.__form_data = kwargs
        self.url.setText(kwargs.get('url', ''))
        self.username.setText(kwargs.get('username', ''))
        self.password.setText(kwargs.get('password', ''))
        self.remark.setPlainText(kwargs.get('remark', ''))

    def __close(self):
        self.__reset()
        super().close()

    def __reset(self):
        self.__form_data = {}
        self.username.clear()
        self.url.clear()
        self.password.clear()
        self.remark.clear()
