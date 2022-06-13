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

from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QDialog, QLineEdit

from design.ui_initialize import Ui_InitializeTransactionWindow

from views.progress_bar import MonthEndProgressBar
from views.pdf_generator import PDF

from db.table_basic_details import getPeriod, increasePeriod
from db.table_trans import removeAllTransactions
from db.save_pdf_data import getAllTransactions, trans_data_exist, getHeadTotals
from db.table_balance import getOpeningBalanceGrandTotal, InitializeBalanceTable, getAccountTotals
from db.table_user import getPassword

from modules.module import MsgBox, resize_and_move


class InitializeTransaction(QDialog):
    def __init__(self, parent, user_id):
        super(InitializeTransaction, self).__init__(parent)
        self.user_id = user_id
        self.parent = parent
        self.common_icon = QIcon("./src/icons/common.png")

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

        self.ui.framePassword.hide()
        self.savePDF()

    def savePDF(self):
        exp_month, exp_year = getPeriod()
        current_date = QDate().currentDate()

        ok = True
        if not trans_data_exist(self):
            ok = MsgBox(title="No data entered for this month",
                        msg="Do you want proceed for initialization?",
                        button_0="&Ok",
                        button_1="&Cancel").confirm()

        if ok:
            # # # # # creating directory  # # # # #
            parent_dir = os.environ['HOME']
            target_dir = "ExpenseTracker/Previous Months Expenses"
            dir_path = os.path.join(parent_dir, target_dir)
            try:
                os.makedirs(dir_path)
            except FileExistsError:
                pass
            finally:

                file_name = f"{exp_month}-{exp_year}.pdf"
                self.file_path = os.path.join(dir_path, file_name)

                if os.path.exists(self.file_path):
                    MsgBox(title="Initialization not done",
                           msg="Expenditures for this Month and Year already saved",
                           button_0="&Ok").danger()
                    self.close()
                else:
                    # show progress bar
                    pb = MonthEndProgressBar(self)
                    pb.start_progress()

                    # set pdf page title
                    first_date = QDate().fromString(f"01-{exp_month}-{exp_year}", "dd-MMMM-yyyy")
                    days_in_month = first_date.daysInMonth()
                    last_date = QDate().fromString(f"{days_in_month}-{exp_month}-{exp_year}", "dd-MMMM-yyyy")

                    if current_date < last_date:
                        last_exp_date = current_date.toString("dd-MM-yyyy")
                    else:
                        last_exp_date = last_date.toString("dd-MM-yyyy")

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

                    # for account_summary
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

                    InitializeBalanceTable(month_end=True)
                    removeAllTransactions(self)
                    increasePeriod()

        else:
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()
