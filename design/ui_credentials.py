# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credentials.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_CredentialsWindow(object):
    def setupUi(self, CredentialsWindow):
        if not CredentialsWindow.objectName():
            CredentialsWindow.setObjectName(u"CredentialsWindow")
        CredentialsWindow.setWindowModality(Qt.ApplicationModal)
        CredentialsWindow.resize(800, 365)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CredentialsWindow.sizePolicy().hasHeightForWidth())
        CredentialsWindow.setSizePolicy(sizePolicy)
        CredentialsWindow.setMinimumSize(QSize(0, 0))
        CredentialsWindow.setMaximumSize(QSize(800, 500))
        font = QFont()
        CredentialsWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        CredentialsWindow.setWindowIcon(icon)
        CredentialsWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(CredentialsWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(CredentialsWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 40))
        self.labelMessage.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.labelMessage.setFont(font1)
        self.labelMessage.setStyleSheet(u"color: rgb(241, 42, 42);\n"
"background-color: rgb(245, 245, 245);")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(CredentialsWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 40))
        self.labelHeading.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setUnderline(False)
        self.labelHeading.setFont(font2)
        self.labelHeading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 112);")
        self.labelHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(50, 20, 50, 30)
        self.labelCurrentPassword = QLabel(CredentialsWindow)
        self.labelCurrentPassword.setObjectName(u"labelCurrentPassword")
        self.labelCurrentPassword.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.labelCurrentPassword.setFont(font3)
        self.labelCurrentPassword.setStyleSheet(u"color: rgb(32, 74, 135);")
        self.labelCurrentPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelCurrentPassword)

        self.editCurrentPassword = QLineEdit(CredentialsWindow)
        self.editCurrentPassword.setObjectName(u"editCurrentPassword")
        self.editCurrentPassword.setMinimumSize(QSize(0, 40))
        self.editCurrentPassword.setFont(font)
        self.editCurrentPassword.setStyleSheet(u"background-color: rgb(245,245,245);\n"
"")
        self.editCurrentPassword.setMaxLength(12)
        self.editCurrentPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editCurrentPassword)

        self.labelNewPassword = QLabel(CredentialsWindow)
        self.labelNewPassword.setObjectName(u"labelNewPassword")
        self.labelNewPassword.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setUnderline(False)
        self.labelNewPassword.setFont(font4)
        self.labelNewPassword.setStyleSheet(u"color: rgb(32, 74, 135);")
        self.labelNewPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNewPassword)

        self.editNewPassword = QLineEdit(CredentialsWindow)
        self.editNewPassword.setObjectName(u"editNewPassword")
        self.editNewPassword.setMinimumSize(QSize(0, 40))
        self.editNewPassword.setFont(font)
        self.editNewPassword.setStyleSheet(u"background-color: rgb(245,245,245);\n"
"")
        self.editNewPassword.setMaxLength(12)
        self.editNewPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editNewPassword)

        self.labelConfirmPassword = QLabel(CredentialsWindow)
        self.labelConfirmPassword.setObjectName(u"labelConfirmPassword")
        self.labelConfirmPassword.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(12)
        self.labelConfirmPassword.setFont(font5)
        self.labelConfirmPassword.setStyleSheet(u"color: rgb(32, 74, 135);")
        self.labelConfirmPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelConfirmPassword)

        self.editConfirmPassword = QLineEdit(CredentialsWindow)
        self.editConfirmPassword.setObjectName(u"editConfirmPassword")
        self.editConfirmPassword.setMinimumSize(QSize(0, 40))
        self.editConfirmPassword.setFont(font)
        self.editConfirmPassword.setStyleSheet(u"background-color: rgb(245,245,245);\n"
"")
        self.editConfirmPassword.setMaxLength(12)
        self.editConfirmPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editConfirmPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 20, 50, 25)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(CredentialsWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBack.sizePolicy().hasHeightForWidth())
        self.buttonBack.setSizePolicy(sizePolicy1)
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        self.buttonBack.setFont(font5)
        self.buttonBack.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../src/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonBack)

        self.buttonSubmit = QPushButton(CredentialsWindow)
        self.buttonSubmit.setObjectName(u"buttonSubmit")
        self.buttonSubmit.setEnabled(False)
        self.buttonSubmit.setMinimumSize(QSize(100, 30))
        self.buttonSubmit.setMaximumSize(QSize(100, 30))
        self.buttonSubmit.setFont(font)
        self.buttonSubmit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../src/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSubmit.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttonSubmit)


        self.verticalLayout.addLayout(self.horizontalLayout)

#if QT_CONFIG(shortcut)
        self.labelCurrentPassword.setBuddy(self.editCurrentPassword)
        self.labelNewPassword.setBuddy(self.editNewPassword)
        self.labelConfirmPassword.setBuddy(self.editConfirmPassword)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(CredentialsWindow)
        self.editCurrentPassword.textChanged.connect(CredentialsWindow.onTextChange)
        self.editNewPassword.textChanged.connect(CredentialsWindow.onTextChange)
        self.buttonBack.clicked.connect(CredentialsWindow.close)
        self.buttonSubmit.clicked.connect(CredentialsWindow.onSubmit)
        self.editConfirmPassword.textChanged.connect(CredentialsWindow.onTextChange)

        self.buttonSubmit.setDefault(True)


        QMetaObject.connectSlotsByName(CredentialsWindow)
    # setupUi

    def retranslateUi(self, CredentialsWindow):
        CredentialsWindow.setWindowTitle(QCoreApplication.translate("CredentialsWindow", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("CredentialsWindow", u"text", None))
        self.labelHeading.setText(QCoreApplication.translate("CredentialsWindow", u"Change Password", None))
        self.labelCurrentPassword.setText(QCoreApplication.translate("CredentialsWindow", u"<html><head/><body><p><span style=\" color:#3465a4;\">Password</span><span style=\" color:#ef2929;\">*</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.editCurrentPassword.setStatusTip(QCoreApplication.translate("CredentialsWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editCurrentPassword.setText("")
        self.editCurrentPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Enter current pssword", None))
        self.labelNewPassword.setText(QCoreApplication.translate("CredentialsWindow", u"<html><head/><body><p><span style=\" color:#3465a4;\">New Password</span><span style=\" color:#ef2929;\">*</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.editNewPassword.setStatusTip(QCoreApplication.translate("CredentialsWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editNewPassword.setInputMask("")
        self.editNewPassword.setText("")
        self.editNewPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Create new pssword", None))
        self.labelConfirmPassword.setText(QCoreApplication.translate("CredentialsWindow", u"<html><head/><body><p><span style=\" color:#3465a4;\">Confirm Password</span><span style=\" color:#ef2929;\">*</span></p></body></html>", None))
        self.editConfirmPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Confirm new password", None))
        self.buttonBack.setText(QCoreApplication.translate("CredentialsWindow", u"&BACK", None))
        self.buttonSubmit.setText(QCoreApplication.translate("CredentialsWindow", u"&SUBMIT", None))
    # retranslateUi

