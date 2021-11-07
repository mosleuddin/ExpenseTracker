from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox

from design.ui_head_view import Ui_ViewHead
from modules.module import resizeMove, valid_char, valid_space, is_unique
from design.ui_head import Ui_HeadWindow
from db.table_head import (insertHead, updateHead, removeHead, getHeadId, setHeadId,
                           populateComboHead, populateEditHeadName)


class Head(QDialog):
    def __init__(self, parent=None, task=None):
        super(Head, self).__init__(parent)
        self.parent = parent
        self.task = task
        self.old_head_name_value = ''
        self.ui = Ui_HeadWindow()
        self.ui.setupUi(self)
        self.configUI()

    def configUI(self):
        self.hideWidgets()
        self.ui.labelMessage.hide()
        populateComboHead(self)

        self.setWindowTitle('Expense Tracker')
        self.ui.editHeadName.addAction(QIcon('src/icons/common.png'), QLineEdit.ActionPosition.LeadingPosition)
        resizeMove(self, self.parent, .4, .6)

    def showWidgets(self):
        self.ui.labelHeadId.show()
        self.ui.labelDispalyId.show()
        self.ui.labelHeadName.show()
        self.ui.editHeadName.show()
        self.ui.editHeadName.setFocus()
        self.ui.editHeadName.end(False)
        self.ui.buttonOk.show()
        self.ui.buttonCancel.show()

        if self.task == 'delete':
            self.ui.buttonOk.setEnabled(True)
        else:
            self.ui.buttonOk.setEnabled(False)

    def hideWidgets(self):
        self.ui.labelHeadId.hide()
        self.ui.labelDispalyId.hide()
        self.ui.labelHeadName.hide()
        self.ui.editHeadName.hide()
        self.ui.buttonOk.hide()
        self.ui.buttonCancel.hide()

    def onIndexChanged(self, index):
        if index != -1:

            self.ui.labelMessage.hide()
            self.showWidgets()
            head_name = self.ui.comboHead.currentText()
            populateEditHeadName(self, head_name)
            self.old_head_name_value = self.ui.editHeadName.text().upper()

    def onTextEdited(self, text):
        if len(text) >= 4 and text.upper() != self.old_head_name_value:
            self.ui.buttonOk.setEnabled(True)
        else:
            self.ui.buttonOk.setEnabled(False)
        self.ui.labelMessage.hide()

    def onDiscardPressed(self):
        self.hideWidgets()
        self.ui.comboHead.setCurrentIndex(-1)

    def onOkPressed(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()


class AddHead(Head):
    def __init__(self, parent=None, task=None):
        super(AddHead, self).__init__(parent, task)
        self.parent = parent
        self.setStyleSheet('background-color: LightBlue')
        self.showWidgets()
        self.ui.comboHead.hide()
        self.ui.buttonCancel.hide()
        getHeadId(self)

        # configure widgets
        self.ui.labelHeading.setText('Add New Head')
        self.ui.buttonOk.setText('&Add')
        self.ui.buttonOk.setIcon(QIcon('src/icons/add.png'))

    def onOkPressed(self):
        head_id = int(self.ui.labelDispalyId.text())
        head_name = self.ui.editHeadName.text().strip().upper()

        chars = [' ', '-']

        if not valid_char(head_name, chars):
            title = 'Invalid character(s) entered'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            title = 'Invalid space(s) entered'
            msg = 'Only single space between to characters is allowed'

        else:
            result = is_unique('head', 'HeadName', 'HeadId', 'HeadId', head_name)
            if result[0]:
                # if first element of result tuple is TRUE
                insertHead(self, head_name)

                msg = f'{head_name} added successfully'
                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()

                self.ui.labelDispalyId.setText(str(head_id + 1))
                self.ui.editHeadName.setText('')
                self.ui.editHeadName.setFocus()
                self.ui.buttonOk.setEnabled(False)
                return
            else:
                title = 'Duplicate head name'
                msg = f'{head_name} exists against head ID:  {result[1]}'

        QMessageBox.warning(self, title, msg)
        self.ui.editHeadName.setFocus()
        self.ui.editHeadName.end(False)
        return


class EditHead(Head):
    def __init__(self, parent=None, task=None):
        super(EditHead, self).__init__(parent, task)
        self.parent = parent
        self.setStyleSheet('background-color: LightYellow')

        # configure widgets
        self.ui.labelHeading.setText('Edit Head')
        self.ui.buttonOk.setText('&Edit')
        self.ui.buttonOk.setIcon(QIcon('src/icons/edit.png'))

    def onOkPressed(self):
        head_id = int(self.ui.labelDispalyId.text())
        head_name = self.ui.editHeadName.text().strip().upper()

        chars = [' ', '-']

        if not valid_char(head_name, chars):
            title = 'Invalid character(s) entered'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(head_name):
            title = 'Invalid space(s) entered'
            msg = 'Only single space between to characters is allowed'

        else:
            result = is_unique('head', 'HeadName', 'HeadId', 'HeadId', head_name, head_id)

            if result[0]:
                # if first element of result tuple is TRUE i.e. same head not exist
                updateHead(self, head_id, head_name)

                msg = f'Head name successfully updated to {head_name}\n\n'
                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()

                self.ui.comboHead.clear()
                populateComboHead(self)
                self.hideWidgets()
                return
            else:
                title = 'Duplicate Head Name'
                msg = f'{head_name} exists against head ID:  {result[1]}'

        QMessageBox.warning(self, title, msg)
        self.ui.editHeadName.setFocus()
        self.ui.editHeadName.end(False)
        return


class DeleteHead(Head):
    def __init__(self, parent=None, task=None):
        super(DeleteHead, self).__init__(parent, task)
        self.parent = parent
        self.bg = 'background-color: LightGreen'
        self.setStyleSheet(self.bg)

        # configure widgets
        self.ui.labelHeading.setText('Delete Head')
        self.ui.buttonOk.setText('&Delete')
        self.ui.buttonOk.setIcon(QIcon('src/icons/delete.png'))

        self.ui.editHeadName.setReadOnly(True)
        self.ui.editHeadName.setStyleSheet(self.bg)

    def onOkPressed(self):
        head_id = int(self.ui.labelDispalyId.text())
        head_name = self.ui.editHeadName.text().strip().upper()
        title = 'Delete Head'
        msg = f'Do you want to delete the head {head_name}?'

        answer = QMessageBox.question(self, title, msg)
        if answer == QMessageBox.Yes:
            removeHead(self, head_id)

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
        resizeMove(self, self.parent, .7, .9)

        # create query
        query = QSqlQuery()
        query.exec("SELECT HeadName FROM head ORDER BY HeadName")

        # create model and load data
        model = QSqlQueryModel()
        model.setQuery(query)
        model.setHeaderData(0, Qt.Horizontal, "Name")
        self.ui.tableView.setModel(model)
