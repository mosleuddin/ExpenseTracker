# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_users.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_ShowUsers(object):
    def setupUi(self, ShowUsers):
        if not ShowUsers.objectName():
            ShowUsers.setObjectName(u"ShowUsers")
        ShowUsers.setWindowModality(Qt.WindowModal)
        ShowUsers.resize(716, 500)
        ShowUsers.setMinimumSize(QSize(700, 500))
        font = QFont()
        font.setPointSize(14)
        ShowUsers.setFont(font)
        ShowUsers.setStyleSheet(u"background-color: rgb(170, 176, 224);")
        ShowUsers.setModal(True)
        self.verticalLayout = QVBoxLayout(ShowUsers)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.labelHeading = QLabel(ShowUsers)
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

        self.tableWidget = QTableWidget(ShowUsers)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(500, 300))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(225, 225,225);")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 30, -1, -1)
        self.buttonBack = QPushButton(ShowUsers)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.buttonBack.setFont(font2)
        self.buttonBack.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ShowUsers)
        self.buttonBack.clicked.connect(ShowUsers.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ShowUsers)
    # setupUi

    def retranslateUi(self, ShowUsers):
        ShowUsers.setWindowTitle(QCoreApplication.translate("ShowUsers", u"Reset Credentials", None))
        self.labelHeading.setText(QCoreApplication.translate("ShowUsers", u"List of users", None))
        self.buttonBack.setText(QCoreApplication.translate("ShowUsers", u"&Back", None))
    # retranslateUi

