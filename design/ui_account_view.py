# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_view.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_ViewAccount(object):
    def setupUi(self, ViewAccount):
        if not ViewAccount.objectName():
            ViewAccount.setObjectName(u"ViewAccount")
        ViewAccount.setWindowModality(Qt.WindowModal)
        ViewAccount.resize(601, 480)
        font = QFont()
        font.setPointSize(14)
        ViewAccount.setFont(font)
        ViewAccount.setStyleSheet(u"background-color: rgb(238, 226,152);")
        ViewAccount.setModal(True)
        self.verticalLayout = QVBoxLayout(ViewAccount)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.labelHeading = QLabel(ViewAccount)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 112);")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.tableView = QTableView(ViewAccount)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font)
        self.tableView.setStyleSheet(u"background-color: rgb(225, 225,225);")
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

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.buttonBack = QPushButton(ViewAccount)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        self.buttonBack.setFont(font2)
        self.buttonBack.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ViewAccount)
        self.buttonBack.clicked.connect(ViewAccount.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ViewAccount)
    # setupUi

    def retranslateUi(self, ViewAccount):
        ViewAccount.setWindowTitle(QCoreApplication.translate("ViewAccount", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("ViewAccount", u"Bank Accounts", None))
        self.buttonBack.setText(QCoreApplication.translate("ViewAccount", u"&Back", None))
    # retranslateUi

