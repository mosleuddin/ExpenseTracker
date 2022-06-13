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
from fpdf import FPDF


class PDF(FPDF):
    def __init__(
            self,
            orientation="portrait",
            unit="mm",
            format="A4",
            font_cache_dir=True,

            # customize arguments for exp table
            exp_fields_width=None,
            exp_fields_heading=None,
            exp_data=None,

            # customize arguments for head_total table
            head_total_fields_width=None,
            head_total_fields_heading=None,
            head_total_data=None,

            # customize arguments for grand_total table
            grand_total_fields_width=None,
            grand_total_fields_heading=None,
            grand_total_data=None,

            # customize arguments for account_summary table
            account_summary_fields_width=None,
            account_summary_fields_heading=None,
            account_summary_data=None,

            # to print a page heading
            page_title=None
    ):
        super().__init__(orientation, unit, format, font_cache_dir)

        # values which are applicable for exp table page only
        self.exp_fields_width = exp_fields_width
        self.exp_fields_heading = exp_fields_heading
        self.exp_data = exp_data

        # values which are applicable for head_total table page only
        self.head_total_fields_width = head_total_fields_width
        self.head_total_fields_heading = head_total_fields_heading
        self.head_total_data = head_total_data

        # values which are applicable for grand_total table
        # grand_total table is not a separate page. The table is created inside the head_table page.
        self.grand_total_fields_width = grand_total_fields_width
        self.grand_total_fields_heading = grand_total_fields_heading
        self.grand_total_data = grand_total_data

        # values which are applicable for account_summary table page only
        self.account_summary_fields_width = account_summary_fields_width
        self.account_summary_fields_heading = account_summary_fields_heading
        self.account_summary_data = account_summary_data

        # global values which are applicable for all pages
        self.page_title = page_title
        self.set_draw_color(255, 100, 100)

        self.heading_height = 14
        self.line_height = self.font_size * 1.50

    def header(self):
        # Rendering logo:
        self.image("./src/icons/expense_tracker_sm.png", 10, 8, 24)

        # set font and text_color for page-header:
        self.set_font("helvetica", size=13)
        self.set_text_color(0)

        self.cell(30)  # Move cursor to the right:
        self.cell(135, 8, self.page_title, 1, 0, "C")  # print page title / heading
        self.ln(20)  # Performing a line break

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)

        # set background-color, text-color, line-color and font:
        self.set_font("helvetica", "I", 10)
        self.set_text_color(115, 55, 150)

        # Printing date and page number:
        date = QDate().currentDate().toString("dd-MM-yyyy")
        self.cell(0, 10, f"Date : {date}           Page {self.page_no()}/{{nb}}", 0, 0, "C")

    def table_heading_style(self):
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font("helvetica", "B", size=12)

    def table_row_style(self):
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font("helvetica", size=12)

    def render_exp_table_headers(self):
        # set table-heading style
        self.table_heading_style()

        for col_width, heading in zip(self.exp_fields_width, self.exp_fields_heading):
            self.cell(col_width, self.heading_height, heading, 1, 0, "C", True)
        self.ln()

        # set table-row style
        self.table_row_style()

    def render_head_total_table_headers(self):
        # print sub title
        self.set_font("helvetica", "B", 12)
        self.set_text_color(115, 55, 150)
        self.cell(185, 10, "Total expenditure on each head", 0, 0, "C")
        self.ln(15)

        # set table-heading style
        self.table_heading_style()

        for col_width, heading in zip(self.head_total_fields_width, self.head_total_fields_heading):
            self.cell(col_width, self.heading_height, heading, 1, 0, "C", True)
        self.ln()

        # set table-row style
        self.table_row_style()

    def render_grand_total_table_headers(self):
        # print sub title
        self.set_font("helvetica", "B", 12)
        self.set_text_color(115, 55, 150)
        self.cell(180, 10, "Grand Total", 0, 0, "C")
        self.ln(10)

        # set table-heading style
        self.table_heading_style()
        self.set_font("helvetica", "B", 10)
        for col_width, heading in zip(self.grand_total_fields_width, self.grand_total_fields_heading):
            self.cell(col_width, self.heading_height, heading, 1, 0, "C", True)
        self.ln()

        # set table-row style
        self.table_row_style()

    def render_account_summary_table_headers(self):
        # print sub title
        self.set_font("helvetica", "B", 12)
        self.set_text_color(115, 55, 150)
        self.cell(200, 10, "Account Summary", 0, 0, "C")
        self.ln(10)

        # set table-heading style
        self.table_heading_style()
        self.set_font("helvetica", "B", 10)

        for col_width, heading in zip(self.account_summary_fields_width, self.account_summary_fields_heading):
            self.cell(col_width, self.heading_height, heading, 1, 0, "C", True)
        self.ln()

        # set table-row style
        self.table_row_style()

    def create_exp_table(self):
        self.set_left_margin(15)
        self.render_exp_table_headers()
        fill = False
        for row in self.exp_data:
            if self.will_page_break(self.line_height):
                self.render_exp_table_headers()

            exp_date = row[0]

            exp_head = row[1]
            if len(exp_head) > 24:
                exp_head = exp_head[:25] + "..."

            exp_details = row[2].lower()
            if len(exp_details) > 24:
                exp_details = exp_details[:25] + "..."

            bank_name = row[3].title()
            if len(bank_name) > 24:
                bank_name = bank_name[:25] + "..."

            customer_name = row[4].title()
            if customer_name.title() == 'Cash':
                customer_name = ''
            else:
                if len(customer_name) > 24:
                    customer_name = customer_name[:25] + "..."

            account_number = row[5].capitalize()
            if account_number.capitalize() == 'Cash':
                account_number = ''
            else:
                account_number = f'(A/c No. {account_number})'
                if len(account_number) > 24:
                    account_number = account_number[:25] + "..."

            receipt_amount = str(row[6])

            payment_amount = str(row[7])

            if exp_head == "ContraReceipt" or exp_head == "ContraPayment":
                self.set_text_color(255, 25, 25)
            else:
                self.set_text_color(0)

            self.cell(self.exp_fields_width[0], self.line_height, exp_date, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[1], self.line_height, exp_head, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[2], self.line_height, account_number, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[3], self.line_height, receipt_amount, "LR", 0, "R", fill)
            self.cell(self.exp_fields_width[4], self.line_height, payment_amount, "LR", 0, "R", fill)
            self.ln()

            self.cell(self.exp_fields_width[0], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[1], self.line_height, exp_details, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[2], self.line_height, bank_name, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[3], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.exp_fields_width[4], self.line_height, "", "LR", 0, "R", fill)
            self.ln()

            self.cell(self.exp_fields_width[0], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[1], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[2], self.line_height, customer_name, "LR", 0, "L", fill)
            self.cell(self.exp_fields_width[3], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.exp_fields_width[4], self.line_height, "", "LR", 0, "R", fill)
            self.ln()

            self.cell(sum(self.exp_fields_width), 0, "", "T")
            self.ln()
            # fill = not fill
        self.cell(sum(self.exp_fields_width), 0, "", "T")
        self.ln()

    def create_head_total_table(self):
        # to keep record of the total of ContraReceipt head and ContraPayment head
        contra_receipt_total = 0
        contra_payment_total = 0

        actual_receipt_total = 0
        actual_payment_total = 0

        # change page margin and line height
        self.set_left_margin(20)
        self.line_height = 12
        self.render_head_total_table_headers()
        fill = False

        for row in self.head_total_data:
            if self.will_page_break(self.line_height):
                self.render_head_total_table_headers()

            head_type = row[0]
            head_name = row[1]
            head_total = row[2]

            if head_type == "Receipt":
                receipt_amount = head_total
                payment_amount = 0

                # update contra receipt total
                if head_name == "ContraReceipt":
                    contra_receipt_total += receipt_amount
                    self.set_text_color(255, 25, 25)
                else:
                    actual_receipt_total += receipt_amount
                    self.set_text_color(0)

            else:
                receipt_amount = 0
                payment_amount = head_total

                # update contra payment total
                if head_name == "ContraPayment":
                    contra_payment_total += payment_amount
                    self.set_text_color(255, 25, 25)
                else:
                    actual_payment_total += payment_amount
                    self.set_text_color(0)

            self.cell(self.head_total_fields_width[0], self.line_height, head_name, "LR", 0, "L", fill)
            self.cell(self.head_total_fields_width[1], self.line_height, str(receipt_amount), "LR", 0, "L", fill)
            self.cell(self.head_total_fields_width[2], self.line_height, str(payment_amount), "LR", 0, "R", fill)
            self.ln()

            self.cell(sum(self.head_total_fields_width), 0, "", "T")
            self.ln()

            # fill = not fill

        self.cell(sum(self.head_total_fields_width), 0, "", "T")
        self.ln()
        self.create_grand_total_table(actual_receipt=actual_receipt_total, contra_receipt=contra_receipt_total,
                                      actual_payment=actual_payment_total, contra_payment=contra_payment_total)

    def create_grand_total_table(self, actual_receipt, contra_receipt, actual_payment, contra_payment):

        self.render_grand_total_table_headers()

        fill = False

        actual_receipt_total = actual_receipt
        contra_receipt_total = contra_receipt
        gross_total = self.grand_total_data + actual_receipt_total + contra_receipt_total

        actual_payment_total = actual_payment
        contra_payment_total = contra_payment
        gross_payment = actual_payment_total + contra_payment_total

        total_closing_balance = gross_total - gross_payment

        self.cell(self.grand_total_fields_width[0], self.line_height, str(self.grand_total_data), "LR", 0, "R", fill)
        self.cell(self.grand_total_fields_width[1], self.line_height, str(actual_receipt_total), "LR", 0, "R", fill)
        self.cell(self.grand_total_fields_width[2], self.line_height, str(contra_receipt_total), "LR", 0, "R", fill)
        self.cell(self.grand_total_fields_width[3], self.line_height, str(actual_payment_total), "LR", 0, "R", fill)
        self.cell(self.grand_total_fields_width[4], self.line_height, str(contra_payment_total), "LR", 0, "R", fill)
        self.cell(self.grand_total_fields_width[5], self.line_height, str(total_closing_balance), "LR", 0, "R", fill)
        self.ln()
        self.cell(sum(self.head_total_fields_width), 0, "", "T")
        self.ln()

    def create_account_summary_table(self):
        # change page margin and line height
        self.set_left_margin(15)
        self.line_height = self.font_size * 1.50

        self.render_account_summary_table_headers()
        fill = False
        for row in self.account_summary_data:
            if self.will_page_break(self.line_height):
                self.render_account_summary_table_headers()

            # format account number
            account_number = row[0].capitalize()
            if account_number.lower() == 'cash':
                account_number = ""
            else:
                account_number = f'A/c No. {account_number}'
                if len(account_number) > 24:
                    account_number = account_number[:25] + "..."

            # format customer_name
            customer_name = row[1].title()
            if customer_name.lower() == 'cash':
                customer_name = 'Cash Account'
            else:
                if len(customer_name) > 24:
                    customer_name = customer_name[:25] + "..."

            # format bank_name
            bank_name = row[2].title()
            if bank_name.lower() == 'cash':
                bank_name = ''
            else:
                if len(bank_name) > 24:
                    bank_name = bank_name[:25] + "..."

            # format branch_name
            branch_name = row[3].title()
            if branch_name.lower() == 'cash':
                branch_name = ''
            if len(branch_name) > 24:
                branch_name = branch_name[:25] + "..."

            # balances
            opening_balance = str(row[4])
            total_receipt = str(row[5])
            gross_amount = str(row[6])
            total_payment = str(row[7])
            closing_balance = str(row[8])

            self.cell(self.account_summary_fields_width[0], self.line_height, account_number, "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[1], self.line_height, opening_balance, "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[2], self.line_height, total_receipt, "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[3], self.line_height, gross_amount, "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[4], self.line_height, total_payment, "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[5], self.line_height, closing_balance, "LR", 0, "R", fill)
            self.ln()

            self.cell(self.account_summary_fields_width[0], self.line_height, customer_name, "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[1], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[2], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[3], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[4], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[5], self.line_height, "", "LR", 0, "R", fill)
            self.ln()

            self.cell(self.account_summary_fields_width[0], self.line_height, bank_name, "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[1], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[2], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[3], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[4], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[5], self.line_height, "", "LR", 0, "R", fill)
            self.ln()

            self.cell(self.account_summary_fields_width[0], self.line_height, branch_name, "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[1], self.line_height, "", "LR", 0, "L", fill)
            self.cell(self.account_summary_fields_width[2], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[3], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[4], self.line_height, "", "LR", 0, "R", fill)
            self.cell(self.account_summary_fields_width[5], self.line_height, "", "LR", 0, "R", fill)
            self.ln()

            self.cell(sum(self.account_summary_fields_width), 0, "", "T")
            self.ln()
            # fill = not fill

        self.cell(sum(self.account_summary_fields_width), 0, "", "T")
        self.ln()
