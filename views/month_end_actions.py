import os

from PySide6.QtGui import QIcon, Qt, QColor
from PySide6.QtSql import QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QDialog, QLineEdit

from db.table_balance import updateBalanceTable
from db.table_basic_details import getPeriod, increasePeriod
from db.table_trans import removeAllTransactions
from db.table_user import getPassword
from design.ui_initialize import Ui_InitializeTransactionWindow
from modules.module import CustomMessage, resize_and_move
from views.pdf_generator import PDF


class PdfDataModel(QSqlQueryModel):
    def __init__(self, query=None):
        super(PdfDataModel, self).__init__()

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


class InitializeTransaction(QDialog):
    def __init__(self, parent, user_id):
        super(InitializeTransaction, self).__init__(parent)
        self.user_id = user_id
        self.parent = parent
        self.common_icon = QIcon("./src/icons/common.png")

        self.cash_receipt_total = 0
        self.bank_receipt_total = 0
        self.contra_receipt_total = 0

        self.cash_payment_total = 0
        self.bank_payment_total = 0
        self.contra_payment_total = 0

        self.ui = Ui_InitializeTransactionWindow()
        self.ui.setupUi(self)
        self.configUI()
        self.show()

    def configUI(self):
        resize_and_move(self, self.parent, .6, .6)
        self.ui.labelMessage.hide()
        self.ui.framePassword.hide()
        self.ui.btnAlertClose.setFocus()
        self.ui.editPassword.addAction(self.common_icon, QLineEdit.ActionPosition.LeadingPosition)
        alert = """This action will carry out the following tasks:
                   \n\n(a) Save all transactions of current month in a pdf file.
                   
                   \n\n(b) Delete all transactions of current month from database.
                   
                   \n\n(c) The application will be ready for making transactions for the next month
                """
        self.ui.labelAlertMsg.setText(alert)

    def onTextEdited(self, text):
        self.ui.labelMessage.hide()
        self.ui.btnPasswordSubmit.setEnabled(True)

    def onProceed(self):
        self.ui.frameAlert.hide()
        self.ui.framePassword.show()
        self.ui.btnPasswordSubmit.setEnabled(False)
        self.ui.editPassword.setFocus()

    def onInitialize(self):
        orig_pass = getPassword(self, self.user_id)
        input_pass = self.ui.editPassword.text().strip()

        if not input_pass == orig_pass:
            self.ui.labelMessage.setText("Incorrect password")
            self.ui.labelMessage.show()
            self.ui.btnPasswordSubmit.setEnabled(False)
            self.ui.editPassword.setFocus()
            return

        self.savePDF()

    def createModel(self):
        query = QSqlQuery()
        query.exec("""SELECT TransDate, HeadName, TransDetails,
                      TransAmount, BankName, AccountNumber, HeadType
                      FROM trans
                      JOIN head ON head.HeadId = trans.HeadId
                      JOIN account ON account.AccountId = trans.AccountId
                      ORDER BY TransDate
                    """)

        # create model
        self.model = PdfDataModel(query)

        rows = self.model.rowCount()
        if rows:
            self.cash_receipt_total = 0
            self.bank_receipt_total = 0
            self.contra_receipt_total = 0

            self.cash_payment_total = 0
            self.bank_payment_total = 0
            self.contra_payment_total = 0

            for row in range(rows):
                transaction_head = self.model.record(row).field(1).value()
                transaction_amount = self.model.record(row).field(3).value()
                transaction_mode = self.model.record(row).field(5).value()
                transaction_type = self.model.record(row).field(6).value()

                if transaction_type == "Receipt":
                    if transaction_mode == "Cash":
                        self.cash_receipt_total += transaction_amount
                    else:
                        self.bank_receipt_total += transaction_amount

                    if transaction_head == "ContraReceipt":
                        self.contra_receipt_total += transaction_amount

                else:
                    if transaction_mode == "Cash":
                        self.cash_payment_total += transaction_amount
                    else:
                        self.bank_payment_total += transaction_amount

                    if transaction_head == "ContraPayment":
                        self.contra_payment_total += transaction_amount

    def getData(self):
        data = []
        query = QSqlQuery()
        query.exec("""SELECT TransDate, HeadName, TransDetails,
                      BankName, CustomerName, AccountNumber,  TransAmount, HeadType
                      FROM trans
                      JOIN head ON head.HeadId = trans.HeadId
                      JOIN account ON account.AccountId = trans.AccountId
                      ORDER BY TransDate
                    """)

        while query.next():
            receipt_amount = 0
            payment_amount = 0

            date = query.value(0)

            head = query.value(1)
            details = query.value(2)

            bank = query.value(3)
            customer = query.value(4)
            account = query.value(5)

            amount = query.value(6)
            trans_type = query.value(7)

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
        query.finish()
        return data

    def savePDF(self):
        ok = True
        cols_width = [25, 55, 55, 25, 25]
        cols_heading = ["Date", "Particulars", "Account Details", "Receipt", "Payment"]
        data = self.getData()
        if not data:
            ok = CustomMessage(self).confirm(
                title="No data entered for this month",
                msg="Do you want proceed for initialization?",
                button_0="&Ok",
                button_1="&Cancel")

        # summary
        summary_headings = ["Transaction Type", "Cash", "Bank", "Total", "Contra Amount"]

        summary_totals = [
            ("Receipt", self.cash_receipt_total, self.bank_receipt_total,
             self.cash_receipt_total + self.bank_receipt_total, self.contra_receipt_total),

            ("Payment", self.cash_payment_total, self.bank_payment_total,
             self.cash_payment_total + self.bank_payment_total, self.contra_payment_total),
        ]

        if ok:
            self.ui.btnPasswordSubmit.setEnabled(False)

            # create class to generate pdf file
            pdf = PDF(cols_width=cols_width,
                      cols_heading=cols_heading,
                      data=data,
                      summary_headings=summary_headings,
                      summary_totals=summary_totals
                      )

            pdf.add_page()
            pdf.create_data_table()

            pdf.add_page()
            pdf.create_summary_table()

            # # # # # creating directory  # # # # #

            parent_dir = os.environ['HOME']
            target_dir = "ExpenseTracker/Previous Months Expenses"
            dir_path = os.path.join(parent_dir, target_dir)

            try:
                os.makedirs(dir_path)
            except FileExistsError:
                pass
            finally:
                month, year = getPeriod()
                f_name = f"{month}-{year}.pdf"
                file_name = os.path.join(dir_path, f_name)

                if os.path.exists(file_name):
                    CustomMessage(self).warn(title="Error : File Exists",
                                             msg="Expenditures for this Month and Year already saved", button_0="&Ok")

                else:
                    pdf.output(file_name)
                    updateBalanceTable(self)
                    removeAllTransactions(self)
                    increasePeriod()
                    CustomMessage(self).info(title="Data saved successfully at the following location",
                                             msg=file_name, button_0="&Ok")

        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()
