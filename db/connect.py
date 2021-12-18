from PySide6.QtSql import QSqlQuery, QSqlDatabase
from modules.module import CustomMessage

def createConnection(parent):
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName("src/expenditure.sqlite3")
    if not conn.open():
        title = "Database Error"
        msg = f"Unable to connect to the database\n\n{conn.lastError().text().upper()}"
        button_0 = '&Close'
        CustomMessage().danger(title=title, msg=msg, button_0= button_0)
        return False
    parent.conn = conn
    createTables()
    return True


def createTables():
    query = QSqlQuery()

    # create table 'user'
    query.exec("""
            CREATE TABLE IF NOT EXISTS user(
            UserId      INTEGER PRIMARY KEY AUTOINCREMENT,
            Username    TEXT NOT NULL UNIQUE,
            Password    TEXT NOT NULL);
        """)

    query.finish()

    # create table 'account'
    query.exec("""
                CREATE TABLE IF NOT EXISTS account(
                AccountId        INTEGER PRIMARY KEY AUTOINCREMENT,
                AccountNumber    TEXT NOT NULL UNIQUE,
                CustomerName     TEXT NOT NULL,
                BankName         TEXT NOT NULL,
                BranchName       TEXT NOT NULL);
            """)

    query.finish()

    # create table 'head'
    query.exec("""
                CREATE TABLE IF NOT EXISTS head(
                HeadId      INTEGER PRIMARY KEY AUTOINCREMENT,
                HeadType    TEXT NOT NULL,
                HeadName    TEXT NOT NULL);
            """)

    query.finish()

    # create table 'trans' (short name of transaction)
    query.exec("""
                   CREATE TABLE IF NOT EXISTS trans(
                   TransId        INTEGER PRIMARY KEY AUTOINCREMENT,
                   TransType      TEXT NOT NULL,
                   TransDate      TEXT NOT NULL,
                   HeadId         INTEGER NOT NULL REFERENCES head(HeadId),
                   TransDetails   TEXT,
                   TransMode      TEXT NOT NULL,
                   AccountId      INTEGER NOT NULL REFERENCES account(AccountId),
                   TransAmount    INTEGER NOT NULL);
               """)

    query.finish()
