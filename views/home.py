from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QMainWindow, QInputDialog

from design.ui_home import Ui_HomeWindow
from db.table_user import viewUser, resetUserCredentials
from modules.module import CustomMessage, resize_and_move

from views.credentials import ShowUsers, ChangeUsername, ChangePassword
from views.about import About
from views.head import AddHead, EditHead, DeleteHead, ViewHead
from views.account import AddAccount, EditAccount, DeleteAccount, ViewAccount


class Home(QMainWindow):
    def __init__(self, conn=None, user_id=None, user_name=None):
        super().__init__()
        self.conn = conn
        self.user_id = user_id
        self.user_name = user_name

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        # self.setWindowState(Qt.WindowFullScreen)
        resize_and_move(self, wd=.9, ht=.8)
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
        title = 'Confirm Exit'
        msg = '<h4 color: rgb(255, 0, 0);>Are you sure you want to exit?</h4>'

        if CustomMessage().confirm(title, msg, 'E&xit',  '&Cancel'):
            self.conn.close()
            self.conn.setDatabaseName("")
            QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())
            event.accept()
            print('is database open while closing mainwindow? ', self.conn.isOpen())
        else:
            event.ignore()

    # function for button Bank Balance
    def bank_balance_details(self):
        CustomMessage().info('Bank Balance', 'This function is not completed', '&Ok' )

    # functions for File Menu
    def print_transactions(self):
        print('print_transactions')

    def about(self):
        dlg = About(self)

    # functions for Account Menu
    def add_account(self):
        dlg = AddAccount(self)

    def edit_account(self):
        dlg = EditAccount(self)

    def delete_account(self):
        dlg = DeleteAccount(self)

    def view_account(self):
        dlg = ViewAccount(self)

    # functions for Head Menu
    def add_head(self):
        dlg = AddHead(self)

    def edit_head(self):
        dlg = EditHead(self)

    def delete_head(self):
        dlg = DeleteHead(self)

    def view_head(self):
        dlg = ViewHead(self)

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

    def reset_user_credentials(self):
        users = viewUser(self)
        user_name, ok = QInputDialog.getItem(self, 'Select user', 'Username', users, 1, False)
        if ok:
            resetUserCredentials(self, user_name)

    def change_password(self):
        dlg = ChangePassword(self, self.user_id)

    def change_username(self):
        dlg = ChangeUsername(self, self.user_id, self.user_name)

    # function for initialization
    def initialize_data(self):
        print('initialize_data')
