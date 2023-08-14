from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from src.web.common.functional import MessageBoxUtil
from src.web.designer.py.register import Ui_Form
from src.admin.controller import UserController


class RegisterWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("注册")

    @QtCore.Slot()
    def on_submit_btn_clicked(self):
        self.handle_register()

    @QtCore.Slot()
    def on_reset_btn_clicked(self):
        self.name.clear()
        self.username.clear()
        self.password.clear()
        self.confirm_password.clear()

    def handle_register(self):
        # 组装数据
        form_data = {
            'name': self.get_name_value(),
            'username': self.get_username_value(),
            'password': self.get_password_value(),
            'confirm_password': self.get_confirm_password_value(),
        }

        # 输入校验
        if not form_data.get('name'):
            MessageBoxUtil.error(self, '姓名必填')
            return

        if not form_data.get('username'):
            MessageBoxUtil.error(self, '账号必填')
            return

        if not form_data.get('password'):
            MessageBoxUtil.error(self, '密码必填')
            return

        if not form_data.get('confirm_password'):
            MessageBoxUtil.error(self, '请二次确认密码')
            return

        res = UserController.register_action(**form_data)
        if not res.is_success():
            MessageBoxUtil.error(self, res.get_msg())
            return
        else:
            MessageBoxUtil.info(self, '注册成功')

        # 注册成功，清空输入，关闭注册框
        self.close()

    def close(self):
        self.on_reset_btn_clicked()
        super().close()

    def get_username_value(self) -> str:
        return self.username.text()

    def get_password_value(self) -> str:
        return self.password.text()

    def get_name_value(self) -> str:
        return self.name.text()

    def get_confirm_password_value(self) -> str:
        return self.confirm_password.text()
