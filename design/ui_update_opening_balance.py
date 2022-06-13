
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
## Form generated from reading UI file 'update_opening_balance.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from src import resource

class Ui_UpdateOpeningBalance(object):
    def setupUi(self, UpdateOpeningBalance):
        if not UpdateOpeningBalance.objectName():
            UpdateOpeningBalance.setObjectName(u"UpdateOpeningBalance")
        UpdateOpeningBalance.setWindowModality(Qt.ApplicationModal)
        UpdateOpeningBalance.resize(654, 573)
        font = QFont()
        UpdateOpeningBalance.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        UpdateOpeningBalance.setWindowIcon(icon)
        UpdateOpeningBalance.setStyleSheet(u"*{\n"
"	    background-color :#10141b;\n"
"	    border: none;\n"
"         font-size: 16px;\n"
"	     color:rgba(255, 255, 255, .50);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgba(0, 255, 0, .50);\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	width: 200px;\n"
"	height: 30px;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"QLineEdit::enabled{\n"
"    background-color: #1f232a;\n"
"	color: rgba(255, 255, 255, .75);\n"
"	border: 1px solid #264BF6;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#10141b;\n"
" 	color:rgba(0, 255, 0, .50);\n"
"    width: 120px;\n"
"	height: 20px;\n"
"	padding: 5px, 10px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	background-color : rgb(0, 0, 0); \n"
"	color : rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, 255, .30);\n"
"     color: rgba(255, 255, 255, .50);\n"
"}")
        UpdateOpeningBalance.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(UpdateOpeningBalance)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 30)
        self.frameBody = QFrame(UpdateOpeningBalance)
        self.frameBody.setObjectName(u"frameBody")
        self.gridLayout = QGridLayout(self.frameBody)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelBankName = QLabel(self.frameBody)
        self.labelBankName.setObjectName(u"labelBankName")
        self.labelBankName.setFont(font)

        self.gridLayout.addWidget(self.labelBankName, 2, 0, 1, 1)

        self.editBankName = QLineEdit(self.frameBody)
        self.editBankName.setObjectName(u"editBankName")
        self.editBankName.setEnabled(False)
        self.editBankName.setMinimumSize(QSize(0, 40))
        self.editBankName.setFont(font)
        self.editBankName.setStyleSheet(u"")
        self.editBankName.setInputMethodHints(Qt.ImhNone)
        self.editBankName.setMaxLength(40)
        self.editBankName.setReadOnly(True)

        self.gridLayout.addWidget(self.editBankName, 2, 1, 1, 1)

        self.labelOpeningBalance = QLabel(self.frameBody)
        self.labelOpeningBalance.setObjectName(u"labelOpeningBalance")
        self.labelOpeningBalance.setFont(font)

        self.gridLayout.addWidget(self.labelOpeningBalance, 4, 0, 1, 1)

        self.editBranchName = QLineEdit(self.frameBody)
        self.editBranchName.setObjectName(u"editBranchName")
        self.editBranchName.setEnabled(False)
        self.editBranchName.setMinimumSize(QSize(0, 40))
        self.editBranchName.setFont(font)
        self.editBranchName.setStyleSheet(u"")
        self.editBranchName.setInputMethodHints(Qt.ImhNone)
        self.editBranchName.setMaxLength(40)
        self.editBranchName.setReadOnly(True)

        self.gridLayout.addWidget(self.editBranchName, 3, 1, 1, 1)

        self.editCustomerName = QLineEdit(self.frameBody)
        self.editCustomerName.setObjectName(u"editCustomerName")
        self.editCustomerName.setEnabled(False)
        self.editCustomerName.setMinimumSize(QSize(0, 40))
        self.editCustomerName.setFont(font)
        self.editCustomerName.setStyleSheet(u"")
        self.editCustomerName.setInputMethodHints(Qt.ImhNone)
        self.editCustomerName.setMaxLength(40)
        self.editCustomerName.setReadOnly(True)

        self.gridLayout.addWidget(self.editCustomerName, 1, 1, 1, 1)

        self.labelCustomerName = QLabel(self.frameBody)
        self.labelCustomerName.setObjectName(u"labelCustomerName")
        self.labelCustomerName.setMinimumSize(QSize(0, 40))
        self.labelCustomerName.setFont(font)

        self.gridLayout.addWidget(self.labelCustomerName, 1, 0, 1, 1)

        self.editBalance = QLineEdit(self.frameBody)
        self.editBalance.setObjectName(u"editBalance")
        self.editBalance.setMinimumSize(QSize(0, 40))
        self.editBalance.setFont(font)
        self.editBalance.setStyleSheet(u"")
        self.editBalance.setMaxLength(8)

        self.gridLayout.addWidget(self.editBalance, 4, 1, 1, 1)

        self.labelAccountNumber = QLabel(self.frameBody)
        self.labelAccountNumber.setObjectName(u"labelAccountNumber")
        self.labelAccountNumber.setMinimumSize(QSize(0, 40))
        self.labelAccountNumber.setFont(font)

        self.gridLayout.addWidget(self.labelAccountNumber, 0, 0, 1, 1)

        self.labelBranchName = QLabel(self.frameBody)
        self.labelBranchName.setObjectName(u"labelBranchName")
        self.labelBranchName.setFont(font)

        self.gridLayout.addWidget(self.labelBranchName, 3, 0, 1, 1)

        self.editAccountNumber = QLineEdit(self.frameBody)
        self.editAccountNumber.setObjectName(u"editAccountNumber")
        self.editAccountNumber.setEnabled(False)
        self.editAccountNumber.setMinimumSize(QSize(0, 40))
        self.editAccountNumber.setFont(font)
        self.editAccountNumber.setStyleSheet(u"")
        self.editAccountNumber.setInputMethodHints(Qt.ImhNone)
        self.editAccountNumber.setMaxLength(25)
        self.editAccountNumber.setReadOnly(True)

        self.gridLayout.addWidget(self.editAccountNumber, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frameBody)

        self.frameFooter = QFrame(UpdateOpeningBalance)
        self.frameFooter.setObjectName(u"frameFooter")
        self.buttonLayout = QHBoxLayout(self.frameFooter)
        self.buttonLayout.setSpacing(6)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_3)

        self.buttonBack = QPushButton(self.frameFooter)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(False)
        self.buttonBack.setFont(font1)
        self.buttonBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)
        self.buttonBack.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonOk = QPushButton(self.frameFooter)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(100, 30))
        self.buttonOk.setMaximumSize(QSize(16777215, 16777215))
        self.buttonOk.setFont(font1)
        self.buttonOk.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon2)
        self.buttonOk.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout_2.addWidget(self.frameFooter)

#if QT_CONFIG(shortcut)
        self.labelOpeningBalance.setBuddy(self.editBalance)
        self.labelCustomerName.setBuddy(self.editCustomerName)
        self.labelAccountNumber.setBuddy(self.editAccountNumber)
        self.labelBranchName.setBuddy(self.editBranchName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.editAccountNumber, self.editCustomerName)
        QWidget.setTabOrder(self.editCustomerName, self.editBranchName)

        self.retranslateUi(UpdateOpeningBalance)
        self.buttonOk.clicked.connect(UpdateOpeningBalance.onOkPressed)
        self.buttonBack.clicked.connect(UpdateOpeningBalance.close)
        self.editBalance.textEdited.connect(UpdateOpeningBalance.onTextEdited)

        self.buttonBack.setDefault(False)
        self.buttonOk.setDefault(True)


        QMetaObject.connectSlotsByName(UpdateOpeningBalance)
    # setupUi

    def retranslateUi(self, UpdateOpeningBalance):
        UpdateOpeningBalance.setWindowTitle(QCoreApplication.translate("UpdateOpeningBalance", u"Expense Tracker", None))
        self.labelBankName.setText(QCoreApplication.translate("UpdateOpeningBalance", u"Bank Name", None))
        self.editBankName.setPlaceholderText("")
        self.labelOpeningBalance.setText(QCoreApplication.translate("UpdateOpeningBalance", u"Opening Balance", None))
        self.editBranchName.setPlaceholderText("")
        self.editCustomerName.setPlaceholderText("")
        self.labelCustomerName.setText(QCoreApplication.translate("UpdateOpeningBalance", u"Customer Name", None))
        self.editBalance.setPlaceholderText("")
        self.labelAccountNumber.setText(QCoreApplication.translate("UpdateOpeningBalance", u"Account Number", None))
        self.labelBranchName.setText(QCoreApplication.translate("UpdateOpeningBalance", u"Branch Name", None))
        self.editAccountNumber.setPlaceholderText("")
        self.buttonBack.setText(QCoreApplication.translate("UpdateOpeningBalance", u"&BACK", None))
        self.buttonOk.setText(QCoreApplication.translate("UpdateOpeningBalance", u"&OK", None))
    # retranslateUi

