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
        AccountWindow.resize(682, 532)
        font = QFont()
        AccountWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        AccountWindow.setWindowIcon(icon)
        AccountWindow.setStyleSheet(u"")
        AccountWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(AccountWindow)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelHeading = QLabel(AccountWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"color: rgb(51, 51, 51);\n"
"background-color: rgb(255, 216, 252);")
        self.labelHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.labelMessage = QLabel(AccountWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(14)
        self.labelMessage.setFont(font2)
        self.labelMessage.setStyleSheet(u"color: rgb(102, 26, 216);")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.comboLayout = QHBoxLayout()
        self.comboLayout.setSpacing(10)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(25, 6, 25, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer)

        self.comboAccount = QComboBox(AccountWindow)
        self.comboAccount.setObjectName(u"comboAccount")
        self.comboAccount.setMinimumSize(QSize(0, 40))
        self.comboAccount.setFont(font2)
        self.comboAccount.setStyleSheet(u"background-color: rgb(200, 255, 211);\n"
"color: rgb(51, 51, 51);")

        self.comboLayout.addWidget(self.comboAccount)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.comboLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(25, 6, 25, 6)
        self.labelAccountNumber = QLabel(AccountWindow)
        self.labelAccountNumber.setObjectName(u"labelAccountNumber")
        self.labelAccountNumber.setMinimumSize(QSize(0, 40))
        self.labelAccountNumber.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelAccountNumber)

        self.editAccountNumber = QLineEdit(AccountWindow)
        self.editAccountNumber.setObjectName(u"editAccountNumber")
        self.editAccountNumber.setMinimumSize(QSize(0, 40))
        self.editAccountNumber.setFont(font2)
        self.editAccountNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.editAccountNumber.setInputMethodHints(Qt.ImhNone)
        self.editAccountNumber.setMaxLength(20)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editAccountNumber)

        self.labelCustomerName = QLabel(AccountWindow)
        self.labelCustomerName.setObjectName(u"labelCustomerName")
        self.labelCustomerName.setMinimumSize(QSize(0, 40))
        self.labelCustomerName.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelCustomerName)

        self.editCustomerName = QLineEdit(AccountWindow)
        self.editCustomerName.setObjectName(u"editCustomerName")
        self.editCustomerName.setMinimumSize(QSize(0, 40))
        self.editCustomerName.setFont(font2)
        self.editCustomerName.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.editCustomerName.setInputMethodHints(Qt.ImhNone)
        self.editCustomerName.setMaxLength(40)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editCustomerName)

        self.labelBankName = QLabel(AccountWindow)
        self.labelBankName.setObjectName(u"labelBankName")
        self.labelBankName.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelBankName)

        self.editBankName = QLineEdit(AccountWindow)
        self.editBankName.setObjectName(u"editBankName")
        self.editBankName.setMinimumSize(QSize(0, 40))
        self.editBankName.setFont(font2)
        self.editBankName.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.editBankName.setInputMethodHints(Qt.ImhNone)
        self.editBankName.setMaxLength(40)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editBankName)

        self.labelBranchName = QLabel(AccountWindow)
        self.labelBranchName.setObjectName(u"labelBranchName")
        self.labelBranchName.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelBranchName)

        self.editBranchName = QLineEdit(AccountWindow)
        self.editBranchName.setObjectName(u"editBranchName")
        self.editBranchName.setMinimumSize(QSize(0, 40))
        self.editBranchName.setFont(font2)
        self.editBranchName.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.editBranchName.setInputMethodHints(Qt.ImhNone)
        self.editBranchName.setMaxLength(40)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editBranchName)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(25, 6, 25, 6)
        self.buttonBack = QPushButton(AccountWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.buttonBack.setFont(font3)
        self.buttonBack.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(AccountWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(0, 40))
        self.buttonCancel.setFont(font3)
        self.buttonCancel.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(AccountWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(0, 40))
        self.buttonOk.setFont(font3)
        self.buttonOk.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

#if QT_CONFIG(shortcut)
        self.labelAccountNumber.setBuddy(self.editAccountNumber)
        self.labelCustomerName.setBuddy(self.editCustomerName)
        self.labelBankName.setBuddy(self.editBankName)
        self.labelBranchName.setBuddy(self.editBranchName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboAccount, self.editAccountNumber)
        QWidget.setTabOrder(self.editAccountNumber, self.editCustomerName)
        QWidget.setTabOrder(self.editCustomerName, self.editBankName)
        QWidget.setTabOrder(self.editBankName, self.editBranchName)
        QWidget.setTabOrder(self.editBranchName, self.buttonOk)
        QWidget.setTabOrder(self.buttonOk, self.buttonCancel)
        QWidget.setTabOrder(self.buttonCancel, self.buttonBack)

        self.retranslateUi(AccountWindow)
        self.buttonCancel.clicked.connect(AccountWindow.onCancelPressed)
        self.comboAccount.currentIndexChanged.connect(AccountWindow.onAccountChanged)
        self.buttonBack.clicked.connect(AccountWindow.close)
        self.editCustomerName.textEdited.connect(AccountWindow.onTextEdited)
        self.buttonOk.clicked.connect(AccountWindow.onOkPressed)
        self.editAccountNumber.textEdited.connect(AccountWindow.onTextEdited)
        self.editBankName.textEdited.connect(AccountWindow.onTextEdited)
        self.editBranchName.textEdited.connect(AccountWindow.onTextEdited)

        QMetaObject.connectSlotsByName(AccountWindow)
    # setupUi

    def retranslateUi(self, AccountWindow):
        AccountWindow.setWindowTitle(QCoreApplication.translate("AccountWindow", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("AccountWindow", u"<h2>Bank Account\n"
"", None))
        self.labelMessage.setText(QCoreApplication.translate("AccountWindow", u"TextLabel", None))
        self.comboAccount.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Select bank account number", None))
        self.labelAccountNumber.setText(QCoreApplication.translate("AccountWindow", u"Accoun&t Number", None))
        self.editAccountNumber.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter account number", None))
        self.labelCustomerName.setText(QCoreApplication.translate("AccountWindow", u"Custome&r Name", None))
        self.editCustomerName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter customer name", None))
        self.labelBankName.setText(QCoreApplication.translate("AccountWindow", u"Ban&k Name", None))
        self.editBankName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter bank name", None))
        self.labelBranchName.setText(QCoreApplication.translate("AccountWindow", u"Branc&h Name", None))
        self.editBranchName.setPlaceholderText(QCoreApplication.translate("AccountWindow", u"Enter branch name", None))
        self.buttonBack.setText(QCoreApplication.translate("AccountWindow", u"&Back", None))
        self.buttonCancel.setText(QCoreApplication.translate("AccountWindow", u"&Cancel", None))
        self.buttonOk.setText(QCoreApplication.translate("AccountWindow", u"&Ok", None))
    # retranslateUi

