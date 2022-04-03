# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans_view.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
from src import resource

class Ui_TransactionView(object):
    def setupUi(self, TransactionView):
        if not TransactionView.objectName():
            TransactionView.setObjectName(u"TransactionView")
        TransactionView.setWindowModality(Qt.WindowModal)
        TransactionView.resize(601, 480)
        font = QFont()
        font.setPointSize(14)
        TransactionView.setFont(font)
        TransactionView.setStyleSheet(u"background-color: rgb(238, 226,152);\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        TransactionView.setModal(True)
        self.verticalLayout = QVBoxLayout(TransactionView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.labelHeading = QLabel(TransactionView)
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

        self.tableView = QTableView(TransactionView)
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

        self.footer = QHBoxLayout()
        self.footer.setSpacing(10)
        self.footer.setObjectName(u"footer")
        self.footer.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footer.addItem(self.horizontalSpacer_2)

        self.labelReceiptTotal = QLabel(TransactionView)
        self.labelReceiptTotal.setObjectName(u"labelReceiptTotal")

        self.footer.addWidget(self.labelReceiptTotal)

        self.editReceiptTotal = QLineEdit(TransactionView)
        self.editReceiptTotal.setObjectName(u"editReceiptTotal")
        self.editReceiptTotal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Ubuntu\";")
        self.editReceiptTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editReceiptTotal.setReadOnly(True)

        self.footer.addWidget(self.editReceiptTotal)

        self.labelPaymentTotal = QLabel(TransactionView)
        self.labelPaymentTotal.setObjectName(u"labelPaymentTotal")

        self.footer.addWidget(self.labelPaymentTotal)

        self.editPaymentTotal = QLineEdit(TransactionView)
        self.editPaymentTotal.setObjectName(u"editPaymentTotal")
        self.editPaymentTotal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Ubuntu\";")
        self.editPaymentTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editPaymentTotal.setReadOnly(True)

        self.footer.addWidget(self.editPaymentTotal)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footer.addItem(self.horizontalSpacer)

        self.buttonBack = QPushButton(TransactionView)
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

        self.footer.addWidget(self.buttonBack)


        self.verticalLayout.addLayout(self.footer)


        self.retranslateUi(TransactionView)
        self.buttonBack.clicked.connect(TransactionView.close)

        self.buttonBack.setDefault(True)


        QMetaObject.connectSlotsByName(TransactionView)
    # setupUi

    def retranslateUi(self, TransactionView):
        TransactionView.setWindowTitle(QCoreApplication.translate("TransactionView", u"Expense Tracker", None))
        self.labelHeading.setText(QCoreApplication.translate("TransactionView", u"Transaction", None))
        self.labelReceiptTotal.setText(QCoreApplication.translate("TransactionView", u"Receipt Contra Total", None))
        self.editReceiptTotal.setText(QCoreApplication.translate("TransactionView", u"0", None))
        self.labelPaymentTotal.setText(QCoreApplication.translate("TransactionView", u"Payment Contra Total", None))
        self.editPaymentTotal.setText(QCoreApplication.translate("TransactionView", u"0", None))
        self.buttonBack.setText(QCoreApplication.translate("TransactionView", u"&Back", None))
    # retranslateUi

