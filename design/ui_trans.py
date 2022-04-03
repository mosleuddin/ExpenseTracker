# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from src import resource

class Ui_TransactionWindow(object):
    def setupUi(self, TransactionWindow):
        if not TransactionWindow.objectName():
            TransactionWindow.setObjectName(u"TransactionWindow")
        TransactionWindow.setWindowModality(Qt.ApplicationModal)
        TransactionWindow.resize(807, 564)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TransactionWindow.sizePolicy().hasHeightForWidth())
        TransactionWindow.setSizePolicy(sizePolicy)
        font = QFont()
        TransactionWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        TransactionWindow.setWindowIcon(icon)
        TransactionWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(239, 224, 200);\n"
"}\n"
"\n"
"QComboBox{\n"
"width: 150px;\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(32, 74, 135);\n"
"}\n"
"\n"
"QLineEdit{\n"
"width: 150px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#labelMessage{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 139, 139);\n"
"}\n"
"\n"
"#centralWidget{\n"
"background-color: #343b47;\n"
"}\n"
"")
        TransactionWindow.setModal(True)
        self.verticalLayout_4 = QVBoxLayout(TransactionWindow)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 10)
        self.centralWidget = QWidget(TransactionWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frameLabels = QFrame(self.centralWidget)
        self.frameLabels.setObjectName(u"frameLabels")
        self.frameLabels.setFrameShape(QFrame.StyledPanel)
        self.frameLabels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameLabels)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.labelMessage = QLabel(self.frameLabels)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setMinimumSize(QSize(0, 0))
        self.labelMessage.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.labelMessage.setFont(font1)
        self.labelMessage.setStyleSheet(u"")
        self.labelMessage.setAlignment(Qt.AlignCenter)
        self.labelMessage.setMargin(0)

        self.verticalLayout_3.addWidget(self.labelMessage)

        self.labelHeading = QLabel(self.frameLabels)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setMinimumSize(QSize(0, 0))
        self.labelHeading.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(False)
        self.labelHeading.setFont(font2)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(0)

        self.verticalLayout_3.addWidget(self.labelHeading)


        self.verticalLayout.addWidget(self.frameLabels)

        self.frameSearch = QFrame(self.centralWidget)
        self.frameSearch.setObjectName(u"frameSearch")
        self.frameSearch.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.frameSearch)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horSpacer4 = QSpacerItem(169, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horSpacer4)

        self.labelTransId = QLabel(self.frameSearch)
        self.labelTransId.setObjectName(u"labelTransId")
        self.labelTransId.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.labelTransId)

        self.editTransId = QLineEdit(self.frameSearch)
        self.editTransId.setObjectName(u"editTransId")
        self.editTransId.setMinimumSize(QSize(0, 30))
        self.editTransId.setStyleSheet(u"")
        self.editTransId.setMaxLength(40)
        self.editTransId.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.editTransId)

        self.buttonSearch = QPushButton(self.frameSearch)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setEnabled(False)
        self.buttonSearch.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.buttonSearch)

        self.horSpacer3 = QSpacerItem(169, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horSpacer3)


        self.verticalLayout.addWidget(self.frameSearch)

        self.frameDetails = QFrame(self.centralWidget)
        self.frameDetails.setObjectName(u"frameDetails")
        self.verticalLayout_2 = QVBoxLayout(self.frameDetails)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameDetailsTop = QFrame(self.frameDetails)
        self.frameDetailsTop.setObjectName(u"frameDetailsTop")
        self.horizontalLayout_4 = QHBoxLayout(self.frameDetailsTop)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelTransDate = QLabel(self.frameDetailsTop)
        self.labelTransDate.setObjectName(u"labelTransDate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTransDate.sizePolicy().hasHeightForWidth())
        self.labelTransDate.setSizePolicy(sizePolicy1)
        self.labelTransDate.setMinimumSize(QSize(100, 0))
        self.labelTransDate.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.labelTransDate)

        self.dateTrans = QDateEdit(self.frameDetailsTop)
        self.dateTrans.setObjectName(u"dateTrans")
        sizePolicy1.setHeightForWidth(self.dateTrans.sizePolicy().hasHeightForWidth())
        self.dateTrans.setSizePolicy(sizePolicy1)
        self.dateTrans.setMinimumSize(QSize(200, 0))
        self.dateTrans.setMaximumSize(QSize(200, 16777215))
        self.dateTrans.setStyleSheet(u"")
        self.dateTrans.setInputMethodHints(Qt.ImhDate)
        self.dateTrans.setWrapping(False)
        self.dateTrans.setFrame(True)
        self.dateTrans.setReadOnly(False)
        self.dateTrans.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateTrans.setSpecialValueText(u"")
        self.dateTrans.setProperty("showGroupSeparator", False)
        self.dateTrans.setMaximumDateTime(QDateTime(QDate(2100, 12, 31), QTime(23, 59, 59)))
        self.dateTrans.setMinimumDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.dateTrans.setMaximumDate(QDate(2100, 12, 31))
        self.dateTrans.setMinimumDate(QDate(2022, 1, 1))
        self.dateTrans.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTrans.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateTrans)

        self.labelHead = QLabel(self.frameDetailsTop)
        self.labelHead.setObjectName(u"labelHead")
        sizePolicy1.setHeightForWidth(self.labelHead.sizePolicy().hasHeightForWidth())
        self.labelHead.setSizePolicy(sizePolicy1)
        self.labelHead.setMinimumSize(QSize(100, 0))
        self.labelHead.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.labelHead.setFont(font3)

        self.horizontalLayout_4.addWidget(self.labelHead)

        self.comboHead = QComboBox(self.frameDetailsTop)
        self.comboHead.setObjectName(u"comboHead")
        sizePolicy1.setHeightForWidth(self.comboHead.sizePolicy().hasHeightForWidth())
        self.comboHead.setSizePolicy(sizePolicy1)
        self.comboHead.setMinimumSize(QSize(200, 0))
        self.comboHead.setMaximumSize(QSize(200, 16777215))
        self.comboHead.setStyleSheet(u"")
        self.comboHead.setMaxCount(500)

        self.horizontalLayout_4.addWidget(self.comboHead)


        self.verticalLayout_2.addWidget(self.frameDetailsTop)

        self.frameDetailsBottom = QFrame(self.frameDetails)
        self.frameDetailsBottom.setObjectName(u"frameDetailsBottom")
        self.horizontalLayout_2 = QHBoxLayout(self.frameDetailsBottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelTransDetails = QLabel(self.frameDetailsBottom)
        self.labelTransDetails.setObjectName(u"labelTransDetails")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelTransDetails.sizePolicy().hasHeightForWidth())
        self.labelTransDetails.setSizePolicy(sizePolicy2)
        self.labelTransDetails.setMinimumSize(QSize(100, 0))
        self.labelTransDetails.setMaximumSize(QSize(100, 16777215))
        self.labelTransDetails.setFont(font3)

        self.horizontalLayout_2.addWidget(self.labelTransDetails)

        self.editTransDetails = QLineEdit(self.frameDetailsBottom)
        self.editTransDetails.setObjectName(u"editTransDetails")
        sizePolicy1.setHeightForWidth(self.editTransDetails.sizePolicy().hasHeightForWidth())
        self.editTransDetails.setSizePolicy(sizePolicy1)
        self.editTransDetails.setMinimumSize(QSize(200, 0))
        self.editTransDetails.setMaximumSize(QSize(200, 16777215))
        self.editTransDetails.setFont(font3)
        self.editTransDetails.setStyleSheet(u"")
        self.editTransDetails.setInputMethodHints(Qt.ImhNone)
        self.editTransDetails.setMaxLength(40)

        self.horizontalLayout_2.addWidget(self.editTransDetails)

        self.labelAccount = QLabel(self.frameDetailsBottom)
        self.labelAccount.setObjectName(u"labelAccount")
        sizePolicy1.setHeightForWidth(self.labelAccount.sizePolicy().hasHeightForWidth())
        self.labelAccount.setSizePolicy(sizePolicy1)
        self.labelAccount.setMinimumSize(QSize(100, 0))
        self.labelAccount.setMaximumSize(QSize(100, 16777215))
        self.labelAccount.setFont(font3)

        self.horizontalLayout_2.addWidget(self.labelAccount)

        self.comboAccount = QComboBox(self.frameDetailsBottom)
        self.comboAccount.setObjectName(u"comboAccount")
        sizePolicy1.setHeightForWidth(self.comboAccount.sizePolicy().hasHeightForWidth())
        self.comboAccount.setSizePolicy(sizePolicy1)
        self.comboAccount.setMinimumSize(QSize(200, 0))
        self.comboAccount.setMaximumSize(QSize(200, 16777215))
        self.comboAccount.setFont(font3)
        self.comboAccount.setStyleSheet(u"")
        self.comboAccount.setInputMethodHints(Qt.ImhNone)
        self.comboAccount.setMaxCount(500)
        self.comboAccount.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.comboAccount)


        self.verticalLayout_2.addWidget(self.frameDetailsBottom)


        self.verticalLayout.addWidget(self.frameDetails)

        self.frameAccount = QFrame(self.centralWidget)
        self.frameAccount.setObjectName(u"frameAccount")
        self.horizontalLayout_3 = QHBoxLayout(self.frameAccount)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horSpacer5 = QSpacerItem(179, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horSpacer5)

        self.labelCustomerName = QLabel(self.frameAccount)
        self.labelCustomerName.setObjectName(u"labelCustomerName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelCustomerName.sizePolicy().hasHeightForWidth())
        self.labelCustomerName.setSizePolicy(sizePolicy3)
        self.labelCustomerName.setMinimumSize(QSize(0, 30))
        self.labelCustomerName.setStyleSheet(u"color: rgb(32, 74, 135);\n"
"")

        self.horizontalLayout_3.addWidget(self.labelCustomerName)

        self.horizontalSpacer_3 = QSpacerItem(180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.labelBankName = QLabel(self.frameAccount)
        self.labelBankName.setObjectName(u"labelBankName")
        sizePolicy3.setHeightForWidth(self.labelBankName.sizePolicy().hasHeightForWidth())
        self.labelBankName.setSizePolicy(sizePolicy3)
        self.labelBankName.setMinimumSize(QSize(0, 30))
        self.labelBankName.setStyleSheet(u"color: rgb(32, 74, 135);\n"
"")

        self.horizontalLayout_3.addWidget(self.labelBankName)

        self.horizontalSpacer = QSpacerItem(179, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frameAccount)

        self.frameAmount = QFrame(self.centralWidget)
        self.frameAmount.setObjectName(u"frameAmount")
        sizePolicy.setHeightForWidth(self.frameAmount.sizePolicy().hasHeightForWidth())
        self.frameAmount.setSizePolicy(sizePolicy)
        self.frameAmount.setMinimumSize(QSize(0, 0))
        self.frameAmount.setMaximumSize(QSize(16777215, 16777215))
        self.amountLayout = QHBoxLayout(self.frameAmount)
        self.amountLayout.setSpacing(0)
        self.amountLayout.setObjectName(u"amountLayout")
        self.amountLayout.setContentsMargins(50, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.amountLayout.addItem(self.horizontalSpacer_5)

        self.labelTransAmount = QLabel(self.frameAmount)
        self.labelTransAmount.setObjectName(u"labelTransAmount")
        sizePolicy1.setHeightForWidth(self.labelTransAmount.sizePolicy().hasHeightForWidth())
        self.labelTransAmount.setSizePolicy(sizePolicy1)
        self.labelTransAmount.setMinimumSize(QSize(100, 0))
        self.labelTransAmount.setMaximumSize(QSize(100, 16777215))
        self.labelTransAmount.setFont(font3)

        self.amountLayout.addWidget(self.labelTransAmount, 0, Qt.AlignLeft)

        self.editTransAmount = QLineEdit(self.frameAmount)
        self.editTransAmount.setObjectName(u"editTransAmount")
        sizePolicy1.setHeightForWidth(self.editTransAmount.sizePolicy().hasHeightForWidth())
        self.editTransAmount.setSizePolicy(sizePolicy1)
        self.editTransAmount.setMinimumSize(QSize(200, 0))
        self.editTransAmount.setMaximumSize(QSize(200, 16777215))
        self.editTransAmount.setFont(font3)
        self.editTransAmount.setStyleSheet(u"")
        self.editTransAmount.setInputMethodHints(Qt.ImhNone)
        self.editTransAmount.setMaxLength(40)

        self.amountLayout.addWidget(self.editTransAmount, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.amountLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frameAmount)

        self.frameButton = QFrame(self.centralWidget)
        self.frameButton.setObjectName(u"frameButton")
        self.buttonLayout = QHBoxLayout(self.frameButton)
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 0, 40, 0)
        self.horSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horSpacer2)

        self.buttonBack = QPushButton(self.frameButton)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.buttonBack.setFont(font4)
        self.buttonBack.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon1)
        self.buttonBack.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonBack)

        self.buttonCancel = QPushButton(self.frameButton)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setEnabled(True)
        self.buttonCancel.setMinimumSize(QSize(100, 30))
        self.buttonCancel.setMaximumSize(QSize(100, 30))
        self.buttonCancel.setFont(font4)
        self.buttonCancel.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCancel.setIcon(icon2)
        self.buttonCancel.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonCancel)

        self.buttonOk = QPushButton(self.frameButton)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setEnabled(False)
        self.buttonOk.setMinimumSize(QSize(100, 30))
        self.buttonOk.setMaximumSize(QSize(100, 30))
        self.buttonOk.setFont(font4)
        self.buttonOk.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonOk.setIcon(icon3)
        self.buttonOk.setAutoDefault(True)

        self.buttonLayout.addWidget(self.buttonOk)


        self.verticalLayout.addWidget(self.frameButton)


        self.verticalLayout_4.addWidget(self.centralWidget)

#if QT_CONFIG(shortcut)
        self.labelTransId.setBuddy(self.editTransId)
        self.labelTransDate.setBuddy(self.dateTrans)
        self.labelHead.setBuddy(self.comboHead)
        self.labelTransDetails.setBuddy(self.editTransDetails)
        self.labelAccount.setBuddy(self.comboAccount)
        self.labelTransAmount.setBuddy(self.editTransAmount)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(TransactionWindow)
        self.editTransId.textEdited.connect(TransactionWindow.onTextChanged)
        self.buttonSearch.clicked.connect(TransactionWindow.onSearchClicked)
        self.dateTrans.userDateChanged.connect(TransactionWindow.onDateChanged)
        self.editTransDetails.textEdited.connect(TransactionWindow.onTextEdited)
        self.comboHead.currentIndexChanged.connect(TransactionWindow.onIndexChanged)
        self.comboAccount.currentIndexChanged.connect(TransactionWindow.onIndexChanged)
        self.editTransAmount.textEdited.connect(TransactionWindow.onTextEdited)
        self.buttonBack.clicked.connect(TransactionWindow.close)
        self.buttonCancel.clicked.connect(TransactionWindow.onCancelPressed)
        self.buttonOk.clicked.connect(TransactionWindow.onOkPressed)

        self.buttonBack.setDefault(False)
        self.buttonCancel.setDefault(False)
        self.buttonOk.setDefault(True)


        QMetaObject.connectSlotsByName(TransactionWindow)
    # setupUi

    def retranslateUi(self, TransactionWindow):
        TransactionWindow.setWindowTitle(QCoreApplication.translate("TransactionWindow", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("TransactionWindow", u"TextLabel", None))
        self.labelHeading.setText(QCoreApplication.translate("TransactionWindow", u" Expenditure", None))
        self.labelTransId.setText(QCoreApplication.translate("TransactionWindow", u"&Enter Transaction ID ", None))
        self.editTransId.setPlaceholderText(QCoreApplication.translate("TransactionWindow", u"Enter Transaction ID", None))
        self.buttonSearch.setText(QCoreApplication.translate("TransactionWindow", u"&Search", None))
        self.labelTransDate.setText(QCoreApplication.translate("TransactionWindow", u"&Date", None))
        self.dateTrans.setDisplayFormat(QCoreApplication.translate("TransactionWindow", u"dd-MM-yyyy", None))
        self.labelHead.setText(QCoreApplication.translate("TransactionWindow", u"&Head", None))
        self.comboHead.setCurrentText("")
        self.comboHead.setPlaceholderText(QCoreApplication.translate("TransactionWindow", u"Select transaction head", None))
        self.labelTransDetails.setText(QCoreApplication.translate("TransactionWindow", u"&Trans. Details", None))
        self.editTransDetails.setPlaceholderText(QCoreApplication.translate("TransactionWindow", u"Enter transaction details", None))
        self.labelAccount.setText(QCoreApplication.translate("TransactionWindow", u"Account &No.", None))
        self.comboAccount.setPlaceholderText(QCoreApplication.translate("TransactionWindow", u"Select bank account number", None))
        self.labelCustomerName.setText(QCoreApplication.translate("TransactionWindow", u"Customer Name", None))
        self.labelBankName.setText(QCoreApplication.translate("TransactionWindow", u"Bank Name", None))
        self.labelTransAmount.setText(QCoreApplication.translate("TransactionWindow", u"A&mount", None))
        self.editTransAmount.setPlaceholderText(QCoreApplication.translate("TransactionWindow", u"Enter amount", None))
        self.buttonBack.setText(QCoreApplication.translate("TransactionWindow", u"&Back", None))
        self.buttonCancel.setText(QCoreApplication.translate("TransactionWindow", u"&Cancel", None))
        self.buttonOk.setText(QCoreApplication.translate("TransactionWindow", u"&Ok", None))
    # retranslateUi

