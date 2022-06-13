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

import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox


def insertAccount(parent, account_number, customer_name, bank_name, branch_name):
    """
        The function create a new account in accordance with the parameters
    """
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
    """
        The function update an existing account in accordance with the parameters
     """
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
    """
        The function delete an existing account in accordance with the parameters
    """
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
    """
    The function confirm whether Cash account exist or not return a numeric value accordingly
    """

    account_number = "Cash".capitalize()
    result = 0
    query = QSqlQuery()
    query.prepare("SELECT COUNT(AccountNumber) FROM account WHERE AccountNumber = :AccountNumber")
    query.bindValue(":AccountNumber", account_number)
    query.exec()
    while query.next():
        result = query.value(0)
    query.finish()

    return result


def bankAccountExists(account_number):
    """
        The function confirm whether a particular bank account exists or not and
        return a numeric value accordingly
    """
    account_number = account_number.capitalize()
    result = 0

    query = QSqlQuery()
    query.prepare("SELECT COUNT(AccountNumber) FROM account WHERE AccountNumber = :AccountNumber")
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        result = query.value(0)
    query.finish()

    return result


def populateComboAccount(parent):
    """
    The function populate all account number in a combo box to make available for selection
    """

    parent.ui.comboAccount.clear()

    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account ORDER BY AccountNumber")
    while query.next():
        item = query.value(0)
        if not item.lower() == "cash":
            parent.ui.comboAccount.addItem(item)
    query.finish()

    if parent.ui.comboAccount.count() == 0:
        parent.ui.comboAccount.setPlaceholderText("No account available")


def populateWidgets(parent, account_number, action=''):
    """
    The function populate all the corresponding data of the selected bank account
    in different widgets to update or delete
    """

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

    # disable editAccountNumber & change it's label to remove access key
    parent.ui.editAccountNumber.setEnabled(False)
    parent.ui.labelAccountNumber.setText('Account Number')

    # set values to parent variables
    parent.selected_account_id = account_id
    parent.selected_account_number = account_number
    parent.selected_customer_name = customer_name
    parent.selected_bank_name = bank_name
    parent.selected_branch_name = branch_name

    if action == 'delete':
        # disable all remaining widgets & change their label to remove access key
        parent.ui.editCustomerName.setEnabled(False)
        parent.ui.comboBankName.setEnabled(False)
        parent.ui.editBranchName.setEnabled(False)

        parent.ui.labelCustomerName.setText('Customer Name')
        parent.ui.labelBankName.setText('Bank Name')
        parent.ui.labelBranchName.setText('Branch Name')


def getAllAccountNumbers():
    """
    The function collects all Account Numbers from account table and return them
    as a list of items

    """

    account_numbers = []
    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account")
    while query.next():
        item = query.value(0)
        account_numbers.append(item)
    query.finish()
    return account_numbers


def account_related_transaction_exists(account_number):
    """
     The function checks whether any transaction of a
     particular account number, exists in the trans table or not
    """

    query = QSqlQuery()
    query.prepare("""SELECT count(TransId)
                     FROM trans
                     join account using(AccountId)
                     WHERE account.AccountNumber = :AccountNumber
                     """)

    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        count = query.value(0)
        return count
