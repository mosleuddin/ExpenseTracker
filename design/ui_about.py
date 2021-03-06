

"""
    Copyright © 2021-2022  Mosleuddin Sarkar

    This file is part of ExpenseTracker.

    ExpenseTracker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ExpenseTracker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ExpenseTracker.  If not, see <https://www.gnu.org/licenses/>.
"""


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
from src import resource

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(650, 500)
        AboutWindow.setMaximumSize(QSize(32000, 32000))
        font = QFont()
        AboutWindow.setFont(font)
        AboutWindow.setStyleSheet(u"*{\n"
"	background-color:#10141b;\n"
"	color: rgba(255, 255, 255, .75);\n"
"}\n"
"\n"
"#browserNotice,\n"
"#textLicense{\n"
"	background-color:#1f232a;\n"
"	color: rgba(255, 255, 255, .50);\n"
"\n"
"}\n"
"\n"
"\n"
"#buttonLicense:hover, #buttonWebsite:hover,  #buttonBack:hover{\n"
"			background-color:#1f232a;\n"
"}\n"
"")
        AboutWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(AboutWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AboutWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.tabApp = QWidget()
        self.tabApp.setObjectName(u"tabApp")
        self.tabApp.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(tooltip)
        self.tabApp.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabApp.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabApp.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.tabApp.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.tabApp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelAppImage = QLabel(self.tabApp)
        self.labelAppImage.setObjectName(u"labelAppImage")
        self.labelAppImage.setPixmap(QPixmap(u":/icons/icons/app_icon.png"))
        self.labelAppImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelAppImage)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.browserNotice = QTextBrowser(self.tabApp)
        self.browserNotice.setObjectName(u"browserNotice")
        self.browserNotice.setFont(font1)
        self.browserNotice.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.browserNotice.setStyleSheet(u"")
        self.browserNotice.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.browserNotice.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.browserNotice.setSource(QUrl(u"file:///home/mosley/Practice-Projects/ExpenseTracker/notice.html"))
        self.browserNotice.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.browserNotice)

        self.textLicense = QTextEdit(self.tabApp)
        self.textLicense.setObjectName(u"textLicense")
        self.textLicense.setFont(font)
        self.textLicense.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textLicense.setStyleSheet(u"")
        self.textLicense.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textLicense.setUndoRedoEnabled(False)
        self.textLicense.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textLicense)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonLicense = QPushButton(self.tabApp)
        self.buttonLicense.setObjectName(u"buttonLicense")
        self.buttonLicense.setMinimumSize(QSize(130, 30))
        self.buttonLicense.setMaximumSize(QSize(130, 30))
        self.buttonLicense.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/license.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonLicense.setIcon(icon)
        self.buttonLicense.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.buttonLicense)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        icon1 = QIcon()
        icon1.addFile(u":/icons/expense_tracker_sm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabApp, icon1, "")
        self.tabDev = QWidget()
        self.tabDev.setObjectName(u"tabDev")
        self.verticalLayout_4 = QVBoxLayout(self.tabDev)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.labelDevImage = QLabel(self.tabDev)
        self.labelDevImage.setObjectName(u"labelDevImage")
        self.labelDevImage.setFont(font1)
        self.labelDevImage.setAutoFillBackground(False)
        self.labelDevImage.setStyleSheet(u"")
        self.labelDevImage.setPixmap(QPixmap(u":/icons/icons/dev.jpg"))
        self.labelDevImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelDevImage)

        self.labelDevCaption = QLabel(self.tabDev)
        self.labelDevCaption.setObjectName(u"labelDevCaption")
        self.labelDevCaption.setFont(font1)
        self.labelDevCaption.setStyleSheet(u"")
        self.labelDevCaption.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelDevCaption)

        icon2 = QIcon()
        icon2.addFile(u":/icons/dev32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabDev, icon2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buttonWebsite = QPushButton(AboutWindow)
        self.buttonWebsite.setObjectName(u"buttonWebsite")
        self.buttonWebsite.setMinimumSize(QSize(100, 30))
        self.buttonWebsite.setMaximumSize(QSize(100, 30))
        self.buttonWebsite.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/website.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonWebsite.setIcon(icon3)

        self.horizontalLayout.addWidget(self.buttonWebsite)

        self.buttonBack = QPushButton(AboutWindow)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(100, 30))
        self.buttonBack.setMaximumSize(QSize(100, 30))
        self.buttonBack.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBack.setIcon(icon4)

        self.horizontalLayout.addWidget(self.buttonBack)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AboutWindow)
        self.buttonBack.clicked.connect(AboutWindow.close)
        self.buttonWebsite.clicked.connect(AboutWindow.open_website)
        self.buttonLicense.clicked.connect(AboutWindow.show_license)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About ExpenseTracker", None))
        self.labelAppImage.setText("")
        self.textLicense.setDocumentTitle("")
        self.textLicense.setMarkdown("")
        self.textLicense.setHtml(QCoreApplication.translate("AboutWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.buttonLicense.setText(QCoreApplication.translate("AboutWindow", u"&Show License", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabApp), QCoreApplication.translate("AboutWindow", u"&Application", None))
#if QT_CONFIG(tooltip)
        self.tabDev.setToolTip(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelDevImage.setText("")
        self.labelDevCaption.setText(QCoreApplication.translate("AboutWindow", u"Designed and Developed by Mosleuddin Sarkar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDev), QCoreApplication.translate("AboutWindow", u"&Developer", None))
        self.buttonWebsite.setText(QCoreApplication.translate("AboutWindow", u"&Website", None))
        self.buttonBack.setText(QCoreApplication.translate("AboutWindow", u"&Back", None))
    # retranslateUi

