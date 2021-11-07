from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QMessageBox


def createConnection(parent):
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName("src/expenditure.sqlite3")
    if not conn.open():
        QMessageBox.warning(None, "Database Error",
                            f"Unable to connect to the database\n\n{conn.lastError().text()}")
        return False
    parent.conn = conn
    createTables()
    return True


def createTables():
    query = QSqlQuery()

    # create table 'user'
    query.exec("""
            CREATE TABLE IF NOT EXISTS user(
            UserId      INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Username    TEXT NOT NULL UNIQUE,
            Password    TEXT NOT NULL);
        """)

    query.finish()

    # create table 'account'
    query.exec("""
                CREATE TABLE IF NOT EXISTS account(
                AccountId        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                AccountNumber    TEXT NOT NULL UNIQUE,
                CustomerName     TEXT NOT NULL,
                BankName         TEXT NOT NULL,
                BranchName       TEXT NOT NULL);
            """)

    query.finish()

    # create table 'head'
    query.exec("""
                CREATE TABLE IF NOT EXISTS head(
                HeadId      INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                HeadName    TEXT NOT NULL);
            """)

    query.finish()

    # create table 'trans' (short name of transaction)
    query.exec("""
                   CREATE TABLE IF NOT EXISTS trans(
                   TransId        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                   TransType      TEXT NOT NULL,
                   TransDate      TEXT NOT NULL,
                   ExpHead        INTEGER NOT NULL,
                   TransDetails   TEXT,
                   TransMode      TEXT NOT NULL,
                   BankAccount    INTEGER NOT NULL,
                   TransAmount    INTEGER NOT NULL,
                   FOREIGN KEY(ExpHead) REFERENCES head(HeadId),
                   FOREIGN KEY(BankAccount) REFERENCES account(AccountId));
               """)

    query.finish()

