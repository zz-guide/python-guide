# from PySide6 import QtCore
# from PySide6.QtCore import Slot
# from PySide6.QtCore import QFile
# from PySide6.QtWidgets import QPushButton
# from PySide6.QtWidgets import QMessageBox, QHBoxLayout
# from PySide6.QtWidgets import QWidget
# from PySide6.QtUiTools import QUiLoader, loadUiType
#
# # from src.logic.login import *
# # from src.widget.share import ShareWidget
# # from src.util.path import get_ui_path
#
#
# # ui, _ = loadUiType(get_ui_path('login'))
#
#
# # class LoginWidget(QWidget, ui):
# #     def __init__(self):
# #         super().__init__()
# #         self.__init_ui()
# #
# #     def __init_ui(self):
# #         self.setWindowTitle("登录")
# #         self.setupUi(self)
# #         # self.okButton = QPushButton('OK')
# #         # self.okButton.setObjectName('okButton')
# #         # layout = self.ui.layout()
# #         # layout.addWidget(self.okButton)
# #         QtCore.QMetaObject.connectSlotsByName(self)
# #         # self.ui.submit.clicked.connect(self.on_submit_clicked)
# #         # loginSignalInstance.login_signal.connect(self.handle_login)
# #
# #     @QtCore.Slot()
# #     def on_submit_clicked(self):
# #         print("点击了ok按钮")
# #         # loginSignalInstance.login_signal.emit('sssss')
#
# # 动态加载方式
# class LoginWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.__init_ui()
#
#     def __init_ui(self):
#         # 动态加载ui
#         qfile = QFile(get_ui_path('login'))
#         qfile.open(QFile.ReadOnly)
#         self.ui = QUiLoader().load(qfile)
#         qfile.close()
#         self.ui.setWindowTitle("登录")
#         QtCore.QMetaObject.connectSlotsByName(self)
#
#     @QtCore.Slot()
#     def on_okButton_clicked(self):
#         print("点击了ok按钮")
#
#     def handle_login(self):
#         res = Login.login(self.get_username_value(), self.get_password_value())
#         if res:
#             QMessageBox.information(self, '信息提示框', '登录成功')
#             self.ui.close()
#             ShareWidget.main_window.ui.show()
#         else:
#             QMessageBox.information(self, '信息提示框', '登录失败')
#
#     def get_username_value(self) -> str:
#         return self.ui.username.text()
#
#     def get_password_value(self) -> str:
#         return self.ui.password.text()
#
# # class LoginWidget(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("信号与槽自动连接")
# #         self.resize(400, 100)
# #         layout = QHBoxLayout()
# #         self.okButton = QPushButton("OK")
# #         self.cancelButton = QPushButton("CANCEL")
# #         # 设置button的内部引用名
# #         self.okButton.setObjectName("okButton")
# #         self.cancelButton.setObjectName("cancelButton")
# #         layout.addWidget(self.okButton)
# #         layout.addWidget(self.cancelButton)
# #         self.setLayout(layout)
# #         # 规定按照内部引用名字（ObjectName）自动绑定信号和槽
# #         QtCore.QMetaObject.connectSlotsByName(self)
# #
# #     @QtCore.Slot()
# #     def on_okButton_clicked(self):  # 槽函数的名字必须是这个，不能改成别的，下面的也一样
# #         print("点击了ok按钮")
# #
# #     @QtCore.Slot()
# #     def on_cancelButton_clicked(self):
# #         print("点击了cancel按钮")
