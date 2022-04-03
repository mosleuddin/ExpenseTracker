import sqlite3

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery

from db.table_basic_details import getPeriod
from modules.module import read_only


def insertTransaction(parent, trans_date, trans_head,
                      trans_details, trans_account, trans_amount):
    tr_date = trans_date.toString("dd-MM-yyyy")
    tr_head_id = getHeadId(trans_head)
    tr_details = trans_details.title()
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
    tr_id = trans_id
    tr_date = trans_date.toString("dd-MM-yyyy")
    tr_head_id = getHeadId(trans_head)
    tr_details = trans_details.title()
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
    try:
        query = QSqlQuery()
        query.exec(""" DELETE FROM trans """)
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete bank n!!!")
    print("all transactions removed")


def getHeadId(head_name):
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
    query = QSqlQuery()
    query.prepare("SELECT HeadName FROM head WHERE HeadType = :HeadType")
    query.bindValue(":HeadType", trans_type)
    query.exec()

    while query.next():
        item = query.value(0)
        parent.ui.comboHead.addItem(parent.parent.common_icon, item)

    query.finish()

    if parent.ui.comboHead.count() == 0:
        parent.ui.comboHead.setPlaceholderText("No head available")


def populateComboAccount(parent):
    query = QSqlQuery()
    query.exec("SELECT AccountNumber FROM account ORDER BY AccountId")
    while query.next():
        account_number = query.value(0)
        parent.ui.comboAccount.addItem(parent.parent.common_icon, account_number)

    query.finish()

    if parent.ui.comboAccount.count() == 0:
        parent.ui.comboAccount.setPlaceholderText("No account available")


def populateBankDetails(parent, account_number):
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
        # set some widgets readonly
        read_only(parent.bg, parent.ui.dateTrans,
                  parent.ui.editTransDetails,
                  parent.ui.editTransAmount)

        parent.ui.comboHead.setEnabled(False)
        parent.ui.comboAccount.setEnabled(False)

        parent.ui.dateTrans.setStyleSheet('background-color: rgb(239, 224, 200); color:rgb(0, 0, 255)')
        parent.ui.editTransDetails.setStyleSheet('background-color: rgb(239, 224, 200); color:rgb(0, 0, 255)')
        parent.ui.comboHead.setStyleSheet('background-color: rgb(239, 224, 200); color:rgb(0, 0, 255)')
        parent.ui.comboAccount.setStyleSheet('background-color: rgb(239, 224, 200); color:rgb(0, 0, 255)')
        parent.ui.editTransAmount.setStyleSheet('background-color: rgb(239, 224, 200); color:rgb(0, 0, 255)')

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


def setDateRange(parent):
    month, year = getPeriod()

    # get minimum date
    minimum = f"01-{month}-{year}"
    min_date = QDate().fromString(minimum, "dd-MMMM-yyyy")

    # get maximum date
    days = min_date.daysInMonth()
    maximum = f"{days}-{month}-{year}"
    max_date = QDate().fromString(maximum, "dd-MMMM-yyyy")

    # set date range to the transDate widget
    parent.ui.dateTrans.setDateRange(min_date, max_date)


def TransDateMismatch():
    status = False
    date = ""
    month, year = getPeriod()
    period_month_year = QDate().fromString(f"{year}{month}", "yyyyMMMM").toString("yyyyMM")

    query = QSqlQuery()
    query.exec("SELECT TransDate FROM trans Order By TransDate")

    while query.next():
        date = query.value(0)
        record_month_year = QDate().fromString(f"{date}", "dd-MM-yyyy").toString("yyyyMM")

        if record_month_year != period_month_year:
            status = True
            break

    query.finish()
    return status


def getMisMatchRecordId():
    data = []
    month, year = getPeriod()
    correct_period = QDate().fromString(f"{year}{month}", "yyyyMMMM").toString("yyyyMM")

    query = QSqlQuery()
    query.exec("SELECT TransId, TransDate FROM trans")

    while query.next():
        trans_id = query.value(0)
        trans_date = query.value(1)

        period = QDate().fromString(f"{trans_date}", "dd-MM-yyyy").toString("yyyyMM")

        if period != correct_period:
            data.append(trans_id)

    query.finish()
    return data


def populateMisMatchRecord(parent, trans_id):
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

    parent.ui.dateTrans.setStyleSheet("background-color:rgb(255, 250, 250); color:rgb(0, 0, 255)")

    parent.ui.dateTrans.setFocus()


def validDate(parent, date):
    month, year = getPeriod()

    # get minimum date
    minimum = f"01-{month}-{year}"
    min_date = QDate().fromString(minimum, "dd-MMMM-yyyy")

    # get maximum date
    days = min_date.daysInMonth()
    maximum = f"{days}-{month}-{year}"
    max_date = QDate().fromString(maximum, "dd-MMMM-yyyy")

    # get current date
    current_date = QDate().currentDate()

    if date > current_date:
        return False
    elif date > max_date:
        return False
    elif date < min_date:
        return False
    else:
        return True
