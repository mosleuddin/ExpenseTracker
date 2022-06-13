

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
## Form generated from reading UI file 'credentials.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
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
        CredentialsWindow.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"	color:rgba(255, 255, 255, .5);\n"
"	font-size: 16px;\n"
"\n"
"}\n"
"\n"
"#labelMessage{\n"
"	color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"\n"
"#labelHeading{\n"
"	color: rgba(.06, 140, 140, 1);\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"            background-color :#1f232a;\n"
"            color:rgba(0, 255, 255, .60);\n"
"            height: 30px;\n"
"        }\n"
"\n"
"QPushButton{\n"
"    background-color:#10141b;\n"
" 	color:rgba(0, 255, 0, .50);\n"
"    width: 75px;\n"
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
"     color: rgba(255, 255, 255, .50);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	background-color: rgba(0, 0, 0, .50);\n"
"     color: rgba(255, 255, 255, .50);\n"
"}\n"
" \n"
"        \n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(CredentialsWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(CredentialsWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 40))
        self.labelMessage.setMaximumSize(QSize(16777215, 40))
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(CredentialsWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 40))
        self.labelHeading.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setBold(False)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
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
        font2 = QFont()
        font2.setBold(False)
        self.labelCurrentPassword.setFont(font2)
        self.labelCurrentPassword.setStyleSheet(u"")
        self.labelCurrentPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelCurrentPassword)

        self.editCurrentPassword = QLineEdit(CredentialsWindow)
        self.editCurrentPassword.setObjectName(u"editCurrentPassword")
        self.editCurrentPassword.setMinimumSize(QSize(0, 40))
        self.editCurrentPassword.setFont(font)
        self.editCurrentPassword.setStyleSheet(u"")
        self.editCurrentPassword.setMaxLength(12)
        self.editCurrentPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editCurrentPassword)

        self.labelNewPassword = QLabel(CredentialsWindow)
        self.labelNewPassword.setObjectName(u"labelNewPassword")
        self.labelNewPassword.setMinimumSize(QSize(0, 40))
        self.labelNewPassword.setFont(font1)
        self.labelNewPassword.setStyleSheet(u"")
        self.labelNewPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNewPassword)

        self.editNewPassword = QLineEdit(CredentialsWindow)
        self.editNewPassword.setObjectName(u"editNewPassword")
        self.editNewPassword.setMinimumSize(QSize(0, 40))
        self.editNewPassword.setFont(font)
        self.editNewPassword.setStyleSheet(u"")
        self.editNewPassword.setMaxLength(12)
        self.editNewPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editNewPassword)

        self.labelConfirmPassword = QLabel(CredentialsWindow)
        self.labelConfirmPassword.setObjectName(u"labelConfirmPassword")
        self.labelConfirmPassword.setMinimumSize(QSize(0, 40))
        self.labelConfirmPassword.setFont(font)
        self.labelConfirmPassword.setStyleSheet(u"")
        self.labelConfirmPassword.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelConfirmPassword)

        self.editConfirmPassword = QLineEdit(CredentialsWindow)
        self.editConfirmPassword.setObjectName(u"editConfirmPassword")
        self.editConfirmPassword.setMinimumSize(QSize(0, 40))
        self.editConfirmPassword.setFont(font)
        self.editConfirmPassword.setStyleSheet(u"")
        self.editConfirmPassword.setMaxLength(12)
        self.editConfirmPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editConfirmPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
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
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBack.setFont(font)
        self.buttonBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../src/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonBack)

        self.buttonSubmit = QPushButton(CredentialsWindow)
        self.buttonSubmit.setObjectName(u"buttonSubmit")
        self.buttonSubmit.setEnabled(False)
        self.buttonSubmit.setMinimumSize(QSize(100, 30))
        self.buttonSubmit.setMaximumSize(QSize(16777215, 16777215))
        self.buttonSubmit.setFont(font)
        self.buttonSubmit.setStyleSheet(u"")
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
        self.labelCurrentPassword.setText(QCoreApplication.translate("CredentialsWindow", u"Password", None))
#if QT_CONFIG(statustip)
        self.editCurrentPassword.setStatusTip(QCoreApplication.translate("CredentialsWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editCurrentPassword.setText("")
        self.editCurrentPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Enter current pssword", None))
        self.labelNewPassword.setText(QCoreApplication.translate("CredentialsWindow", u"New Password", None))
#if QT_CONFIG(statustip)
        self.editNewPassword.setStatusTip(QCoreApplication.translate("CredentialsWindow", u"username should be 4 to 12 characters long", None))
#endif // QT_CONFIG(statustip)
        self.editNewPassword.setInputMask("")
        self.editNewPassword.setText("")
        self.editNewPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Create new pssword", None))
        self.labelConfirmPassword.setText(QCoreApplication.translate("CredentialsWindow", u"Confirm Password", None))
        self.editConfirmPassword.setPlaceholderText(QCoreApplication.translate("CredentialsWindow", u"Confirm new password", None))
        self.buttonBack.setText(QCoreApplication.translate("CredentialsWindow", u"&BACK", None))
        self.buttonSubmit.setText(QCoreApplication.translate("CredentialsWindow", u"&SUBMIT", None))
    # retranslateUi

