# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'head.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src import resource

class Ui_HeadWindow(object):
    def setupUi(self, HeadWindow):
        if not HeadWindow.objectName():
            HeadWindow.setObjectName(u"HeadWindow")
        HeadWindow.setWindowModality(Qt.ApplicationModal)
        HeadWindow.resize(513, 532)
        font = QFont()
        HeadWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        HeadWindow.setWindowIcon(icon)
        HeadWindow.setStyleSheet(u"")
        HeadWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(HeadWindow)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelHeading = QLabel(HeadWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"color: rgb(51, 51, 51);\n"
"background-color: rgb(169, 216, 252);")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.labelMessage = QLabel(HeadWindow)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 40))
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet(u"color: rgb(102, 26, 216);")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.comboLayout = QHBoxLayout()
        self.comboLayout.setSpacing(10)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(25, 6, 25, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer)

        self.comboHead = QComboBox(HeadWindow)
        self.comboHead.setObjectName(u"comboHead")
        self.comboHead.setMinimumSize(QSize(0, 40))
        self.comboHead.setFont(font)
        self.comboHead.setStyleSheet(u"background-color: rgb(254, 255, 211);\n"
"color: rgb(51, 51, 51);")

        self.comboLayout.addWidget(self.comboHead)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.comboLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.comboLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(25, 6, 25, 6)
        self.labelHeadId = QLabel(HeadWindow)
        self.labelHeadId.setObjectName(u"labelHeadId")
        self.labelHeadId.setMinimumSize(QSize(0, 40))
        self.labelHeadId.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelHeadId)

        self.labelDispalyId = QLabel(HeadWindow)
        self.labelDispalyId.setObjectName(u"labelDispalyId")
        self.labelDispalyId.setMinimumSize(QSize(0, 40))
        self.labelDispalyId.setFont(font)
        self.labelDispalyId.setStyleSheet(u"color: rgb(102, 26, 216);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelDispalyId)

        self.labelHeadName = QLabel(HeadWindow)
        self.labelHeadName.setObjectName(u"labelHeadName")
        self.labelHeadName.setMinimumSize(QSize(0, 40))
        self.labelHeadName.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelHeadName)

        self.editHeadName = QLineEdit(HeadWindow)
        self.editHeadName.setObjectName(u"editHeadName")
        self.editHeadName.setMinimumSize(QSize(0, 40))
        self.editHeadName.setFont(font)
        self.editHeadName.setStyleSheet(u"background-color: rgb(254, 255, 211);\n"
"color: rgb(51, 51, 51);")
        self.editHeadName.setMaxLength(32)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editHeadName)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(25, 6, 25, 6)
        self.buttonBack = QPushButton(HeadWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.buttonBack.setFont(font2)
        self.buttonBack.setStyleSheet(u"background-color: rgb(10, 125, 130);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(HeadWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(0, 40))
        self.buttonCancel.setFont(font2)
        self.buttonCancel.setStyleSheet(u"background-color: rgb(10, 125, 130);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(HeadWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(0, 40))
        self.buttonOk.setFont(font2)
        self.buttonOk.setStyleSheet(u"background-color: rgb(10, 125, 130);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

#if QT_CONFIG(shortcut)
        self.labelHeadName.setBuddy(self.editHeadName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.editHeadName, self.buttonOk)
        QWidget.setTabOrder(self.buttonOk, self.buttonBack)

        self.retranslateUi(HeadWindow)
        self.buttonCancel.clicked.connect(HeadWindow.onDiscardPressed)
        self.comboHead.currentIndexChanged.connect(HeadWindow.onIndexChanged)
        self.buttonBack.clicked.connect(HeadWindow.close)
        self.editHeadName.textEdited.connect(HeadWindow.onTextEdited)
        self.buttonOk.clicked.connect(HeadWindow.onOkPressed)

        QMetaObject.connectSlotsByName(HeadWindow)
    # setupUi

    def retranslateUi(self, HeadWindow):
        HeadWindow.setWindowTitle(QCoreApplication.translate("HeadWindow", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("HeadWindow", u"<h2>Head\n"
"", None))
        self.labelMessage.setText(QCoreApplication.translate("HeadWindow", u"TextLabel", None))
        self.comboHead.setPlaceholderText(QCoreApplication.translate("HeadWindow", u"Select Head", None))
        self.labelHeadId.setText(QCoreApplication.translate("HeadWindow", u"Head ID", None))
        self.labelDispalyId.setText(QCoreApplication.translate("HeadWindow", u"TextLabel", None))
        self.labelHeadName.setText(QCoreApplication.translate("HeadWindow", u"Head &Name", None))
        self.editHeadName.setPlaceholderText(QCoreApplication.translate("HeadWindow", u"Enter head name", None))
        self.buttonBack.setText(QCoreApplication.translate("HeadWindow", u"&Back", None))
        self.buttonCancel.setText(QCoreApplication.translate("HeadWindow", u"&Cancel", None))
        self.buttonOk.setText(QCoreApplication.translate("HeadWindow", u"&Ok", None))
    # retranslateUi

