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

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QIntValidator, QColor
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLabel, QTableView

from design.ui_trans import Ui_TransactionWindow
from design.ui_trans_view import Ui_TransactionView
from db.table_trans import *
from modules.module import MsgBox, resize_and_move, valid_char, valid_space


class MyTransaction(QDialog):
    def __init__(self, parent=None, trans_type=None, task=None):
        super(MyTransaction, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color :#10141b;'
        self.task = task
        self.allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              ' ', '@', '%', '&', '(', ')', '[', ']', '_', '-', '.'

                              ]

        month, year = getPeriod()
        self.trans_month = month
        self.trans_year = year

        # variables for 'trans' table fields
        self.current_trans_type = trans_type
        self.current_trans_id = None
        self.current_trans_date = None
        self.current_trans_head_id = None
        self.current_trans_details = None
        self.current_trans_account_id = None
        self.current_trans_amount = None

        self.current_trans_head_name = None
        self.current_trans_account_number = None

        self.ui = Ui_TransactionWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        self.setWindowTitle('Expense Tracker')
        resize_and_move(self, self.parent, .8, .8)

        # Change value of some widgets
        self.ui.labelHeading.setText(f'{self.task} {self.current_trans_type} Transaction')
        self.ui.labelMessage.hide()
        self.showMainWidgets(False)
        # setDateRange(self)
        populateComboHead(self, self.current_trans_type)
        populateComboAccount(self)

        # setting validators editTransAmount
        self.ui.editTransId.setValidator(QIntValidator())
        self.ui.editTransAmount.setValidator(QIntValidator())

        self.ui.buttonOk.setText(f'&{self.task.upper()}')
        self.ui.buttonOk.setIcon(QIcon(f'src/icons/{self.task.lower()}.png'))

    def showMainWidgets(self, arg=True):
        if arg:
            self.ui.frameSearch.hide()

            self.ui.frameDetailsTop.show()
            self.ui.frameDetailsBottom.show()
            self.ui.frameAmount.show()

            self.ui.comboHead.setCurrentIndex(-1)
            self.ui.editTransDetails.setText('')
            self.ui.comboAccount.setCurrentIndex(-1)
            self.ui.editTransAmount.setText('')

            self.ui.dateTrans.setFocus()

            self.ui.buttonOk.show()
            self.ui.buttonCancel.show()
            self.ui.buttonOk.setEnabled(False)
        else:
            self.ui.frameDetailsTop.hide()
            self.ui.frameDetailsBottom.hide()
            self.ui.frameAmount.hide()

            self.ui.buttonOk.hide()
            self.ui.buttonCancel.hide()

            self.ui.frameSearch.show()
            self.ui.editTransId.setText('')
            self.ui.editTransId.setFocus()
            self.ui.buttonSearch.setEnabled(False)

        self.ui.frameAccount.hide()

    def onSearchClicked(self):
        title = f'{self.task.title()} Transaction'
        msg = ''
        button = '&Got it'
        trans_id = self.ui.editTransId.text().strip()
        trans_type = self.current_trans_type

        if not recordExists(trans_id, trans_type):
            msg = 'Record not found'
            MsgBox(title, msg, button).warn()
            self.ui.editTransId.setFocus()
            self.ui.buttonSearch.setEnabled(False)
            return

        self.showMainWidgets(True)
        populateWidgets(self, trans_id, f'{self.task.lower()}')
        self.ui.dateTrans.setFocus()

    def onTextEdited(self, text):
        if text:
            self.ui.buttonOk.setEnabled(True)
        else:
            self.ui.buttonOk.setEnabled(False)

        self.ui.labelMessage.hide()

    def onTextChanged(self, text):
        if text:
            self.ui.buttonSearch.setEnabled(True)
        else:
            self.ui.buttonSearch.setEnabled(False)

        self.ui.labelMessage.hide()

    def onDateChanged(self):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)
        self.ui.comboHead.setFocus()

    def onIndexChanged(self, index):
        sender = self.sender()
        if sender == self.ui.comboHead:
            self.ui.editTransDetails.setFocus()

        elif sender == self.ui.comboAccount:
            item = self.ui.comboAccount.currentText()
            if item.lower() == 'cash':
                self.ui.frameAccount.hide()
            else:
                self.ui.frameAccount.show()
                populateBankDetails(self, item)
            self.ui.editTransAmount.setFocus()

        # in all cases labelMessage will be hidden and button ok will be enabled
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)

    def onCancelPressed(self):
        self.showMainWidgets(False)

    def onOkPressed(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()


class AddTransaction(MyTransaction):
    def __init__(self, parent, trans_type):
        super(AddTransaction, self).__init__(parent, trans_type, 'Add')

        # hide/show widgets
        self.showMainWidgets(True)

        self.ui.buttonCancel.setText('&Reset')
        self.ui.buttonCancel.setIcon(QIcon('src/icons/reset.png'))

        # set transaction date in DateEdit
        default_date = None
        current_date = QDate().currentDate()

        current_month_year = current_date.toString("MMMM-yyyy")
        transaction_month_year = f"{self.trans_month}-{self.trans_year}"

        if current_month_year == transaction_month_year:
            default_date = current_date
        else:
            date_string = f"01-{self.trans_month}-{self.trans_year}"
            default_date = QDate().fromString(date_string, "dd-MMMM-yyyy")

        self.ui.dateTrans.setDate(default_date)

    def onCancelPressed(self):
        self.showMainWidgets(True)

    def onOkPressed(self):
        new_date = self.ui.dateTrans.date()
        new_details = self.ui.editTransDetails.text()
        new_amount = self.ui.editTransAmount.text()
        new_head = self.ui.comboHead.currentText()
        new_account = self.ui.comboAccount.currentText()

        title = 'Insert Record'
        msg = ''
        obj = None

        # ###########################  Validating date ##############################
        date_status = validDate(self, new_date)
        if date_status != "ok" :
            obj = self.ui.dateTrans
            title = f'Incorrect Transaction Date'
            msg = date_status

        # ###########################  Validating Transaction Details ##############################
        elif len(new_details) < 3:
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Minimum 3 characters required'

        elif not valid_char(new_details, self.allowed_chars):
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Invalid input'

        elif not valid_space(new_details):
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Only single space between to characters is allowed'

        # ###########################  Validating Transaction Amount ##############################
        elif new_amount == '0' or new_amount == '':
            obj = self.ui.editTransAmount
            title = 'Invalid Amount'
            msg = 'Please enter amount'

        # ###########################  Validating Transaction Head ##############################
        elif self.ui.comboHead.currentIndex() < 0:
            obj = self.ui.comboHead
            title = 'Transaction Head'
            msg = 'Please select a Transaction Head'

        # ###########################  Validating Account Number ##############################
        elif self.ui.comboAccount.currentIndex() < 0:
            obj = self.ui.comboAccount
            title = 'Transaction Account'
            msg = 'Please select a Transaction Account'
        else:
            insertTransaction(self, new_date, new_head, new_details,
                              new_account, new_amount)

            self.showMainWidgets(True)

            msg = f'Transaction completed successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            return

        MsgBox(title, msg, '&Got it').warn()
        self.ui.buttonOk.setEnabled(False)
        if obj == self.ui.editTransDetails or obj == self.ui.editTransAmount:
            obj.end(False)
        obj.setFocus()
        return


class EditTransaction(MyTransaction):
    def __init__(self, parent, trans_type):
        super(EditTransaction, self).__init__(parent, trans_type, 'Edit')
        self.parent = parent
        self.ui.editTransId.setFocus()

    def onOkPressed(self):
        new_date = self.ui.dateTrans.date()
        new_details = self.ui.editTransDetails.text()
        new_amount = self.ui.editTransAmount.text()
        new_head = self.ui.comboHead.currentText()
        new_account = self.ui.comboAccount.currentText()

        title = 'Update Record'
        msg = ''
        obj = None

        # Check whether data changed or not

        data_changed = False

        old_value = [self.current_trans_date,
                     self.current_trans_details,
                     self.current_trans_amount,
                     self.current_trans_head_name,
                     self.current_trans_account_number]

        new_value = [new_date, new_details, new_amount, new_head, new_account]

        for i in range(len(new_value)):
            if new_value[i] != old_value[i]:
                data_changed = True
                break

        # ###########################  If data not changed ##############################
        if not data_changed:
            obj = self.ui.dateTrans
            title = 'No change found '
            msg = 'Nothing to update???'

        # ###########################  Validating date ##############################
        date_status = validDate(self, new_date)
        if date_status != "ok":
            obj = self.ui.dateTrans
            title = f'Incorrect Transaction Date'
            msg = date_status

        # ###########################  Validating Transaction Details ##############################
        elif len(new_details) < 3:
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Minimum 3 characters required'

        elif not valid_char(new_details, self.allowed_chars):
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Invalid input'

        elif not valid_space(new_details):
            obj = self.ui.editTransDetails
            title = 'Transaction Details'
            msg = 'Only single space between to characters is allowed'

            # ###########################  Validating Transaction Amount ##############################
        elif new_amount == '0' or new_amount == '':
            obj = self.ui.editTransAmount
            title = 'Invalid Amount'
            msg = 'Please enter amount'

            # ###########################  Validating Transaction Head ##############################
        elif self.ui.comboHead.currentIndex() < 0:
            obj = self.ui.comboHead
            title = 'Transaction Head'
            msg = 'Please select a Transaction Head'

            # ###########################  Validating Account Number ##############################
        elif self.ui.comboAccount.currentIndex() < 0:
            obj = self.ui.comboAccount
            title = 'Bank Account'
            msg = 'Please select a Bank Account Number'
        else:
            updateTransaction(self, self.current_trans_id,
                              new_date, new_head,
                              new_details, new_account, new_amount)

            msg = f'Record updated successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()
            self.showMainWidgets(False)
            return

        MsgBox(title, msg, '&Got it').warn()
        self.ui.buttonOk.setEnabled(False)
        if obj == self.ui.editTransDetails or obj == self.ui.editTransAmount:
            obj.end(False)
        obj.setFocus()
        return


class DeleteTransaction(MyTransaction):
    def __init__(self, parent, trans_type):
        super(DeleteTransaction, self).__init__(parent, trans_type, 'Delete')
        self.parent = parent
        self.ui.editTransId.setFocus()

    def onOkPressed(self):
        title = 'Confirm Delete'
        msg = f'Do you want delete this record?'
        if MsgBox(title, msg, '&Delete', '&Cancel').confirm():
            removeTransaction(self, self.current_trans_id)

            msg = f'Record deleted successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

        self.showMainWidgets(False)


class ViewTransaction(QDialog):
    def __init__(self, parent, trans_type):
        super(ViewTransaction, self).__init__(parent)
        self.parent = parent
        self.trans_type = trans_type
        self.ui = Ui_TransactionView()
        self.ui.setupUi(self)
        resize_and_move(self, self.parent, .9, .9)
        self.show()

        # create widgets
        self.text_label = QLabel(self)
        self.text_label.setText("<h2>No Transaction Exists</h2>")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("background-color: rgb(225, 225, 225); color: rgb(0, 0, 255)")
        self.text_label.setGeometry(int(self.width() / 3), int(self.height() / 3),
                                    int(self.width() / 3), int(self.height() / 3))
        self.text_label.hide()

        # create model and set query
        self.query = QSqlQuery()

        if self.trans_type == "Receipt":
            self.ui.labelHeading.setText("Receipt")
            self.query.prepare("""SELECT TransId, TransDate, HeadName, TransDetails,
                                  TransAmount, BankName, CustomerName, AccountNumber
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  JOIN account ON account.AccountId = trans.AccountId
                                  WHERE HeadType = :HeadType  AND HeadName NOT IN (:HeadName)
                                  ORDER BY TransDate
                               """)

            self.query.bindValue(":HeadType", "Receipt")
            self.query.bindValue(":HeadName", "ContraReceipt")
            self.query.exec()

        elif self.trans_type == "Payment":
            self.ui.labelHeading.setText("Payment")
            self.query.prepare("""SELECT TransId, TransDate, HeadName, TransDetails,
                                  TransAmount, BankName, CustomerName, AccountNumber
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  JOIN account ON account.AccountId = trans.AccountId
                                  WHERE HeadType = :HeadType  AND HeadName NOT IN (:HeadName)
                                  ORDER BY TransDate
                               """)

            self.query.bindValue(":HeadType", "Payment")
            self.query.bindValue(":HeadName", "ContraPayment")
            self.query.exec()

        elif self.trans_type == "ContraReceipt":
            self.ui.labelHeading.setText(f'{self.trans_type[6:]}  {self.trans_type[0:6]}  Entries')

            self.query.prepare("""SELECT TransId, TransDate, HeadName, TransDetails,
                                  TransAmount, BankName, CustomerName, AccountNumber
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  JOIN account ON account.AccountId = trans.AccountId
                                  WHERE HeadName = :HeadName
                                  ORDER BY TransDate
                                """)

            self.query.bindValue(":HeadName", "ContraReceipt")
            self.query.exec()

        elif self.trans_type == "ContraPayment":
            self.ui.labelHeading.setText(f'{self.trans_type[6:]}  {self.trans_type[0:6]}  Entries')

            self.query.prepare("""SELECT TransId, TransDate, HeadName, TransDetails,
                                  TransAmount, BankName, CustomerName, AccountNumber
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  JOIN account ON account.AccountId = trans.AccountId
                                  WHERE HeadName = :HeadName
                                  ORDER BY TransDate
                                """)

            self.query.bindValue(":HeadName", "ContraPayment")
            self.query.exec()
        else:
            self.ui.labelHeading.setText(f'{self.trans_type[6:]}  {self.trans_type[0:6]}  Entries')

            self.query.prepare("""SELECT TransId, TransDate, HeadName, TransDetails,
                                  TransAmount, BankName, CustomerName, AccountNumber
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  JOIN account ON account.AccountId = trans.AccountId
                                  WHERE HeadName = :HeadName1 OR HeadName = :HeadName2
                                  ORDER BY TransDate
                             """)

            self.query.bindValue(":HeadName1", "ContraReceipt")
            self.query.bindValue(":HeadName2", "ContraPayment")

            self.query.exec()

        # get total
        receipt_total = 0
        payment_total = 0
        total = 0

        if self.trans_type == "ContraAll":
            while self.query.next():
                head_name = self.query.value(2)
                amount = self.query.value(4)
                if head_name == "ContraReceipt":
                    receipt_total += amount
                else:
                    payment_total += amount

            self.ui.editReceiptTotal.setText(str(receipt_total))
            self.ui.editPaymentTotal.setText(str(payment_total))

        else:
            while self.query.next():
                amount = self.query.value(4)
                total += amount

            self.ui.labelReceiptTotal.hide()
            self.ui.editReceiptTotal.hide()
            self.ui.labelPaymentTotal.setText("Total")
            self.ui.editPaymentTotal.setText(str(total))

        self.model = ViewTransactionModel()
        self.model.setQuery(self.query)

        self.model.setHeaderData(0, Qt.Horizontal, "Id")
        self.model.setHeaderData(1, Qt.Horizontal, "Date")
        self.model.setHeaderData(2, Qt.Horizontal, "Head")
        self.model.setHeaderData(3, Qt.Horizontal, "Details")
        self.model.setHeaderData(4, Qt.Horizontal, "Amount")
        self.model.setHeaderData(5, Qt.Horizontal, "Bank Name")
        self.model.setHeaderData(6, Qt.Horizontal, "Customer Name")
        self.model.setHeaderData(7, Qt.Horizontal, "A/c No.")

        # set model to table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView.setColumnWidth(0, 50)
        self.ui.tableView.setColumnWidth(1, 125)
        self.ui.tableView.setColumnWidth(2, 200)
        self.ui.tableView.setColumnWidth(3, 250)
        self.ui.tableView.setColumnWidth(4, 110)
        self.ui.tableView.setColumnWidth(5, 175)
        self.ui.tableView.setColumnWidth(6, 150)

        rows = self.model.rowCount()
        if rows:
            self.text_label.hide()
            for row in range(rows):
                # set height of each row
                self.ui.tableView.setRowHeight(row, 50)
        else:
            self.text_label.show()

    def closeEvent(self, event):
        self.model.clear()
        self.query.finish()
        event.accept()


class ViewTransactionModel(QSqlQueryModel):
    def __init__(self, query=None):
        super(ViewTransactionModel, self).__init__()
        self.setQuery(query)

    def data(self, index, role):
        if index.isValid():
            col = index.column()
            row = index.row()

            if role == Qt.TextAlignmentRole:
                if col == 4:
                    return Qt.AlignRight

                if col == 5:
                    return Qt.AlignHCenter
                else:
                    return Qt.AlignLeft

            if role == Qt.ForegroundRole:
                head = index.sibling(row, 2).data()
                if head == "ContraReceipt" or head == "ContraPayment":
                    return QColor("#DA8989")

        return QSqlQueryModel.data(self, index, role)
