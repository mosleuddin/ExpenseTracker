
"""
    Copyright © 2021-2022  Mosleuddin Sarkar

    This file is part of ExpenseTracker.

    ExpenseTracker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ExpenseTracker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ExpenseTracker.  If not, see <https://www.gnu.org/licenses/>.
"""


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_users.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from src import resource

class Ui_ShowUsers(object):
    def setupUi(self, ShowUsers):
        if not ShowUsers.objectName():
            ShowUsers.setObjectName(u"ShowUsers")
        ShowUsers.setWindowModality(Qt.WindowModal)
        ShowUsers.resize(716, 500)
        ShowUsers.setMinimumSize(QSize(700, 500))
        font = QFont()
        ShowUsers.setFont(font)
        ShowUsers.setStyleSheet(u"\n"
"*{\n"
"  background-color :#10141b;\n"
"  color:rgba(255, 255, 255, .75);\n"
"  border: none;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QLabel{\n"
"  color:rgba(255, 255, 255, .5);\n"
"}\n"
"\n"
"\n"
"#tableBalance\n"
"{\n"
"  background-color: #1f232a;\n"
"  color:rgba(255, 255, 255, .5);\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 1px solid #264BF6;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, 255, .30);\n"
"}\n"
"\n"
"")
        ShowUsers.setModal(True)
        self.verticalLayout = QVBoxLayout(ShowUsers)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.labelHeading = QLabel(ShowUsers)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setBold(True)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.tableWidget = QTableWidget(ShowUsers)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(500, 300))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 30, -1, -1)
        self.buttonBack = QPushButton(ShowUsers)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(0, 0))
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBack.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ShowUsers)
        self.buttonBack.clicked.connect(ShowUsers.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ShowUsers)
    # setupUi

    def retranslateUi(self, ShowUsers):
        ShowUsers.setWindowTitle(QCoreApplication.translate("ShowUsers", u"Reset Credentials", None))
        self.labelHeading.setText(QCoreApplication.translate("ShowUsers", u"List of users", None))
        self.buttonBack.setText(QCoreApplication.translate("ShowUsers", u"&Back", None))
    # retranslateUi

