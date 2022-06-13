

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
## Form generated from reading UI file 'account.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from src import resource

class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        if not AccountWindow.objectName():
            AccountWindow.setObjectName(u"AccountWindow")
        AccountWindow.setWindowModality(Qt.ApplicationModal)
        AccountWindow.resize(654, 573)
        font = QFont()
        AccountWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        AccountWindow.setWindowIcon(icon)
        AccountWindow.setStyleSheet(u"*{\n"
"    		 background-color :#10141b;\n"
"		color: rgb(0, 145, 145);\n"
"		font-size: 16px;\n"
"}\n"
"\n"
"QLabel{\n"
"		color:rgba(255, 255, 255, .60);\n"
"}\n"
"\n"
"QLineEdit{\n"
"            background-color :#1f232a;\n"
"        }\n"
"\n"
"QComboBox{\n"
"		background-color :#1f232a;\n"
"		selection-color: rgb(255, 255, 255);\n"
"		selection-background-color: rgb(32, 74, 135);\n"
"}\n"
"\n"
"QLineEdit::disabled,\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #10141b;\n"
" }\n"
"\n"
"#comboAccount{\n"
"		border: 1px solid #264BF6;\n"
"}\n"
"\n"
"#labelMessage{\n"
"	color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"QPushButton{\n"
" 	color:rgba(0, 255, 0, .50);\n"
"    width: 100px;\n"
"	height: 20px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 1px solid #264BF6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, 255, .30);\n"
"     color: rgba(255, 255, 255, .50);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	background-color: rgba(0, 0, 0, .50);\n"
""
                        "     color: rgba(255, 255, 255, .50);\n"
"}\n"
" \n"
"       \n"
"\n"
"        \n"
"\n"
"\n"
"\n"
"")
        AccountWindow.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(AccountWindow)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(AccountWindow)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setFont(font)
        self.frameHeader.setFrameShape(QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameHeader)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(self.frameHeader)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 0))
        self.labelMessage.setMaximumSize(QSize(16777215, 16777215))
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(self.frameHeader)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 0))
        self.labelHeading.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frameHeader)

        self.frameCombo = QFrame(AccountWindow)
        self.frameCombo.setObjectName(u"frameCombo")
        self.frameCombo.setFont(font)
        self.comboLayout = QHBoxLayout(self.frameCombo)
        self.comboLayout.setSpacing(0)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(100, 0, 100, 0)
        self.comboAccount = QComboBox(self.frameCombo)
        self.comboAccount.setObjectName(u"comboAccount")
        self.comboAccount.setEnabled(True)
        self.comboAccount.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(True)
        self.comboAccount.setFont(font2)
        self.comboAccount.setCursor(QCursor(Qt.ArrowCursor))
        self.comboAccount.setAcceptDrops(False)
        self.comboAccount.setStyleSheet(u"")
        self.comboAccount.setMaxVisibleItems(5000)
        self.comboAccount.setFrame(True)

        self.comboLayout.addWidget(self.comboAccount)


        self.verticalLayout_2.addWidget(self.frameCombo)

        self.frameBody = QFrame(AccountWindow)
        self.frameBody.setObjectName(u"frameBody")
        self.frameBody.setFont(font)
        self.formLayout = QFormLayout(self.frameBody)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(25, 20, 25, 0)
        self.labelAccountNumber = QLabel(self.frameBody)
        self.labelAccountNumber.setObjectName(u"labelAccountNumber")
        self.labelAccountNumber.setMinimumSize(QSize(0, 40))
        self.labelAccountNumber.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelAccountNumber)

        self.editAccountNumber = QLineEdit(self.frameBody)
        self.editAccountNumber.setObjectName(u"editAccountNumber")
        self.editAccountNumber.setEnabled(True)
        self.editAccountNumber.setMinimumSize(QSize(0, 40))
        self.editAccountNumber.setFont(font)
        self.editAccountNumber.setStyleSheet(u"")
        self.editAccountNumber.setInputMethodHints(Qt.ImhNone)
        self.editAccountNumber.setMaxLength(25)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editAccountNumber)

        self.labelCustomerName = QLabel(self.frameBody)
        self.labelCustomerName.setObjectName(u"labelCustomerName")
        self.labelCustomerName.setMinimumSize(QSize(0, 40))
        self.labelCustomerName.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelCustomerName)

        self.editCustomerName = QLineEdit(self.frameBody)
        self.editCustomerName.setObjectName(u"editCustomerName")
        self.editCustomerName.setMinimumSize(QSize(0, 40))
        self.editCustomerName.setFont(font)
        self.editCustomerName.setStyleSheet(u"")
        self.editCustomerName.setInputMethodHints(Qt.ImhNone)
        self.editCustomerName.setMaxLength(40)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editCustomerName)

        self.labelBankName = QLabel(self.frameBody)
        self.labelBankName.setObjectName(u"labelBankName")
        self.labelBankName.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelBankName)

        self.comboBankName = QComboBox(self.frameBody)
        self.comboBankName.setObjectName(u"comboBankName")
        self.comboBankName.setMinimumSize(QSize(0, 40))
        self.comboBankName.setFont(font)
        self.comboBankName.setStyleSheet(u"")
        self.comboBankName.setModelColumn(0)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBankName)

        self.labelBranchName = QLabel(self.frameBody)
        self.labelBranchName.setObjectName(u"labelBranchName")
        self.labelBranchName.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelBranchName)

        self.editBranchName = QLineEdit(self.frameBody)
        self.editBranchName.setObjectName(u"editBranchName")
        self.editBranchName.setMinimumSize(QSize(0, 40))
        self.editBranchName.setFont(font)
        self.editBranchName.setStyleSheet(u"")
        self.editBranchName.setInputMethodHints(Qt.ImhNone)
        self.editBranchName.setMaxLength(40)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.editBranchName)

        self.labelOpeningBalance = QLabel(self.frameBody)
        self.labelOpeningBalance.setObjectName(u"labelOpeningBalance")
        self.labelOpeningBalance.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelOpeningBalance)

        self.editBalance = QLineEdit(self.frameBody)
        self.editBalance.setObjectName(u"editBalance")
        self.editBalance.setMinimumSize(QSize(0, 40))
        self.editBalance.setFont(font)
        self.editBalance.setStyleSheet(u"")
        self.editBalance.setMaxLength(8)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.editBalance)


        self.verticalLayout_2.addWidget(self.frameBody)

        self.framefooter = QFrame(AccountWindow)
        self.framefooter.setObjectName(u"framefooter")
        self.framefooter.setFont(font)
        self.buttonLayout = QHBoxLayout(self.framefooter)
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 50, 25, 25)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_3)

        self.buttonBack = QPushButton(self.framefooter)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(0, 0))
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBack.setFont(font)
        self.buttonBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)
        self.buttonBack.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(self.framefooter)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(0, 0))
        self.buttonCancel.setMaximumSize(QSize(16777215, 16777215))
        self.buttonCancel.setFont(font)
        self.buttonCancel.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)
        self.buttonCancel.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(self.framefooter)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(0, 0))
        self.buttonOk.setMaximumSize(QSize(16777215, 16777215))
        self.buttonOk.setFont(font)
        self.buttonOk.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)
        self.buttonOk.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout_2.addWidget(self.framefooter)

#if QT_CONFIG(shortcut)
        self.labelAccountNumber.setBuddy(self.editAccountNumber)
        self.labelCustomerName.setBuddy(self.editCustomerName)
        self.labelBankName.setBuddy(self.comboBankName)
        self.labelBranchName.setBuddy(self.editBranchName)
        self.labelOpeningBalance.setBuddy(self.editBalance)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboAccount, self.editAccountNumber)
        QWidget.setTabOrder(self.editAccountNumber, self.editCustomerName)
        QWidget.setTabOrder(self.editCustomerName, self.comboBankName)
        QWidget.setTabOrder(self.comboBankName, self.editBranchName)

        self.retranslateUi(AccountWindow)
        self.buttonOk.clicked.connect(AccountWindow.onOkPressed)
        self.buttonBack.clicked.connect(AccountWindow.close)
        self.buttonCancel.clicked.connect(AccountWindow.onCancelPressed)
        self.comboAccount.currentIndexChanged.connect(AccountWindow.onAccountChanged)
        self.comboBankName.currentIndexChanged.connect(AccountWindow.onBankNameChanged)
        self.editAccountNumber.textEdited.connect(AccountWindow.onTextEdited)
        self.editCustomerName.textEdited.connect(AccountWindow.onTextEdited)
        self.editBranchName.textEdited.connect(AccountWindow.onTextEdited)
        self.editBalance.textEdited.connect(AccountWindow.onTextEdited)

        self.buttonBack.setDefault(False)
        self.buttonCancel.setDefault(False)
        self.buttonOk.setDefault(True)


        QMetaObject.connectSlotsByName(AccountWindow)
    # setupUi

    def retranslateUi(self, AccountWindow):
        AccountWindow.setWindowTitle(QCoreApplication.translate("AccountWindow", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("AccountWindow", u"TextLabel", None))
        self.labelHeading.setText(QCoreApplication.translate("AccountWindow", u"BANK ACCOUNT", None))
        self.comboAccount.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Select bank account number", None))
        self.labelAccountNumber.setText(QCoreApplication.translate("AccountWindow", u"Accoun&t Number", None))
        self.editAccountNumber.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter account number", None))
        self.labelCustomerName.setText(QCoreApplication.translate("AccountWindow", u"Custome&r Name", None))
        self.editCustomerName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter customer name", None))
        self.labelBankName.setText(QCoreApplication.translate("AccountWindow", u"Ban&k Name", None))
        self.comboBankName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Select Bank Name", None))
        self.labelBranchName.setText(QCoreApplication.translate("AccountWindow", u"Branc&h Name", None))
        self.editBranchName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter branch name", None))
        self.labelOpeningBalance.setText(QCoreApplication.translate("AccountWindow", u"Openin&g Balance", None))
        self.editBalance.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter opening balance", None))
        self.buttonBack.setText(QCoreApplication.translate("AccountWindow", u"&BACK", None))
        self.buttonCancel.setText(QCoreApplication.translate("AccountWindow", u"&CANCEL", None))
        self.buttonOk.setText(QCoreApplication.translate("AccountWindow", u"&OK", None))
    # retranslateUi

