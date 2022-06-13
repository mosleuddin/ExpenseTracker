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

import os

from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLabel, QTableView

from db.table_balance import getOpeningBalanceGrandTotal, getAccountTotals
from design.ui_show_trans import Ui_ShowTransactions

from views.progress_bar import MidMonthProgressBar
from views.pdf_generator import PDF

from db.table_basic_details import getPeriod
from db.table_trans import transDateMismatch
from db.save_pdf_data import getAllTransactions, trans_data_exist, getHeadTotals

from modules.module import resize_and_move, MsgBox, showMismatchMessage


class ShowTransactionModel(QSqlQueryModel):
    def __init__(self, query=None):
        super(ShowTransactionModel, self).__init__()

        self.setQuery(query)

    def data(self, index, role):
        if index.isValid():
            col = index.column()
            row = index.row()

            if role == Qt.TextAlignmentRole:
                if col == 3:
                    return Qt.AlignRight
                if col == 4:
                    return Qt.AlignCenter
                else:
                    return Qt.AlignLeft

            if role == Qt.ForegroundRole:
                head = index.sibling(row, 1).data()
                if head == "ContraReceipt" or head == "ContraPayment":
                    return QColor("#DA2929")

        return QSqlQueryModel.data(self, index, role)


class ShowTransactions(QDialog):
    def __init__(self, parent=None):
        super(ShowTransactions, self).__init__(parent)
        self.parent = parent
        self.query = QSqlQuery()
        self.query_string = """SELECT TransDate, HeadName, TransDetails,
                               TransAmount, BankName, AccountNumber,
                               CustomerName, HeadType
                               FROM trans
                               JOIN head ON head.HeadId = trans.HeadId
                               JOIN account ON account.AccountId = trans.AccountId
                           """

        self.ui = Ui_ShowTransactions()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        resize_and_move(self, wd=.99, ht=.9)

        self.createLabel()
        self.loadRecords()
        self.populateComboHeadName()
        self.populateComboAccountNumber()
        self.populateComboTransDate()

    def createLabel(self):
        # create widgets
        self.text_label = QLabel(self)
        self.text_label.setText("<h2>No Transaction Exists</h2>")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setGeometry(int(self.width() / 3), int(self.height() / 3),
                                    int(self.width() / 2), int(self.height() / 4))
        self.text_label.hide()

    def populateComboHeadName(self, arg='all'):
        self.ui.comboHeadName.clear()

        query = QSqlQuery()
        if arg.lower() == "all":
            query.exec("""SELECT DISTINCT HeadName
                                  FROM trans
                                  JOIN head ON head.HeadId = trans.HeadId
                                  ORDER BY HeadName
                                """)
        else:
            query.prepare("""SELECT DISTINCT HeadName
                             FROM trans
                             JOIN head ON head.HeadId = trans.HeadId
                             WHERE head.HeadType = :HeadType
                             ORDER BY HeadName
                             """)

            query.bindValue(":HeadType", arg)
            query.exec()

        while query.next():
            item = query.value(0)
            self.ui.comboHeadName.addItem(item)

        query.finish()

        if self.ui.comboHeadName.count() > 0:
            self.ui.comboHeadName.insertItem(0, 'All')

    def populateComboAccountNumber(self, arg='all'):
        self.ui.comboAccountNumber.clear()

        query = QSqlQuery()
        if arg.lower() == "all":
            query.exec("""SELECT DISTINCT AccountNumber
                          FROM trans
                          JOIN account ON account.AccountId = trans.AccountId
                          ORDER BY AccountNumber
                        """)
        else:
            query.prepare("""SELECT DISTINCT AccountNumber
                          FROM trans
                          JOIN head ON head.HeadId = trans.HeadId
                          JOIN account ON account.AccountId = trans.AccountId
                          WHERE head.HeadType = :HeadType
                          ORDER BY AccountNumber
                         """)

            query.bindValue(":HeadType", arg)
            query.exec()

        while query.next():
            item = query.value(0)
            self.ui.comboAccountNumber.addItem(item)

        query.finish()

        if self.ui.comboAccountNumber.count() > 0:
            self.ui.comboAccountNumber.insertItem(0, 'All')

    def populateComboTransDate(self, arg='all'):
        self.ui.comboTransDate.clear()

        query = QSqlQuery()
        if arg.lower() == "all":
            query.exec("""SELECT DISTINCT TransDate
                          FROM trans
                          ORDER BY TransDate
                        """)
        else:
            query.prepare("""SELECT DISTINCT TransDate
                          FROM trans
                          JOIN head ON head.HeadId = trans.HeadId
                          WHERE head.HeadType = :HeadType
                          ORDER BY TransDate
                         """)

            query.bindValue(":HeadType", arg)
            query.exec()

        while query.next():
            item = query.value(0)
            self.ui.comboTransDate.addItem(item)

        query.finish()

        if self.ui.comboTransDate.count() > 0:
            self.ui.comboTransDate.insertItem(0, 'All')

    def onSelectTransactionType(self):
        sender = self.sender()
        if sender.isChecked():
            option = sender.text()
            self.populateComboAccountNumber(option)
            self.populateComboHeadName(option)
            self.populateComboTransDate(option)

        self.ui.buttonSearch.setEnabled(True)

    def onComboTextChanged(self, text):
        self.ui.buttonSearch.setEnabled(True)

    def onSearch(self):
        head_name = "All"
        account_number = "All"
        trans_date = "All"

        bind_values = {}

        # know which radio button is active
        if self.ui.radioReceipts.isChecked():
            trans_type = "Receipt"
        elif self.ui.radioPayments.isChecked():
            trans_type = "Payment"
        else:
            trans_type = "All"

        # get ComboBox current text
        if self.ui.comboHeadName.currentIndex() > 0:
            head_name = self.ui.comboHeadName.currentText()
        else:
            head_name = "All"

        if self.ui.comboAccountNumber.currentIndex() > 0:
            account_number = self.ui.comboAccountNumber.currentText()
        else:
            account_number = "All"

        if self.ui.comboTransDate.currentIndex() > 0:
            trans_date = self.ui.comboTransDate.currentText()
        else:
            trans_date = "All"

        self.ui.editHead.setText(head_name)
        self.ui.editAccount.setText(account_number)
        self.ui.editDate.setText(trans_date)

        # in case of all records are to be displayed
        if trans_type == "All" and account_number == "All" and head_name == "All" and trans_date == "All":
            self.loadRecords()

        # in case of selected records are to be displayed
        else:
            criteria_exists = False
            q_str = self.query_string

            if not trans_type == "All":
                where_clause = "WHERE HeadType = :HeadType"
                q_str = q_str + " " + where_clause
                bind_values.update({":HeadType": trans_type})

                criteria_exists = True
                self.setWindowTitle(trans_type)

            if not account_number == "All":
                if criteria_exists:
                    where_clause = " AND AccountNumber = :AccountNumber"
                else:
                    where_clause = "WHERE AccountNumber = :AccountNumber"

                q_str = q_str + " " + where_clause
                bind_values.update({":AccountNumber": account_number})

                criteria_exists = True

            if not head_name == "All":
                if criteria_exists:
                    where_clause = "AND HeadName = :HeadName"
                else:
                    where_clause = "WHERE HeadName = :HeadName"

                q_str = q_str + " " + where_clause
                bind_values.update({":HeadName": head_name})

                criteria_exists = True

            if not trans_date == "All":
                if criteria_exists:
                    where_clause = "AND TransDate = :TransDate"
                else:
                    where_clause = "WHERE TransDate = :TransDate"

                q_str = q_str + " " + where_clause
                bind_values.update({":TransDate": trans_date})

                criteria_exists = True

            # load records with criteria
            self.loadRecords(q_str, bind_values)

    def loadRecords(self, q_str=None, bind_values=None):
        # where totals to be shown or not

        if self.ui.radioAll.isChecked():
            self.ui.footerFrame.hide()

        elif self.ui.comboHeadName.currentText() == "ContraReceipt":
            self.ui.footerFrame.hide()

        elif self.ui.comboHeadName.currentText() == "ContraPayment":
            self.ui.footerFrame.hide()

        else:
            self.ui.footerFrame.show()

        self.query.finish()
        order_by_clause = "ORDER BY TransDate"
        self.ui.buttonSearch.setEnabled(False)

        if q_str is None or bind_values is None:
            self.setWindowTitle("All Transactions")
            self.query.exec(self.query_string + " " + order_by_clause)
        else:
            q_str = q_str + " " + order_by_clause
            self.query.prepare(q_str)

            for key, value in bind_values.items():
                self.query.bindValue(key, value)

            self.query.exec()

        # create model
        self.model = ShowTransactionModel(self.query)

        # set table vie
        table_column_headers = ["Date", "Head", "Details", "Amount", "Bank Name", "Account Number"]
        table_column_widths = [100, 225, 250, 100, 200, 175]

        self.model.setHeaderData(0, Qt.Horizontal, table_column_headers[0])
        self.model.setHeaderData(1, Qt.Horizontal, table_column_headers[1])
        self.model.setHeaderData(2, Qt.Horizontal, table_column_headers[2])
        self.model.setHeaderData(3, Qt.Horizontal, table_column_headers[3])
        self.model.setHeaderData(4, Qt.Horizontal, table_column_headers[4])
        self.model.setHeaderData(5, Qt.Horizontal, table_column_headers[5])

        # set model to table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)

        self.ui.tableView.hideColumn(6)
        self.ui.tableView.hideColumn(7)

        self.ui.tableView.setColumnWidth(0, table_column_widths[0])
        self.ui.tableView.setColumnWidth(1, table_column_widths[1])
        self.ui.tableView.setColumnWidth(2, table_column_widths[2])
        self.ui.tableView.setColumnWidth(3, table_column_widths[3])
        self.ui.tableView.setColumnWidth(4, table_column_widths[4])
        self.ui.tableView.setColumnWidth(5, table_column_widths[5])

        rows = self.model.rowCount()
        if rows:
            total = 0
            for row in range(rows):
                # update total
                amount = self.model.record(row).field(3).value()
                total += amount

                # set height for each row of table view
                self.ui.tableView.setRowHeight(row, 40)

            self.ui.editTotal.setText(str(total))
            self.text_label.hide()
            self.ui.buttonDownload.setEnabled(True)
        else:
            self.ui.footerFrame.hide()
            self.text_label.show()
            self.ui.buttonDownload.setEnabled(False)

    def downloadPDF(self):
        exp_month, exp_year = getPeriod()
        current_date = QDate().currentDate()
        current_time = QTime().currentTime()

        self.ui.buttonDownload.setEnabled(False)
        if transDateMismatch():
            title = "Unable to export data"
            showMismatchMessage(self, title=title)
            return

        if not trans_data_exist(self):
            MsgBox(title="Invalid operation",
                   msg="No data entered",
                   button_0="&Ok").warn(
            )
        else:
            # # # # # create file name and path  # # # # #
            parent_dir = os.environ["HOME"]
            directory = "Downloads"
            date = current_date.toString("yyyyMMdd")
            time = current_time.toString("hhmmss")
            file_name = f"ET{date}{time}.pdf"

            self.file_path = os.path.join(parent_dir, directory, file_name)

            # show progress bar
            pb = MidMonthProgressBar(self)
            pb.start_progress()

            # set pdf page title
            first_date = QDate().fromString(f"01-{exp_month}-{exp_year}", "dd-MMMM-yyyy")
            days_in_month = first_date.daysInMonth()
            last_date = QDate().fromString(f"{days_in_month}-{exp_month}-{exp_year}", "dd-MMMM-yyyy")

            if current_date > last_date:
                last_exp_date = last_date.toString("dd-MM-yyyy")
            else:
                last_exp_date = current_date.toString("dd-MM-yyyy")

            first_date = first_date.toString("dd-MM-yyyy")
            page_title = f"Details of Expenditures from {first_date} to {last_exp_date}"

            # for exp
            exp_fields_width = [25, 60, 60, 20, 20]
            exp_fields_heading = ["Date", "Particulars", "Account Details", "Receipt", "Payment"]
            exp_data = getAllTransactions()

            # for head total
            head_total_fields_width = [120, 30, 30]
            head_total_fields_heading = ["Expenditure Head", "Receipt ", "Payment"]
            head_total_data = getHeadTotals()

            # for grand total
            grand_total_fields_width = [30, 30, 30, 30, 30, 30]
            grand_total_fields_heading = ["Balance B/F", "Actual Receipt", "Contra Receipt",
                                          "Actual Payment", "Contra Payment", "Balance C/F"]
            grand_total_data = getOpeningBalanceGrandTotal()

            # for account summary
            account_summary_fields_width = [60, 25, 25, 25, 25, 25]
            account_summary_fields_heading = ["Account Details", "Balance B/F", "Receipt", "Gross Total",
                                              "Payment", "Balance C/F"]
            account_summary_data = getAccountTotals()

            # create class to generate pdf file
            pdf = PDF(exp_fields_width=exp_fields_width,
                      exp_fields_heading=exp_fields_heading,
                      exp_data=exp_data,

                      head_total_fields_width=head_total_fields_width,
                      head_total_fields_heading=head_total_fields_heading,
                      head_total_data=head_total_data,

                      grand_total_fields_width=grand_total_fields_width,
                      grand_total_fields_heading=grand_total_fields_heading,
                      grand_total_data=grand_total_data,

                      account_summary_fields_width=account_summary_fields_width,
                      account_summary_fields_heading=account_summary_fields_heading,
                      account_summary_data=account_summary_data,

                      page_title=page_title
                      )

            pdf.add_page()
            pdf.create_exp_table()

            pdf.add_page()
            pdf.create_head_total_table()

            pdf.add_page()
            pdf.create_account_summary_table()

            pdf.output(self.file_path)

        return

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.query.finish()
        event.accept()
