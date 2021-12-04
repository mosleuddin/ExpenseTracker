import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox


def insertHead(parent, head_type, head_name):
    try:
        query = QSqlQuery()
        query.prepare(""" INSERT INTO head(HeadType, HeadName)
                          VALUES(:HeadType, :HeadName)
                     """)

        query.bindValue(":HeadType", head_type)
        query.bindValue(":HeadName", head_name)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not add head!!!")


def updateHead(parent, head_id, head_type, head_name):
    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE head SET
                                        HeadType = :HeadType,
                                        HeadName = :HeadName
                          WHERE HeadId = :HeadId
                      """)

        query.bindValue(":HeadType", head_type)
        query.bindValue(":HeadName", head_name)
        query.bindValue(":HeadId", head_id)

        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not edit head!!!")


def removeHead(parent, head_name):
    try:
        query = QSqlQuery()
        query.prepare(""" DELETE from head
                          WHERE HeadName = :HeadName
                      """)

        query.bindValue(":HeadName", head_name)
        query.exec()
        query.finish()

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Can not delete head!!!")


def populateComboHead(parent):
    query = QSqlQuery()
    query.exec("SELECT HeadName FROM head ORDER BY HeadName")
    while query.next():
        item = query.value(0)
        parent.ui.comboHead.addItem(item)
    query.finish()

    if parent.ui.comboHead.count() == 0:
        parent.ui.comboHead.setPlaceholderText("No head available")


def populateWidgets(parent, head_name):
    head_id =''
    head_type = ''
    query = QSqlQuery()
    query.prepare("""SELECT HeadId, HeadType
                     FROM head
                     WHERE HeadName = :HeadName
                 """)
    query.bindValue(":HeadName", head_name)
    query.exec()

    while query.next():
        head_id = query.value(0)
        head_type = query.value(1)

    query.finish()

    # set parent widget values
    parent.ui.comboHeadType.setCurrentText(head_type)
    parent.ui.editHeadName.setText(head_name)

    # set parent variables values
    parent.selected_head_id = head_id
    parent.selected_head_name = head_name

