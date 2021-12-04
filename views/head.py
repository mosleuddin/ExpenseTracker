from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox, QTableView, QLabel

from modules.module import resize_and_move, valid_char, valid_space
from design.ui_head import Ui_HeadWindow
from design.ui_head_view import Ui_ViewHead
from db.table_head import (insertHead, updateHead, removeHead,
                           populateComboHead, populateWidgets)


class Head(QDialog):
    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.parent = parent

        self.selected_head_id = None
        self.selected_head_name = None

        self.ui = Ui_HeadWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        self.setWindowTitle('Expense Tracker')
        resize_and_move(self, self.parent, .4, .6)
        self.hideWidgets()
        self.ui.labelMessage.hide()

        self.ui.comboHeadType.addItems(['Payment', 'Receipt', 'Contra Entry'])
        self.ui.editHeadName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)

    def showWidgets(self):
        self.ui.labelHeadType.show()
        self.ui.labelHeadName.show()

        self.ui.comboHeadType.show()
        self.ui.editHeadName.show()

        self.ui.buttonOk.show()
        self.ui.buttonCancel.show()

        self.ui.comboHeadType.setFocus()

    def hideWidgets(self):
        self.ui.labelHeadType.hide()
        self.ui.labelHeadName.hide()

        self.ui.comboHeadType.hide()
        self.ui.editHeadName.hide()

        self.ui.buttonOk.hide()
        self.ui.buttonCancel.hide()

    def onHeadChanged(self, index):
        if index != -1:
            self.ui.labelMessage.hide()
            self.ui.comboHead.hide()
            self.showWidgets()

            head_name = self.ui.comboHead.currentText()
            populateWidgets(self, head_name)

    def onHeadTypeChanged(self, index):
        if index != -1:
            self.ui.editHeadName.setFocus()

    def onTextEdited(self, text):
        if len(text) >= 3 and text.upper() != self.selected_head_name:
            self.ui.buttonOk.setEnabled(True)
        else:
            self.ui.buttonOk.setEnabled(False)
        self.ui.labelMessage.hide()

    def onDiscardPressed(self):
        self.hideWidgets()
        self.ui.comboHead.show()
        self.ui.comboHead.setCurrentIndex(-1)

    def onOkPressed(self):
        pass

    def headExists(self, head_name, task):
        query = QSqlQuery()
        if task == 'add':
            query.exec("SELECT HeadName FROM head")
        else:
            query.exec(f"""SELECT HeadName FROM head
                           WHERE HeadId != {self.selected_head_id}""")
        while query.next():
            if query.value(0) == head_name:
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
        self.setStyleSheet('background-color: LightBlue')

        # hide/show widgets
        self.ui.comboHead.hide()
        self.showWidgets()
        self.ui.buttonCancel.hide()

        # Change value of some widgets
        self.ui.labelHeading.setText('Add New Head')
        self.ui.buttonOk.setText('&Add')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))
        self.ui.comboHeadType.setCurrentIndex(-1)

    def onOkPressed(self):
        head_type = self.ui.comboHeadType.currentText()
        head_name = self.ui.editHeadName.text().strip().upper()
        chars = [' ', '-']

        if self.ui.comboHeadType.currentIndex() < 0:
            title = 'Head type is required'
            msg = 'Please select head type'

        elif not valid_char(head_name, chars):
            title = 'Invalid character(s) entered'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            title = 'Invalid space(s) entered'
            msg = 'Only single space between to characters is allowed'

        elif self.headExists(head_name, 'add'):
            title = 'Duplicate Head Name'
            msg = f'{head_name} exists!!!'
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

        QMessageBox.warning(self, title, msg)
        self.ui.editHeadName.setFocus()
        self.ui.editHeadName.end(False)
        self.ui.buttonOk.setEnabled(False)
        return


class EditHead(Head):
    def __init__(self, parent=None):
        super(EditHead, self).__init__(parent)
        self.parent = parent
        self.setStyleSheet('background-color: LightYellow')
        populateComboHead(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Edit Head')
        self.ui.buttonOk.setText('&Edit')
        self.ui.buttonOk.setIcon(QIcon('src/icons/edit.png'))

    def onOkPressed(self):
        head_type = self.ui.comboHeadType.currentText()
        head_name = self.ui.editHeadName.text().strip().upper()
        chars = [' ', '-']

        if self.ui.comboHeadType.currentIndex() < 0:
            title = 'Head type is required'
            msg = 'Please select head type'

        if not valid_char(head_name, chars):
            title = 'Invalid character(s) entered'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            title = 'Invalid space(s) entered'
            msg = 'Only single space between to characters is allowed'

        else:
            if self.headExists(head_name, 'edit'):
                title = 'Duplicate Head Name'
                msg = f'{head_name} exists!!!'

            else:
                updateHead(self, self.selected_head_id, head_type, head_name)

                msg = f'Head name successfully updated to {head_name}\n\n'
                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()

                self.ui.comboHead.clear()
                populateComboHead(self)
                self.hideWidgets()
                return

        QMessageBox.warning(self, title, msg)
        self.ui.editHeadName.setFocus()
        self.ui.editHeadName.end(False)
        return


class DeleteHead(Head):
    def __init__(self, parent=None):
        super(DeleteHead, self).__init__(parent)
        self.parent = parent
        self.bg = 'background-color: LightGreen'
        self.setStyleSheet(self.bg)
        populateComboHead(self)

        # Change value of some widgets
        self.ui.labelHeading.setText('Delete Head')
        self.ui.buttonOk.setText('&Delete')
        self.ui.buttonOk.setIcon(QIcon('src/icons/delete.png'))

        self.ui.comboHeadType.setEnabled(False)
        self.ui.editHeadName.setReadOnly(True)
        self.ui.editHeadName.setStyleSheet(self.bg)
        self.ui.buttonOk.setEnabled(True)

    def onOkPressed(self):
        head_name = self.ui.editHeadName.text().strip().upper()
        title = 'Delete Head'
        msg = f'Delete head "{head_name}"?'

        answer = QMessageBox.question(self, title, msg)
        if answer == QMessageBox.Yes:
            removeHead(self, head_name)

            msg = f'{head_name} deleted successfully'
            self.ui.labelMessage.setText(msg)
            self.ui.labelMessage.show()

            self.ui.comboHead.clear()
            populateComboHead(self)
            self.hideWidgets()


class ViewHead(QDialog):
    def __init__(self, parent):
        super(ViewHead, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ViewHead()
        self.ui.setupUi(self)
        resize_and_move(self, self.parent, .7, .9)
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
        self.ui.tableView.setColumnWidth(0, 500)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)

        if self.model.rowCount() == 0:
            self.text_label.show()
        else:
            self.text_label.hide()

    def closeEvent(self, event):
        self.query.finish()
        self.model.clear()
        event.accept()
