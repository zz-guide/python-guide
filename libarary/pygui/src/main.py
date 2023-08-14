import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QStyleFactory

from src.common import GlobalVariableInit, VariableCache

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    GlobalVariableInit.init()
    # VariableCache.login_widget.show()
    VariableCache.main_widget.show()
    sys.exit(app.exec())
