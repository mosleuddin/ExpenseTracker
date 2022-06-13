
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
## Form generated from reading UI file 'trans_view.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
from src import resource

class Ui_TransactionView(object):
    def setupUi(self, TransactionView):
        if not TransactionView.objectName():
            TransactionView.setObjectName(u"TransactionView")
        TransactionView.setWindowModality(Qt.WindowModal)
        TransactionView.resize(677, 480)
        font = QFont()
        TransactionView.setFont(font)
        TransactionView.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"	color:rgb(0, 145, 145);\n"
"  	border: none;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#labelHeading{\n"
"    background-color: rgba(238, 226,15, .20);\n"
"}\n"
"\n"
"#tableView{\n"
"	background-color: #1f232a;\n"
"	color:rgba(255, 255, 255, .60);\n"
"}\n"
"\n"
"QLineEdit{\n"
"		background-color: #1f232a;\n"
"		color:rgba(255, 255, 255, .60);\n"
"		font-size: 20px;\n"
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
"")
        TransactionView.setModal(True)
        self.verticalLayout = QVBoxLayout(TransactionView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.heading_layout = QHBoxLayout()
        self.heading_layout.setSpacing(0)
        self.heading_layout.setObjectName(u"heading_layout")
        self.labelHeading = QLabel(TransactionView)
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
        self.table_layout.setContentsMargins(25, 25, 25, 25)
        self.tableView = QTableView(TransactionView)
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
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(50)
        self.tableView.horizontalHeader().setDefaultSectionSize(50)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setStretchLastSection(False)

        self.table_layout.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.table_layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(10)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(25, 0, 25, 25)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_layout.addItem(self.horizontalSpacer_2)

        self.labelReceiptTotal = QLabel(TransactionView)
        self.labelReceiptTotal.setObjectName(u"labelReceiptTotal")

        self.bottom_layout.addWidget(self.labelReceiptTotal)

        self.editReceiptTotal = QLineEdit(TransactionView)
        self.editReceiptTotal.setObjectName(u"editReceiptTotal")
        self.editReceiptTotal.setStyleSheet(u"")
        self.editReceiptTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editReceiptTotal.setReadOnly(True)

        self.bottom_layout.addWidget(self.editReceiptTotal)

        self.labelPaymentTotal = QLabel(TransactionView)
        self.labelPaymentTotal.setObjectName(u"labelPaymentTotal")

        self.bottom_layout.addWidget(self.labelPaymentTotal)

        self.editPaymentTotal = QLineEdit(TransactionView)
        self.editPaymentTotal.setObjectName(u"editPaymentTotal")
        self.editPaymentTotal.setStyleSheet(u"")
        self.editPaymentTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editPaymentTotal.setReadOnly(True)

        self.bottom_layout.addWidget(self.editPaymentTotal)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_layout.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(TransactionView)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        self.buttonBack.setFont(font)
        self.buttonBack.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.bottom_layout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.bottom_layout)


        self.retranslateUi(TransactionView)
        self.buttonBack.clicked.connect(TransactionView.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(TransactionView)
    # setupUi

    def retranslateUi(self, TransactionView):
        TransactionView.setWindowTitle(QCoreApplication.translate("TransactionView", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("TransactionView", u"Transaction", None))
        self.labelReceiptTotal.setText(QCoreApplication.translate("TransactionView", u"Receipt Contra Total", None))
        self.editReceiptTotal.setText(QCoreApplication.translate("TransactionView", u"0", None))
        self.labelPaymentTotal.setText(QCoreApplication.translate("TransactionView", u"Payment Contra Total", None))
        self.editPaymentTotal.setText(QCoreApplication.translate("TransactionView", u"0", None))
        self.buttonBack.setText(QCoreApplication.translate("TransactionView", u"&Back", None))
    # retranslateUi

