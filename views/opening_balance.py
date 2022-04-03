from PySide6.QtGui import QIcon, QIntValidator, Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLineEdit

from design.ui_show_opening_balance import Ui_ShowOpeningBalance
from design.ui_update_opening_balance import Ui_UpdateOpeningBalance
from db.table_balance import getOpeningBalance, updateOpeningBalance

from modules.module import CustomButtonBalance


class ShowOpeningBalance(QDialog):
    def __init__(self, parent=None):
        super(ShowOpeningBalance, self).__init__(parent=parent)
        self.ui = Ui_ShowOpeningBalance()
        self.ui.setupUi(self)

        self.setWindowTitle("Opening Balance")
        self.setFixedSize(1000, 600)
        self.show()
        self.loadData()

    def loadData(self):
        self.ui.tableBalance.clear()
        bank_data = getOpeningBalance("all")
        headers = ['A/c No.', 'Bank Name', 'Customer Name', 'Balance', 'Action']

        rows = len(bank_data)  # to determine number of rows in table widget
        cols = len(headers)  # to determine number of columns in table widget

        self.ui.tableBalance.setRowCount(rows)

        self.ui.tableBalance.setColumnWidth(0, 225)
        self.ui.tableBalance.setColumnWidth(1, 250)
        self.ui.tableBalance.setColumnWidth(2, 250)
        self.ui.tableBalance.setColumnWidth(3, 125)

        for row in range(rows):
            self.ui.tableBalance.setRowHeight(row, 40)

            for col in range(cols):
                if row == 0:
                    # set heading
                    self.ui.tableBalance.setHorizontalHeaderItem(col, QTableWidgetItem(headers[col]))

                if col == 4:
                    # get bank data from data variable which is a list of tuples
                    account_number = bank_data[row][0]

                    # create a button for fifth column of each row
                    self.buttonUpdate = CustomButtonBalance()
                    self.buttonUpdate.setMaximumSize(75, 30)

                    # store the corrent row's account number in this button's account number attribute
                    self.buttonUpdate.account_number = account_number

                    # add update button's functionality
                    self.buttonUpdate.clicked.connect(self.showDialog)

                    # place the update button in the table at column 5 of each row
                    self.ui.tableBalance.setCellWidget(row, col, self.buttonUpdate)
                else:
                    # fill the columns with corresponding bank-data
                    value = bank_data[row][col]  # get bank-data
                    item = QTableWidgetItem(value)
                    self.ui.tableBalance.setItem(row, col, item)  # place the item in the table

    def showDialog(self):
        btn = self.sender()
        dlg = UpdateOpeningBalance(self, btn.account_number)


class UpdateOpeningBalance(QDialog):
    def __init__(self, parent=None, acct_num=None):
        super(UpdateOpeningBalance, self).__init__(parent)
        self.ui = Ui_UpdateOpeningBalance()
        self.ui.setupUi(self)
        self.parent = parent
        self.account_number = acct_num
        self.common_icon = QIcon('src/icons/common.png')
        self.configUI()
        self.show()
        self.populateWidgets(self.account_number)

    def configUI(self):
        self.setWindowTitle("Update Opening Balance")
        self.setFixedSize(500, 400)
        self.ui.editBalance.setValidator(QIntValidator())
        self.ui.editBalance.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)

    def populateWidgets(self, account_number):
        data = getOpeningBalance(account_number)

        customer_name = data[0]
        bank_name = data[1]
        branch_name = data[2]
        opening_balance = data[3]

        self.ui.editAccountNumber.setText(account_number)
        self.ui.editCustomerName.setText(customer_name)
        self.ui.editBankName.setText(bank_name)
        self.ui.editBranchName.setText(branch_name)
        self.ui.editBalance.setText(opening_balance)

        self.ui.editBalance.setFocus()
        self.ui.editBalance.end(False)

    def onTextEdited(self, text):
        if not text or text.startswith(('-', '+')):
            self.ui.buttonOk.setEnabled(False)
        else:
            self.ui.buttonOk.setEnabled(True)

    def onOkPressed(self):
        opening_balance = self.ui.editBalance.text()
        updateOpeningBalance(self, self.account_number, opening_balance)
        self.parent.loadData()
        self.close()
        self.parent.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()
