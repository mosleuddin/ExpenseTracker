
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
## Form generated from reading UI file 'initialize.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from src import resource

class Ui_InitializeTransactionWindow(object):
    def setupUi(self, InitializeTransactionWindow):
        if not InitializeTransactionWindow.objectName():
            InitializeTransactionWindow.setObjectName(u"InitializeTransactionWindow")
        InitializeTransactionWindow.setWindowModality(Qt.ApplicationModal)
        InitializeTransactionWindow.setEnabled(True)
        InitializeTransactionWindow.resize(596, 461)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InitializeTransactionWindow.sizePolicy().hasHeightForWidth())
        InitializeTransactionWindow.setSizePolicy(sizePolicy)
        font = QFont()
        InitializeTransactionWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        InitializeTransactionWindow.setWindowIcon(icon)
        InitializeTransactionWindow.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"	color:rgba(255, 255, 255, .5);\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"#labelMessage{\n"
"	color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"#labelPassword{\n"
"	color: rgba(255, 255, 255, .60);\n"
"\n"
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
" \n"
"        \n"
"\n"
"")
        InitializeTransactionWindow.setModal(True)
        self.verticalLayout_4 = QVBoxLayout(InitializeTransactionWindow)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.labelMessage = QLabel(InitializeTransactionWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 0))
        self.labelMessage.setMaximumSize(QSize(16777215, 40))
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(0)

        self.verticalLayout_4.addWidget(self.labelMessage)

        self.centralWidget = QWidget(InitializeTransactionWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.frameAlert = QFrame(self.centralWidget)
        self.frameAlert.setObjectName(u"frameAlert")
        self.verticalLayout_2 = QVBoxLayout(self.frameAlert)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.frameAlertLabel = QFrame(self.frameAlert)
        self.frameAlertLabel.setObjectName(u"frameAlertLabel")
        self.horizontalLayout_4 = QHBoxLayout(self.frameAlertLabel)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelAlertMsg = QLabel(self.frameAlertLabel)
        self.labelAlertMsg.setObjectName(u"labelAlertMsg")
        self.labelAlertMsg.setMinimumSize(QSize(0, 0))
        self.labelAlertMsg.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.labelAlertMsg)


        self.verticalLayout_2.addWidget(self.frameAlertLabel)

        self.frameAlertButtons = QFrame(self.frameAlert)
        self.frameAlertButtons.setObjectName(u"frameAlertButtons")
        self.horizontalLayout = QHBoxLayout(self.frameAlertButtons)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAlertClose = QPushButton(self.frameAlertButtons)
        self.btnAlertClose.setObjectName(u"btnAlertClose")
        self.btnAlertClose.setEnabled(True)
        self.btnAlertClose.setMinimumSize(QSize(100, 30))
        self.btnAlertClose.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setBold(False)
        self.btnAlertClose.setFont(font1)
        self.btnAlertClose.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAlertClose.setIcon(icon1)
        self.btnAlertClose.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.btnAlertClose)

        self.btnAlertProceed = QPushButton(self.frameAlertButtons)
        self.btnAlertProceed.setObjectName(u"btnAlertProceed")
        self.btnAlertProceed.setEnabled(True)
        self.btnAlertProceed.setMinimumSize(QSize(100, 30))
        self.btnAlertProceed.setMaximumSize(QSize(100, 30))
        self.btnAlertProceed.setFont(font1)
        self.btnAlertProceed.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAlertProceed.setIcon(icon2)
        self.btnAlertProceed.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.btnAlertProceed)


        self.verticalLayout_2.addWidget(self.frameAlertButtons)


        self.verticalLayout_3.addWidget(self.frameAlert)

        self.framePassword = QFrame(self.centralWidget)
        self.framePassword.setObjectName(u"framePassword")
        sizePolicy.setHeightForWidth(self.framePassword.sizePolicy().hasHeightForWidth())
        self.framePassword.setSizePolicy(sizePolicy)
        self.framePassword.setMinimumSize(QSize(0, 0))
        self.framePassword.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.framePassword)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.framePasswordInput = QFrame(self.framePassword)
        self.framePasswordInput.setObjectName(u"framePasswordInput")
        sizePolicy.setHeightForWidth(self.framePasswordInput.sizePolicy().hasHeightForWidth())
        self.framePasswordInput.setSizePolicy(sizePolicy)
        self.framePasswordInput.setMinimumSize(QSize(0, 0))
        self.framePasswordInput.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.framePasswordInput)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelPassword = QLabel(self.framePasswordInput)
        self.labelPassword.setObjectName(u"labelPassword")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelPassword.sizePolicy().hasHeightForWidth())
        self.labelPassword.setSizePolicy(sizePolicy1)
        self.labelPassword.setMinimumSize(QSize(0, 0))
        self.labelPassword.setMaximumSize(QSize(16777215, 16777215))
        self.labelPassword.setFont(font)
        self.labelPassword.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelPassword)

        self.editPassword = QLineEdit(self.framePasswordInput)
        self.editPassword.setObjectName(u"editPassword")
        sizePolicy1.setHeightForWidth(self.editPassword.sizePolicy().hasHeightForWidth())
        self.editPassword.setSizePolicy(sizePolicy1)
        self.editPassword.setMinimumSize(QSize(0, 0))
        self.editPassword.setMaximumSize(QSize(16777215, 16777215))
        self.editPassword.setFont(font)
        self.editPassword.setStyleSheet(u"")
        self.editPassword.setInputMethodHints(Qt.ImhNone)
        self.editPassword.setMaxLength(40)

        self.verticalLayout_5.addWidget(self.editPassword)


        self.verticalLayout.addWidget(self.framePasswordInput)

        self.framePasswordButtons = QFrame(self.framePassword)
        self.framePasswordButtons.setObjectName(u"framePasswordButtons")
        self.horizontalLayout_2 = QHBoxLayout(self.framePasswordButtons)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btnPasswordCancel = QPushButton(self.framePasswordButtons)
        self.btnPasswordCancel.setObjectName(u"btnPasswordCancel")
        self.btnPasswordCancel.setMinimumSize(QSize(100, 30))
        self.btnPasswordCancel.setMaximumSize(QSize(100, 30))
        self.btnPasswordCancel.setFont(font1)
        self.btnPasswordCancel.setStyleSheet(u"")
        self.btnPasswordCancel.setIcon(icon1)
        self.btnPasswordCancel.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btnPasswordCancel)

        self.btnPasswordSubmit = QPushButton(self.framePasswordButtons)
        self.btnPasswordSubmit.setObjectName(u"btnPasswordSubmit")
        self.btnPasswordSubmit.setEnabled(True)
        self.btnPasswordSubmit.setMinimumSize(QSize(100, 30))
        self.btnPasswordSubmit.setMaximumSize(QSize(100, 30))
        self.btnPasswordSubmit.setFont(font1)
        self.btnPasswordSubmit.setStyleSheet(u"")
        self.btnPasswordSubmit.setIcon(icon2)
        self.btnPasswordSubmit.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btnPasswordSubmit)


        self.verticalLayout.addWidget(self.framePasswordButtons)


        self.verticalLayout_3.addWidget(self.framePassword)


        self.verticalLayout_4.addWidget(self.centralWidget)


        self.retranslateUi(InitializeTransactionWindow)
        self.btnAlertClose.clicked.connect(InitializeTransactionWindow.close)
        self.btnPasswordCancel.clicked.connect(InitializeTransactionWindow.close)
        self.btnAlertProceed.clicked.connect(InitializeTransactionWindow.onProceed)
        self.btnPasswordSubmit.clicked.connect(InitializeTransactionWindow.onInitialize)
        self.editPassword.textEdited.connect(InitializeTransactionWindow.onTextEdited)

        self.btnAlertClose.setDefault(False)
        self.btnAlertProceed.setDefault(True)
        self.btnPasswordCancel.setDefault(False)
        self.btnPasswordSubmit.setDefault(True)


        QMetaObject.connectSlotsByName(InitializeTransactionWindow)
    # setupUi

    def retranslateUi(self, InitializeTransactionWindow):
        InitializeTransactionWindow.setWindowTitle(QCoreApplication.translate("InitializeTransactionWindow", u"Month End Data Initialization", None))
        self.labelMessage.setText(QCoreApplication.translate("InitializeTransactionWindow", u"TextLabel", None))
        self.labelAlertMsg.setText("")
        self.btnAlertClose.setText(QCoreApplication.translate("InitializeTransactionWindow", u"&Close", None))
        self.btnAlertProceed.setText(QCoreApplication.translate("InitializeTransactionWindow", u"&Proceed", None))
        self.labelPassword.setText(QCoreApplication.translate("InitializeTransactionWindow", u"Enter password to complete the initialization process.\n"
"Once submitted, the action can not be undone.", None))
        self.editPassword.setPlaceholderText(QCoreApplication.translate("InitializeTransactionWindow", u"password", None))
        self.btnPasswordCancel.setText(QCoreApplication.translate("InitializeTransactionWindow", u"C&ancel", None))
        self.btnPasswordSubmit.setText(QCoreApplication.translate("InitializeTransactionWindow", u"&Submit", None))
    # retranslateUi

