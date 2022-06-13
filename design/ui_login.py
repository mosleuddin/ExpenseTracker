

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
## Form generated from reading UI file 'login.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setWindowModality(Qt.ApplicationModal)
        LoginWindow.resize(800, 329)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QSize(0, 0))
        LoginWindow.setMaximumSize(QSize(800, 500))
        font = QFont()
        LoginWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"	color:rgba(255, 255, 255, .5);\n"
"	font-size: 16px;\n"
"\n"
"}\n"
"QLabel{\n"
"		color:rgba(255, 255, 255, .5);\n"
"     \n"
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
"\n"
"#labelCopyright{\n"
"	color:rgba(255, 255, 255, .75);\n"
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
"     color: rgba(255, "
                        "255, 255, .50);\n"
"}\n"
" \n"
" \n"
"        \n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(LoginWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(LoginWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setBold(False)
        self.labelMessage.setFont(font1)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(LoginWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setBold(False)
        font2.setUnderline(False)
        self.labelHeading.setFont(font2)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(4)
        self.labelHeading.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.labelHeading)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(50, 10, 50, 30)
        self.labelUsername = QLabel(LoginWindow)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setMinimumSize(QSize(0, 40))
        self.labelUsername.setFont(font1)
        self.labelUsername.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelUsername)

        self.editUsername = QLineEdit(LoginWindow)
        self.editUsername.setObjectName(u"editUsername")
        self.editUsername.setMinimumSize(QSize(0, 20))
        self.editUsername.setFont(font)
        self.editUsername.setStyleSheet(u"")
        self.editUsername.setMaxLength(12)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editUsername)

        self.labelPassword = QLabel(LoginWindow)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setMinimumSize(QSize(0, 40))
        self.labelPassword.setFont(font2)
        self.labelPassword.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPassword)

        self.editPassword = QLineEdit(LoginWindow)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setMinimumSize(QSize(0, 20))
        self.editPassword.setFont(font)
        self.editPassword.setMaxLength(12)
        self.editPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 10, 50, 20)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buttonCancel = QPushButton(LoginWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy1)
        self.buttonCancel.setMinimumSize(QSize(100, 30))
        self.buttonCancel.setMaximumSize(QSize(16777215, 16777215))
        self.buttonCancel.setFont(font)
        self.buttonCancel.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(LoginWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(100, 30))
        self.buttonOk.setMaximumSize(QSize(16777215, 16777215))
        self.buttonOk.setFont(font)
        self.buttonOk.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttonOk)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelCopyright = QLabel(LoginWindow)
        self.labelCopyright.setObjectName(u"labelCopyright")
        self.labelCopyright.setMinimumSize(QSize(0, 40))
        self.labelCopyright.setFont(font)
        self.labelCopyright.setStyleSheet(u"")
        self.labelCopyright.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelCopyright)


        self.retranslateUi(LoginWindow)
        self.editUsername.textChanged.connect(LoginWindow.onTextChange)
        self.editPassword.textChanged.connect(LoginWindow.onTextChange)
        self.buttonCancel.clicked.connect(LoginWindow.close)
        self.buttonOk.clicked.connect(LoginWindow.onLogin)

        self.buttonOk.setDefault(True)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("LoginWindow", u"Invalid username / password", None))
        self.labelHeading.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))
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
        self.labelCopyright.setText(QCoreApplication.translate("LoginWindow", u"Copyright", None))
    # retranslateUi

