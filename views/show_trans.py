import os

from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLabel, QTableView

from db.table_trans import TransDateMismatch
from views.pdf_generator import PDF

from design.ui_show_trans import Ui_ShowTransactions
from modules.module import resize_and_move, CustomMessage, showMismatchMessage


class TransactionModel(QSqlQueryModel):
    def __init__(self, query=None):
        super(TransactionModel, self).__init__()

        self.setQuery(query)

    def data(self, index, role):
        if index.isValid():
            col = index.column()
            row = index.row()

            if role == Qt.TextAlignmentRole:
                if col == 3:
                    return Qt.AlignRight
                elif col == 4:
                    return Qt.AlignHCenter
                else:
                    return Qt.AlignLeft

            if role == Qt.BackgroundRole:
                if row % 2 == 0:
                    return QColor("#d4e5f6")
                else:
                    return QColor("#EAF1CE")

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

        self.headings = ["Date", "Head", "Details", "Amount", "Bank Name", "Account Number"]
        self.col_widths = [100, 225, 250, 100, 200, 175]

        self.cash_receipt_total = 0
        self.bank_receipt_total = 0
        self.contra_receipt_total = 0

        self.cash_payment_total = 0
        self.bank_payment_total = 0
        self.contra_payment_total = 0

        self.ui = Ui_ShowTransactions()
        self.ui.setupUi(self)
        resize_and_move(self, wd=.99, ht=.9)

        self.createLabel()
        self.loadRecords()
        self.populateComboHeadName()
        self.populateComboAccountNumber()
        self.populateComboTransDate()

        self.show()

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
            self.ui.footerFrame.hide()

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
        self.query.finish()
        order_by_clause = "ORDER BY TransDate"

        self.ui.buttonSearch.setEnabled(False)

        if q_str is None or bind_values is None:
            self.ui.footerFrame.hide()
            self.setWindowTitle("All Transactions")
            self.query.exec(self.query_string + " " + order_by_clause)
        else:
            q_str = q_str + " " + order_by_clause
            self.query.prepare(q_str)

            for key, value in bind_values.items():
                self.query.bindValue(key, value)

            self.query.exec()
            self.ui.footerFrame.show()

        # create model
        self.model = TransactionModel(self.query)

        self.model.setHeaderData(0, Qt.Horizontal, self.headings[0])
        self.model.setHeaderData(1, Qt.Horizontal, self.headings[1])
        self.model.setHeaderData(2, Qt.Horizontal, self.headings[2])
        self.model.setHeaderData(3, Qt.Horizontal, self.headings[3])
        self.model.setHeaderData(4, Qt.Horizontal, self.headings[4])
        self.model.setHeaderData(5, Qt.Horizontal, self.headings[5])

        # set model to table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)

        self.ui.tableView.hideColumn(6)
        self.ui.tableView.hideColumn(7)

        self.ui.tableView.setColumnWidth(0, self.col_widths[0])
        self.ui.tableView.setColumnWidth(1, self.col_widths[1])
        self.ui.tableView.setColumnWidth(2, self.col_widths[2])
        self.ui.tableView.setColumnWidth(3, self.col_widths[3])
        self.ui.tableView.setColumnWidth(4, self.col_widths[4])
        self.ui.tableView.setColumnWidth(5, self.col_widths[5])

        rows = self.model.rowCount()
        if rows:
            for row in range(rows):
                self.ui.tableView.setRowHeight(row, 40)
            self.getData(only_update_totals=True)  # update totals
            total = (self.cash_receipt_total + self.bank_receipt_total +
                     self.cash_payment_total + self.bank_payment_total)

            self.text_label.hide()
            self.ui.editTotal.setText(str(total))
            if not self.ui.radioAll.isChecked():
                self.ui.footerFrame.show()

            self.ui.buttonExport.setEnabled(True)

        else:
            self.text_label.show()
            self.ui.footerFrame.hide()
            self.ui.buttonExport.setEnabled(False)

    def onExportToPDF(self):
        if TransDateMismatch():
            title = "Unable to export data"
            showMismatchMessage(self, title=title)
            return

        # get data
        data = self.getData()
        if not data:
            CustomMessage(self).warn(
                title="Invalid operation",
                msg="No data entered",
                button_0="&Ok")
        else:
            # data columns
            cols_width = [25, 55, 55, 25, 25]
            cols_heading = ["Date", "Particulars", "Account Details", "Receipt", "Payment"]

            # summary
            summary_headings = ["Transaction Type", "Cash", "Bank", "Total", "Contra Amount"]

            summary_totals = [
                ("Receipt", self.cash_receipt_total, self.bank_receipt_total,
                 self.cash_receipt_total + self.bank_receipt_total, self.contra_receipt_total),

                ("Payment", self.cash_payment_total, self.bank_payment_total,
                 self.cash_payment_total + self.bank_payment_total, self.contra_payment_total),
            ]

            # # # # # create file name and path  # # # # #
            date = QDate().currentDate().toString("yyyyMMdd")
            time = QTime().currentTime().toString("hhmmss")

            parent_dir = os.environ["HOME"]
            directory = "Downloads"
            file_name = f"ET{date}{time}.pdf"

            file_path = os.path.join(parent_dir, directory, file_name)

            # create class to generate pdf file
            pdf = PDF(cols_width=cols_width,
                      cols_heading=cols_heading,
                      data=data,
                      summary_headings=summary_headings,
                      summary_totals=summary_totals,
                      period=date
                      )

            pdf.add_page()
            pdf.create_data_table()

            pdf.add_page()
            pdf.create_summary_table()

            pdf.output(file_path)
            CustomMessage(self).info(title="Data saved successfully",
                                     msg=f"\n{file_path}", button_0="&Ok")

        self.ui.buttonExport.setEnabled(False)

    def getData(self, only_update_totals=False):
        data = []
        receipt_amount = 0
        payment_amount = 0
        rows = self.model.rowCount()

        self.cash_receipt_total = 0
        self.bank_receipt_total = 0
        self.contra_receipt_total = 0

        self.cash_payment_total = 0
        self.bank_payment_total = 0
        self.contra_payment_total = 0

        for row in range(rows):
            date = self.model.record(row).field(0).value()
            head = self.model.record(row).field(1).value()
            details = self.model.record(row).field(2).value()
            amount = self.model.record(row).field(3).value()
            bank = self.model.record(row).field(4).value()
            account = self.model.record(row).field(5).value()
            customer = self.model.record(row).field(6).value()
            trans_type = self.model.record(row).field(7).value()

            if trans_type == "Receipt":
                receipt_amount = amount

                # update cash and bank receipt totals
                if account == "Cash":
                    self.cash_receipt_total += amount
                else:
                    self.bank_receipt_total += amount

                # update contra receipt total
                if head == "ContraReceipt":
                    self.contra_receipt_total += amount
            else:
                payment_amount = amount

                # update cash and bank payment totals
                if account == "Cash":
                    self.cash_payment_total += amount
                else:
                    self.bank_payment_total += amount

                # update contra payment total
                if head == "ContraPayment":
                    self.contra_payment_total += amount

            record = (date, head, details, bank, customer, account, receipt_amount, payment_amount, trans_type)
            data.append(record)

        if only_update_totals:
            return
        else:
            return data

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.query.finish()
        event.accept()
