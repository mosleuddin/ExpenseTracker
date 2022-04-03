from PySide6.QtSql import QSqlQuery, QSqlDatabase

from db.table_account import cashAccountExists, insertAccount
from db.table_balance import insertOpeningBalance
from db.table_basic_details import ownerExists, periodExists, insertOwner, insertPeriod
from db.table_head import headExists, insertHead
from db.table_user import userExists, createUser
from modules.module import CustomMessage


def createConnection(parent):
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName("src/expenditure.sqlite3")
    if not conn.open():
        title = "Database Error"
        msg = f"Unable to connect to the database\n\n{conn.lastError().text().upper()}"
        button_0 = '&Close'
        CustomMessage().danger(title=title, msg=msg, button_0=button_0)
        return False
    conn.exec("PRAGMA foreign_keys = ON;")
    parent.conn = conn
    createTables()
    appendData()
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

    # create table 'owner'
    query.exec("""
                  CREATE TABLE IF NOT EXISTS owner(
                  Id             INTEGER PRIMARY KEY CHECK(id = 1),
                  OwnerName      TEXT NOT NULL,
                  OwnerAddress   TEXT NOT NULL);  
                   
              """)

    query.finish()

    # create table 'period'
    query.exec("""
                     CREATE TABLE IF NOT EXISTS period(
                     Id             INTEGER PRIMARY KEY CHECK(id = 1),
                     ExpMonth       TEXT NOT NULL,
                     ExpYear        TEXT NOT NULL);  
                      
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

    # create table 'balance'
    query.exec("""
                   CREATE TABLE IF NOT EXISTS balance(
                   BalanceId        INTEGER PRIMARY KEY AUTOINCREMENT,
                   OpeningBalance   INTEGER DEFAULT 0,
                   TotalReceipt     INTEGER DEFAULT 0,
                   TotalPayment     INTEGER DEFAULT 0,
                   AccountNumber    TEXT NOT NULL UNIQUE REFERENCES account(AccountNumber) ON DELETE CASCADE)
            """)

    query.finish()

    # create table 'head'
    query.exec("""
                CREATE TABLE IF NOT EXISTS head(
                HeadId      INTEGER PRIMARY KEY AUTOINCREMENT,
                HeadType    TEXT NOT NULL,
                HeadName    TEXT NOT NULL UNIQUE);
            """)

    query.finish()

    # create table 'trans' (short name of transaction)
    query.exec("""
                   CREATE TABLE IF NOT EXISTS trans(
                   TransId        INTEGER PRIMARY KEY AUTOINCREMENT,
                   TransDate      TEXT NOT NULL,
                   HeadId         INTEGER NOT NULL REFERENCES head(HeadId),
                   TransDetails   TEXT,
                   AccountId      INTEGER NOT NULL REFERENCES account(AccountId),
                   TransAmount    INTEGER NOT NULL);
               """)

    query.finish()


def appendData():
    # appended default data to various tables
    if not userExists(None):
        createUser(None)

    if not ownerExists():
        insertOwner("", "")

    if not periodExists():
        insertPeriod()

    if not cashAccountExists(None):
        insertAccount(None, account_number="Cash", customer_name="Cash",
                      bank_name="Cash", branch_name="Cash")

        insertOpeningBalance(None, account_number="Cash", opening_balance=0)

    if not headExists(None):
        insertHead(None, head_type="Receipt", head_name="ContraReceipt")
        insertHead(None, head_type="Payment", head_name="ContraPayment")

