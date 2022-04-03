import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QMessageBox


# functions to manipulate opening balance

def insertOpeningBalance(parent, account_number, opening_balance):
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


def getOpeningBalance(account_number):
    data = []
    if account_number == "all":
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


def updateTotal(parent, account_number):
    account_number = account_number.capitalize()
    total_receipt = 0
    total_payment = 0
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

    # update TotalReceipt and TotalPayment for the  current AccountNumber
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


class AccountBalanceSummary(QSqlQueryModel):
    def __init__(self):
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
                   "B/F", "Receipt", "Total", "Payment","C/F")

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
                if col == 7:
                    return QColor(Qt.blue)

            if role == Qt.BackgroundRole:
                if row % 2 == 0:
                    return QColor("#d4e5f6")
                else:
                    return QColor("#EAF1CE")

        return QSqlQueryModel.data(self, index, role)


def updateBalanceTable(parent):
    print("Balance table updated")
    query = QSqlQuery()
    query.exec("""SELECT AccountNumber,
                         OpeningBalance,
                         TotalReceipt,
                         TotalPayment,
                         OpeningBalance + TotalReceipt - TotalPayment
                  FROM   account
                  JOIN   balance USING(AccountNumber)
                  ORDER BY AccountNumber
              """)

    query.exec()

    while query.next():
        account_number = query.value(0)
        closing_balance = query.value(4)
        updateBalanceTableAllData(parent, account_number, closing_balance)

    query.finish()


def updateBalanceTableAllData(parent, acct_num, balance):
    account_number = str(acct_num.capitalize())
    opening_balance = int(balance)
    total_receipt = 0
    total_payment = 0

    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE balance SET 
                          OpeningBalance = :OpeningBalance,
                          TotalReceipt = :TotalReceipt,
                          TotalPayment = :TotalPayment
                          WHERE AccountNumber = :AccountNumber
                      """)

        query.bindValue(":OpeningBalance", opening_balance)
        query.bindValue(":TotalReceipt", total_receipt)
        query.bindValue(":TotalPayment", total_payment)
        query.bindValue(":AccountNumber", account_number)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not update cash balance!!!")

