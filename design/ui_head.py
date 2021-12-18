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
        HeadWindow.resize(565, 434)
        font = QFont()
        HeadWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        HeadWindow.setWindowIcon(icon)
        HeadWindow.setStyleSheet(u"")
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
        self.labelMessage.setStyleSheet(u"color: rgb(0, 139, 139);\n"
"background-color: rgb(245, 245, 245);")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(10)

        self.verticalLayout.addWidget(self.labelMessage)

        self.labelHeading = QLabel(HeadWindow)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelHeading.setFont(font1)
        self.labelHeading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 112);")
        self.labelHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelHeading.setMargin(10)

        self.verticalLayout.addWidget(self.labelHeading)

        self.comboLayout = QHBoxLayout()
        self.comboLayout.setSpacing(0)
        self.comboLayout.setObjectName(u"comboLayout")
        self.comboLayout.setContentsMargins(50, 10, 50, 10)
        self.comboHead = QComboBox(HeadWindow)
        self.comboHead.setObjectName(u"comboHead")
        self.comboHead.setMinimumSize(QSize(200, 40))
        self.comboHead.setMaximumSize(QSize(350, 16777215))
        self.comboHead.setFont(font)
        self.comboHead.setAutoFillBackground(False)
        self.comboHead.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"selection-background-color: rgb(64, 107, 191);\n"
"selection-color: rgb(255, 255, 255);")

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
        self.editHeadName.setMinimumSize(QSize(200, 40))
        self.editHeadName.setFont(font)
        self.editHeadName.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"")
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
        self.comboHeadType.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"selection-background-color: rgb(64, 107, 191);\n"
"selection-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboHeadType)

        self.editHeadType = QLineEdit(HeadWindow)
        self.editHeadType.setObjectName(u"editHeadType")
        self.editHeadType.setMinimumSize(QSize(200, 40))
        self.editHeadType.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"")
        self.editHeadType.setMaxLength(32)
        self.editHeadType.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editHeadType)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(5)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(50, 0, 50, 50)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(HeadWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.buttonBack.setFont(font2)
        self.buttonBack.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(HeadWindow)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(100, 30))
        self.buttonCancel.setMaximumSize(QSize(100, 30))
        self.buttonCancel.setFont(font2)
        self.buttonCancel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(HeadWindow)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(100, 30))
        self.buttonOk.setMaximumSize(QSize(100, 30))
        self.buttonOk.setFont(font2)
        self.buttonOk.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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

