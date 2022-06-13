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

from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QDialog

from design.ui_about import Ui_AboutWindow
from modules.module import resize_and_move


class About(QDialog):
    def __init__(self, parent):
        super(About, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        self.configTabs()
        resize_and_move(self, self.parent, .75, .8)
        self.show()

    def configTabs(self):
        text = open('LICENSE').read()
        self.ui.textLicense.setText(text)
        self.ui.textLicense.setVisible(False)
        self.ui.browserNotice.setViewportMargins(10, 5, 10, 10)

    def show_license(self):
        if self.ui.buttonLicense.isChecked():

            self.ui.buttonLicense.setCheckable(False)

            self.ui.browserNotice.setVisible(False)
            self.ui.textLicense.setVisible(True)

            self.ui.buttonLicense.setText('&Hide License')
            self.ui.buttonLicense.setIcon(QIcon('src/icons/notice.png'))
        else:
            self.ui.buttonLicense.setCheckable(True)

            self.ui.browserNotice.setVisible(True)
            self.ui.textLicense.setVisible(False)

            self.ui.buttonLicense.setText('&Show License')
            self.ui.buttonLicense.setIcon(QIcon('src/icons/license.png'))

    def open_website(self):
        url = QUrl('https://github.com/mosleuddin/ExpenseTracker.git')
        QDesktopServices.openUrl(url)
