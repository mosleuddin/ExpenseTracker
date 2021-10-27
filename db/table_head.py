import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox


def insertHead(parent, head_name):
    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO head(HeadName)
                          VALUES(:HeadName)
                     """)

        query.bindValue(":HeadName", head_name)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not add head!!!")


def updateHead(parent, head_id, head_name):
    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE head SET HeadName = :HeadName
                                         WHERE HeadId = :HeadId """)

        query.bindValue(":HeadId", head_id)
        query.bindValue(":HeadName", head_name)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not edit head!!!")


def removeHead(parent, head_id):
    try:
        query = QSqlQuery()
        query.prepare(""" DELETE from head
                          WHERE HeadId = :HeadId
                      """)

        query.bindValue(":HeadId", head_id)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete head!!!")


def getHeadId(parent):
    """
    get value of the field LastId from tracker table and
    the function to be called once only from __init__ method
    of ExpHead class
    """
    ref = 'head_tracker'
    head_id = 0

    query = QSqlQuery()
    query.prepare("SELECT LastId FROM tracker WHERE TableRef = :TableRef")
    query.bindValue(":TableRef", ref)
    query.exec()

    while query.next():
        head_id = query.value(0)

    query.finish()

    head_id += 1
    parent.ui.labelDispalyId.setText(str(head_id))


def setHeadId(val):
    """
    1.  set value to the field LastId in tracker table

    2.  the function to be called from onOkPressed function
        after every successful addition of a head
   """
    ref = 'head_tracker'
    query = QSqlQuery()
    if val == 1:
        query.prepare("INSERT INTO tracker(TableRef, LastId) VALUES(:TableRef, :LastId)")

    else:
        query.prepare("""UPDATE tracker SET LastId = :LastId
                         WHERE TableRef = :TableRef
                     """)

    query.bindValue(":LastId", val)
    query.bindValue(":TableRef", ref)
    query.exec()
    query.finish()


def populateComboHead(parent):
    query = QSqlQuery()
    query.exec("SELECT HeadName FROM head ORDER BY HeadName")
    while query.next():
        item = query.value(0)
        parent.ui.comboHead.addItem(item)
    query.finish()


def populateEditHeadName(parent, head_name):
    """
    Populate Head Id and Head Name depending on the value selected in the
    comboHeadName.

    The function needs to be called from onSearchPressed function

   """
    h_id = 0
    h_name = ''
    query = QSqlQuery()
    query.prepare("""SELECT HeadId, HeadName
                     FROM head
                     WHERE HeadName = :HeadName
                 """)
    query.bindValue(":HeadName", head_name)
    query.exec()

    while query.next():
        h_id = query.value(0)
        h_name = query.value(1)

    query.finish()

    parent.ui.labelDispalyId.setText(str(h_id))
    parent.ui.editHeadName.setText(h_name)

