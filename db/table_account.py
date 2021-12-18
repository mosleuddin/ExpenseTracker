import sqlite3

from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox

from modules.module import read_only


def insertAccount(parent, account_number, customer_name, bank_name, branch_name):
    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO account(AccountNumber, CustomerName, BankName, BranchName)
                          VALUES(:AccountNumber, :CustomerName, :BankName, :BranchName)
                     """)

        query.bindValue(":AccountNumber", account_number)
        query.bindValue(":CustomerName", customer_name)
        query.bindValue(":BankName", bank_name)
        query.bindValue(":BranchName", branch_name)

        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not add bank account!!!")


def updateAccount(parent, account_number, customer_name, bank_name, branch_name):
    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE account SET 
                          CustomerName = :CustomerName,
                          BankName = :BankName,
                          BranchName = :BranchName
                          WHERE AccountNumber = :AccountNumber
                      """)

        query.bindValue(":CustomerName", customer_name)
        query.bindValue(":BankName", bank_name)
        query.bindValue(":BranchName", branch_name)
        query.bindValue(":AccountNumber", account_number)

        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not edit bank account!!!")


def removeAccount(parent, account_number):
    try:
        query = QSqlQuery()
        query.prepare(""" DELETE from account
                          WHERE AccountNumber = :AccountNumber
                      """)

        query.bindValue(":AccountNumber", account_number)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete bank account!!!")


def populateComboAccount(parent):
    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account ORDER BY AccountNumber")
    while query.next():
        item = query.value(0)
        parent.ui.comboAccount.addItem(item)
    query.finish()

    if parent.ui.comboAccount.count() == 0:
        parent.ui.comboAccount.setPlaceholderText("No account available")


def populateWidgets(parent, account_number, action=''):
    account_id = ''
    customer_name = ''
    bank_name = ''
    branch_name = ''

    query = QSqlQuery()
    query.prepare("""SELECT AccountId, CustomerName, BankName, BranchName
                     FROM account
                     WHERE AccountNumber = :AccountNumber
                 """)
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        account_id = query.value(0)
        customer_name = query.value(1)
        bank_name = query.value(2)
        branch_name = query.value(3)

    query.finish()

    if action == 'delete':
        # set parent widget values for delete account window
        parent.ui.labelBankName2.hide()
        parent.ui.comboBankName.hide()

        parent.ui.editBankName.setText(bank_name)
        parent.ui.labelBankName1.show()
        parent.ui.editBankName.show()

        read_only(parent.bg, parent.ui.editAccountNumber, parent.ui.editCustomerName,
                  parent.ui.editBankName, parent.ui.editBranchName)

        parent.ui.labelAccountNumber.setText('Account Number')
        parent.ui.labelCustomerName.setText('Customer Name')
        parent.ui.labelBranchName.setText('Branch Name')

        parent.ui.buttonOk.setEnabled(True)
        parent.ui.buttonOk.setFocus()

    else:
        # set parent widget value for edit account windows
        parent.ui.comboBankName.setCurrentText(bank_name)
        read_only(parent.bg, parent.ui.editAccountNumber)
        parent.ui.labelAccountNumber.setText('Account Number')
        parent.ui.buttonOk.setEnabled(False)

    # set parent widget values for the both edit & delete account windows
    parent.ui.editAccountNumber.setText(str(account_number))
    parent.ui.editCustomerName.setText(customer_name)
    parent.ui.editBranchName.setText(branch_name)

    # set parent variables values
    parent.selected_account_id = account_id
    parent.selected_account_number = account_number
    parent.selected_customer_name = customer_name
    parent.selected_bank_name = bank_name
    parent.selected_branch_name = branch_name
