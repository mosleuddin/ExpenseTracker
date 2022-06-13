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

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QMessageBox

# functions to manipulate opening balance
from db.table_account import getAllAccountNumbers


class AccountBalanceSummary(QSqlQueryModel):
    def __init__(self):
        """
        class to show balances in respect of all accounts at HOME WINDOW
        """
        super(AccountBalanceSummary, self).__init__()
        self.cash_balance = 0
        self.bank_balance = 0
        self.query = QSqlQuery()
        self.query.exec("""SELECT AccountNumber,
                             CustomerName,
                             BankName, 
                             OpeningBalance,
                             TotalReceipt,
                             OpeningBalance + TotalReceipt, 
                             TotalPayment,
                             OpeningBalance + TotalReceipt - TotalPayment
                      FROM   account
                      JOIN   balance USING(AccountNumber)
                      ORDER BY AccountNumber, CustomerName, BankName
                  """)

        while self.query.next():
            account_number = self.query.value(0)
            balance = self.query.value(7)

            if account_number == "Cash":
                self.cash_balance += balance
            else:
                self.bank_balance += balance

        self.setQuery(self.query)

        headers = ("Account Number", "Customer Name", "Bank Name",
                   "Balance B/F", "Receipt", "Total", "Payment", "Balance C/F")

        for columnIndex, header in enumerate(headers):
            self.setHeaderData(columnIndex, Qt.Horizontal, header)

    def data(self, index, role):
        if index.isValid():
            col = index.column()
            row = index.row()

            if role == Qt.TextAlignmentRole:
                if col > 2:
                    return Qt.AlignRight
                else:
                    return Qt.AlignLeft

            if role == Qt.ForegroundRole:
                active_account_number = index.sibling(row, 0).data()
                if active_account_number == "cash".title():
                    return QColor("#EA2929")

        return QSqlQueryModel.data(self, index, role)


def insertOpeningBalance(parent, account_number, opening_balance):
    """
    The function add a new record into the balance table using the parameters
    """
    opening_balance = int(opening_balance)
    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO balance(AccountNumber, OpeningBalance)
                          VALUES(:AccountNumber, :OpeningBalance)
                     """)

        query.bindValue(":AccountNumber", account_number)
        query.bindValue(":OpeningBalance", opening_balance)

        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not insert balance!!!")


def updateOpeningBalance(parent, acct_num, balance):
    """
    The function update opening balance of a account using the  parameters
    """
    account_number = str(acct_num.capitalize())
    opening_balance = int(balance)
    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE balance SET 
                          OpeningBalance = :OpeningBalance
                          WHERE AccountNumber = :AccountNumber
                      """)

        query.bindValue(":OpeningBalance", opening_balance)
        query.bindValue(":AccountNumber", account_number)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not update cash balance!!!")


def getOpeningBalanceGrandTotal():
    """
    The function calculate and return the sum of opening balances
    i/r/o all the existing account in balance table
    """
    total_opening_balance = 0

    query = QSqlQuery()
    query.exec("SELECT SUM(OpeningBalance) FROM balance")

    while query.next():
        total_opening_balance = query.value(0)

    query.finish()

    if total_opening_balance == "":
        return 0
    else:
        return total_opening_balance


def getOpeningBalanceAndBankDetails(account_number=None):
    """
    The function returns opening balances and other bank details i/r/o all accounts
    if account number is not supplied.

    If account number is supplied, details and opening balance of the supplied
    account number will be returned.

    """
    data = []
    if account_number is None:
        query = QSqlQuery()
        query.exec("""SELECT AccountNumber, BankName, CustomerName, OpeningBalance
                      FROM account
                      JOIN balance USING(AccountNumber)
                      ORDER BY AccountNumber, BankName, CustomerName
                  """)

        while query.next():
            account_number = query.value(0)
            bank_name = query.value(1)
            customer_name = query.value(2)
            opening_balance = query.value(3)

            record = (account_number, bank_name, customer_name, str(opening_balance))
            data.append(record)

        query.finish()
        return data
    else:
        account_number = account_number.capitalize()
        query = QSqlQuery()
        query.prepare("""SELECT CustomerName, BankName, BranchName, OpeningBalance
                         FROM account
                         JOIN balance USING(AccountNumber)
                         WHERE AccountNumber = :AccountNumber
                      """)

        query.bindValue(":AccountNumber", account_number)
        query.exec()

        while query.next():
            customer_name = query.value(0)
            bank_name = query.value(1)
            branch_name = query.value(2)
            opening_balance = query.value(3)

            data.append(customer_name)
            data.append(bank_name)
            data.append(branch_name)
            data.append(str(opening_balance))

        query.finish()
        return data


def getTotalReceipt(account_number):
    """
    The function returns the Total Receipt i/r/o the account number parameter
    """
    account_number = account_number.capitalize()
    total_receipt = 0
    query = QSqlQuery()

    # getting TotalReceipt
    query.prepare(""" SELECT SUM(TransAmount)
                      from trans
                      JOIN head USING(HeadId)
                      JOIN account USING(AccountId)
                      WHERE HeadType = :HeadType 
                      AND AccountNumber = :AccountNumber
                 """)

    query.bindValue(":HeadType", "Receipt")
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        total_receipt = query.value(0)

    query.finish()
    if total_receipt == "":
        return 0
    else:
        return total_receipt


def getTotalPayment(account_number):
    """
    This function returns the Total Payment i/r/o the account number parameter
    """
    account_number = account_number.capitalize()
    total_payment = 0
    query = QSqlQuery()

    # getting TotalPayment
    query.prepare(""" SELECT SUM(TransAmount)
                      from trans
                      JOIN head USING(HeadId)
                      JOIN account USING(AccountId)
                      WHERE HeadType = :HeadType
                      AND AccountNumber = :AccountNumber
                 """)

    query.bindValue(":HeadType", "Payment")
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        total_payment = query.value(0)

    query.finish()

    if total_payment == "":
        return 0
    else:
        return total_payment


def getAccountTotals():
    """
    The function calculate and returns opening_balance, total_receipt, gross_amount,
    total_payment, closing_balance and bank details of all accounts
    """

    data = []

    # collect all account numbers
    account_numbers = getAllAccountNumbers()

    for acct_num in account_numbers:
        # get opening balance and corresponding bank details for this account
        bank_details = getOpeningBalanceAndBankDetails(acct_num)

        # store bank details and opening_balance for this account in local variables
        customer = bank_details[0]
        bank = bank_details[1]
        branch = bank_details[2]
        opening_balance = int(bank_details[3])

        # get total receipt for this account and store
        total_receipt = getTotalReceipt(acct_num)

        # calculate and store gross total for this account
        gross_amount = opening_balance + total_receipt

        # get total payment for this account and store
        total_payment = getTotalPayment(acct_num)

        # calculate and store closing balance for this account
        closing_balance = gross_amount - total_payment

        # store the values of all above variables in a tuple
        record = (acct_num, customer, bank, branch,
                  opening_balance, total_receipt, gross_amount,
                  total_payment, closing_balance)

        # add the tuple in a list
        data.append(record)

    # return the list
    return data


def InitializeBalanceTable(month_end=False):
    """
    The function first collect account totals and bank details for each account and then
    performs the following jobs.

    1.   If it is called for  month end initialization(month_end=True), it will replace

    opening balance with closing balance
    total_receipt with 0
    total_payment with 0

    2.   If  called using (month_end=False) or without any argument,  it will only update
    total receipt and total payment with the received data and will not touch opening balance.
    """

    data = getAccountTotals()
    query = QSqlQuery()

    if month_end:
        for record in data:
            account_number = record[0]
            closing_balance = record[8]  # closing balance will be the opening balance of the new month
            total_receipt = 0  # set total receipt and total payment to 0 for the new month
            total_payment = 0

            query.prepare("""UPDATE balance SET
                            OpeningBalance = :OpeningBalance,
                            TotalReceipt = :TotalReceipt,
                            TotalPayment = :TotalPayment
                            WHERE AccountNumber = :AccountNumber
                        """)

            query.bindValue(":OpeningBalance", closing_balance)
            query.bindValue(":TotalReceipt", total_receipt)
            query.bindValue(":TotalPayment", total_payment)
            query.bindValue(":AccountNumber", account_number)
            query.exec()

    else:
        for record in data:
            account_number = record[0]
            total_receipt = record[5]
            total_payment = record[7]

            query.prepare("""UPDATE balance SET
                             TotalReceipt = :TotalReceipt,
                             TotalPayment = :TotalPayment
                             WHERE AccountNumber = :AccountNumber
                          """)

            query.bindValue(":TotalReceipt", total_receipt)
            query.bindValue(":TotalPayment", total_payment)
            query.bindValue(":AccountNumber", account_number)
            query.exec()

    query.finish()
    return
