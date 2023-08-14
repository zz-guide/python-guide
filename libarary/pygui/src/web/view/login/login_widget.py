from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from src.admin.controller import UserController
from src.common import VariableCache
from src.web.common.functional import MessageBoxUtil
from src.web.designer.py.login import Ui_LoginForm


class LoginWidget(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("登录")

    @QtCore.Slot()
    def on_submit_btn_clicked(self):
        self.handle_login()

    @QtCore.Slot()
    def on_reset_btn_clicked(self):
        self.username.clear()
        self.password.clear()

    @QtCore.Slot()
    def on_register_btn_clicked(self):
        VariableCache.register_widget.show()

    def handle_login(self):
        # 组装数据
        form_data = {
            'username': self.get_username_value(),
            'password': self.get_password_value(),
        }

        if not form_data.get('username'):
            MessageBoxUtil.error(self, '账号必填')
            return

        if not self.get_password_value():
            MessageBoxUtil.error(self, '密码必填')
            return

        res = UserController.login_action(**form_data)
        if not res.is_success():
            MessageBoxUtil.error(self, res.get_msg())
            return

        # 不应该手动点击确认
        MessageBoxUtil.info(self, '登录成功')

        # 打开主界面
        self.close()
        VariableCache.main_widget.show()

    def get_username_value(self) -> str:
        return self.username.text()

    def get_password_value(self) -> str:
        return self.password.text()
