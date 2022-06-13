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

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QTableView, QLabel

from modules.module import MsgBox, resize_and_move, valid_char, valid_space
from design.ui_head import Ui_HeadWindow
from design.ui_head_view import Ui_ViewHead
from db.table_head import (insertHead, updateHead, removeHead,
                           populateComboHead, populateWidgets, head_related_transaction_exists)


class Head(QDialog):
    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color :#10141b;'

        self.selected_head_id = None
        self.selected_head_type = None
        self.selected_head_name = None

        self.ui = Ui_HeadWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        self.setWindowTitle('Expense Tracker')
        resize_and_move(self, self.parent, .6, .6)
        self.hideWidgets()
        self.ui.labelMessage.hide()

        # configure comboHeadType
        for item in self.parent.trans_types_list:
            self.ui.comboHeadType.addItem(item)

    def showWidgets(self):
        self.ui.labelHeadType2.show()
        self.ui.labelHeadName.show()

        self.ui.comboHeadType.show()
        self.ui.editHeadName.show()

        self.ui.buttonOk.show()
        self.ui.buttonCancel.show()

        self.ui.comboHeadType.setFocus()

    def hideWidgets(self):

        self.ui.labelHeadType1.hide()
        self.ui.labelHeadType2.hide()
        self.ui.labelHeadName.hide()

        self.ui.editHeadType.hide()
        self.ui.comboHeadType.hide()
        self.ui.editHeadName.hide()

        self.ui.buttonOk.hide()
        self.ui.buttonCancel.hide()

    def onHeadChanged(self, index):
        pass

    def onHeadTypeChanged(self, index):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)
        self.ui.editHeadName.setFocus()

    def onTextEdited(self, text):
        self.ui.labelMessage.hide()
        self.ui.buttonOk.setEnabled(True)

    def onDiscardPressed(self):
        self.hideWidgets()
        self.ui.comboHead.show()
        self.ui.comboHead.setCurrentIndex(-1)

    def onOkPressed(self):
        pass

    def headNameExists(self, head_name, task):
        query = QSqlQuery()
        if task == 'add':
            query.exec("SELECT HeadName FROM head")
        else:
            query.exec(f"""SELECT HeadName FROM head
                           WHERE HeadId != {self.selected_head_id}""")
        while query.next():
            if query.value(0).lower() == head_name.lower():
                return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()


class AddHead(Head):
    def __init__(self, parent=None):
        super(AddHead, self).__init__(parent)
        self.parent = parent

        # hide/show widgets
        self.ui.comboHead.hide()
        self.showWidgets()
        self.ui.buttonCancel.hide()

        # Change value of some widgets
        self.ui.labelHeading.setText('Add New Head')
        self.ui.comboHeadType.setCurrentIndex(-1)
        self.ui.comboHeadType.setFocus()
        self.ui.buttonOk.setText('&ADD')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))

    def onOkPressed(self):
        head_type = self.ui.comboHeadType.currentText()
        head_name = self.ui.editHeadName.text().strip().upper()
        obj = None
        chars = [' ', '-']

        if self.ui.comboHeadType.currentIndex() < 0:
            obj = self.ui.comboHeadType
            title = 'Head type is a required field'
            msg = 'Please select head type'

        elif len(head_name) < 3:
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Minimum 3 characters required'

        elif not valid_char(head_name, chars):
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Only single space between to characters is allowed'

        elif self.headNameExists(head_name, 'add'):
            obj = self.ui.editHeadName
            title = 'Duplicate Head'
            msg = f'            {head_name} exists!!!'

        elif 'contra' in (head_name.lower()):
            obj = self.ui.editHeadName
            title = 'The word "Contra" is reserved'
            msg = 'It can not be used for user defined Head Name'
        else:
            insertHead(self, head_type, head_name)
            msg = f'{head_name} added successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

            self.ui.comboHeadType.setCurrentIndex(-1)
            self.ui.editHeadName.setText('')
            self.ui.comboHead.setFocus()
            self.ui.buttonOk.setEnabled(False)
            return
        MsgBox(title, msg, '&Got it').warn()
        self.ui.buttonOk.setEnabled(False)
        obj.setFocus()
        if obj != self.ui.comboHeadType:
            obj.end(False)
        return


class EditHead(Head):
    def __init__(self, parent=None):
        super(EditHead, self).__init__(parent)
        self.parent = parent
        populateComboHead(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Edit Head')
        self.ui.buttonOk.setText('&EDIT')
        self.ui.buttonOk.setIcon(QIcon('src/icons/edit.png'))

    def onOkPressed(self):
        head_type = self.ui.comboHeadType.currentText()
        head_name = self.ui.editHeadName.text().strip().upper()
        obj = None
        chars = [' ', '-']

        if head_type == self.selected_head_type and head_name == self.selected_head_name:
            obj = self.ui.comboHeadType
            title = 'Head Details'
            msg = 'Nothing to update !!!'

        elif self.ui.comboHeadType.currentIndex() < 0:
            obj = self.ui.comboHeadType
            title = 'Head type is a required field'
            msg = 'Please select head type'

        elif len(head_name) < 3:
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Minimum 3 characters required'

        elif not valid_char(head_name, chars):
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            obj = self.ui.editHeadName
            title = 'Invalid Head'
            msg = 'Only single space between to characters is allowed'
        else:
            if self.headNameExists(head_name, 'edit'):
                title = 'Duplicate Head'
                msg = f'         {head_name} exists!!!'

            else:
                updateHead(self, self.selected_head_id, head_type, head_name)

                msg = f'Head name successfully updated to {head_name}'

                self.hideWidgets()
                self.ui.labelHeading.hide()

                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()
                return

        MsgBox(title, msg, '&Got it').warn()
        self.ui.buttonOk.setEnabled(False)
        obj.setFocus()
        if obj != self.ui.comboHeadType:
            obj.end(False)
        return

    def onHeadChanged(self, index):
        head_name = self.ui.comboHead.currentText()
        self.ui.labelMessage.hide()
        self.ui.comboHead.hide()

        self.showWidgets()
        populateWidgets(self, head_name, 'edit')


class DeleteHead(Head):
    def __init__(self, parent=None):
        super(DeleteHead, self).__init__(parent)
        self.parent = parent
        populateComboHead(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Delete Head')
        self.ui.buttonOk.setText('&DELETE')
        self.ui.buttonOk.setIcon(QIcon('src/icons/delete.png'))

    def onOkPressed(self):
        head_name = self.ui.editHeadName.text().strip().upper()

        if head_related_transaction_exists(head_name):
            MsgBox(f"{head_name} has related transaction",
                   f"To remove the head, all the related records in the "
                   f"transaction table must be deleted first").warn()
        else:
            title = 'Confirm Delete'
            msg = f'Delete head "{head_name}"?'

            if MsgBox(title, msg, '&Delete', '&Cancel').confirm():
                removeHead(self, head_name)
                msg = f'{head_name} deleted successfully'
                populateComboHead(self)
                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()

        self.hideWidgets()
        self.ui.comboHead.show()
        self.ui.comboHead.setCurrentIndex(-1)

    def onHeadChanged(self, index):
        head_name = self.ui.comboHead.currentText()
        self.ui.labelMessage.hide()
        self.ui.comboHead.hide()

        self.showWidgets()
        populateWidgets(self, head_name, 'delete')


class ViewHead(QDialog):
    def __init__(self, parent):
        super(ViewHead, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ViewHead()
        self.ui.setupUi(self)
        resize_and_move(self, self.parent, .5, .8)
        self.show()

        # create widgets
        self.text_label = QLabel(self)
        self.text_label.setText("<h2>No head available</h2>")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("background-color: rgb(225, 225, 225); color: rgb(0, 0, 255)")
        self.text_label.setGeometry(int(self.width() / 3), int(self.height() / 3),
                                    int(self.width() / 3), int(self.height() / 3))
        self.text_label.hide()

        # create query
        self.query = QSqlQuery()
        self.query.exec("SELECT HeadName, HeadType FROM head ORDER BY HeadType DESC, HeadName")

        # create model and set query
        self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.model.setHeaderData(0, Qt.Horizontal, "Head Name")
        self.model.setHeaderData(1, Qt.Horizontal, "Head Type")

        # set model to table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0, 350)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)

        if self.model.rowCount() == 0:
            self.text_label.show()
        else:
            self.text_label.hide()

    def closeEvent(self, event):
        self.query.finish()
        self.model.clear()
        event.accept()
