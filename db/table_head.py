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
    head_id = 0
    query = QSqlQuery()
    query.exec("SELECT seq FROM sqlite_sequence WHERE name = 'head'")
    while query.next():
        if query.isValid():
            head_id = int(query.value(0))
            break
    query.finish()
    parent.ui.labelDispalyId.setText(str(head_id + 1))


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
