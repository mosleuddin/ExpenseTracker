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


def trans_data_exist(parent):
    """
    This function count and return total number of transactions available in trans table

    """

    data_count = 0
    try:
        query = QSqlQuery()
        query.exec("SELECT COUNT(TransId) FROM trans")
        while query.next():
            data_count = query.value(0)

        query.finish()

        return data_count

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not count data!!!")


def getAllTransactions():
    """
    The function collect all receipt transactions and payment transactions from trans table.

    It also collect other details related with each transaction from head and account tables.

    Return all the collected data in the form of a list of tuple.
    """

    data = []

    query = QSqlQuery()
    query.exec("""SELECT TransDate, HeadName, TransDetails,
                  BankName, CustomerName, AccountNumber,  TransAmount, HeadType
                  FROM trans
                  JOIN head ON head.HeadId = trans.HeadId
                  JOIN account ON account.AccountId = trans.AccountId
                  ORDER BY TransDate
                """)

    while query.next():
        date = query.value(0)
        head = query.value(1)
        details = query.value(2)
        bank = query.value(3)
        customer = query.value(4)
        account = query.value(5)
        amount = query.value(6)
        head_type = query.value(7)

        if head_type == "Receipt":
            receipt_amount = amount
            payment_amount = 0
        else:
            receipt_amount = 0
            payment_amount = amount

        record = (date, head, details, bank, customer, account, receipt_amount, payment_amount, head_type)
        data.append(record)
    query.finish()
    return data


def getHeadTotals():
    """
       The function collect sum of transactions i/r/o of each Transaction Head from trans table.

       Return all the collected data in the form of a list of tuple.
       """

    data = []

    query = QSqlQuery()
    query.exec("""SELECT HeadType, HeadName, SUM(TransAmount)
                  FROM trans
                  JOIN head ON head.HeadId = trans.HeadId
                  Group BY HeadName
                  ORDER BY HeadType, HeadName
                """)

    while query.next():
        head_type = query.value(0)
        head_name = query.value(1)
        head_total = query.value(2)

        record = (head_type, head_name, head_total)
        data.append(record)

    query.finish()
    return data


