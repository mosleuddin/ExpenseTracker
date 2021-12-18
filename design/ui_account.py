# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        if not AccountWindow.objectName():
            AccountWindow.setObjectName(u"AccountWindow")
        AccountWindow.setWindowModality(Qt.ApplicationModal)
        AccountWindow.resize(518, 438)
        font = QFont()
        AccountWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        AccountWindow.setWindowIcon(icon)
        AccountWindow.setStyleSheet(u"")
        AccountWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(AccountWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.labelMessage = QLabel(AccountWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 0))
        self.labelMessage.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(14)
        self.labelMessage.setFont(font1)
        self.labelMessage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 139, 139);\n"
"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(AccountWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 10))
        self.labelHeading.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(False)
        self.labelHeading.setFont(font2)
        self.labelHeading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 112);\n"
"")
        self.labelHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.comboLayout = QHBoxLayout()
        self.comboLayout.setSpacing(0)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(25, 6, 25, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer)

        self.comboAccount = QComboBox(AccountWindow)
        self.comboAccount.setObjectName(u"comboAccount")
        self.comboAccount.setMinimumSize(QSize(0, 40))
        self.comboAccount.setFont(font1)
        self.comboAccount.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"selection-background-color: rgb(64, 107, 191);\n"
"selection-color: rgb(255, 255, 255);\n"
"")

        self.comboLayout.addWidget(self.comboAccount)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.comboLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(25, 15, 25, 0)
        self.labelAccountNumber = QLabel(AccountWindow)
        self.labelAccountNumber.setObjectName(u"labelAccountNumber")
        self.labelAccountNumber.setMinimumSize(QSize(0, 40))
        self.labelAccountNumber.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelAccountNumber)

        self.editAccountNumber = QLineEdit(AccountWindow)
        self.editAccountNumber.setObjectName(u"editAccountNumber")
        self.editAccountNumber.setMinimumSize(QSize(0, 40))
        self.editAccountNumber.setFont(font1)
        self.editAccountNumber.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.editAccountNumber.setInputMethodHints(Qt.ImhNone)
        self.editAccountNumber.setMaxLength(20)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editAccountNumber)

        self.labelCustomerName = QLabel(AccountWindow)
        self.labelCustomerName.setObjectName(u"labelCustomerName")
        self.labelCustomerName.setMinimumSize(QSize(0, 40))
        self.labelCustomerName.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelCustomerName)

        self.editCustomerName = QLineEdit(AccountWindow)
        self.editCustomerName.setObjectName(u"editCustomerName")
        self.editCustomerName.setMinimumSize(QSize(0, 40))
        self.editCustomerName.setFont(font1)
        self.editCustomerName.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.editCustomerName.setInputMethodHints(Qt.ImhNone)
        self.editCustomerName.setMaxLength(40)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editCustomerName)

        self.labelBankName2 = QLabel(AccountWindow)
        self.labelBankName2.setObjectName(u"labelBankName2")
        self.labelBankName2.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelBankName2)

        self.comboBankName = QComboBox(AccountWindow)
        self.comboBankName.setObjectName(u"comboBankName")
        self.comboBankName.setMinimumSize(QSize(0, 40))
        self.comboBankName.setFont(font1)
        self.comboBankName.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"selection-background-color: rgb(64, 107, 191);\n"
"selection-color: rgb(255, 255, 255);\n"
"")
        self.comboBankName.setModelColumn(0)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBankName)

        self.labelBranchName = QLabel(AccountWindow)
        self.labelBranchName.setObjectName(u"labelBranchName")
        self.labelBranchName.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelBranchName)

        self.editBranchName = QLineEdit(AccountWindow)
        self.editBranchName.setObjectName(u"editBranchName")
        self.editBranchName.setMinimumSize(QSize(0, 40))
        self.editBranchName.setFont(font1)
        self.editBranchName.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.editBranchName.setInputMethodHints(Qt.ImhNone)
        self.editBranchName.setMaxLength(40)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.editBranchName)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 30, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_3)

        self.buttonBack = QPushButton(AccountWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.buttonBack.setFont(font3)
        self.buttonBack.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)
        self.buttonBack.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(AccountWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(100, 30))
        self.buttonCancel.setMaximumSize(QSize(100, 30))
        self.buttonCancel.setFont(font3)
        self.buttonCancel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)
        self.buttonCancel.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(AccountWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(100, 30))
        self.buttonOk.setMaximumSize(QSize(100, 30))
        self.buttonOk.setFont(font3)
        self.buttonOk.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)
        self.buttonOk.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonOk)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.buttonLayout)

        self.editBankName = QLineEdit(AccountWindow)
        self.editBankName.setObjectName(u"editBankName")
        self.editBankName.setMinimumSize(QSize(0, 40))
        self.editBankName.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editBankName)

        self.labelBankName1 = QLabel(AccountWindow)
        self.labelBankName1.setObjectName(u"labelBankName1")
        self.labelBankName1.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelBankName1)


        self.verticalLayout.addLayout(self.formLayout)

#if QT_CONFIG(shortcut)
        self.labelAccountNumber.setBuddy(self.editAccountNumber)
        self.labelCustomerName.setBuddy(self.editCustomerName)
        self.labelBankName2.setBuddy(self.comboBankName)
        self.labelBranchName.setBuddy(self.editBranchName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboAccount, self.editAccountNumber)
        QWidget.setTabOrder(self.editAccountNumber, self.editCustomerName)
        QWidget.setTabOrder(self.editCustomerName, self.comboBankName)
        QWidget.setTabOrder(self.comboBankName, self.editBranchName)
        QWidget.setTabOrder(self.editBranchName, self.buttonOk)
        QWidget.setTabOrder(self.buttonOk, self.buttonCancel)
        QWidget.setTabOrder(self.buttonCancel, self.buttonBack)

        self.retranslateUi(AccountWindow)
        self.buttonCancel.clicked.connect(AccountWindow.onCancelPressed)
        self.comboAccount.activated.connect(AccountWindow.onAccountChanged)
        self.buttonBack.clicked.connect(AccountWindow.close)
        self.editCustomerName.textEdited.connect(AccountWindow.onTextEdited)
        self.buttonOk.clicked.connect(AccountWindow.onOkPressed)
        self.editAccountNumber.textEdited.connect(AccountWindow.onTextEdited)
        self.editBranchName.textEdited.connect(AccountWindow.onTextEdited)
        self.comboBankName.activated.connect(AccountWindow.onBankNameChanged)

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
        self.labelBankName2.setText(QCoreApplication.translate("AccountWindow", u"Ban&k Name", None))
        self.comboBankName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Select Bank Name", None))
        self.labelBranchName.setText(QCoreApplication.translate("AccountWindow", u"Branc&h Name", None))
        self.editBranchName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter branch name", None))
        self.buttonBack.setText(QCoreApplication.translate("AccountWindow", u"&BACK", None))
        self.buttonCancel.setText(QCoreApplication.translate("AccountWindow", u"&CANCEL", None))
        self.buttonOk.setText(QCoreApplication.translate("AccountWindow", u"&OK", None))
        self.labelBankName1.setText(QCoreApplication.translate("AccountWindow", u"Bank Name", None))
    # retranslateUi

