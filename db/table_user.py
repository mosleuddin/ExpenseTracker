import sqlite3

from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMessageBox
from modules.module import CustomMessage


def userExists(parent):
    users = 0
    try:
        query = QSqlQuery()
        query.exec("SELECT COUNT(Username) FROM user")
        while query.next():
            users = query.value(0)

        query.finish()

        return users

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not count users!!!")


def createUser(parent):
    users = ['admin', 'user']
    password = ['1234', '1234']
    for i in range(2):
        try:
            query = QSqlQuery()
            query.prepare(""" INSERT INTO user(Username, Password)
                              VALUES(:Username, :Password)
                         """)

            query.bindValue(":Username", users[i])
            query.bindValue(":Password", password[i])

            query.exec()
            query.finish()

        except sqlite3.Error:
            QMessageBox.critical(parent, "DataBase Error", "Could not create user!!!")
            break


def getPassword(parent, user_id):
    """
    This function retrieve the password of the received user_id.
    :param parent: The class object from where the function is called.
    :param user_id: The UserId of the record whose Password to be retrieved.
    :return: Value of the Password field corresponding to the UserId value.
    """
    try:
        pwd = ''
        query = QSqlQuery()
        query.prepare("""SELECT Password FROM user
                         WHERE  UserId = :UserId
                      """)
        query.bindValue(":UserId", user_id)
        query.exec()
        while query.next():
            pwd = query.value(0)
        query.finish()
        return pwd

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not get password!!!")


def viewUser(parent):
    """
    This function retrieve the userid and username of all the users of the application.
    :param parent: The class object from where the function is called.
    :return:Values of the userid, username  retrieved and another value depend on the
            values of username and password.

    """
    try:
        users = []
        query = QSqlQuery()
        query.prepare("SELECT UserId, Username, Password from user")
        query.exec()
        while query.next():
            status = 'customized'
            u_id = str(query.value(0))
            u_name = query.value(1)
            p_word = query.value(2)

            if u_name == 'admin':
                if p_word == '1234':
                    status = 'default'
            else:
                if u_name == 'user' or p_word == '1234':
                    status = 'default'

            record = (u_id, u_name, status, '')
            users.append(record)
        query.finish()
        return users

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not view users!!!")


def resetUserCredentials(parent, user_name):
    """
    This function reset username and password of the supplied user to default values.
    :param parent: The class object from where the function is called.
    :param user_name: Value of Username field supplied while calling the function.
    """
    default_username = 'user'  # default Username for user
    default_password_user = 1234  # default Password for user
    default_password_admin = 1234  # default Password for admin

    query = QSqlQuery()

    try:
        if user_name != 'admin':
            query.prepare(""" UPDATE user SET
                              Username = :Username,
                              Password = :Password
                              WHERE Username = :user_name
                         """)

            query.bindValue(":Username", default_username)
            query.bindValue(":Password", default_password_user)
            query.bindValue(":user_name", user_name)

            title = "User Credentials Changed as follows"
            msg = f"\n\n      Username:    {default_username}      Password:    {default_password_user}     \n\n"

        else:
            query.prepare(""" UPDATE user SET
                              Password = :Password
                              WHERE Username = :user_name
                          """)

            query.bindValue(":Password", default_password_admin)
            query.bindValue(":user_name", user_name)

            title = "Admin Password reset"
            msg = f"\n\n      Default Password:    {default_password_admin}     \n\n"

        query.exec()
        query.finish()
        QMessageBox.information(parent, title, msg)
        return True

    except sqlite3.Error:
        QMessageBox.critical(parent, "Database Error", "Could not reset Password")
        return False


def changePassword(parent, user_id, new_pwd):
    """
    This function changes password for the active user.
    :param parent: The class object from where the function is called.
    :param user_id: Value of the UserId field of the active user.
    :param new_pwd: New password of the active user will be set to this value.
    """
    try:
        query = QSqlQuery()
        query.prepare(""" UPDATE user SET Password = :Password
                          WHERE UserId = :UserId
                      """)

        query.bindValue(":UserId", user_id)
        query.bindValue(":Password", new_pwd)
        query.exec()
        query.finish()

        title = "Password changed successfully"
        msg = "\n\nPlease login again using new password."
        CustomMessage().warn(title, msg, '&Thanks')

    except sqlite3.Error:
        QMessageBox.critical(parent, "DataBase Error", "Could not change password!!!")


def changeUsername(parent, user_id, new_user_name):
    """
    This function changes Username of the active user.
    :param parent: The class object from where the function is called.
    :param user_id: Value of the UserId field of the active user.
    :param new_user_name: New username of the active user will be set to this value.
    :return:
    """
    if new_user_name != 'admin':
        try:
            query = QSqlQuery()
            query.prepare(""" UPDATE user SET Username = :Username
                              WHERE UserId = :UserId
                          """)

            query.bindValue(":UserId", user_id)
            query.bindValue(":Username", new_user_name)
            query.exec()
            query.finish()

            title = 'Username changed successfully. \n\nPlease login again using new username.'
            msg = f'\n\n New Username :   {new_user_name}    \n\n'
            CustomMessage().warn(title, msg, '&Thanks')

        except sqlite3.Error:
            QMessageBox.critical(parent, "DataBase Error", "Could not change username!!!")
    else:
        CustomMessage().warn("Username 'admin' is not available", "Please select a different username", "&Got it")


def checkCredentials(parent, user_name, user_pwd):
    """
    This function first check  whether user_name and user_pwd supplied by the user are correct
    as per the database. If both matches, it returns the corresponding UserId and Username as a list.

    :param parent:    The class object from where the function is called.
    :param user_name: Value supplied by the user for Username field.
    :param user_pwd:  Value supplied by the user for Password field.
    :return:          A list containing the values of UserId and UserName fields
                      if UserId and Password supplied by the user matches, else None.
    """
    try:
        query = QSqlQuery()
        query.prepare(""" SELECT UserId, Username from user
                          WHERE Username = :Username
                          AND Password = :Password
                     """)

        query.bindValue(":Username", user_name)
        query.bindValue(":Password", user_pwd)
        query.exec()

        record = []
        while query.next():
            u_id = query.value(0)
            u_name = query.value(1)
            record.append(u_id)
            record.append(u_name)

        query.finish()
        return record

    except sqlite3.Error:
        QMessageBox.critical(parent, "Login Failed", "DataBase Error!!!")
