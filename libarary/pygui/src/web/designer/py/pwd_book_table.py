# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwd_book_table.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(641, 532)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_header = QHBoxLayout()
        self.layout_header.setObjectName(u"layout_header")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_header.addItem(self.horizontalSpacer_6)

        self.title = QLabel(Form)
        self.title.setObjectName(u"title")

        self.layout_header.addWidget(self.title)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_header.addItem(self.horizontalSpacer_5)

        self.create_btn = QPushButton(Form)
        self.create_btn.setObjectName(u"create_btn")

        self.layout_header.addWidget(self.create_btn)


        self.verticalLayout.addLayout(self.layout_header)

        self.layout_action = QHBoxLayout()
        self.layout_action.setObjectName(u"layout_action")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_action.addItem(self.horizontalSpacer_9)

        self.remove_btn = QPushButton(Form)
        self.remove_btn.setObjectName(u"remove_btn")

        self.layout_action.addWidget(self.remove_btn)

        self.update_btn = QPushButton(Form)
        self.update_btn.setObjectName(u"update_btn")

        self.layout_action.addWidget(self.update_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_action.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.layout_action)

        self.layout_query = QVBoxLayout()
        self.layout_query.setObjectName(u"layout_query")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.url = QLineEdit(Form)
        self.url.setObjectName(u"url")

        self.horizontalLayout_3.addWidget(self.url)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.remark = QLineEdit(Form)
        self.remark.setObjectName(u"remark")

        self.horizontalLayout_5.addWidget(self.remark)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.query_btn = QPushButton(Form)
        self.query_btn.setObjectName(u"query_btn")

        self.horizontalLayout_2.addWidget(self.query_btn)

        self.reset_query_btn = QPushButton(Form)
        self.reset_query_btn.setObjectName(u"reset_query_btn")

        self.horizontalLayout_2.addWidget(self.reset_query_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)


        self.layout_query.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.layout_query)

        self.layout_table = QVBoxLayout()
        self.layout_table.setObjectName(u"layout_table")

        self.verticalLayout.addLayout(self.layout_table)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u672c", None))
        self.create_btn.setText(QCoreApplication.translate("Form", u"\u521b\u5efa", None))
        self.remove_btn.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7f51\u5740", None))
        self.url.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
        self.remark.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165", None))
        self.query_btn.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.reset_query_btn.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
    # retranslateUi

