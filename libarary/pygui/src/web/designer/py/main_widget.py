# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 631)
        self.actionmenu2 = QAction(MainWindow)
        self.actionmenu2.setObjectName(u"actionmenu2")
        self.actionmenu3 = QAction(MainWindow)
        self.actionmenu3.setObjectName(u"actionmenu3")
        self.actionmenu4 = QAction(MainWindow)
        self.actionmenu4.setObjectName(u"actionmenu4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout_main = QVBoxLayout(self.centralwidget)
        self.layout_main.setObjectName(u"layout_main")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 799, 22))
        self.menumenu = QMenu(self.menuBar)
        self.menumenu.setObjectName(u"menumenu")
        self.menumenu1 = QMenu(self.menumenu)
        self.menumenu1.setObjectName(u"menumenu1")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menumenu.menuAction())
        self.menumenu.addAction(self.menumenu1.menuAction())
        self.menumenu.addAction(self.actionmenu2)
        self.menumenu1.addAction(self.actionmenu3)
        self.menumenu1.addAction(self.actionmenu4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionmenu2.setText(QCoreApplication.translate("MainWindow", u"menu2", None))
        self.actionmenu3.setText(QCoreApplication.translate("MainWindow", u"menu3", None))
        self.actionmenu4.setText(QCoreApplication.translate("MainWindow", u"menu4", None))
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"menu", None))
        self.menumenu1.setTitle(QCoreApplication.translate("MainWindow", u"menu1", None))
    # retranslateUi

