import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QDialog, QLineEdit

from modules.module import resize_and_move
from design.ui_login import Ui_LoginWindow
from db.connect import createConnection
from db.table_user import userExist, createUser, checkCredentials
from views.home import Home


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.conn = None
        if not createConnection(self):
            sys.exit(1)

        self.main_window_open = False  # whether MainWindow is called or not
        self.initUI()             # set up ui and other related tasks

        # confirm whether users already created or not
        if not userExist(self):
            createUser(self)

        self.show()

    def initUI(self):
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        resize_and_move(self, wd=.5, ht=.7)
        self.ui.labelMessage.hide()
        self.ui.editUsername.addAction(QIcon("src/icons/user.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editPassword.addAction(QIcon("src/icons/password.png"), QLineEdit.ActionPosition.LeadingPosition)

        self.ui.editUsername.returnPressed.connect(lambda: self.function_return_pressed('user'))
        self.ui.editPassword.returnPressed.connect(lambda: self.function_return_pressed('pass'))

    def function_return_pressed(self, text):
        if text == 'user':
            self.ui.editPassword.setFocus()
        else:
            if self.ui.buttonOk.isEnabled():
                self.ui.buttonOk.setFocus()
            else:
                self.ui.editUsername.setFocus()

    def onLogin(self):
        # collect the username and the password submitted through the login form
        input_username = self.ui.editUsername.text()
        input_password = self.ui.editPassword.text()

        record = checkCredentials(self, input_username, input_password)

        if record:
            self.win = Home(conn=self.conn, user_id=record[0], user_name=record[1])
            self.main_window_open = True
            if record[1] != "admin":
                self.win.ui.action_Show_Users.setEnabled(False)
                self.win.ui.action_Data_Initialization.setEnabled(False)
            else:
                self.win.ui.action_Change_Username.setEnabled(False)

            self.close()

        else:
            self.ui.labelMessage.show()
            self.ui.editPassword.setText('')
            self.ui.editUsername.setFocus()
            self.ui.editUsername.end(False)

    def onTextChange(self, text):
        if text:
            self.ui.labelMessage.hide()
            self.ui.buttonOk.setEnabled(True)
        else:
            self.ui.buttonOk.setEnabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        if not self.main_window_open:
            self.conn.close()
            self.conn.setDatabaseName("")
            QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
        print('is database open while closing loginwindow? ', self.conn.isOpen())
        event.accept()
