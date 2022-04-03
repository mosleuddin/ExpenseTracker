import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox

from modules.module import read_only


def insertAccount(parent, account_number, customer_name, bank_name, branch_name):
    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO account(
                          AccountNumber, CustomerName, BankName, BranchName)
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


def cashAccountExists(parent):
    account_number = "Cash".capitalize()
    result = 0
    query = QSqlQuery()
    query.prepare("SELECT COUNT(AccountNumber) FROM account WHERE AccountNumber = :AccountNumber")
    query.bindValue(":AccountNumber", account_number)
    query.exec()
    while query.next():
        acct = query.value(0)
    query.finish()

    return result


def bankAccountExists(account_number, task):
    query = QSqlQuery()
    if task == 'add':
        query.prepare("SELECT AccountNumber FROM account")
    else:
        query.prepare(f"SELECT AccountNumber FROM account WHERE AccountId != :AccountId")
        query.bindValue(":AccountId", account_number)
    query.exec()

    while query.next():
        if query.value(0) == account_number:
            query.finish()
            return True
    query.finish()
    return False


def populateComboAccount(parent):
    parent.ui.comboAccount.clear()

    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account ORDER BY AccountNumber")
    while query.next():
        item = query.value(0)
        if not item.lower() == "cash":
            parent.ui.comboAccount.addItem(parent.common_icon, item)
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

    # set values to parent widget
    parent.ui.editAccountNumber.setText(account_number)
    parent.ui.editCustomerName.setText(customer_name)
    parent.ui.comboBankName.setCurrentText(bank_name)
    parent.ui.editBranchName.setText(branch_name)

    # make editAccountNumber read-only & change it's label to remove access key
    read_only(parent.bg, parent.ui.editAccountNumber)
    parent.ui.labelAccountNumber.setText('Account Number')

    # set values to parent variables
    parent.selected_account_id = account_id
    parent.selected_account_number = account_number
    parent.selected_customer_name = customer_name
    parent.selected_bank_name = bank_name
    parent.selected_branch_name = branch_name

    if action == 'delete':
        # make all remaining widgets read-only & change their label to remove access key
        read_only(parent.bg, parent.ui.editCustomerName, parent.ui.editBranchName)

        parent.ui.comboBankName.setEnabled(False)
        parent.ui.comboBankName.setStyleSheet(parent.bg)

        parent.ui.labelCustomerName.setText('Customer Name')
        parent.ui.labelBankName.setText('Bank Name')
        parent.ui.labelBranchName.setText('Branch Name')


def getAllAccountNumbers(parent):
    account_numbers = []
    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account")
    while query.next():
        item = query.value(0)
        account_numbers.append(item)
    query.finish()
    return account_numbers
