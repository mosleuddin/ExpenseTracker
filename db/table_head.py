import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox

from modules.module import read_only


def headExists(parent=None):
    head = 0
    try:
        query = QSqlQuery()
        query.exec("SELECT COUNT(HeadId) FROM head")
        while query.next():
            head = query.value(0)

        query.finish()

        return head

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not count head!!!")


def insertHead(parent=None, head_type=None, head_name=None):
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
    head_name1 = "ContraReceipt"
    head_name2 = "ContraPayment"

    query = QSqlQuery()
    query.prepare("""SELECT HeadName FROM head
                  WHERE HeadName NOT IN (:HeadName1, :HeadName2)
                  ORDER BY HeadName
                """)
    query.bindValue(":HeadName1", head_name1)
    query.bindValue(":HeadName2", head_name2)
    query.exec()

    while query.next():
        item = query.value(0)
        parent.ui.comboHead.addItem(parent.parent.common_icon, item)
    query.finish()

    if parent.ui.comboHead.count() == 0:
        parent.ui.comboHead.setPlaceholderText("No head available")


def populateWidgets(parent, head_name, action=''):
    head_id = ''
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

    if action == 'delete':
        # set parent widget values for delete head window
        parent.ui.labelHeadType2.hide()
        parent.ui.comboHeadType.hide()

        parent.ui.editHeadType.setText(head_type)
        parent.ui.labelHeadType1.show()
        parent.ui.editHeadType.show()

        parent.ui.buttonOk.setEnabled(True)
        parent.ui.buttonOk.setFocus()

        read_only(parent.bg, parent.ui.editHeadType, parent.ui.editHeadName)
        parent.ui.labelHeadName.setText('Head Name')
    else:
        # set parent widget value for edit head windows
        parent.ui.comboHeadType.setCurrentText(head_type)
        parent.ui.buttonOk.setEnabled(False)

    # set parent widget values for the both edit & delete account windows
    parent.ui.editHeadName.setText(head_name)

    # set parent variables values
    parent.selected_head_id = head_id
    parent.selected_head_type = head_type
    parent.selected_head_name = head_name
