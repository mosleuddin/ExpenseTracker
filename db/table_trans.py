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

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery

from db.table_basic_details import getPeriod


def insertTransaction(parent, trans_date, trans_head, trans_details,
                      trans_account, trans_amount):

    """
    The function inserts new transaction into trans table using the parameters values
    """

    tr_date = trans_date.toString("dd-MM-yyyy")
    tr_head_id = getHeadId(trans_head)
    tr_details = trans_details
    tr_account_id = getAccountId(trans_account)
    tr_amount = int(trans_amount)

    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO trans(TransDate, HeadId,
                          TransDetails, AccountId, TransAmount)
                          
                          VALUES(:TransDate, :HeadId,
                                 :TransDetails, :AccountId, :TransAmount)
                     """)

        query.bindValue(":TransDate", tr_date)
        query.bindValue(":HeadId", tr_head_id)

        query.bindValue(":TransDetails", tr_details)
        query.bindValue(":AccountId", tr_account_id)
        query.bindValue(":TransAmount", tr_amount)

        query.exec()
        query.finish()

    except sqlite3.Error:
        title = "Database Error"
        msg = "Unable to complete the transaction"
        QMessageBox().warning(parent=parent, title=title, text=msg)


def updateTransaction(parent, trans_id, trans_date, trans_head,
                      trans_details, trans_account, trans_amount):
    """
    The function edits an existing transaction in trans table using the parameters values
    """

    tr_id = trans_id
    tr_date = trans_date.toString("dd-MM-yyyy")
    tr_head_id = getHeadId(trans_head)
    tr_details = trans_details
    tr_account_id = getAccountId(trans_account)
    tr_amount = int(trans_amount)

    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE trans SET 
                          TransDate = :TransDate,
                          HeadId = :HeadId,
                          TransDetails = :TransDetails,
                          AccountId = :AccountId,
                          TransAmount = :TransAmount
                          WHERE TransId = :TransId
                      """)

        query.bindValue(":TransDate", tr_date)
        query.bindValue(":HeadId", tr_head_id)
        query.bindValue(":TransDetails", tr_details)
        query.bindValue(":AccountId", tr_account_id)
        query.bindValue(":TransAmount", tr_amount)
        query.bindValue(":TransId", tr_id)

        query.exec()
        query.finish()

    except sqlite3.Error:
        title = "Database Error"
        msg = "could not update transaction"
        QMessageBox().warning(parent=parent, title=title, text=msg)


def removeTransaction(parent, trans_id):
    """
    The function deletes an existing transaction from trans table using trans_id value
    """

    try:
        query = QSqlQuery()
        query.prepare(""" DELETE from trans
                          WHERE TransId = :TransId
                      """)

        query.bindValue(":TransId", trans_id)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete bank n!!!")


def removeAllTransactions(parent):
    """
    The function deletes all the records from the trans table
    """
    try:
        query = QSqlQuery()
        query.exec("DELETE FROM trans")
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete bank n!!!")
    print("all transactions removed")


def getHeadId(head_name):
    """
    The function collects HeadId from head table using head_name parameter
    """
    head_id = None
    query = QSqlQuery()
    query.prepare("SELECT HeadId FROM head WHERE HeadName = :HeadName")
    query.bindValue(":HeadName", head_name)
    query.exec()

    while query.next():
        head_id = query.value(0)

    query.finish()
    return head_id


def getAccountId(account_number):
    """
    The function collects Account Id from account table using account_number parameter
    """

    account_id = None

    query = QSqlQuery()
    query.prepare("SELECT AccountId FROM account WHERE AccountNumber = :AccountNumber")
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        account_id = query.value(0)

    query.finish()
    return account_id


def populateComboHead(parent, trans_type=''):
    """
    The function collects all the HeadName from head table using trans_type parameter
    and populates the collected data in a combo box
    """
    query = QSqlQuery()
    query.prepare("SELECT HeadName FROM head WHERE HeadType = :HeadType ORDER BY HeadName")
    query.bindValue(":HeadType", trans_type)
    query.exec()

    while query.next():
        item = query.value(0)
        parent.ui.comboHead.addItem(item)

    query.finish()

    if parent.ui.comboHead.count() == 0:
        parent.ui.comboHead.setPlaceholderText("No head available")


def populateComboAccount(parent):
    """
     The function collects all the AccountNumber from account table and
     populates the collected data in a combo box
    """
    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account ORDER BY AccountId")
    while query.next():
        account_number = query.value(0)
        parent.ui.comboAccount.addItem(account_number)

    query.finish()

    if parent.ui.comboAccount.count() == 0:
        parent.ui.comboAccount.setPlaceholderText("No account available")


def populateBankDetails(parent, account_number):
    """
    The function collects CustomerName and BankName from account table using
    account_number criteria and update the setText property of two QLabel widgets.
    """
    customer_name = None
    bank_name = None

    query = QSqlQuery()
    query.prepare("SELECT CustomerName, BankName FROM account WHERE AccountNumber = :AccountNumber")
    query.bindValue(":AccountNumber", account_number)
    query.exec()

    while query.next():
        customer_name = query.value(0)
        bank_name = query.value(1)

    query.finish()

    parent.ui.labelCustomerName.setText(customer_name)
    parent.ui.labelBankName.setText(bank_name)
    return


def recordExists(trans_id, trans_type):
    """
     The function checks whether any transaction of a
     particular head_type exists in the trans table or not
    """
    trans_id = int(trans_id)

    query = QSqlQuery()

    query.prepare("""SELECT count(TransId)
                     FROM trans
                     join head using(HeadId)
                     WHERE head.HeadType = :TransType AND trans.TransId = :TransId
                     """)

    query.bindValue(":TransType", trans_type)
    query.bindValue(":TransId", trans_id)
    query.exec()

    while query.next():
        item = query.value(0)
        return item


def populateWidgets(parent, trans_id, action=''):
    """
    The function collects TransDate, HeadName, TransDetails, AccountNumber, TransAmount
    data from trans, head and account table using the value of trans_id parameters and
    populate them in various widgets
    """

    trans_id = int(trans_id)
    date = None
    head_name = None
    details = None
    account_number = None
    amount = None

    query = QSqlQuery()

    query.prepare("""SELECT TransDate, HeadName, TransDetails, AccountNumber, TransAmount
                        FROM trans
                        join head using(HeadId)
                        join account using(AccountId)
                        WHERE TransId = :TransId 
                    """)

    query.bindValue(":TransId", trans_id)
    query.exec()
    while query.next():
        date = query.value(0)
        head_name = query.value(1)
        details = query.value(2)
        account_number = query.value(3)
        amount = query.value(4)

    query.finish()

    # set parent variables values
    parent.current_trans_id = trans_id
    parent.current_trans_date = QDate().fromString(date, "dd-MM-yyyy")
    parent.current_trans_details = details
    parent.current_trans_amount = str(amount)

    parent.current_trans_head_name = head_name
    parent.current_trans_account_number = account_number

    # populate data in line edits and date widget
    parent.ui.dateTrans.setDate(parent.current_trans_date)
    parent.ui.editTransDetails.setText(parent.current_trans_details)
    parent.ui.editTransAmount.setText(parent.current_trans_amount)
    parent.ui.comboHead.setCurrentText(parent.current_trans_head_name)
    parent.ui.comboAccount.setCurrentText(parent.current_trans_account_number)

    # if called from DeleteTransaction class
    if action.lower() == 'delete':
        # disable some widgets
        parent.ui.dateTrans.setEnabled(False)
        parent.ui.comboHead.setEnabled(False)
        parent.ui.editTransDetails.setEnabled(False)
        parent.ui.comboAccount.setEnabled(False)
        parent.ui.editTransAmount.setEnabled(False)

        # Reassign the text of labels to remove accelerate key
        parent.ui.labelTransDate.setText('Date')
        parent.ui.labelHead.setText('Head')

        parent.ui.labelTransDetails.setText('Details')
        parent.ui.labelAccount.setText('Account Number')

        parent.ui.labelTransAmount.setText('Amount')

        # enable Ok button
        parent.ui.buttonOk.setEnabled(True)
        parent.ui.buttonOk.setFocus()

    else:
        # enable Ok button
        parent.ui.buttonOk.setEnabled(False)
        parent.ui.dateTrans.setFocus()


def transDateMismatch():
    """
    1.  The function collects month and year from period table via getPeriod().

    2.  Then create QDate() in the format "yyyyMM" using the collected month and year and
    stores it's value as a string in valid_month_year variable.

    3. Now selects all TransDate from trans table.

    4. Each and every date is a string in "dd-MM-yyyy" format.

    5. converts Each and every date to a string in "yyyyMM" format so that it can be compared
    with the valid_month_year variable.

    6. Lastly check whether each and every date is matching with valid_month_year variable.

    """
    status = False
    date = ""
    month, year = getPeriod()
    valid_month_year = QDate().fromString(f"{year}{month}", "yyyyMMMM").toString("yyyyMM")

    query = QSqlQuery()
    query.exec("SELECT TransDate FROM trans Order By TransDate")

    while query.next():
        date = query.value(0)
        month_year = QDate().fromString(f"{date}", "dd-MM-yyyy").toString("yyyyMM")

        if month_year != valid_month_year:
            status = True
            break

    query.finish()
    return status


def getMisMatchRecordId():
    """
       1.  This function is quite similar to the TransDateMismatch function.

       2.  However this function also select the TransId in addition to the TransDate.

       4. Then it scans all the records and appends the TransId of all the records whose
        transaction period does not match with the valid_period variable in a list.

       5. Lastly it returns the list of mismatch TransId.

       """

    data = []
    month, year = getPeriod()
    valid_month_year = QDate().fromString(f"{year}{month}", "yyyyMMMM").toString("yyyyMM")

    query = QSqlQuery()
    query.exec("SELECT TransId, TransDate FROM trans")

    while query.next():
        trans_id = query.value(0)
        trans_date = query.value(1)

        period = QDate().fromString(f"{trans_date}", "dd-MM-yyyy").toString("yyyyMM")

        if period != valid_month_year:
            data.append(trans_id)

    query.finish()
    return data


def populateMisMatchRecord(parent, trans_id):
    """
    1.  The function collects all the required fields of a record (from trans table)
    which has a invalid period.

    2. The record is fetched using the trans_id parameter.

    2.  Lastly it populates the widgets of the calling window accordingly.

    """

    trans_id = int(trans_id)
    date = None
    head_name = None
    details = None
    account_number = None
    customer_name = None
    bank_name = None
    amount = None

    query = QSqlQuery()

    query.prepare("""SELECT TransDate, HeadName, TransDetails, AccountNumber,
                     TransAmount, CustomerName, BankName
                        FROM trans
                        join head using(HeadId)
                        join account using(AccountId)
                        WHERE TransId = :TransId 
                    """)

    query.bindValue(":TransId", trans_id)
    query.exec()
    while query.next():
        date = query.value(0)
        head_name = query.value(1)
        details = query.value(2)
        account_number = query.value(3)
        amount = query.value(4)
        customer_name = query.value(5)
        bank_name = query.value(6)

    query.finish()

    # change data types
    date = QDate().fromString(date, "dd-MM-yyyy")
    amount = str(amount)

    # update parent date variable
    parent.old_trans_date = date

    # populate data in line edits and date widget
    parent.ui.dateTrans.setDate(date)
    parent.ui.editHead.setText(head_name)
    parent.ui.editTransDetails.setText(details)
    parent.ui.editAccount.setText(account_number)
    parent.ui.editTransAmount.setText(amount)

    if account_number.lower() == "cash":
        parent.ui.labelCustomerName.setText("")
        parent.ui.labelBankName.setText("")
    else:
        parent.ui.labelCustomerName.setText(customer_name)
        parent.ui.labelBankName.setText(bank_name)

    parent.ui.dateTrans.setFocus()


def validDate(parent, date):
    """
    1.  The function performs the date validation in following classes:
     AddTransaction, EditTransaction and PeriodMisMatch

    """

    exp_month, exp_year = getPeriod()

    first_date = QDate().fromString(f"01-{exp_month}-{exp_year}", "dd-MMMM-yyyy")
    days_in_month = first_date.daysInMonth()
    last_date = QDate().fromString(f"{days_in_month}-{exp_month}-{exp_year}", "dd-MMMM-yyyy")

    # get current date
    current_date = QDate().currentDate()

    if date > current_date:
        return "Expenditure for future date is not allowed !!!"
    else:
        if date < first_date or date > last_date:
            return f'Please select a date between {first_date.toString("dd MMMM yyyy")} to {last_date.toString("dd MMMM yyyy")}'
        else:
            return "ok"
