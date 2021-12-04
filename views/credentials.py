from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit, QTableWidgetItem

from design.ui_credentials import Ui_CredentialsWindow
from db.table_user import changePassword, getPassword, changeUsername, viewUser, resetUserCredentials
from design.ui_show_users import Ui_ShowUsers
from modules.module import resize_and_move, CustomButton


class Credentials(QDialog):
    def __init__(self, *args, **kwargs):
        super(Credentials, self).__init__()
        self.ui = Ui_CredentialsWindow()
        self.ui.setupUi(self)
        self.ui.labelMessage.hide()
        self.show()

    def function_return_pressed(self, text):
        pass

    def onSubmit(self):
        pass

    def onTextChange(self, text):
        if text:
            self.ui.labelMessage.hide()
            self.ui.buttonSubmit.setEnabled(True)
        else:
            self.ui.buttonSubmit.setEnabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()


class ChangePassword(Credentials):
    def __init__(self, parent=None, user_id=None):
        super().__init__()
        self.parent = parent
        self.user_id = user_id
        resize_and_move(self, self.parent, .5, .7)
        self.show()

        self.ui.editCurrentPassword.addAction(QIcon("src/icons/password.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editNewPassword.addAction(QIcon("src/icons/password.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editConfirmPassword.addAction(QIcon("src/icons/password.png"), QLineEdit.ActionPosition.LeadingPosition)

        self.ui.editCurrentPassword.returnPressed.connect(lambda: self.function_return_pressed('current'))
        self.ui.editNewPassword.returnPressed.connect(lambda: self.function_return_pressed('new'))
        self.ui.editConfirmPassword.returnPressed.connect(lambda: self.function_return_pressed('confirm'))

    def function_return_pressed(self, text):
        if text == 'current':
            self.ui.editNewPassword.setFocus()
            self.ui.editNewPassword.end(False)

        elif text == 'new':
            self.ui.editConfirmPassword.setFocus()
            self.ui.editConfirmPassword.end(False)

        else:
            if self.ui.buttonSubmit.isEnabled():
                self.ui.buttonSubmit.setFocus()
            else:
                self.ui.editCurrentPassword.setFocus()
                self.ui.editCurrentPassword.end(False)

    def onSubmit(self):
        self.msg = ''
        password = getPassword(self, self.user_id)
        input_current_password = self.ui.editCurrentPassword.text().strip()
        input_new_password = self.ui.editNewPassword.text().strip()
        input_confirm_password = self.ui.editConfirmPassword.text().strip()

        if not input_current_password == password:
            self.msg = 'Incorrect Password'
            self.ui.editCurrentPassword.setFocus()

        elif len(input_new_password) < 4:
            self.msg = 'Length of Password should be 4 to 20 characters'
            self.ui.editNewPassword.setFocus()

        elif input_new_password != input_confirm_password:
            self.msg = 'Confirm Password does not match with the New Password'
            self.ui.editConfirmPassword.setFocus()

        elif input_new_password == input_current_password:
            self.msg = 'New Password must be different from the Current Password'
            self.ui.editNewPassword.setFocus()

        else:
            changePassword(self, self.user_id, input_new_password)
            self.close()

        self.ui.labelMessage.setText(self.msg)
        self.ui.labelMessage.setVisible(True)
        self.ui.editCurrentPassword.setText('')
        self.ui.editNewPassword.setText('')
        self.ui.editConfirmPassword.setText('')
        self.ui.editCurrentPassword.setFocus()


class ChangeUsername(Credentials):
    def __init__(self, parent=None, user_id=None, user_name=None):
        super().__init__()
        self.parent = parent
        self.user_id = user_id
        self.user_name = user_name
        resize_and_move(self, self.parent, .5, .7)
        self.setStyleSheet('background-color: rgb(153, 210, 255)')
        self.show()
        self.initUI()

    def initUI(self):
        self.editPassword = self.ui.editCurrentPassword
        self.editNewUsername = self.ui.editNewPassword
        self.editConfirmUsername = self.ui.editConfirmPassword

        self.editPassword.addAction(QIcon("src/icons/password.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.editNewUsername.addAction(QIcon("src/icons/user.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.editConfirmUsername.addAction(QIcon("src/icons/user.png"), QLineEdit.ActionPosition.LeadingPosition)

        self.editPassword.setPlaceholderText('Enter password')
        self.editNewUsername.setPlaceholderText('Create new username')
        self.editConfirmUsername.setPlaceholderText('Enter username again')

        self.editPassword.returnPressed.connect(lambda: self.function_return_pressed('password'))
        self.editNewUsername.returnPressed.connect(lambda: self.function_return_pressed('new'))
        self.editConfirmUsername.returnPressed.connect(lambda: self.function_return_pressed('confirm'))

        self.ui.labelHeading.setText('<h2>Change Username')
        self.ui.labelCurrentPassword.setText('Password')
        self.ui.labelNewPassword.setText('New Username')
        self.ui.labelConfirmPassword.setText('Confirm Username')

    def onSubmit(self):
        self.msg = ''
        password = getPassword(self, self.user_id)
        input_password = self.editPassword.text().strip()
        input_new_username = self.editNewUsername.text().strip()
        input_confirm_username = self.editConfirmUsername.text().strip()

        if len(input_new_username) < 4:
            self.msg = 'Length of username should be 4 to 12 characters\n'

        elif input_new_username == 'admin':
            self.msg = 'Username \'admin\' is not available.' \
                       '\nPlease select a different username\n'

        elif input_new_username == self.user_name:
            self.msg = f'\'{self.user_name}\' is your current username.' \
                       '\nYou may provide a different username\n'

        elif input_new_username != input_confirm_username:
            self.msg = 'Confirm username does not match with the New username\n'

        elif password != input_password:
            self.msg = 'Incorrect password\n'
            self.editPassword.setFocus()

        else:
            changeUsername(self, self.user_id, input_new_username)
            self.close()

        self.ui.labelMessage.setText(self.msg)
        self.ui.labelMessage.setVisible(True)
        self.editPassword.setText('')
        self.editNewUsername.setText('')
        self.editConfirmUsername.setText('')
        self.editPassword.setFocus()

    def function_return_pressed(self, text):
        if text == 'password':
            self.editNewUsername.setFocus()
            self.editNewUsername.end(False)

        elif text == 'new':
            self.editConfirmUsername.setFocus()
            self.editConfirmUsername.end(False)

        else:
            if self.ui.buttonSubmit.isEnabled():
                self.ui.buttonSubmit.setFocus()
            else:
                self.editPassword.setFocus()
                self.editPassword.end(False)


class ShowUsers(QDialog):
    def __init__(self, parent=None):
        super(ShowUsers, self).__init__(parent=parent)
        self.ui = Ui_ShowUsers()
        self.ui.setupUi(self)
        self.show()
        self.loadData()

    def loadData(self):
        self.ui.tableWidget.clear()
        headers = ['Userid', 'Username', 'Value', 'Reset']
        users = viewUser(self)

        rows = len(users)
        cols = len(headers)
        self.ui.tableWidget.setRowCount(rows)
        self.ui.tableWidget.setColumnWidth(0, 60)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 130)

        for row in range(rows):
            self.ui.tableWidget.setRowHeight(row, 40)

            for col in range(cols):
                if row == 0:
                    self.ui.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(headers[col]))

                if col == 3:
                    val = QTableWidgetItem(users[row][2]).text()

                    if val != 'default':
                        self.buttonReset = CustomButton()
                        self.buttonReset.user_name = QTableWidgetItem(users[row][1]).text()
                        self.buttonReset.clicked.connect(self.resetUsers)
                        self.ui.tableWidget.setCellWidget(row, col, self.buttonReset)
                        self.buttonReset.setEnabled(True)

                else:
                    item = QTableWidgetItem(users[row][col])
                    self.ui.tableWidget.setItem(row, col, item)

    def resetUsers(self):
        button = self.sender()
        if resetUserCredentials(self, button.user_name):
            self.loadData()