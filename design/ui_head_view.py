# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'head_view.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_ViewHead(object):
    def setupUi(self, ViewHead):
        if not ViewHead.objectName():
            ViewHead.setObjectName(u"ViewHead")
        ViewHead.setWindowModality(Qt.WindowModal)
        ViewHead.resize(693, 480)
        font = QFont()
        font.setPointSize(14)
        ViewHead.setFont(font)
        ViewHead.setStyleSheet(u"background-color: rgb(150, 175, 210);")
        ViewHead.setModal(True)
        self.verticalLayout = QVBoxLayout(ViewHead)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.labelHeading = QLabel(ViewHead)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.labelHeading)

        self.tableView = QTableView(ViewHead)
        self.tableView.setObjectName(u"tableView")
        font2 = QFont()
        font2.setPointSize(12)
        self.tableView.setFont(font2)
        self.tableView.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(ViewHead)
        self.buttonBack.setObjectName(u"buttonBack")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.buttonBack.setFont(font3)
        self.buttonBack.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ViewHead)
        self.buttonBack.clicked.connect(ViewHead.close)

        QMetaObject.connectSlotsByName(ViewHead)
    # setupUi

    def retranslateUi(self, ViewHead):
        ViewHead.setWindowTitle(QCoreApplication.translate("ViewHead", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("ViewHead", u"Expenditure Head", None))
        self.buttonBack.setText(QCoreApplication.translate("ViewHead", u"&Back", None))
    # retranslateUi

