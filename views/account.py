from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit, QTableView, QLabel

from modules.module import CustomMessage, resize_and_move, valid_char, valid_space
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
        resize_and_move(self, self.parent, .9, .7)
        self.hideWidgets()
        self.ui.labelMessage.hide()

        # configure comboBankName
        icon = QIcon('src/icons/common.png')
        bank_list = ['Canara Bank', 'HDFC Bank Limited', 'State Bank of India',
                     'Uttarbanga Kshetrya Gramin Bank']

        for bank_name in bank_list:
            self.ui.comboBankName.addItem(icon, bank_name)

        self.ui.editAccountNumber.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editCustomerName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBankName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBranchName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)

    def showWidgets(self):
        self.ui.labelAccountNumber.show()
        self.ui.labelCustomerName.show()
        self.ui.labelBankName2.show()
        self.ui.labelBranchName.show()

        self.ui.editAccountNumber.show()
        self.ui.editCustomerName.show()
        self.ui.comboBankName.show()
        self.ui.editBranchName.show()

        self.ui.buttonOk.show()
        self.ui.buttonCancel.show()

        self.ui.editCustomerName.setFocus()

    def hideWidgets(self):
        self.ui.labelAccountNumber.hide()
        self.ui.labelCustomerName.hide()
        self.ui.labelBankName1.hide()
        self.ui.labelBankName2.hide()
        self.ui.labelBranchName.hide()

        self.ui.editAccountNumber.hide()
        self.ui.editCustomerName.hide()
        self.ui.comboBankName.hide()
        self.ui.editBankName.hide()
        self.ui.editBranchName.hide()

        self.ui.buttonOk.hide()
        self.ui.buttonCancel.hide()

    def onAccountChanged(self, index):
        pass

    def onBankNameChanged(self, index):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)
        self.ui.editBranchName.setFocus()

    def onTextEdited(self, text):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)

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
        self.setStyleSheet('background-color: rgb(255,239,213);')

        # hide/show widgets
        self.ui.comboAccount.hide()
        self.showWidgets()
        self.ui.buttonCancel.hide()

        # Change value of some widgets
        self.ui.labelHeading.setText('ADD ACCOUNT')
        self.ui.editAccountNumber.setFocus()
        self.ui.comboBankName.setCurrentIndex(-1)
        self.ui.buttonOk.setText('&ADD')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        customer_name = self.ui.editCustomerName.text().strip().upper()
        bank_name = self.ui.comboBankName.currentText()
        branch_name = self.ui.editBranchName.text().strip().title()
        obj = None
        chars = [' ', '-']

        # ###########################  Validating Bank Name ##############################
        if self.ui.comboBankName.currentIndex() < 0:
            obj = self.ui.comboBankName
            title = 'Bank Name'
            msg = 'Please select a bank'

        # ###########################  Validating Customer Name ##############################
        elif len(customer_name) < 3:
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(customer_name, chars):
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(customer_name):
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Branch Name ##############################

        elif len(branch_name) < 3:
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(branch_name, chars):
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(branch_name):
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Account Number ##############################
        elif len(account_number) < 10:
            obj = self.ui.editAccountNumber
            title = 'Account Number'
            msg = 'Minimum 10 digits are required'

        elif not account_number.isdigit():
            obj = self.ui.editAccountNumber
            title = 'Account Number'
            msg = 'Only digits are allowed'

        elif self.accountExists(account_number, 'add'):
            obj = self.ui.editAccountNumber
            title = 'Account Number'
            msg = f'A/c No.  {account_number} exists!!!'

        else:
            insertAccount(self, account_number, customer_name, bank_name, branch_name)
            msg = f'Bank Account No. {account_number} added successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

            self.ui.editAccountNumber.setText('')
            self.ui.editCustomerName.setText('')
            self.ui.comboBankName.setCurrentIndex(-1)
            self.ui.editBranchName.setText('')
            self.ui.editAccountNumber.setFocus()
            self.ui.buttonOk.setEnabled(False)
            return
        CustomMessage().warn(title, msg, '&Got it')
        self.ui.buttonOk.setEnabled(False)
        obj.setFocus()
        if obj != self.ui.comboBankName:
            obj.end(False)
        return


class EditAccount(Account):
    def __init__(self, parent=None):
        super(EditAccount, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color: rgb(255,228,225)'
        self.setStyleSheet(self.bg)
        populateComboAccount(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('EDIT ACCOUNT')
        self.ui.buttonOk.setText('&EDIT')
        self.ui.buttonOk.setIcon(QIcon('src/icons/edit.png'))

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        customer_name = self.ui.editCustomerName.text().strip().upper()
        bank_name = self.ui.comboBankName.currentText()
        branch_name = self.ui.editBranchName.text().strip().title()
        obj = None
        chars = [' ', '-']

        # Check whether data changed or not
        if customer_name == self.selected_customer_name and \
                bank_name == self.selected_bank_name and \
                branch_name == self.selected_branch_name:
            obj = self.ui.editCustomerName
            title = 'Account Details'
            msg = 'Nothing to update???'

        # ###########################  Validating Bank Name ##############################
        elif self.ui.comboBankName.currentIndex() < 0:
            obj = self.ui.comboBankName
            title = 'Bank Name'
            msg = 'Please select a bank'

        # ###########################  Validating Customer Name ##############################
        elif len(customer_name) < 3:
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(customer_name, chars):
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(customer_name):
            obj = self.ui.editCustomerName
            title = 'Customer Name'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Branch Name ##############################
        elif len(branch_name) < 3:
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(branch_name, chars):
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(branch_name):
            obj = self.ui.editBranchName
            title = 'Branch Name'
            msg = 'Only single space between to characters is allowed'

        else:
            updateAccount(self, account_number, customer_name, bank_name, branch_name)
            msg = f'Bank Account No. "{account_number}" updated successfully'

            self.hideWidgets()
            self.ui.labelHeading.hide()

            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            return

        CustomMessage().warn(title, msg, '&Got it')
        obj.setFocus()
        if obj != self.ui.comboBankName:
            obj.end(False)
        return

    def onAccountChanged(self, index):
        account_number = self.ui.comboAccount.currentText()
        self.ui.labelMessage.hide()
        self.ui.comboAccount.hide()

        self.showWidgets()
        populateWidgets(self, account_number, 'edit')


class DeleteAccount(Account):
    def __init__(self, parent=None):
        super(DeleteAccount, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color: rgb(255,240,245);'
        self.setStyleSheet(self.bg)
        populateComboAccount(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Delete Account')
        self.ui.buttonOk.setText('&DELETE')
        self.ui.buttonOk.setIcon(QIcon('src/icons/delete.png'))

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        title = 'Confirm Delete'
        msg = f' Delete account number "{account_number}" ?'
        if CustomMessage().confirm(title, msg, '&Delete', '&Cancel'):
            removeAccount(self, account_number)
            msg = f'Bank Account No. "{account_number}" deleted successfully'
            self.hideWidgets()
            self.ui.labelHeading.hide()

            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
        return

    def onAccountChanged(self, index):
        account_number = self.ui.comboAccount.currentText()
        self.ui.labelMessage.hide()
        self.ui.comboAccount.hide()

        self.showWidgets()
        populateWidgets(self, account_number, 'delete')


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
