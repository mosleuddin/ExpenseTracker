from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery


# owner table
def ownerExists():
    result = 0
    query = QSqlQuery()
    query.exec("SELECT COUNT(OwnerName) FROM owner")
    while query.next():
        result = query.value(0)
    query.finish()
    return result


def getOwner():
    query = QSqlQuery()
    query.exec("SELECT OwnerName, OwnerAddress FROM owner")

    while query.next():
        name = query.value(0)
        address = query.value(1)
        query.finish()
        return name, address


def insertOwner(owner_name, owner_address):
    owner = owner_name.strip().title()
    address = owner_address.strip().title()

    query = QSqlQuery()
    query.prepare(""" INSERT INTO owner(OwnerName, OwnerAddress)
                      VALUES(:OwnerName, :OwnerAddress)
                  """)

    query.bindValue(":OwnerName", owner)
    query.bindValue(":OwnerAddress", address)

    query.exec()
    query.finish()


def updateOwner(owner_name, owner_address):
    owner = owner_name.title()
    address = owner_address.title()

    query = QSqlQuery()
    query.prepare(""" UPDATE owner SET
                        OwnerName = :OwnerName,
                        OwnerAddress = :OwnerAddress
                 """)

    query.bindValue(":OwnerName", owner)
    query.bindValue(":OwnerAddress", address)

    query.exec()
    query.finish()


# period table
def periodExists():
    result = 0
    query = QSqlQuery()
    query.exec("SELECT COUNT(ExpMonth) FROM period")
    while query.next():
        result = query.value(0)
    query.finish()
    return result


def getPeriod():
    query = QSqlQuery()
    query.exec("SELECT ExpMonth, ExpYear FROM period")

    while query.next():
        month = query.value(0)
        year = query.value(1)
        query.finish()
        return month, year


def insertPeriod():
    month = QDate().currentDate().toString('MMMM')
    year = QDate().currentDate().toString('yyyy')

    query = QSqlQuery()
    query.prepare(""" INSERT INTO period(ExpMonth, ExpYear)
                      VALUES(:ExpMonth, :ExpYear)
                  """)

    query.bindValue(":ExpMonth", month)
    query.bindValue(":ExpYear", year)

    query.exec()
    query.finish()


def updatePeriod(month, year):
    query = QSqlQuery()
    query.prepare(""" UPDATE period SET
                       ExpMonth = :ExpMonth,
                       ExpYear = :ExpYear
                 """)

    query.bindValue(":ExpMonth", month)
    query.bindValue(":ExpYear", year)

    query.exec()
    query.finish()


def increasePeriod():
    month, year = getPeriod()

    date_string = f"01-{month}-{year}"
    active_period = QDate().fromString(date_string, "dd-MMMM-yyyy")

    # increase active_period by one month
    new_period = active_period.addMonths(1)

    new_month = new_period.toString("MMMM")
    new_year = new_period.toString("yyyy")

    query = QSqlQuery()
    query.prepare(""" UPDATE period SET
                          ExpMonth = :ExpMonth,
                          ExpYear = :ExpYear
                 """)

    query.bindValue(":ExpMonth", new_month)
    query.bindValue(":ExpYear", new_year)
    query.exec()
    query.finish()
    print(f"Period increased {new_month}  {new_year} ")


# validate period
def validPeriod(month_arg=None, year_arg=None):
    obj = ''
    title = ''
    msg = ''

    months = ("January", "February", "March",
              "April", "May", "June",
              "July", "August", "September",
              "October", "November", "December"
              )

    years = [str(x) for x in range(2021, 2100)]

    if month_arg is None or year_arg is None:
        month, year = getPeriod()
    else:
        month = month_arg
        year = year_arg

    if month not in months:
        obj = 'month'
        title = 'Invalid month'
        msg = 'Please enter valid month'

    elif year not in years:
        obj = 'year'
        title = 'Invalid year'
        msg = 'Please enter valid year'

    else:
        period = QDate().fromString(f"{year}{month}", "yyyyMMMM").toString("yyyyMM")
        current_period = QDate().currentDate().toString("yyyyMM")
        if period <= current_period:
            return True, obj, title, msg
        else:
            obj = 'month'
            title = 'Invalid period'
            msg = 'Period should not exceed current month and year'

    return False, obj, title, msg
