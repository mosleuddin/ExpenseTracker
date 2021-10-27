from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QMainWindow, QInputDialog, QMessageBox

from design.ui_home import Ui_HomeWindow
from db.table_user import viewUser, resetUserCredentials

from views.credentials import ShowUsers, ChangeUsername, ChangePassword
from views.about import About
from views.head import AddHead, EditHead, DeleteHead, ViewHead


class Home(QMainWindow):
    def __init__(self, conn=None, user_id=None, user_name=None):
        super().__init__()
        self.conn = conn
        self.user_id = user_id
        self.user_name = user_name

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowFullScreen)
        self.show()

        # The below portion will be changed in future

        query = QSqlQuery()
        query.exec("SELECT HeadName FROM head ORDER BY HeadName")

        model = QSqlQueryModel()
        model.setQuery(query)
        model.setHeaderData(0, Qt.Horizontal, "Name")
        self.ui.tableView.setModel(model)

        # The above portion  will be changed in future

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        confirm = QMessageBox.question(self, "Confirm Exit ", f"Are you sure you want to exit?")
        if confirm == QMessageBox.Yes:
            self.conn.close()
            self.conn.setDatabaseName("")
            QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
            event.accept()
            print('is database open while closing mainwindow? ', self.conn.isOpen())
        else:
            event.ignore()

    # function for button Bank Balance
    def bank_balance_details(self):
        print('Bank balance details')

    # functions for File Menu
    def print_transactions(self):
        print('print_transactions')

    def about(self):
        dlg = About(self)
        dlg.show()

    # functions for Account Menu
    def add_account(self):
        print('add_account')

    def edit_account(self):
        print('edit_account')

    def view_account(self):
        print('view_account')

    def delete_account(self):
        print('delete_account')

    # functions for Head Menu
    def add_head(self):
        dlg = AddHead(parent=self, task='add')
        dlg.show()

    def edit_head(self):
        dlg = EditHead(parent=self, task='edit')
        dlg.show()

    def view_head(self):
        dlg = ViewHead(parent=self)
        dlg.show()

    def delete_head(self):
        dlg = DeleteHead(parent=self, task='delete')
        dlg.show()

    # functions for Transaction Menu
    def add_transaction(self):
        print('add_transaction')

    def edit_transaction(self):
        print('edit_transaction')

    def view_transaction(self):
        print('view_transaction')

    def delete_transaction(self):
        print('delete_transaction')

    # function for users
    def show_all_users(self):
        dlg = ShowUsers(self)
        dlg.show()

    def reset_user_credentials(self):
        users = viewUser(self)
        user_name, ok = QInputDialog.getItem(self, 'Select user', 'Username', users, 1, False)
        if ok:
            resetUserCredentials(self, user_name)

    def change_password(self):
        dlg = ChangePassword(self, self.user_id)
        dlg.show()

    def change_username(self):
        dlg = ChangeUsername(self, self.user_id, self.user_name)
        dlg.show()

    # function for initialization
    def initialize_data(self):
        print('initialize_data')


