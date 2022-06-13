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
import shutil

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMainWindow, QInputDialog, QApplication, QFileDialog

from db.table_balance import InitializeBalanceTable, AccountBalanceSummary
from db.table_basic_details import getOwner, getPeriod
from db.table_trans import transDateMismatch
from design.ui_home import Ui_HomeWindow
from db.table_user import viewUser, resetUserCredentials
from modules.module import MsgBox, resize_and_move, showMismatchMessage
from views.month_end_actions import InitializeTransaction
from views.opening_balance import ShowOpeningBalance

from views.credentials import ShowUsers, ChangeUsername, ChangePassword
from views.period_mismatch import PeriodMisMatch
from views.show_trans import ShowTransactions
from views.update_basic_details import UpdateBasicDetails
from views.about import About
from views.head import AddHead, EditHead, DeleteHead, ViewHead
from views.account import AddAccount, EditAccount, DeleteAccount, ViewAccount
from views.trans import AddTransaction, EditTransaction, DeleteTransaction, ViewTransaction


class Home(QMainWindow):
    def __init__(self, conn=None, user_id=None, user_name=None):
        super().__init__()
        self.conn = conn
        self.user_id = user_id
        self.user_name = user_name
        self.query = QSqlQuery()

        self.common_icon = QIcon('src/icons/common.png')
        self.trans_types_list = ['Receipt', 'Payment']
        self.bank_names_list = ['Canara Bank',
                                'HDFC Bank Limited',
                                'State Bank of India',
                                'Uttarbanga Kshetrya Gramin Bank'
                                ]

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        resize_and_move(self, None, .95, .9)
        # self.setWindowState(Qt.WindowFullScreen)

        self.showBasicInfo()
        self.loadOwnerImage()
        self.updateAccountBalanceSummary()
        self.show()

        if transDateMismatch():
            showMismatchMessage(self)

        QApplication.instance().focusChanged.connect(self.onFocusChanged)

    def onFocusChanged(self, old, new):
        if self.isActiveWindow():
            self.showBasicInfo()
            self.loadOwnerImage()
            self.updateAccountBalanceSummary()

    def showBasicInfo(self):
        owner, address = getOwner()
        month, year = getPeriod()

        self.ui.labelOwner.setText(f"{owner}")
        self.ui.labelAddress.setText(f"{address}")

        self.ui.labelMonth.setText(f"{month}")
        self.ui.labelYear.setText(f"{year}")

    def updateAccountBalanceSummary(self):
        InitializeBalanceTable()
        self.balance_model = AccountBalanceSummary()
        self.ui.tableView.setModel(self.balance_model)

        rows = self.balance_model.rowCount()
        for row in range(rows):
            self.ui.tableView.setRowHeight(row, 50)

        self.ui.tableView.setColumnWidth(0, 215)
        self.ui.tableView.setColumnWidth(1, 275)
        self.ui.tableView.setColumnWidth(2, 250)
        self.ui.tableView.setColumnWidth(3, 110)
        self.ui.tableView.setColumnWidth(4, 110)
        self.ui.tableView.setColumnWidth(5, 110)
        self.ui.tableView.setColumnWidth(6, 110)
        self.ui.tableView.setColumnWidth(7, 110)

        cash_balance = self.balance_model.cash_balance
        bank_balance = self.balance_model.bank_balance
        total_balance = cash_balance + bank_balance

        self.ui.editCashBalance.setText(str(cash_balance))
        self.ui.editBankBalance.setText(str(bank_balance))
        self.ui.editTotalBalance.setText(str(total_balance))

    # #########################  functions for File Menu  #########################
    def editBasicDetails(self):
        dlg = UpdateBasicDetails(self)

    def periodMismatch(self):
        dlg = PeriodMisMatch(self)

    def editAccountBalance(self):
        dlg = ShowOpeningBalance(self)

    def showTransactions(self):
        dlg = ShowTransactions(self)

    def loadOwnerImage(self):
        img = "src/icons/app_image.png"
        pixmap = QPixmap(img).scaled(375, 125, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labelImage.setPixmap(pixmap)

    def changeOwnerImage(self):
        # when user will select a file to change the current image
        src, _ = QFileDialog.getOpenFileName(self, "Select Image", "/home/", "Image files (*.jpg *.png)")
        if src:
            img = "src/icons/app_image.png"
            shutil.copyfile(src, img, follow_symlinks=True)
            pixmap = QPixmap(img).scaled(375, 125, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.labelImage.setPixmap(pixmap)
            self.ui.labelImage.setAlignment(Qt.AlignRight)

    def aboutAppDev(self):
        dlg = About(self)

    # #########################  functions for Account Menu  #########################
    def addAccount(self):
        dlg = AddAccount(self)

    def editAccount(self):
        dlg = EditAccount(self)

    def deleteAccount(self):
        dlg = DeleteAccount(self)

    def viewAccount(self):
        dlg = ViewAccount(self)

    # #########################  functions for Head Menu  #########################
    def addHead(self):
        dlg = AddHead(self)

    def editHead(self):
        dlg = EditHead(self)

    def viewHead(self):
        dlg = ViewHead(self)

    def deleteHead(self):
        dlg = DeleteHead(self)

    # #########################  functions for Receipt Menu  #########################
    def addReceipt(self):
        dlg = AddTransaction(self, self.trans_types_list[0])

    def editReceipt(self):
        dlg = EditTransaction(self, self.trans_types_list[0])

    def viewReceipt(self):
        dlg = ViewTransaction(self, self.trans_types_list[0])

    def deleteReceipt(self):
        dlg = DeleteTransaction(self, self.trans_types_list[0])

    # #########################  functions for Payment Menu  #########################
    def addPayment(self):
        dlg = AddTransaction(self, self.trans_types_list[1])

    def editPayment(self):
        dlg = EditTransaction(self, self.trans_types_list[1])

    def viewPayment(self):
        dlg = ViewTransaction(self, self.trans_types_list[1])

    def deletePayment(self):
        dlg = DeleteTransaction(self, self.trans_types_list[1])

    # #########################  functions for Contra Entry Menu  #########################
    def viewReceiptContra(self):
        dlg = ViewTransaction(self, 'ContraReceipt')

    def viewPaymentContra(self):
        dlg = ViewTransaction(self, 'ContraPayment')

    def viewAllContra(self):
        dlg = ViewTransaction(self, "ContraAll")

    # #########################  function for Users Menu #########################
    def showUsers(self):
        dlg = ShowUsers(self)

    def resetUserCredentials(self):
        users = viewUser(self)
        user_name, ok = QInputDialog.getItem(self, 'Select user', 'Username', users, 1, False)
        if ok:
            resetUserCredentials(self, user_name)

    def changePassword(self):
        dlg = ChangePassword(self, self.user_id)

    def changeUsername(self):
        dlg = ChangeUsername(self, self.user_id, self.user_name)

    # #########################  function for initialization  #########################
    def initializeData(self):
        if transDateMismatch():
            title = "Initialization can not be done"
            showMismatchMessage(self, title=title)
            return
        dlg = InitializeTransaction(self, self.user_id)

    # #########################  function for events  #########################

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        title = 'Confirm Exit'
        msg = 'Are you sure you want to exit?'

        if MsgBox(title, msg, 'E&xit', '&Cancel').confirm():
            self.query.finish()
            self.balance_model.query.finish()
            self.conn.close()
            self.conn.setDatabaseName("")
            QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
            event.accept()
            print('is database open while closing mainwindow? ', self.conn.isOpen())
        else:
            event.ignore()
