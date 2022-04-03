from PySide6.QtCore import QDate
from fpdf import FPDF

from db.table_basic_details import getPeriod


class PDF(FPDF):
    def __init__(
            self,
            orientation="portrait",
            unit="mm",
            format="A4",
            font_cache_dir=True,

            # customize arguments for data_table
            cols_width=None,
            cols_heading=None,
            data=None,

            # customize arguments for summary_table
            summary_headings=None,
            summary_totals=None,

            # used foe headers in case of mid month pdf files only
            period=None
    ):
        super().__init__(orientation, unit, format, font_cache_dir)

        self.cols_width = cols_width
        self.cols_heading = cols_heading
        self.data = data
        
        self.summary_headings = summary_headings
        self.summary_totals = summary_totals

        self.period = period

        self.line_height = self.font_size*1.5
        self.set_left_margin(15)

    def header(self):

        # Rendering logo:
        self.image("./src/icons/expense_tracker_sm.png", 10, 8, 24)

        # set background-color, text-color, line-color and font:
        # self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_draw_color(255, 100, 100)
        self.set_font("helvetica", "B", 14)

        # Moving cursor to the right:
        self.cell(50)
        # Printing title:
        if self.period is None:
            # for month end initialization
            month, year = getPeriod()
            title = f"Details of Expenditures for {month} {year}"
        else:
            # for mid month
            year = self.period[:4]
            month = self.period[4:6]
            day = self.period[6:8]

            title = f"Details of Expenditures upto {day}-{month}-{year}"

        self.cell(100, 8,title , 1, 0, "C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)

        # set background-color, text-color, line-color and font:
        # self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_draw_color(255, 100, 100)
        self.set_font("helvetica", "I", 12)

        # Printing date and page number:
        date = QDate().currentDate().toString("dd-MM-yyyy")
        self.cell(0, 10, f"Date : {date}           Page {self.page_no()}/{{nb}}", 0, 0, "C")

    def render_table_headers(self):
        # set background-color, text-color, line-color   and font:
        self.set_fill_color(13, 125, 126)
        self.set_text_color(255)
        self.set_draw_color(255, 100, 100)
        self.set_font("helvetica", style="B", size=12)

        for col_width, heading in zip(self.cols_width, self.cols_heading):
            self.cell(col_width, 16, heading, 1, 0, "C", True)
        self.ln()

        # restore background-color, text-color, line-color   and font:
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_draw_color(255, 100, 100)
        self.set_font("helvetica", size=12)

    def create_data_table(self):
        self.render_table_headers()
        fill = False
        for _ in range(100):
            for row in self.data:
                if self.will_page_break(self.line_height):
                    self.render_table_headers()

                exp_date = row[0]

                exp_head = row[1].title()
                if len(exp_head) > 25:
                    exp_head = exp_head[:25] + "..."

                exp_details = row[2].capitalize()
                if len(exp_details) > 25:
                    exp_details = exp_details[:25] + "..."

                bank_name = row[3].title()
                if len(bank_name) > 25:
                    bank_name = bank_name[:25] + "..."

                customer_name = row[4].title()
                if customer_name.title() == 'Cash':
                    customer_name = ''
                else:
                    if len(customer_name) > 25:
                        customer_name = customer_name[:25] + "..."

                account_number = row[5].capitalize()
                if account_number.capitalize() == 'Cash':
                    account_number = ''
                else:
                    account_number = f'(A/c No. {account_number})'
                    if len(account_number) > 25:
                        account_number = account_number[:25] + "..."

                receipt_amount = str(row[6])

                payment_amount = str(row[7])

                self.cell(self.cols_width[0], self.line_height, exp_date, "LR", 0, "L", fill)
                self.cell(self.cols_width[1], self.line_height, exp_head, "LR", 0, "L", fill)
                self.cell(self.cols_width[2], self.line_height, account_number, "LR", 0, "L", fill)
                self.cell(self.cols_width[3], self.line_height, receipt_amount, "LR", 0, "R", fill)
                self.cell(self.cols_width[4], self.line_height, payment_amount, "LR", 0, "R", fill)
                self.ln()

                self.cell(self.cols_width[0], self.line_height, "", "LR", 0, "L", fill)
                self.cell(self.cols_width[1], self.line_height, exp_details, "LR", 0, "L", fill)
                self.cell(self.cols_width[2], self.line_height, bank_name, "LR", 0, "L", fill)
                self.cell(self.cols_width[3], self.line_height, "", "LR", 0, "R", fill)
                self.cell(self.cols_width[4], self.line_height, "", "LR", 0, "R", fill)
                self.ln()

                self.cell(self.cols_width[0], self.line_height, "", "LR", 0, "L", fill)
                self.cell(self.cols_width[1], self.line_height, "", "LR", 0, "L", fill)
                self.cell(self.cols_width[2], self.line_height, customer_name, "LR", 0, "L", fill)
                self.cell(self.cols_width[3], self.line_height, "", "LR", 0, "R", fill)
                self.cell(self.cols_width[4], self.line_height, "", "LR", 0, "R", fill)
                self.ln()
                self.cell(sum(self.cols_width), 0, "", "T")
                self.ln()
                fill = not fill
            self.cell(sum(self.cols_width), 0, "", "T")
            self.ln()

    def create_summary_table(self):
        # change values for draw_color and fill_color attributes
        self.set_draw_color(255, 100, 100)
        self.set_fill_color(224, 235, 255)

        # change values for text_color and font attributes for heading of the page
        self.set_text_color(115, 55, 150)
        self.set_font("helvetica", "B", 13)

        self.cell(200, 10, "Summary of Totals", 0, 0, "C")
        self.ln(20)

        # change values for text_color and font attributes for column headings
        self.set_text_color(13, 125, 125)
        self.set_font("helvetica", "B", 12)

        for heading in self.summary_headings:
            self.cell(38, 10, heading, 1, 0, "C", True)
        self.ln()

        # change values for text_color and font attributes for data
        self.set_text_color(0)
        self.set_font("helvetica", "", 12)

        for row in self.summary_totals:
            for index, col in enumerate(row):
                if index == 0:
                    self.cell(38, 10, str(col), "LR", 0, "L")
                else:
                    self.cell(38, 10, str(col), "LR", 0, "R")
            self.ln()
            self.cell(190, 0, "", "T")
            self.ln()
