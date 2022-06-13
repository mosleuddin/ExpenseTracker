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

from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlQuery


# owner table
def ownerExists():
    """
    The function checks whether owner exists or not in owner table
    """
    result = 0
    query = QSqlQuery()
    query.exec("SELECT COUNT(OwnerName) FROM owner")
    while query.next():
        result = query.value(0)
    query.finish()
    return result


def getOwner():
    """
    The function collect owner name and owner address from the owner table
    """
    query = QSqlQuery()
    query.exec("SELECT OwnerName, OwnerAddress FROM owner")

    while query.next():
        name = query.value(0)
        address = query.value(1)
        query.finish()
        return name, address


def insertOwner(owner_name, owner_address):
    """
    The function simply insert a new record in the owner table using the parameters value
    """
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
    """
    The function update an existing owner using the parameters value
    """

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
    """
     The function checks whether period exists or not in period table
    """

    result = 0
    query = QSqlQuery()
    query.exec("SELECT COUNT(ExpMonth) FROM period")
    while query.next():
        result = query.value(0)
    query.finish()
    return result


def getPeriod():
    """
     The function collect month and year from the period table
    """
    query = QSqlQuery()
    query.exec("SELECT ExpMonth, ExpYear FROM period")

    while query.next():
        month = query.value(0)
        year = query.value(1)
        query.finish()
        return month, year


def insertPeriod():
    """
     The function insert current month and current year in period table
    """
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
    """
    The function update month and year in period table using parameter values
    """
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
    """
    The function increase existing period by 1 month
    """
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


# validate period
def validPeriod(month_arg=None, year_arg=None):
    """
    The function ensure that a valid month name is entered.

    It also allows a user to enter a year between 2021 to 2100
    """

    obj = ''
    title = ''
    msg = ''

    months = ("January", "February", "March",
              "April", "May", "June",
              "July", "August", "September",
              "October", "November", "December"
              )

    years = [str(x) for x in range(2021, 2101)]

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
