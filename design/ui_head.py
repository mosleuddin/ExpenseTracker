

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
## Form generated from reading UI file 'head.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from src import resource

class Ui_HeadWindow(object):
    def setupUi(self, HeadWindow):
        if not HeadWindow.objectName():
            HeadWindow.setObjectName(u"HeadWindow")
        HeadWindow.setWindowModality(Qt.ApplicationModal)
        HeadWindow.resize(565, 434)
        font = QFont()
        HeadWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        HeadWindow.setWindowIcon(icon)
        HeadWindow.setStyleSheet(u"*{\n"
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
"QLineEdit::disabled{\n"
"            background-color :#10141b;\n"
"        }\n"
"\n"
"QComboBox{\n"
"		background-color :#1f232a;\n"
"		selection-color: rgb(255, 255, 255);\n"
"		selection-background-color: rgb(32, 74, 135);\n"
"		border: 1px solid #264BF6;\n"
"}\n"
"\n"
"\n"
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
"     color: rgba(255, 255, 255"
                        ", .50);\n"
"}\n"
" \n"
" \n"
"        \n"
"\n"
"        \n"
"\n"
"\n"
"\n"
"")
        HeadWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(HeadWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(HeadWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 0))
        self.labelMessage.setMaximumSize(QSize(16777215, 40))
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(HeadWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.comboLayout = QHBoxLayout()
        self.comboLayout.setSpacing(0)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(50, 10, 50, 10)
        self.comboHead = QComboBox(HeadWindow)
        self.comboHead.setObjectName(u"comboHead")
        self.comboHead.setEnabled(True)
        self.comboHead.setMinimumSize(QSize(200, 40))
        self.comboHead.setMaximumSize(QSize(350, 16777215))
        self.comboHead.setFont(font)
        self.comboHead.setAutoFillBackground(False)
        self.comboHead.setStyleSheet(u"")

        self.comboLayout.addWidget(self.comboHead)


        self.verticalLayout.addLayout(self.comboLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(50, 0, 50, 0)
        self.labelHeadName = QLabel(HeadWindow)
        self.labelHeadName.setObjectName(u"labelHeadName")
        self.labelHeadName.setMinimumSize(QSize(0, 40))
        self.labelHeadName.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelHeadName)

        self.editHeadName = QLineEdit(HeadWindow)
        self.editHeadName.setObjectName(u"editHeadName")
        self.editHeadName.setEnabled(True)
        self.editHeadName.setMinimumSize(QSize(200, 40))
        self.editHeadName.setFont(font)
        self.editHeadName.setStyleSheet(u"")
        self.editHeadName.setMaxLength(32)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.editHeadName)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)

        self.labelHeadType2 = QLabel(HeadWindow)
        self.labelHeadType2.setObjectName(u"labelHeadType2")
        self.labelHeadType2.setMinimumSize(QSize(0, 40))
        self.labelHeadType2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelHeadType2)

        self.labelHeadType1 = QLabel(HeadWindow)
        self.labelHeadType1.setObjectName(u"labelHeadType1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelHeadType1)

        self.comboHeadType = QComboBox(HeadWindow)
        self.comboHeadType.setObjectName(u"comboHeadType")
        self.comboHeadType.setMinimumSize(QSize(200, 40))
        self.comboHeadType.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboHeadType)

        self.editHeadType = QLineEdit(HeadWindow)
        self.editHeadType.setObjectName(u"editHeadType")
        self.editHeadType.setEnabled(True)
        self.editHeadType.setMinimumSize(QSize(200, 40))
        self.editHeadType.setStyleSheet(u"")
        self.editHeadType.setMaxLength(32)
        self.editHeadType.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editHeadType)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(50, 0, 50, 50)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(HeadWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(0, 0))
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setBold(False)
        self.buttonBack.setFont(font2)
        self.buttonBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(HeadWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(0, 0))
        self.buttonCancel.setMaximumSize(QSize(16777215, 16777215))
        self.buttonCancel.setFont(font2)
        self.buttonCancel.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(HeadWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(0, 0))
        self.buttonOk.setMaximumSize(QSize(16777215, 16777215))
        self.buttonOk.setFont(font2)
        self.buttonOk.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout.addLayout(self.buttonLayout)

#if QT_CONFIG(shortcut)
        self.labelHeadName.setBuddy(self.editHeadName)
        self.labelHeadType2.setBuddy(self.comboHeadType)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboHead, self.editHeadName)
        QWidget.setTabOrder(self.editHeadName, self.buttonBack)
        QWidget.setTabOrder(self.buttonBack, self.buttonCancel)
        QWidget.setTabOrder(self.buttonCancel, self.buttonOk)

        self.retranslateUi(HeadWindow)
        self.buttonCancel.clicked.connect(HeadWindow.onDiscardPressed)
        self.comboHead.activated.connect(HeadWindow.onHeadChanged)
        self.buttonBack.clicked.connect(HeadWindow.close)
        self.buttonOk.clicked.connect(HeadWindow.onOkPressed)
        self.editHeadName.textEdited.connect(HeadWindow.onTextEdited)
        self.comboHeadType.activated.connect(HeadWindow.onHeadTypeChanged)

        self.buttonOk.setDefault(True)


        QMetaObject.connectSlotsByName(HeadWindow)
    # setupUi

    def retranslateUi(self, HeadWindow):
        HeadWindow.setWindowTitle(QCoreApplication.translate("HeadWindow", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("HeadWindow", u"TextLabel", None))
        self.labelHeading.setText(QCoreApplication.translate("HeadWindow", u"Head", None))
        self.comboHead.setPlaceholderText(QCoreApplication.translate("HeadWindow", u"Select head", None))
        self.labelHeadName.setText(QCoreApplication.translate("HeadWindow", u"Head &Name", None))
        self.editHeadName.setPlaceholderText(QCoreApplication.translate("HeadWindow", u"Enter head name", None))
        self.labelHeadType2.setText(QCoreApplication.translate("HeadWindow", u"Head &Type", None))
        self.labelHeadType1.setText(QCoreApplication.translate("HeadWindow", u"Head Type", None))
        self.comboHeadType.setPlaceholderText(QCoreApplication.translate("HeadWindow", u"Select head type", None))
        self.buttonBack.setText(QCoreApplication.translate("HeadWindow", u"&Back", None))
        self.buttonCancel.setText(QCoreApplication.translate("HeadWindow", u"&Cancel", None))
        self.buttonOk.setText(QCoreApplication.translate("HeadWindow", u"&Ok", None))
    # retranslateUi

