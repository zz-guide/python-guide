# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(508, 391)
        self.verticalLayout = QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(LoginForm)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.usernameLable = QLabel(LoginForm)
        self.usernameLable.setObjectName(u"usernameLable")

        self.horizontalLayout.addWidget(self.usernameLable)

        self.username = QLineEdit(LoginForm)
        self.username.setObjectName(u"username")

        self.horizontalLayout.addWidget(self.username)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.passwordLabel = QLabel(LoginForm)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.horizontalLayout_2.addWidget(self.passwordLabel)

        self.password = QLineEdit(LoginForm)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.reset_btn = QPushButton(LoginForm)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_3.addWidget(self.reset_btn)

        self.submit_btn = QPushButton(LoginForm)
        self.submit_btn.setObjectName(u"submit_btn")

        self.horizontalLayout_3.addWidget(self.submit_btn)

        self.register_btn = QPushButton(LoginForm)
        self.register_btn.setObjectName(u"register_btn")

        self.horizontalLayout_3.addWidget(self.register_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.title.setText(QCoreApplication.translate("LoginForm", u"\u6b22\u8fce\u4f7f\u7528XXX\u7cfb\u7edf", None))
        self.usernameLable.setText(QCoreApplication.translate("LoginForm", u"\u8d26\u53f7", None))
        self.username.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u8bf7\u8f93\u5165", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginForm", u"\u5bc6\u7801", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u8bf7\u8f93\u5165", None))
        self.reset_btn.setText(QCoreApplication.translate("LoginForm", u"\u91cd\u7f6e", None))
        self.submit_btn.setText(QCoreApplication.translate("LoginForm", u"\u767b\u5f55", None))
        self.register_btn.setText(QCoreApplication.translate("LoginForm", u"\u6ce8\u518c", None))
    # retranslateUi

