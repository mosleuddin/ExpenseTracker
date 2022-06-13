
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
## Form generated from reading UI file 'head_view.ui'
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
    QSizePolicy, QTableView, QVBoxLayout, QWidget)
from src import resource

class Ui_ViewHead(object):
    def setupUi(self, ViewHead):
        if not ViewHead.objectName():
            ViewHead.setObjectName(u"ViewHead")
        ViewHead.setWindowModality(Qt.WindowModal)
        ViewHead.resize(693, 480)
        font = QFont()
        ViewHead.setFont(font)
        ViewHead.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"	color:rgba(255, 255, 255, .60);\n"
"  	border: none;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#labelHeading{\n"
"	color:rgba(20, 145, 145, 1);\n"
"    background-color: rgba(238, 226,15, .20);\n"
"}\n"
"\n"
"\n"
"#tableView{\n"
"	background-color: #1f232a;\n"
"	color: rgb(20, 145, 145);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#1f232a;\n"
" 	color:rgba(0, 255, 0, .60);\n"
"    width: 80px;\n"
"	height: 18px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 1px solid #264BF6;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, 255, .30);\n"
"}\n"
"\n"
"")
        ViewHead.setModal(True)
        self.verticalLayout = QVBoxLayout(ViewHead)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.heading_layout = QHBoxLayout()
        self.heading_layout.setSpacing(0)
        self.heading_layout.setObjectName(u"heading_layout")
        self.labelHeading = QLabel(ViewHead)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setBold(True)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.heading_layout.addWidget(self.labelHeading)


        self.verticalLayout.addLayout(self.heading_layout)

        self.table_layout = QHBoxLayout()
        self.table_layout.setSpacing(0)
        self.table_layout.setObjectName(u"table_layout")
        self.table_layout.setContentsMargins(50, 25, 50, 25)
        self.tableView = QTableView(ViewHead)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font)
        self.tableView.setStyleSheet(u"")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setStretchLastSection(False)

        self.table_layout.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.table_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(0)
        self.button_layout.setObjectName(u"button_layout")
        self.button_layout.setContentsMargins(0, 0, 0, 25)
        self.buttonBack = QPushButton(ViewHead)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        self.buttonBack.setFont(font1)
        self.buttonBack.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.button_layout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.button_layout)


        self.retranslateUi(ViewHead)
        self.buttonBack.clicked.connect(ViewHead.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ViewHead)
    # setupUi

    def retranslateUi(self, ViewHead):
        ViewHead.setWindowTitle(QCoreApplication.translate("ViewHead", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("ViewHead", u"Expenditure Head", None))
        self.buttonBack.setText(QCoreApplication.translate("ViewHead", u"&Back", None))
    # retranslateUi

