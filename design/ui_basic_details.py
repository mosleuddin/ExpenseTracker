

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
## Form generated from reading UI file 'basic_details.ui'
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
    QVBoxLayout, QWidget)
from src import resource

class Ui_BasicDetailsWindow(object):
    def setupUi(self, BasicDetailsWindow):
        if not BasicDetailsWindow.objectName():
            BasicDetailsWindow.setObjectName(u"BasicDetailsWindow")
        BasicDetailsWindow.setWindowModality(Qt.WindowModal)
        BasicDetailsWindow.resize(907, 478)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BasicDetailsWindow.sizePolicy().hasHeightForWidth())
        BasicDetailsWindow.setSizePolicy(sizePolicy)
        BasicDetailsWindow.setMinimumSize(QSize(0, 0))
        BasicDetailsWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        BasicDetailsWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        BasicDetailsWindow.setWindowIcon(icon)
        BasicDetailsWindow.setStyleSheet(u"*{\n"
"	    background-color : #1f232a;\n"
"	    border: none;\n"
"         font-size: 16px;\n"
"}\n"
"\n"
"#mainBodyWidget{\n"
"	    background-color:#10141b;\n"
"     	color:rgba(255, 255, 255, .5);\n"
"}\n"
"\n"
"QLabel{	\n"
" 	color:rgba(255, 255, 255, .50);\n"
"}\n"
"\n"
"#lblMsg{\n"
"	color: rgb(239, 41, 41);\n"
"     padding: 10px, 10px;\n"
"}\n"
"\n"
"#lblHead{\n"
"	color: rgba(.06, 140, 140, 1);\n"
"	font-size: 20px;\n"
"    padding: 10px, 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color:#10141b;\n"
"	color: rgba(255, 255, 255, .75);\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	width: 200px;\n"
"	height: 30px;\n"
"	margin: 5px\n"
"}\n"
"\n"
"QLineEdit::disabled{\n"
"    background-color: #1f232a;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#10141b;\n"
" 	color:rgba(0, 255, 0, .50);\n"
"    width: 75px;\n"
"	height: 20px;\n"
"	padding: 5px, 10px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, "
                        "255, .30);\n"
"     color: rgba(255, 255, 255, .50);\n"
"}\n"
"\n"
"#footerWidget QPushButton{\n"
"	width: 100px;\n"
"	height: 20px;\n"
"	text-align: center;\n"
"	border-radius: 15px;	\n"
"}\n"
"")
        BasicDetailsWindow.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(BasicDetailsWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerWidget = QWidget(BasicDetailsWindow)
        self.headerWidget.setObjectName(u"headerWidget")
        sizePolicy.setHeightForWidth(self.headerWidget.sizePolicy().hasHeightForWidth())
        self.headerWidget.setSizePolicy(sizePolicy)
        self.headerWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.headerWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.headerWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(0, 0))
        self.headerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lblMsg = QLabel(self.headerFrame)
        self.lblMsg.setObjectName(u"lblMsg")
        sizePolicy.setHeightForWidth(self.lblMsg.sizePolicy().hasHeightForWidth())
        self.lblMsg.setSizePolicy(sizePolicy)
        self.lblMsg.setMinimumSize(QSize(0, 0))
        self.lblMsg.setMaximumSize(QSize(16777215, 16777215))
        self.lblMsg.setFont(font)
        self.lblMsg.setStyleSheet(u"")
        self.lblMsg.setAlignment(Qt.AlignCenter)
        self.lblMsg.setMargin(0)

        self.verticalLayout_5.addWidget(self.lblMsg)

        self.lblHead = QLabel(self.headerFrame)
        self.lblHead.setObjectName(u"lblHead")
        sizePolicy.setHeightForWidth(self.lblHead.sizePolicy().hasHeightForWidth())
        self.lblHead.setSizePolicy(sizePolicy)
        self.lblHead.setMinimumSize(QSize(0, 0))
        self.lblHead.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(False)
        font1.setUnderline(False)
        self.lblHead.setFont(font1)
        self.lblHead.setStyleSheet(u"")
        self.lblHead.setAlignment(Qt.AlignCenter)
        self.lblHead.setMargin(0)

        self.verticalLayout_5.addWidget(self.lblHead)


        self.verticalLayout_8.addWidget(self.headerFrame, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.headerWidget)

        self.mainBodyWidget = QWidget(BasicDetailsWindow)
        self.mainBodyWidget.setObjectName(u"mainBodyWidget")
        sizePolicy.setHeightForWidth(self.mainBodyWidget.sizePolicy().hasHeightForWidth())
        self.mainBodyWidget.setSizePolicy(sizePolicy)
        self.mainBodyWidget.setMinimumSize(QSize(0, 0))
        self.mainBodyWidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.mainBodyWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.ownerWidget = QWidget(self.mainBodyWidget)
        self.ownerWidget.setObjectName(u"ownerWidget")
        sizePolicy.setHeightForWidth(self.ownerWidget.sizePolicy().hasHeightForWidth())
        self.ownerWidget.setSizePolicy(sizePolicy)
        self.ownerWidget.setMinimumSize(QSize(0, 0))
        self.ownerWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.ownerWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nameFrame = QFrame(self.ownerWidget)
        self.nameFrame.setObjectName(u"nameFrame")
        sizePolicy.setHeightForWidth(self.nameFrame.sizePolicy().hasHeightForWidth())
        self.nameFrame.setSizePolicy(sizePolicy)
        self.nameFrame.setMinimumSize(QSize(0, 0))
        self.nameFrame.setMaximumSize(QSize(16777215, 16777215))
        self.nameFrame.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.nameFrame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lblName = QLabel(self.nameFrame)
        self.lblName.setObjectName(u"lblName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblName.sizePolicy().hasHeightForWidth())
        self.lblName.setSizePolicy(sizePolicy1)
        self.lblName.setMinimumSize(QSize(100, 0))
        self.lblName.setMaximumSize(QSize(16777215, 16777215))
        self.lblName.setFont(font1)
        self.lblName.setStyleSheet(u"")
        self.lblName.setTextFormat(Qt.RichText)
        self.lblName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lblName)

        self.editName = QLineEdit(self.nameFrame)
        self.editName.setObjectName(u"editName")
        self.editName.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.editName.sizePolicy().hasHeightForWidth())
        self.editName.setSizePolicy(sizePolicy1)
        self.editName.setMinimumSize(QSize(0, 0))
        self.editName.setMaximumSize(QSize(16777215, 16777215))
        self.editName.setFont(font)
        self.editName.setStyleSheet(u"")
        self.editName.setMaxLength(40)
        self.editName.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.editName)

        self.btnName = QPushButton(self.nameFrame)
        self.btnName.setObjectName(u"btnName")
        sizePolicy1.setHeightForWidth(self.btnName.sizePolicy().hasHeightForWidth())
        self.btnName.setSizePolicy(sizePolicy1)
        self.btnName.setMinimumSize(QSize(0, 0))
        self.btnName.setMaximumSize(QSize(16777215, 16777215))
        self.btnName.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnName)


        self.verticalLayout_4.addWidget(self.nameFrame)

        self.addressFrame = QFrame(self.ownerWidget)
        self.addressFrame.setObjectName(u"addressFrame")
        sizePolicy.setHeightForWidth(self.addressFrame.sizePolicy().hasHeightForWidth())
        self.addressFrame.setSizePolicy(sizePolicy)
        self.addressFrame.setMaximumSize(QSize(16777215, 16777215))
        self.addressFrame.setFrameShape(QFrame.StyledPanel)
        self.addressFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.addressFrame)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.lblAddress = QLabel(self.addressFrame)
        self.lblAddress.setObjectName(u"lblAddress")
        sizePolicy1.setHeightForWidth(self.lblAddress.sizePolicy().hasHeightForWidth())
        self.lblAddress.setSizePolicy(sizePolicy1)
        self.lblAddress.setMinimumSize(QSize(100, 0))
        self.lblAddress.setMaximumSize(QSize(16777215, 16777215))
        self.lblAddress.setFont(font1)
        self.lblAddress.setStyleSheet(u"")
        self.lblAddress.setTextFormat(Qt.RichText)
        self.lblAddress.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lblAddress)

        self.editAddress = QLineEdit(self.addressFrame)
        self.editAddress.setObjectName(u"editAddress")
        self.editAddress.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.editAddress.sizePolicy().hasHeightForWidth())
        self.editAddress.setSizePolicy(sizePolicy1)
        self.editAddress.setMinimumSize(QSize(0, 0))
        self.editAddress.setMaximumSize(QSize(16777215, 16777215))
        self.editAddress.setFont(font)
        self.editAddress.setStyleSheet(u"")
        self.editAddress.setMaxLength(40)
        self.editAddress.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_8.addWidget(self.editAddress)

        self.btnAddress = QPushButton(self.addressFrame)
        self.btnAddress.setObjectName(u"btnAddress")
        sizePolicy1.setHeightForWidth(self.btnAddress.sizePolicy().hasHeightForWidth())
        self.btnAddress.setSizePolicy(sizePolicy1)
        self.btnAddress.setMinimumSize(QSize(0, 0))
        self.btnAddress.setMaximumSize(QSize(16777215, 16777215))
        self.btnAddress.setFont(font)

        self.horizontalLayout_8.addWidget(self.btnAddress)


        self.verticalLayout_4.addWidget(self.addressFrame)

        self.balanceFrame = QFrame(self.ownerWidget)
        self.balanceFrame.setObjectName(u"balanceFrame")
        sizePolicy.setHeightForWidth(self.balanceFrame.sizePolicy().hasHeightForWidth())
        self.balanceFrame.setSizePolicy(sizePolicy)
        self.balanceFrame.setMaximumSize(QSize(16777215, 16777215))
        self.balanceFrame.setFrameShape(QFrame.StyledPanel)
        self.balanceFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.balanceFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.lblCashBalance = QLabel(self.balanceFrame)
        self.lblCashBalance.setObjectName(u"lblCashBalance")
        sizePolicy1.setHeightForWidth(self.lblCashBalance.sizePolicy().hasHeightForWidth())
        self.lblCashBalance.setSizePolicy(sizePolicy1)
        self.lblCashBalance.setMinimumSize(QSize(100, 0))
        self.lblCashBalance.setMaximumSize(QSize(16777215, 16777215))
        self.lblCashBalance.setFont(font1)
        self.lblCashBalance.setStyleSheet(u"")
        self.lblCashBalance.setTextFormat(Qt.RichText)
        self.lblCashBalance.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lblCashBalance)

        self.editCashBalance = QLineEdit(self.balanceFrame)
        self.editCashBalance.setObjectName(u"editCashBalance")
        self.editCashBalance.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.editCashBalance.sizePolicy().hasHeightForWidth())
        self.editCashBalance.setSizePolicy(sizePolicy1)
        self.editCashBalance.setMinimumSize(QSize(0, 0))
        self.editCashBalance.setMaximumSize(QSize(16777215, 16777215))
        self.editCashBalance.setFont(font)
        self.editCashBalance.setStyleSheet(u"")
        self.editCashBalance.setInputMethodHints(Qt.ImhDigitsOnly)
        self.editCashBalance.setMaxLength(40)
        self.editCashBalance.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_7.addWidget(self.editCashBalance)

        self.btnCashBalance = QPushButton(self.balanceFrame)
        self.btnCashBalance.setObjectName(u"btnCashBalance")
        sizePolicy1.setHeightForWidth(self.btnCashBalance.sizePolicy().hasHeightForWidth())
        self.btnCashBalance.setSizePolicy(sizePolicy1)
        self.btnCashBalance.setMinimumSize(QSize(0, 0))
        self.btnCashBalance.setMaximumSize(QSize(16777215, 16777215))
        self.btnCashBalance.setFont(font)

        self.horizontalLayout_7.addWidget(self.btnCashBalance)


        self.verticalLayout_4.addWidget(self.balanceFrame)


        self.horizontalLayout.addWidget(self.ownerWidget, 0, Qt.AlignHCenter)

        self.periodWidget = QWidget(self.mainBodyWidget)
        self.periodWidget.setObjectName(u"periodWidget")
        sizePolicy.setHeightForWidth(self.periodWidget.sizePolicy().hasHeightForWidth())
        self.periodWidget.setSizePolicy(sizePolicy)
        self.periodWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.periodWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.monthFrame = QFrame(self.periodWidget)
        self.monthFrame.setObjectName(u"monthFrame")
        sizePolicy.setHeightForWidth(self.monthFrame.sizePolicy().hasHeightForWidth())
        self.monthFrame.setSizePolicy(sizePolicy)
        self.monthFrame.setMaximumSize(QSize(16777215, 16777215))
        self.monthFrame.setFrameShape(QFrame.StyledPanel)
        self.monthFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.monthFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblMonth = QLabel(self.monthFrame)
        self.lblMonth.setObjectName(u"lblMonth")
        sizePolicy1.setHeightForWidth(self.lblMonth.sizePolicy().hasHeightForWidth())
        self.lblMonth.setSizePolicy(sizePolicy1)
        self.lblMonth.setMinimumSize(QSize(50, 0))
        self.lblMonth.setMaximumSize(QSize(16777215, 16777215))
        self.lblMonth.setFont(font)
        self.lblMonth.setStyleSheet(u"")
        self.lblMonth.setTextFormat(Qt.RichText)

        self.horizontalLayout_4.addWidget(self.lblMonth)

        self.editMonth = QLineEdit(self.monthFrame)
        self.editMonth.setObjectName(u"editMonth")
        self.editMonth.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.editMonth.sizePolicy().hasHeightForWidth())
        self.editMonth.setSizePolicy(sizePolicy1)
        self.editMonth.setMinimumSize(QSize(0, 0))
        self.editMonth.setMaximumSize(QSize(16777215, 16777215))
        self.editMonth.setFont(font)
        self.editMonth.setStyleSheet(u"")
        self.editMonth.setMaxLength(40)
        self.editMonth.setEchoMode(QLineEdit.Normal)
        self.editMonth.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.editMonth)

        self.btnMonth = QPushButton(self.monthFrame)
        self.btnMonth.setObjectName(u"btnMonth")
        sizePolicy1.setHeightForWidth(self.btnMonth.sizePolicy().hasHeightForWidth())
        self.btnMonth.setSizePolicy(sizePolicy1)
        self.btnMonth.setMinimumSize(QSize(0, 0))
        self.btnMonth.setMaximumSize(QSize(16777215, 16777215))
        self.btnMonth.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnMonth)


        self.verticalLayout.addWidget(self.monthFrame)

        self.yearFrame = QFrame(self.periodWidget)
        self.yearFrame.setObjectName(u"yearFrame")
        sizePolicy.setHeightForWidth(self.yearFrame.sizePolicy().hasHeightForWidth())
        self.yearFrame.setSizePolicy(sizePolicy)
        self.yearFrame.setMaximumSize(QSize(16777215, 16777215))
        self.yearFrame.setFrameShape(QFrame.StyledPanel)
        self.yearFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.yearFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblYear = QLabel(self.yearFrame)
        self.lblYear.setObjectName(u"lblYear")
        sizePolicy1.setHeightForWidth(self.lblYear.sizePolicy().hasHeightForWidth())
        self.lblYear.setSizePolicy(sizePolicy1)
        self.lblYear.setMinimumSize(QSize(50, 0))
        self.lblYear.setMaximumSize(QSize(16777215, 16777215))
        self.lblYear.setFont(font)

        self.horizontalLayout_5.addWidget(self.lblYear)

        self.editYear = QLineEdit(self.yearFrame)
        self.editYear.setObjectName(u"editYear")
        self.editYear.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.editYear.sizePolicy().hasHeightForWidth())
        self.editYear.setSizePolicy(sizePolicy1)
        self.editYear.setMinimumSize(QSize(0, 0))
        self.editYear.setMaximumSize(QSize(16777215, 16777215))
        self.editYear.setFont(font)
        self.editYear.setStyleSheet(u"")
        self.editYear.setMaxLength(40)
        self.editYear.setEchoMode(QLineEdit.Normal)
        self.editYear.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.editYear)

        self.btnYear = QPushButton(self.yearFrame)
        self.btnYear.setObjectName(u"btnYear")
        sizePolicy1.setHeightForWidth(self.btnYear.sizePolicy().hasHeightForWidth())
        self.btnYear.setSizePolicy(sizePolicy1)
        self.btnYear.setMinimumSize(QSize(0, 0))
        self.btnYear.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.btnYear)


        self.verticalLayout.addWidget(self.yearFrame)


        self.horizontalLayout.addWidget(self.periodWidget)


        self.verticalLayout_2.addWidget(self.mainBodyWidget, 0, Qt.AlignTop)

        self.footerWidget = QWidget(BasicDetailsWindow)
        self.footerWidget.setObjectName(u"footerWidget")
        sizePolicy.setHeightForWidth(self.footerWidget.sizePolicy().hasHeightForWidth())
        self.footerWidget.setSizePolicy(sizePolicy)
        self.footerWidget.setMinimumSize(QSize(0, 0))
        self.footerWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.footerWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.footerFrame = QFrame(self.footerWidget)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy)
        self.footerFrame.setMinimumSize(QSize(0, 0))
        self.footerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnBack = QPushButton(self.footerFrame)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy1)
        self.btnBack.setMinimumSize(QSize(0, 0))
        self.btnBack.setMaximumSize(QSize(16777215, 16777215))
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../.designer/src/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBack.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btnBack)

        self.btnSubmit = QPushButton(self.footerFrame)
        self.btnSubmit.setObjectName(u"btnSubmit")
        self.btnSubmit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy1)
        self.btnSubmit.setMinimumSize(QSize(0, 0))
        self.btnSubmit.setMaximumSize(QSize(16777215, 16777215))
        self.btnSubmit.setFont(font)
        self.btnSubmit.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../.designer/src/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSubmit.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnSubmit)


        self.verticalLayout_3.addWidget(self.footerFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.footerWidget, 0, Qt.AlignHCenter)

        QWidget.setTabOrder(self.editName, self.editAddress)
        QWidget.setTabOrder(self.editAddress, self.editCashBalance)
        QWidget.setTabOrder(self.editCashBalance, self.btnName)
        QWidget.setTabOrder(self.btnName, self.btnAddress)
        QWidget.setTabOrder(self.btnAddress, self.btnCashBalance)
        QWidget.setTabOrder(self.btnCashBalance, self.btnSubmit)
        QWidget.setTabOrder(self.btnSubmit, self.btnBack)
        QWidget.setTabOrder(self.btnBack, self.editMonth)
        QWidget.setTabOrder(self.editMonth, self.btnMonth)
        QWidget.setTabOrder(self.btnMonth, self.editYear)
        QWidget.setTabOrder(self.editYear, self.btnYear)

        self.retranslateUi(BasicDetailsWindow)
        self.btnAddress.clicked.connect(BasicDetailsWindow.onLockUnlock)
        self.btnName.clicked.connect(BasicDetailsWindow.onLockUnlock)
        self.btnMonth.clicked.connect(BasicDetailsWindow.onLockUnlock)
        self.btnYear.clicked.connect(BasicDetailsWindow.onLockUnlock)
        self.btnSubmit.clicked.connect(BasicDetailsWindow.onSubmit)
        self.btnBack.clicked.connect(BasicDetailsWindow.close)
        self.editAddress.returnPressed.connect(BasicDetailsWindow.onReturnPressed)
        self.editName.returnPressed.connect(BasicDetailsWindow.onReturnPressed)
        self.editName.textEdited.connect(BasicDetailsWindow.onTextEdited)
        self.editAddress.textEdited.connect(BasicDetailsWindow.onTextEdited)
        self.btnCashBalance.clicked.connect(BasicDetailsWindow.onLockUnlock)
        self.editCashBalance.textEdited.connect(BasicDetailsWindow.onTextEdited)
        self.editCashBalance.returnPressed.connect(BasicDetailsWindow.onReturnPressed)
        self.editMonth.returnPressed.connect(BasicDetailsWindow.onReturnPressed)
        self.editMonth.textEdited.connect(BasicDetailsWindow.onTextEdited)
        self.editYear.returnPressed.connect(BasicDetailsWindow.onReturnPressed)
        self.editYear.textEdited.connect(BasicDetailsWindow.onTextEdited)

        self.btnSubmit.setDefault(True)


        QMetaObject.connectSlotsByName(BasicDetailsWindow)
    # setupUi

    def retranslateUi(self, BasicDetailsWindow):
        BasicDetailsWindow.setWindowTitle(QCoreApplication.translate("BasicDetailsWindow", u"Expense Tracker", None))
        self.lblMsg.setText(QCoreApplication.translate("BasicDetailsWindow", u"text", None))
        self.lblHead.setText(QCoreApplication.translate("BasicDetailsWindow", u"Enter Basic Details", None))
        self.lblName.setText(QCoreApplication.translate("BasicDetailsWindow", u"Name", None))
#if QT_CONFIG(statustip)
        self.editName.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.editName.setPlaceholderText(QCoreApplication.translate("BasicDetailsWindow", u"Enter owner's name", None))
        self.btnName.setText(QCoreApplication.translate("BasicDetailsWindow", u"Unlock", None))
        self.lblAddress.setText(QCoreApplication.translate("BasicDetailsWindow", u"Address", None))
#if QT_CONFIG(statustip)
        self.editAddress.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.editAddress.setInputMask("")
        self.editAddress.setText("")
        self.editAddress.setPlaceholderText(QCoreApplication.translate("BasicDetailsWindow", u"Enter owner's address", None))
        self.btnAddress.setText(QCoreApplication.translate("BasicDetailsWindow", u"Unlock", None))
        self.lblCashBalance.setText(QCoreApplication.translate("BasicDetailsWindow", u"Cash in hand", None))
#if QT_CONFIG(statustip)
        self.editCashBalance.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.editCashBalance.setInputMask("")
        self.editCashBalance.setText("")
        self.editCashBalance.setPlaceholderText(QCoreApplication.translate("BasicDetailsWindow", u"Enter cash opening balance", None))
        self.btnCashBalance.setText(QCoreApplication.translate("BasicDetailsWindow", u"Unlock", None))
        self.lblMonth.setText(QCoreApplication.translate("BasicDetailsWindow", u"Month", None))
#if QT_CONFIG(statustip)
        self.editMonth.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.editMonth.setInputMask("")
        self.editMonth.setText("")
        self.editMonth.setPlaceholderText(QCoreApplication.translate("BasicDetailsWindow", u"Enter month", None))
        self.btnMonth.setText(QCoreApplication.translate("BasicDetailsWindow", u"Unlock", None))
        self.lblYear.setText(QCoreApplication.translate("BasicDetailsWindow", u"Year", None))
#if QT_CONFIG(statustip)
        self.editYear.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.editYear.setPlaceholderText(QCoreApplication.translate("BasicDetailsWindow", u"Enter year", None))
        self.btnYear.setText(QCoreApplication.translate("BasicDetailsWindow", u"Unlock", None))
        self.btnBack.setText(QCoreApplication.translate("BasicDetailsWindow", u"&Back", None))
        self.btnSubmit.setText(QCoreApplication.translate("BasicDetailsWindow", u"&Submit", None))
    # retranslateUi

