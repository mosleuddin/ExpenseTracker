from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox, QTableView, QLabel

from modules.module import resize_and_move, read_only, valid_char, valid_space
from design.ui_account import Ui_AccountWindow
from design.ui_account_view import Ui_ViewAccount
from db.table_account import (insertAccount, updateAccount, removeAccount,
                              populateComboAccount, populateWidgets)


class Account(QDialog):
    def __init__(self, parent=None):
        super(Account, self).__init__(parent)
        self.parent = parent

        self.selected_account_id = None
        self.selected_account_number = None
        self.selected_customer_name = None
        self.selected_bank_name = None
        self.selected_branch_name = None

        self.ui = Ui_AccountWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        self.setWindowTitle('Expense Tracker')
        resize_and_move(self, self.parent, .4, .6)
        self.hideWidgets()
        self.ui.labelMessage.hide()

        self.ui.editAccountNumber.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editCustomerName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBankName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBranchName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)

    def showWidgets(self):
        self.ui.labelAccountNumber.show()
        self.ui.labelCustomerName.show()
        self.ui.labelBankName.show()
        self.ui.labelBranchName.show()

        self.ui.editAccountNumber.show()
        self.ui.editCustomerName.show()
        self.ui.editBankName.show()
        self.ui.editBranchName.show()

        self.ui.buttonOk.show()
        self.ui.buttonCancel.show()

        self.ui.editCustomerName.setFocus()

    def hideWidgets(self):
        self.ui.labelAccountNumber.hide()
        self.ui.labelCustomerName.hide()
        self.ui.labelBankName.hide()
        self.ui.labelBranchName.hide()

        self.ui.editAccountNumber.hide()
        self.ui.editCustomerName.hide()
        self.ui.editBankName.hide()
        self.ui.editBranchName.hide()

        self.ui.buttonOk.hide()
        self.ui.buttonCancel.hide()

    def onAccountChanged(self, index):
        if index != -1:
            self.ui.labelMessage.hide()
            self.ui.comboAccount.hide()
            self.showWidgets()

            account_number = self.ui.comboAccount.currentText()
            populateWidgets(self, account_number)

    def onBankNameChanged(self, index):
        if index != -1:
            self.ui.editBranchName.setFocus()

    def onTextEdited(self, text):
        sender = self.sender()

        if sender == self.ui.editAccountNumber:
            if len(text) >= 3 and text.upper() != self.selected_account_number:
                self.ui.buttonOk.setEnabled(True)

        elif sender == self.ui.editCustomerName:
            if len(text) >= 3 and text.upper() != self.selected_customer_name:
                self.ui.buttonOk.setEnabled(True)

        elif sender == self.ui.editBankName:
            if len(text) >= 3 and text.upper() != self.selected_bank_name:
                self.ui.buttonOk.setEnabled(True)

        elif sender == self.ui.editBranchName:
            if len(text) >= 3 and text.upper() != self.selected_branch_name:
                self.ui.buttonOk.setEnabled(True)

        else:
            self.ui.buttonOk.setEnabled(False)

        self.ui.labelMessage.hide()

    def onCancelPressed(self):
        self.hideWidgets()
        self.ui.comboAccount.show()
        self.ui.comboAccount.setCurrentIndex(-1)

    def onOkPressed(self):
        pass

    def accountExists(self, account_number, task):
        query = QSqlQuery()
        if task == 'add':
            query.exec("SELECT AccountNumber FROM account")
        else:
            query.exec(f"""SELECT AccountNumber FROM account
                           WHERE AccountId != {self.selected_account_id}""")
        while query.next():
            if query.value(0) == account_number:
                return True
        return False


def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
        self.close()


def closeEvent(self, event):
    event.accept()


class AddAccount(Account):
    def __init__(self, parent=None):
        super(AddAccount, self).__init__(parent)
        self.parent = parent
        self.setStyleSheet('background-color: rgb(200, 255, 100)')

        # hide/show widgets
        self.ui.comboAccount.hide()
        self.showWidgets()
        self.ui.buttonCancel.hide()

        # Change value of some widgets
        self.ui.labelHeading.setText('Add New Bank Account')
        self.ui.buttonOk.setText('&Add')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))
        self.ui.editAccountNumber.setFocus()

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        customer_name = self.ui.editCustomerName.text().strip().upper()
        bank_name = self.ui.editBankName.text().strip().upper()
        branch_name = self.ui.editBranchName.text().strip().upper()
        obj = None
        chars = [' ', '-']

        # ###########################  Validating Customer Name ##############################
        if len(customer_name) < 3:
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(customer_name, chars):
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(customer_name):
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Bank Name ##############################

        elif len(bank_name) < 3:
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(bank_name, chars):
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(bank_name):
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Branch Name ##############################

        elif len(branch_name) < 3:
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(branch_name, chars):
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(branch_name):
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Account Number ##############################
        elif len(account_number) < 10:
            obj = self.ui.editAccountNumber
            title = 'Invalid Account Number'
            msg = 'Minimum 10 characters required'

        elif not account_number.isdigit():
            obj = self.ui.editAccountNumber
            title = 'Invalid Account Number'
            msg = 'Only digits are allowed'

        elif self.accountExists(account_number, 'add'):
            obj = self.ui.editAccountNumber
            title = 'Duplicate Data'
            msg = f'Account Number {account_number} exists!!!'

        else:
            insertAccount(self, account_number, customer_name, bank_name, branch_name)
            msg = f'Bank account No. {account_number} added successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

            self.ui.editAccountNumber.setText('')
            self.ui.editCustomerName.setText('')
            self.ui.editBankName.setText('')
            self.ui.editBranchName.setText('')
            self.ui.editAccountNumber.setFocus()
            self.ui.buttonOk.setEnabled(False)
            return

        QMessageBox.warning(self, title, msg)
        obj.setFocus()
        obj.end(False)
        self.ui.buttonOk.setEnabled(False)
        return


class EditAccount(Account):
    def __init__(self, parent=None):
        super(EditAccount, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color: LightGreen'
        self.setStyleSheet(self.bg)
        populateComboAccount(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Edit Account')
        self.ui.buttonOk.setText('&Edit')
        self.ui.buttonOk.setIcon(QIcon('src/icons/edit.png'))
        read_only(self.bg, self.ui.editAccountNumber)

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        customer_name = self.ui.editCustomerName.text().strip().upper()
        bank_name = self.ui.editBankName.text().strip().upper()
        branch_name = self.ui.editBranchName.text().strip().upper()
        obj = None
        chars = [' ', '-']

        # ###########################  Validating Customer Name ##############################
        if len(customer_name) < 3:
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(customer_name, chars):
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(customer_name):
            obj = self.ui.editCustomerName
            title = 'Invalid Customer Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Bank Name ##############################

        elif len(bank_name) < 3:
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(bank_name, chars):
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(bank_name):
            obj = self.ui.editBankName
            title = 'Invalid Bank Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Branch Name ##############################

        elif len(branch_name) < 3:
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(branch_name, chars):
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(branch_name):
            obj = self.ui.editBranchName
            title = 'Invalid Branch Name'
            msg = 'Only single space between to characters is allowed'

        else:
            updateAccount(self, account_number, customer_name, bank_name, branch_name)
            msg = f'Bank account No. "{account_number}" updated successfully'
            self.ui.comboAccount.clear()
            populateComboAccount(self)
            self.hideWidgets()
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            return

        QMessageBox.warning(self, title, msg)
        obj.setFocus()
        obj.end(False)
        self.ui.buttonOk.setEnabled(False)


class DeleteAccount(Account):
    def __init__(self, parent=None):
        super(DeleteAccount, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color: LightBlue;'
        self.setStyleSheet(self.bg)
        populateComboAccount(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Delete Account')
        self.ui.buttonOk.setText('&Delete')
        self.ui.buttonOk.setIcon(QIcon('src/icons/delete.png'))
        self.ui.buttonOk.setEnabled(True)

        read_only(self.bg, self.ui.editAccountNumber, self.ui.editCustomerName,
                  self.ui.editBankName, self.ui.editBranchName)

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        title = 'Delete'
        msg = f' Delete account number "{account_number}" ?'
        answer = QMessageBox.question(self, title, msg)
        if answer == QMessageBox.Yes:
            removeAccount(self, account_number)

            msg = f'Account number "{account_number}" deleted successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

            self.ui.comboAccount.clear()
            populateComboAccount(self)
            self.hideWidgets()
        return


class ViewAccount(QDialog):
    def __init__(self, parent):
        super(ViewAccount, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ViewAccount()
        self.ui.setupUi(self)
        resize_and_move(self, self.parent, .8, .9)
        self.show()
        # create widgets
        self.text_label = QLabel(self)
        self.text_label.setText("<h2>No account available</h2>")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("background-color: rgb(225, 225, 225); color: rgb(0, 0, 255)")
        self.text_label.setGeometry(int(self.width() / 3), int(self.height() / 3),
                                    int(self.width() / 3), int(self.height() / 3))
        self.text_label.hide()

        # create query
        self.query = QSqlQuery()
        self.query.exec("SELECT AccountNumber, CustomerName, BankName, BranchName  FROM account ORDER BY AccountNumber")

        # create model and set query
        self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.model.setHeaderData(0, Qt.Horizontal, "Account Number")
        self.model.setHeaderData(1, Qt.Horizontal, "Customer Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Bank Name")
        self.model.setHeaderData(3, Qt.Horizontal, "Branch Name")

        # set model to table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView.setColumnWidth(0, 200)
        self.ui.tableView.setColumnWidth(1, 300)
        self.ui.tableView.setColumnWidth(2, 300)

        if self.model.rowCount() == 0:
            self.text_label.show()
        else:
            self.text_label.hide()

    def closeEvent(self, event):
        self.query.finish()
        self.model.clear()
        event.accept()
