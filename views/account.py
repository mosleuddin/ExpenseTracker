from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QIntValidator
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit, QTableView, QLabel

from modules.module import CustomMessage, resize_and_move, valid_char, valid_space
from design.ui_account import Ui_AccountWindow
from design.ui_account_view import Ui_ViewAccount
from db.table_account import *
from db.table_balance import insertOpeningBalance, updateOpeningBalance, getOpeningBalance


class Account(QDialog):
    def __init__(self, parent=None):
        super(Account, self).__init__(parent)
        self.parent = parent

        self.setWindowTitle('Expense Tracker')
        self.common_icon = QIcon('src/icons/common.png')

        self.task = None
        self.selected_account_id = None
        self.selected_account_number = None
        self.selected_customer_name = None
        self.selected_bank_name = None
        self.selected_branch_name = None
        self.selected_balance = None

        self.ui = Ui_AccountWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        resize_and_move(self, self.parent, .6, .7)
        self.ui.editBalance.setValidator(QIntValidator())
        self.ui.labelOpeningBalance.hide()
        self.ui.editBalance.hide()
        self.ui.buttonCancel.hide()
        self.ui.buttonOk.hide()
        self.ui.labelMessage.hide()

        # configure comboBankName
        for bank_name in self.parent.bank_names_list:
            self.ui.comboBankName.addItem(self.common_icon, bank_name)

        self.ui.editAccountNumber.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editCustomerName.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBranchName.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)
        self.ui.editBalance.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)

    def showBody(self, arg=True):
        if arg:
            self.ui.frameBody.show()
            if self.task == "add":
                self.clearBodyWidgetsContent()
            else:
                self.ui.buttonOk.setVisible(True)
                self.ui.buttonCancel.setVisible(True)

                if self.task == 'edit':
                    self.ui.buttonOk.setEnabled(False)
                    self.ui.editCustomerName.setFocus()
                else:
                    self.ui.buttonOk.setEnabled(True)
                    self.ui.buttonOk.setFocus()
        else:
            self.ui.frameBody.hide()
            if not self.task == "add":
                self.ui.buttonOk.setVisible(False)
                self.ui.buttonCancel.setVisible(False)

    def showCombo(self, arg=True):
        if arg:
            self.ui.frameCombo.show()
            self.ui.comboAccount.setCurrentIndex(-1)
            self.ui.comboAccount.setFocus()
        else:
            self.ui.frameCombo.hide()

    def clearBodyWidgetsContent(self):
        self.ui.editAccountNumber.setText('')
        self.ui.editCustomerName.setText('')
        self.ui.comboBankName.setCurrentIndex(-1)
        self.ui.editBranchName.setText('')
        self.ui.editBalance.setText('')
        self.ui.editAccountNumber.setFocus()
        self.ui.buttonOk.setEnabled(False)

    def onAccountChanged(self, index):
        if index > -1:
            account_number = self.ui.comboAccount.currentText()
            self.ui.labelMessage.hide()
            self.showCombo(False)
            populateWidgets(self, account_number, self.task)
            self.showBody(True)
            self.current_account_index = index

    def onBankNameChanged(self, index):
        if index > -1:
            self.ui.labelMessage.hide()
            self.ui.buttonOk.setEnabled(True)
            self.ui.editBranchName.setFocus()

    def onTextEdited(self, text):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)

    def onCancelPressed(self):
        self.showBody(False)
        self.showCombo(True)

    def onOkPressed(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()


class AddAccount(Account):
    def __init__(self, parent=None):
        super(AddAccount, self).__init__(parent)
        self.parent = parent
        self.task = 'add'
        self.setStyleSheet('background-color: rgb(255,239,213);')

        self.showCombo(False)
        self.ui.labelOpeningBalance.show()
        self.ui.editBalance.show()
        self.ui.buttonCancel.show()
        self.ui.buttonOk.show()
        self.ui.labelHeading.setText('ADD ACCOUNT')

        self.ui.buttonOk.setText('&ADD')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))

        self.ui.buttonCancel.setText('&Reset')
        self.ui.buttonCancel.setIcon(QIcon('src/icons/reset.png'))

    def onCancelPressed(self):
        self.clearBodyWidgetsContent()

    def onOkPressed(self):
        account_number = self.ui.editAccountNumber.text().strip()
        customer_name = self.ui.editCustomerName.text().strip().upper()
        bank_name = self.ui.comboBankName.currentText()
        branch_name = self.ui.editBranchName.text().strip().title()
        opening_balance = self.ui.editBalance.text().strip()
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

        elif bankAccountExists(account_number, 'add'):
            obj = self.ui.editAccountNumber
            title = 'Account Number'
            msg = f'A/c No.  {account_number} exists!!!'

        # ###########################  Validating Opening Balance ##############################
        elif not opening_balance.isdigit():
            obj = self.ui.editBalance
            title = 'Opening Balance'
            msg = 'Only digits are allowed'

        else:
            insertAccount(self, account_number, customer_name, bank_name, branch_name)
            insertOpeningBalance(self, account_number, opening_balance)
            msg = f'Bank Account No. {account_number} added successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            self.showBody()
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
        self.task = 'edit'
        self.bg = 'background-color: rgb(255,228,225)'
        self.setStyleSheet(self.bg)

        self.showBody(False)
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
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            self.showBody(False)
            self.showCombo(True)
            return
        CustomMessage().warn(title, msg, '&Got it')
        obj.setFocus()
        if obj != self.ui.comboBankName:
            obj.end(False)
        return


class DeleteAccount(Account):
    def __init__(self, parent=None):
        super(DeleteAccount, self).__init__(parent)
        self.parent = parent
        self.task = 'delete'
        self.bg = 'background-color: rgb(255,240,245);'
        self.setStyleSheet(self.bg)

        self.showBody(False)
        populateComboAccount(self)

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
            self.showBody(False)
            self.showCombo(True)
            populateComboAccount(self)
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
        else:
            self.showBody(False)
            self.showCombo(True)


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
        self.query.exec("""SELECT AccountNumber, CustomerName, BankName, BranchName
                              FROM account WHERE AccountNumber != "Cash"
                              ORDER BY AccountNumber
                           """)

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
        self.ui.tableView.setColumnWidth(0, 175)
        self.ui.tableView.setColumnWidth(1, 270)
        self.ui.tableView.setColumnWidth(2, 270)

        if self.model.rowCount() == 0:
            self.text_label.show()
        else:
            self.text_label.hide()

    def closeEvent(self, event):
        self.query.finish()
        self.model.clear()
        event.accept()
