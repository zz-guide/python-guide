from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox


class MessageBoxUtil:
    @staticmethod
    def info(w: QWidget, text: str, title: str = None):
        if not title:
            title = '信息提示'
        QMessageBox.information(w, title, text)

    @staticmethod
    def error(w: QWidget, text: str, title: str = None):
        if not title:
            title = '警告'
        QMessageBox.information(w, title, text)
