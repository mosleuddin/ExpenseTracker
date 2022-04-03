# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_opening_balance.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from src import resource

class Ui_ShowOpeningBalance(object):
    def setupUi(self, ShowOpeningBalance):
        if not ShowOpeningBalance.objectName():
            ShowOpeningBalance.setObjectName(u"ShowOpeningBalance")
        ShowOpeningBalance.setWindowModality(Qt.WindowModal)
        ShowOpeningBalance.resize(716, 500)
        ShowOpeningBalance.setMinimumSize(QSize(700, 500))
        font = QFont()
        ShowOpeningBalance.setFont(font)
        ShowOpeningBalance.setStyleSheet(u"\n"
"*{\n"
"border: none;\n"
"background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"\n"
"\n"
"#tableBalance\n"
"{\n"
"	\n"
"	background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(100, 100, 255);\n"
"    width: 75px;\n"
"	height: 15px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"#frameFooter QPushButton{\n"
"	width: 150px;\n"
"	height: 30px;\n"
"	text-align: center;\n"
"	padding: 5px, 10px;\n"
"	border: 2px solid #264BF6;\n"
"	border-radius: 15px;\n"
"    background-color: rgb(186, 189, 182);\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"#frameFooter QPushButton::hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"    color: white;\n"
"}")
        ShowOpeningBalance.setModal(True)
        self.verticalLayout = QVBoxLayout(ShowOpeningBalance)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(ShowOpeningBalance)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setFrameShape(QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameHeader)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frameHeader)

        self.frameBody = QFrame(ShowOpeningBalance)
        self.frameBody.setObjectName(u"frameBody")
        self.frameBody.setFrameShape(QFrame.NoFrame)
        self.frameBody.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frameBody)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 0)
        self.tableBalance = QTableWidget(self.frameBody)
        if (self.tableBalance.columnCount() < 5):
            self.tableBalance.setColumnCount(5)
        self.tableBalance.setObjectName(u"tableBalance")
        self.tableBalance.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(14)
        self.tableBalance.setFont(font1)
        self.tableBalance.setFrameShape(QFrame.HLine)
        self.tableBalance.setFrameShadow(QFrame.Raised)
        self.tableBalance.setLineWidth(1)
        self.tableBalance.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableBalance.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBalance.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableBalance.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBalance.setIconSize(QSize(16, 16))
        self.tableBalance.setColumnCount(5)
        self.tableBalance.horizontalHeader().setCascadingSectionResizes(False)
        self.tableBalance.horizontalHeader().setMinimumSectionSize(25)
        self.tableBalance.horizontalHeader().setHighlightSections(False)
        self.tableBalance.horizontalHeader().setStretchLastSection(True)
        self.tableBalance.verticalHeader().setVisible(False)
        self.tableBalance.verticalHeader().setCascadingSectionResizes(False)
        self.tableBalance.verticalHeader().setDefaultSectionSize(22)
        self.tableBalance.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.tableBalance)


        self.verticalLayout.addWidget(self.frameBody)

        self.frameFooter = QFrame(ShowOpeningBalance)
        self.frameFooter.setObjectName(u"frameFooter")
        self.horizontalLayout = QHBoxLayout(self.frameFooter)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 20, 15, 20)
        self.buttonBack = QPushButton(self.frameFooter)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        self.buttonBack.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)


        self.verticalLayout.addWidget(self.frameFooter, 0, Qt.AlignHCenter)


        self.retranslateUi(ShowOpeningBalance)
        self.buttonBack.clicked.connect(ShowOpeningBalance.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(ShowOpeningBalance)
    # setupUi

    def retranslateUi(self, ShowOpeningBalance):
        ShowOpeningBalance.setWindowTitle(QCoreApplication.translate("ShowOpeningBalance", u"Expense Tracker", None))
        self.buttonBack.setText(QCoreApplication.translate("ShowOpeningBalance", u"&Back", None))
    # retranslateUi

