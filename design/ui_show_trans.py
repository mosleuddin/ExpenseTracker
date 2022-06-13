
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
## Form generated from reading UI file 'show_trans.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDialog, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
from src import resource

class Ui_ShowTransactions(object):
    def setupUi(self, ShowTransactions):
        if not ShowTransactions.objectName():
            ShowTransactions.setObjectName(u"ShowTransactions")
        ShowTransactions.setWindowModality(Qt.WindowModal)
        ShowTransactions.resize(791, 568)
        font = QFont()
        ShowTransactions.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/view.png", QSize(), QIcon.Normal, QIcon.Off)
        ShowTransactions.setWindowIcon(icon)
        ShowTransactions.setStyleSheet(u"*{\n"
"     background-color :#10141b;\n"
"  	border: none;\n"
"	color: rgb(0, 145, 145);\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#groupRadio, #comboFrame, #buttonFrame{\n"
"	border: 1px solid #1DAD5F;\n"
"}\n"
"\n"
"QComboBox{\n"
"	width: 200px;\n"
"	height: 30px;\n"
"	background-color: #1f232a;\n"
"	color:rgba(255, 255, 255, .60);\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(32, 74, 135);\n"
"	border: 1px solid #264BF6;\n"
"}\n"
"\n"
"#radioAll,\n"
"#radioReceipts,\n"
"#radioPayments{\n"
"	color:rgba(255, 255, 255, .60);\n"
"}\n"
"#tableView{\n"
"	background-color: #1f232a;\n"
"	color:rgba(255, 255, 255, .60);\n"
" }\n"
"\n"
"QLineEdit{\n"
"	background-color: #1f232a;\n"
"	color:rgba(255, 255, 255, .60);\n"
"	font-size: 20px \n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#10141b;\n"
" 	color:rgba(0, 255, 0, .60);\n"
"    width: 80px;\n"
"	height: 18px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 1px solid #264BF6;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
""
                        "\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 0, 255, .30);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	background-color: rgba(0, 0, 0, .50);\n"
"     color: rgba(255, 255, 255, .60);\n"
"}\n"
" \n"
" \n"
"        \n"
"\n"
"\n"
"\n"
"")
        ShowTransactions.setModal(True)
        self.horizontalLayout_2 = QHBoxLayout(ShowTransactions)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.leftFrame = QFrame(ShowTransactions)
        self.leftFrame.setObjectName(u"leftFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy)
        self.leftFrame.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftFrame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupRadio = QGroupBox(self.leftFrame)
        self.groupRadio.setObjectName(u"groupRadio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupRadio.sizePolicy().hasHeightForWidth())
        self.groupRadio.setSizePolicy(sizePolicy1)
        self.groupRadio.setMaximumSize(QSize(16777215, 250))
        self.groupRadio.setStyleSheet(u"")
        self.groupRadio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupRadio.setFlat(False)
        self.groupRadio.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupRadio)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 20, -1, 9)
        self.radioAll = QRadioButton(self.groupRadio)
        self.radioAll.setObjectName(u"radioAll")
        self.radioAll.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioAll)

        self.radioReceipts = QRadioButton(self.groupRadio)
        self.radioReceipts.setObjectName(u"radioReceipts")

        self.verticalLayout_2.addWidget(self.radioReceipts)

        self.radioPayments = QRadioButton(self.groupRadio)
        self.radioPayments.setObjectName(u"radioPayments")

        self.verticalLayout_2.addWidget(self.radioPayments)


        self.verticalLayout.addWidget(self.groupRadio)

        self.comboFrame = QFrame(self.leftFrame)
        self.comboFrame.setObjectName(u"comboFrame")
        self.comboFrame.setFrameShape(QFrame.StyledPanel)
        self.comboFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.comboFrame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelAccountNumber = QLabel(self.comboFrame)
        self.labelAccountNumber.setObjectName(u"labelAccountNumber")
        self.labelAccountNumber.setFont(font)

        self.verticalLayout_3.addWidget(self.labelAccountNumber)

        self.comboAccountNumber = QComboBox(self.comboFrame)
        self.comboAccountNumber.setObjectName(u"comboAccountNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboAccountNumber.sizePolicy().hasHeightForWidth())
        self.comboAccountNumber.setSizePolicy(sizePolicy2)
        self.comboAccountNumber.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.comboAccountNumber)

        self.labelHeadName = QLabel(self.comboFrame)
        self.labelHeadName.setObjectName(u"labelHeadName")
        self.labelHeadName.setFont(font)

        self.verticalLayout_3.addWidget(self.labelHeadName)

        self.comboHeadName = QComboBox(self.comboFrame)
        self.comboHeadName.setObjectName(u"comboHeadName")
        sizePolicy2.setHeightForWidth(self.comboHeadName.sizePolicy().hasHeightForWidth())
        self.comboHeadName.setSizePolicy(sizePolicy2)
        self.comboHeadName.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.comboHeadName)

        self.labelTransDate = QLabel(self.comboFrame)
        self.labelTransDate.setObjectName(u"labelTransDate")
        self.labelTransDate.setFont(font)

        self.verticalLayout_3.addWidget(self.labelTransDate)

        self.comboTransDate = QComboBox(self.comboFrame)
        self.comboTransDate.setObjectName(u"comboTransDate")
        sizePolicy2.setHeightForWidth(self.comboTransDate.sizePolicy().hasHeightForWidth())
        self.comboTransDate.setSizePolicy(sizePolicy2)
        self.comboTransDate.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.comboTransDate)

        self.buttonSearch = QPushButton(self.comboFrame)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.buttonSearch.sizePolicy().hasHeightForWidth())
        self.buttonSearch.setSizePolicy(sizePolicy2)
        self.buttonSearch.setMinimumSize(QSize(0, 0))
        self.buttonSearch.setMaximumSize(QSize(16777215, 16777215))
        self.buttonSearch.setFont(font)
        self.buttonSearch.setStyleSheet(u"")
        self.buttonSearch.setIcon(icon)

        self.verticalLayout_3.addWidget(self.buttonSearch, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.comboFrame, 0, Qt.AlignTop)

        self.buttonFrame = QFrame(self.leftFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.buttonFrame)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, 9, -1)
        self.buttonDownload = QPushButton(self.buttonFrame)
        self.buttonDownload.setObjectName(u"buttonDownload")
        self.buttonDownload.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.buttonDownload.sizePolicy().hasHeightForWidth())
        self.buttonDownload.setSizePolicy(sizePolicy2)
        self.buttonDownload.setMinimumSize(QSize(0, 0))
        self.buttonDownload.setMaximumSize(QSize(16777215, 16777215))
        self.buttonDownload.setFont(font)
        self.buttonDownload.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/show_users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDownload.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.buttonDownload)

        self.buttonBack = QPushButton(self.buttonFrame)
        self.buttonBack.setObjectName(u"buttonBack")
        sizePolicy2.setHeightForWidth(self.buttonBack.sizePolicy().hasHeightForWidth())
        self.buttonBack.setSizePolicy(sizePolicy2)
        self.buttonBack.setMinimumSize(QSize(0, 0))
        self.buttonBack.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBack.setFont(font)
        self.buttonBack.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.buttonBack)


        self.verticalLayout.addWidget(self.buttonFrame, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.leftFrame, 0, Qt.AlignLeft)

        self.rightFrame = QFrame(ShowTransactions)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.rightFrame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font)
        self.tableView.setStyleSheet(u"")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(50)
        self.tableView.horizontalHeader().setDefaultSectionSize(50)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tableView)

        self.footerFrame = QFrame(self.rightFrame)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelAccount = QLabel(self.footerFrame)
        self.labelAccount.setObjectName(u"labelAccount")

        self.horizontalLayout.addWidget(self.labelAccount)

        self.editAccount = QLineEdit(self.footerFrame)
        self.editAccount.setObjectName(u"editAccount")
        self.editAccount.setReadOnly(True)

        self.horizontalLayout.addWidget(self.editAccount)

        self.labelHead = QLabel(self.footerFrame)
        self.labelHead.setObjectName(u"labelHead")

        self.horizontalLayout.addWidget(self.labelHead)

        self.editHead = QLineEdit(self.footerFrame)
        self.editHead.setObjectName(u"editHead")
        self.editHead.setReadOnly(True)

        self.horizontalLayout.addWidget(self.editHead)

        self.labelDate = QLabel(self.footerFrame)
        self.labelDate.setObjectName(u"labelDate")

        self.horizontalLayout.addWidget(self.labelDate)

        self.editDate = QLineEdit(self.footerFrame)
        self.editDate.setObjectName(u"editDate")
        self.editDate.setReadOnly(True)

        self.horizontalLayout.addWidget(self.editDate)

        self.labelTotal = QLabel(self.footerFrame)
        self.labelTotal.setObjectName(u"labelTotal")

        self.horizontalLayout.addWidget(self.labelTotal)

        self.editTotal = QLineEdit(self.footerFrame)
        self.editTotal.setObjectName(u"editTotal")
        self.editTotal.setFont(font)
        self.editTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editTotal.setReadOnly(True)

        self.horizontalLayout.addWidget(self.editTotal)


        self.verticalLayout_4.addWidget(self.footerFrame)


        self.horizontalLayout_2.addWidget(self.rightFrame)


        self.retranslateUi(ShowTransactions)
        self.buttonSearch.clicked.connect(ShowTransactions.onSearch)
        self.comboAccountNumber.currentTextChanged.connect(ShowTransactions.onComboTextChanged)
        self.comboHeadName.currentTextChanged.connect(ShowTransactions.onComboTextChanged)
        self.comboTransDate.currentTextChanged.connect(ShowTransactions.onComboTextChanged)
        self.buttonBack.clicked.connect(ShowTransactions.close)
        self.radioAll.toggled.connect(ShowTransactions.onSelectTransactionType)
        self.radioReceipts.toggled.connect(ShowTransactions.onSelectTransactionType)
        self.radioPayments.toggled.connect(ShowTransactions.onSelectTransactionType)
        self.buttonDownload.clicked.connect(ShowTransactions.downloadPDF)

        self.buttonSearch.setDefault(True)
        self.buttonDownload.setDefault(True)
        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ShowTransactions)
    # setupUi

    def retranslateUi(self, ShowTransactions):
        ShowTransactions.setWindowTitle(QCoreApplication.translate("ShowTransactions", u"Transactions", None))
        self.groupRadio.setTitle(QCoreApplication.translate("ShowTransactions", u"Select Transaction Type", None))
        self.radioAll.setText(QCoreApplication.translate("ShowTransactions", u"All", None))
        self.radioReceipts.setText(QCoreApplication.translate("ShowTransactions", u"Receipt", None))
        self.radioPayments.setText(QCoreApplication.translate("ShowTransactions", u"Payment", None))
        self.labelAccountNumber.setText(QCoreApplication.translate("ShowTransactions", u"Account Number", None))
        self.comboAccountNumber.setPlaceholderText(QCoreApplication.translate("ShowTransactions", u"-----select account-----", None))
        self.labelHeadName.setText(QCoreApplication.translate("ShowTransactions", u"Transaction Head", None))
        self.comboHeadName.setPlaceholderText(QCoreApplication.translate("ShowTransactions", u"-----select head-----", None))
        self.labelTransDate.setText(QCoreApplication.translate("ShowTransactions", u"Transaction Date", None))
        self.comboTransDate.setPlaceholderText(QCoreApplication.translate("ShowTransactions", u"-----Select  date-----", None))
        self.buttonSearch.setText(QCoreApplication.translate("ShowTransactions", u"&Search", None))
        self.buttonDownload.setText(QCoreApplication.translate("ShowTransactions", u"&Download", None))
        self.buttonBack.setText(QCoreApplication.translate("ShowTransactions", u"&Back", None))
        self.labelAccount.setText(QCoreApplication.translate("ShowTransactions", u"A/c No", None))
        self.editAccount.setText(QCoreApplication.translate("ShowTransactions", u"All", None))
        self.labelHead.setText(QCoreApplication.translate("ShowTransactions", u"Head", None))
        self.editHead.setText(QCoreApplication.translate("ShowTransactions", u"All", None))
        self.labelDate.setText(QCoreApplication.translate("ShowTransactions", u"Date", None))
        self.editDate.setText(QCoreApplication.translate("ShowTransactions", u"All", None))
        self.labelTotal.setText(QCoreApplication.translate("ShowTransactions", u"Total", None))
        self.editTotal.setText(QCoreApplication.translate("ShowTransactions", u"0", None))
    # retranslateUi

