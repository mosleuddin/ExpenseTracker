# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setWindowModality(Qt.ApplicationModal)
        LoginWindow.resize(690, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QSize(0, 0))
        LoginWindow.setMaximumSize(QSize(800, 600))
        font = QFont()
        LoginWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"background-color: rgb(255, 255,255);")
        self.verticalLayout = QVBoxLayout(LoginWindow)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelHeading = QLabel(LoginWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"color: rgb(51, 51, 51);\n"
"background-color: rgb(201, 219, 220);")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)
        self.labelHeading.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.labelHeading)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.labelMessage = QLabel(LoginWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.labelMessage.setFont(font2)
        self.labelMessage.setStyleSheet(u"color: rgb(241, 42, 42);")
        self.labelMessage.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelMessage)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.labelUsername = QLabel(LoginWindow)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setBold(False)
        self.labelUsername.setFont(font3)
        self.labelUsername.setStyleSheet(u"color: rgb(32, 74, 135);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelUsername)

        self.editUsername = QLineEdit(LoginWindow)
        self.editUsername.setObjectName(u"editUsername")
        self.editUsername.setMinimumSize(QSize(0, 40))
        self.editUsername.setFont(font)
        self.editUsername.setStyleSheet(u"background-color: rgb(254, 255, 211);\n"
"color: rgb(51, 51, 51);")
        self.editUsername.setMaxLength(12)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editUsername)

        self.labelPassword = QLabel(LoginWindow)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setBold(False)
        font4.setUnderline(False)
        self.labelPassword.setFont(font4)
        self.labelPassword.setStyleSheet(u"color: rgb(32, 74, 135);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPassword)

        self.editPassword = QLineEdit(LoginWindow)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setMinimumSize(QSize(0, 40))
        self.editPassword.setFont(font)
        self.editPassword.setStyleSheet(u"background-color: rgb(254, 255, 211);\n"
"color: rgb(51, 51, 51);")
        self.editPassword.setMaxLength(12)
        self.editPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, 50, 0)
        self.buttonCancel = QPushButton(LoginWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy1)
        self.buttonCancel.setMinimumSize(QSize(150, 40))
        self.buttonCancel.setFont(font)
        self.buttonCancel.setStyleSheet(u"background-color: rgb(10, 145, 145);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(LoginWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(150, 40))
        self.buttonOk.setFont(font)
        self.buttonOk.setStyleSheet(u"background-color: rgb(10, 145, 145);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttonOk)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelCopyright = QLabel(LoginWindow)
        self.labelCopyright.setObjectName(u"labelCopyright")
        self.labelCopyright.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(12)
        self.labelCopyright.setFont(font5)
        self.labelCopyright.setStyleSheet(u"color: rgb(51, 51, 51);\n"
"background-color: rgb(201, 219, 220);")
        self.labelCopyright.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelCopyright)


        self.retranslateUi(LoginWindow)
        self.editUsername.textChanged.connect(LoginWindow.onTextChange)
        self.editPassword.textChanged.connect(LoginWindow.onTextChange)
        self.buttonCancel.clicked.connect(LoginWindow.close)
        self.buttonOk.clicked.connect(LoginWindow.onLogin)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("LoginWindow", u"<h2> Login\n"
"", None))
        self.labelMessage.setText(QCoreApplication.translate("LoginWindow", u"Invalid username / password", None))
        self.labelUsername.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p>Username<span style=\" color:#ef2929;\">*</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.editUsername.setStatusTip(QCoreApplication.translate("LoginWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editUsername.setText("")
        self.editUsername.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter username", None))
        self.labelPassword.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p>Password<span style=\" color:#ef2929;\">*</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.editPassword.setStatusTip(QCoreApplication.translate("LoginWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editPassword.setInputMask("")
        self.editPassword.setText("")
        self.editPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter password", None))
        self.buttonCancel.setText(QCoreApplication.translate("LoginWindow", u"&Cancel", None))
        self.buttonOk.setText(QCoreApplication.translate("LoginWindow", u"&Ok", None))
        self.labelCopyright.setText(QCoreApplication.translate("LoginWindow", u"Copyright (c) 2021 Mosleuddin Sarkar", None))
    # retranslateUi

