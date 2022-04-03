# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'period_mismatch.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDateTimeEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from src import resource

class Ui_PeriodMismatch(object):
    def setupUi(self, PeriodMismatch):
        if not PeriodMismatch.objectName():
            PeriodMismatch.setObjectName(u"PeriodMismatch")
        PeriodMismatch.setWindowModality(Qt.ApplicationModal)
        PeriodMismatch.resize(992, 596)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PeriodMismatch.sizePolicy().hasHeightForWidth())
        PeriodMismatch.setSizePolicy(sizePolicy)
        PeriodMismatch.setMinimumSize(QSize(0, 30))
        font = QFont()
        PeriodMismatch.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        PeriodMismatch.setWindowIcon(icon)
        PeriodMismatch.setStyleSheet(u"*{\n"
"background-color: rgb(200, 200, 200);\n"
"\n"
"}\n"
"\n"
"#centralWidget{\n"
"background-color: #343b47;\n"
"}\n"
"\n"
"#labelMessage{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 139, 139);\n"
"}\n"
"\n"
"\n"
"\n"
"QDateEdit{\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	width: 125px;\n"
"	height: 30px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 15px;\n"
"	color: rgb(255,255, 255);\n"
"	background-color: rgb(0, 30, 100);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(130, 30, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"#frameDelete QPushButton{\n"
"	width: 0px;\n"
"	height: 30px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	margin: 10px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 15px;\n"
"    background-color: rgb(200, 200, 200);"
                        "\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"#frameDelete QPushButton::hover{\n"
"	background-color: rgb(130, 30, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"#frameDelete QPushButton::disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"\n"
"#frameSaveCancel QPushButton{\n"
"	width: 100px;\n"
"	height: 30px;\n"
"	text-align: center;\n"
"	padding: 5px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 15px;\n"
"    background-color: rgb(200, 200, 200);\n"
"	color: rgb(10, 75, 0);\n"
"}\n"
"\n"
"#frameSaveCancel QPushButton::hover{\n"
"	background-color: rgb(130, 30, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"#frameSaveCancel QPushButton::disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(136, 138, 133);\n"
"}")
        PeriodMismatch.setModal(True)
        self.verticalLayout_5 = QVBoxLayout(PeriodMismatch)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.centralWidget = QWidget(PeriodMismatch)
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
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setUnderline(False)
        self.labelHeading.setFont(font2)
        self.labelHeading.setStyleSheet(u"")
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.labelHeading.setMargin(0)

        self.verticalLayout_3.addWidget(self.labelHeading)


        self.verticalLayout.addWidget(self.frameLabels)

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
        self.labelTransDate.setMinimumSize(QSize(100, 30))
        self.labelTransDate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.labelTransDate)

        self.dateTrans = QDateEdit(self.frameDetailsTop)
        self.dateTrans.setObjectName(u"dateTrans")
        sizePolicy1.setHeightForWidth(self.dateTrans.sizePolicy().hasHeightForWidth())
        self.dateTrans.setSizePolicy(sizePolicy1)
        self.dateTrans.setMinimumSize(QSize(200, 30))
        self.dateTrans.setMaximumSize(QSize(200, 30))
        self.dateTrans.setStyleSheet(u"")
        self.dateTrans.setInputMethodHints(Qt.ImhDate)
        self.dateTrans.setWrapping(False)
        self.dateTrans.setFrame(True)
        self.dateTrans.setReadOnly(False)
        self.dateTrans.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateTrans.setSpecialValueText(u"")
        self.dateTrans.setProperty("showGroupSeparator", False)
        self.dateTrans.setMaximumDate(QDate(9999, 12, 31))
        self.dateTrans.setMinimumDate(QDate(1752, 9, 14))
        self.dateTrans.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTrans.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateTrans)

        self.labelHead = QLabel(self.frameDetailsTop)
        self.labelHead.setObjectName(u"labelHead")
        sizePolicy1.setHeightForWidth(self.labelHead.sizePolicy().hasHeightForWidth())
        self.labelHead.setSizePolicy(sizePolicy1)
        self.labelHead.setMinimumSize(QSize(100, 30))
        self.labelHead.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.labelHead.setFont(font3)

        self.horizontalLayout_4.addWidget(self.labelHead)

        self.editHead = QLineEdit(self.frameDetailsTop)
        self.editHead.setObjectName(u"editHead")
        self.editHead.setEnabled(True)
        self.editHead.setMinimumSize(QSize(200, 30))
        self.editHead.setMaximumSize(QSize(200, 30))
        self.editHead.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.editHead)


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
        self.labelTransDetails.setMinimumSize(QSize(100, 30))
        self.labelTransDetails.setMaximumSize(QSize(100, 30))
        self.labelTransDetails.setFont(font3)

        self.horizontalLayout_2.addWidget(self.labelTransDetails)

        self.editTransDetails = QLineEdit(self.frameDetailsBottom)
        self.editTransDetails.setObjectName(u"editTransDetails")
        self.editTransDetails.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.editTransDetails.sizePolicy().hasHeightForWidth())
        self.editTransDetails.setSizePolicy(sizePolicy1)
        self.editTransDetails.setMinimumSize(QSize(200, 30))
        self.editTransDetails.setMaximumSize(QSize(200, 30))
        self.editTransDetails.setFont(font3)
        self.editTransDetails.setStyleSheet(u"")
        self.editTransDetails.setInputMethodHints(Qt.ImhNone)
        self.editTransDetails.setMaxLength(40)
        self.editTransDetails.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.editTransDetails)

        self.labelAccount = QLabel(self.frameDetailsBottom)
        self.labelAccount.setObjectName(u"labelAccount")
        sizePolicy1.setHeightForWidth(self.labelAccount.sizePolicy().hasHeightForWidth())
        self.labelAccount.setSizePolicy(sizePolicy1)
        self.labelAccount.setMinimumSize(QSize(100, 30))
        self.labelAccount.setMaximumSize(QSize(100, 30))
        self.labelAccount.setFont(font3)

        self.horizontalLayout_2.addWidget(self.labelAccount)

        self.editAccount = QLineEdit(self.frameDetailsBottom)
        self.editAccount.setObjectName(u"editAccount")
        self.editAccount.setEnabled(True)
        self.editAccount.setMinimumSize(QSize(200, 30))
        self.editAccount.setMaximumSize(QSize(200, 30))
        self.editAccount.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.editAccount)


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
        self.labelCustomerName.setMaximumSize(QSize(16777215, 30))
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
        self.labelBankName.setMaximumSize(QSize(16777215, 30))
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
        self.labelTransAmount.setMinimumSize(QSize(100, 30))
        self.labelTransAmount.setMaximumSize(QSize(100, 30))
        self.labelTransAmount.setFont(font3)

        self.amountLayout.addWidget(self.labelTransAmount, 0, Qt.AlignLeft)

        self.editTransAmount = QLineEdit(self.frameAmount)
        self.editTransAmount.setObjectName(u"editTransAmount")
        self.editTransAmount.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.editTransAmount.sizePolicy().hasHeightForWidth())
        self.editTransAmount.setSizePolicy(sizePolicy1)
        self.editTransAmount.setMinimumSize(QSize(200, 30))
        self.editTransAmount.setMaximumSize(QSize(200, 30))
        self.editTransAmount.setFont(font3)
        self.editTransAmount.setStyleSheet(u"")
        self.editTransAmount.setInputMethodHints(Qt.ImhNone)
        self.editTransAmount.setMaxLength(40)
        self.editTransAmount.setReadOnly(True)

        self.amountLayout.addWidget(self.editTransAmount, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.amountLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frameAmount)

        self.frameButtons = QFrame(self.centralWidget)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.frameButtons)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frameDelete = QFrame(self.frameButtons)
        self.frameDelete.setObjectName(u"frameDelete")
        self.frameDelete.setMaximumSize(QSize(150, 300))
        self.frameDelete.setFrameShape(QFrame.StyledPanel)
        self.frameDelete.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameDelete)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.buttonDelete = QPushButton(self.frameDelete)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setEnabled(True)
        self.buttonDelete.setMinimumSize(QSize(0, 0))
        self.buttonDelete.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.buttonDelete.setFont(font4)
        self.buttonDelete.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDelete.setIcon(icon1)
        self.buttonDelete.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.buttonDelete)


        self.horizontalLayout_6.addWidget(self.frameDelete)

        self.frameSearchRecord = QFrame(self.frameButtons)
        self.frameSearchRecord.setObjectName(u"frameSearchRecord")
        self.frameSearchRecord.setFrameShape(QFrame.StyledPanel)
        self.frameSearchRecord.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSearchRecord)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 25, 0)
        self.buttonFirst = QPushButton(self.frameSearchRecord)
        self.buttonFirst.setObjectName(u"buttonFirst")
        self.buttonFirst.setEnabled(True)
        self.buttonFirst.setMinimumSize(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/first.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonFirst.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttonFirst)

        self.buttonPrevious = QPushButton(self.frameSearchRecord)
        self.buttonPrevious.setObjectName(u"buttonPrevious")
        self.buttonPrevious.setEnabled(True)
        self.buttonPrevious.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonPrevious.setIcon(icon3)

        self.horizontalLayout.addWidget(self.buttonPrevious)

        self.buttonNext = QPushButton(self.frameSearchRecord)
        self.buttonNext.setObjectName(u"buttonNext")
        self.buttonNext.setEnabled(True)
        self.buttonNext.setMinimumSize(QSize(0, 0))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonNext.setIcon(icon4)

        self.horizontalLayout.addWidget(self.buttonNext)

        self.buttonLast = QPushButton(self.frameSearchRecord)
        self.buttonLast.setObjectName(u"buttonLast")
        self.buttonLast.setEnabled(True)
        self.buttonLast.setMinimumSize(QSize(0, 0))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/last.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonLast.setIcon(icon5)

        self.horizontalLayout.addWidget(self.buttonLast)


        self.horizontalLayout_6.addWidget(self.frameSearchRecord)

        self.frameSaveCancel = QFrame(self.frameButtons)
        self.frameSaveCancel.setObjectName(u"frameSaveCancel")
        self.frameSaveCancel.setMaximumSize(QSize(150, 300))
        self.verticalLayout_4 = QVBoxLayout(self.frameSaveCancel)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 10, 0, 10)
        self.buttonUpdate = QPushButton(self.frameSaveCancel)
        self.buttonUpdate.setObjectName(u"buttonUpdate")
        self.buttonUpdate.setEnabled(False)
        self.buttonUpdate.setMinimumSize(QSize(0, 0))
        self.buttonUpdate.setMaximumSize(QSize(16777215, 16777215))
        self.buttonUpdate.setFont(font4)
        self.buttonUpdate.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonUpdate.setIcon(icon6)
        self.buttonUpdate.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.buttonUpdate)

        self.buttonReset = QPushButton(self.frameSaveCancel)
        self.buttonReset.setObjectName(u"buttonReset")
        self.buttonReset.setEnabled(False)
        self.buttonReset.setMinimumSize(QSize(0, 0))
        self.buttonReset.setMaximumSize(QSize(16777215, 16777215))
        self.buttonReset.setFont(font4)
        self.buttonReset.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonReset.setIcon(icon7)
        self.buttonReset.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.buttonReset)

        self.buttonClose = QPushButton(self.frameSaveCancel)
        self.buttonClose.setObjectName(u"buttonClose")
        self.buttonClose.setMinimumSize(QSize(0, 0))
        self.buttonClose.setMaximumSize(QSize(16777215, 16777215))
        self.buttonClose.setFont(font4)
        self.buttonClose.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClose.setIcon(icon8)
        self.buttonClose.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.buttonClose)


        self.horizontalLayout_6.addWidget(self.frameSaveCancel, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frameButtons)


        self.verticalLayout_5.addWidget(self.centralWidget)

#if QT_CONFIG(shortcut)
        self.labelTransDate.setBuddy(self.dateTrans)
        self.labelTransDetails.setBuddy(self.editTransDetails)
        self.labelTransAmount.setBuddy(self.editTransAmount)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(PeriodMismatch)
        self.dateTrans.userDateChanged.connect(PeriodMismatch.onDateChanged)
        self.buttonUpdate.clicked.connect(PeriodMismatch.onUpdate)
        self.buttonReset.clicked.connect(PeriodMismatch.onReset)
        self.buttonClose.clicked.connect(PeriodMismatch.close)
        self.buttonDelete.clicked.connect(PeriodMismatch.onDelete)
        self.buttonFirst.clicked.connect(PeriodMismatch.onFirst)
        self.buttonPrevious.clicked.connect(PeriodMismatch.onPrevious)
        self.buttonNext.clicked.connect(PeriodMismatch.onNext)
        self.buttonLast.clicked.connect(PeriodMismatch.onLast)

        self.buttonDelete.setDefault(True)
        self.buttonUpdate.setDefault(True)
        self.buttonReset.setDefault(False)
        self.buttonClose.setDefault(False)


        QMetaObject.connectSlotsByName(PeriodMismatch)
    # setupUi

    def retranslateUi(self, PeriodMismatch):
        PeriodMismatch.setWindowTitle(QCoreApplication.translate("PeriodMismatch", u"Expense Tracker", None))
        self.labelMessage.setText(QCoreApplication.translate("PeriodMismatch", u"TextLabel", None))
        self.labelHeading.setText(QCoreApplication.translate("PeriodMismatch", u"Transaction Date not matching with current period ", None))
        self.labelTransDate.setText(QCoreApplication.translate("PeriodMismatch", u"D&ate", None))
        self.dateTrans.setDisplayFormat(QCoreApplication.translate("PeriodMismatch", u"dd-MM-yyyy", None))
        self.labelHead.setText(QCoreApplication.translate("PeriodMismatch", u"Head", None))
        self.editHead.setPlaceholderText(QCoreApplication.translate("PeriodMismatch", u"head", None))
        self.labelTransDetails.setText(QCoreApplication.translate("PeriodMismatch", u"Trans. Details", None))
        self.editTransDetails.setPlaceholderText(QCoreApplication.translate("PeriodMismatch", u"transaction details", None))
        self.labelAccount.setText(QCoreApplication.translate("PeriodMismatch", u"Account No.", None))
        self.editAccount.setPlaceholderText(QCoreApplication.translate("PeriodMismatch", u"account number", None))
        self.labelCustomerName.setText(QCoreApplication.translate("PeriodMismatch", u"Customer Name", None))
        self.labelBankName.setText(QCoreApplication.translate("PeriodMismatch", u"Bank Name", None))
        self.labelTransAmount.setText(QCoreApplication.translate("PeriodMismatch", u"Amount", None))
        self.editTransAmount.setPlaceholderText(QCoreApplication.translate("PeriodMismatch", u"amount", None))
        self.buttonDelete.setText(QCoreApplication.translate("PeriodMismatch", u"&Delete", None))
        self.buttonFirst.setText(QCoreApplication.translate("PeriodMismatch", u"&First", None))
        self.buttonPrevious.setText(QCoreApplication.translate("PeriodMismatch", u"&Previous", None))
        self.buttonNext.setText(QCoreApplication.translate("PeriodMismatch", u"&Next", None))
        self.buttonLast.setText(QCoreApplication.translate("PeriodMismatch", u"&Last", None))
        self.buttonUpdate.setText(QCoreApplication.translate("PeriodMismatch", u"&Update", None))
        self.buttonReset.setText(QCoreApplication.translate("PeriodMismatch", u"&Reset", None))
        self.buttonClose.setText(QCoreApplication.translate("PeriodMismatch", u"&Close", None))
    # retranslateUi

