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
        url = QUrl('https://github.com/mosleuddin/MyContacts.git')
        QDesktopServices.openUrl(url)
