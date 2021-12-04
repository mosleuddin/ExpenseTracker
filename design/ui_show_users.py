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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelHeading = QLabel(ShowUsers)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(16)
        self.labelHeading.setFont(font1)
        self.labelHeading.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelHeading)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.tableWidget = QTableWidget(ShowUsers)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(500, 300))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.buttonBack = QPushButton(ShowUsers)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(150, 40))
        self.buttonBack.setFont(font)
        self.buttonBack.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.buttonBack)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(ShowUsers)
        self.buttonBack.clicked.connect(ShowUsers.close)

        QMetaObject.connectSlotsByName(ShowUsers)
    # setupUi

    def retranslateUi(self, ShowUsers):
        ShowUsers.setWindowTitle(QCoreApplication.translate("ShowUsers", u"Reset Credentials", None))
        self.labelHeading.setText(QCoreApplication.translate("ShowUsers", u"List of users", None))
        self.buttonBack.setText(QCoreApplication.translate("ShowUsers", u"&Back", None))
    # retranslateUi

