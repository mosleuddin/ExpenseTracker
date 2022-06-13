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

from PySide6.QtWidgets import QDialog

from db.table_basic_details import getPeriod
from db.table_trans import getMisMatchRecordId, populateMisMatchRecord, removeTransaction, \
    updateTransaction, validDate
from design.ui_period_mismatch import Ui_PeriodMismatch

from modules.module import resize_and_move, MsgBox


class PeriodMisMatch(QDialog):
    def __init__(self, parent):
        super(PeriodMisMatch, self).__init__(parent)
        self.parent = parent
        self.records = None
        self.record_count = 0
        self.current_index = 0
        self.old_trans_date = ""

        self.ui = Ui_PeriodMismatch()
        self.ui.setupUi(self)
        resize_and_move(self, self.parent, .75, .8)

        # set heading
        month, year = getPeriod()
        self.trans_month = month
        self.trans_year = year
        heading = f"Transaction date of some records are not matching with the current period : " \
                  f"<b><u>{self.trans_month} {self.trans_year}</u></b>"
        self.ui.labelHeading.setText(heading)

        self.setWindowTitle(f"Incorrect transaction date(s)")
        self.ui.labelMessage.hide()
        self.loadRecords()

    def configUI(self):
        self.ui.buttonReset.setEnabled(False)
        self.ui.buttonUpdate.setEnabled(False)

    def loadRecords(self):
        self.records = getMisMatchRecordId()
        self.record_count = len(self.records)

        if self.record_count == 0:
            title = "No MisMatch Records Found"
            msg = "Transaction Date of all records match with current period"
            MsgBox(title, msg, '&Got it').info()
            self.close()
        else:
            self.navigateRecords(0)
            self.show()

    def onDateChanged(self):
        self.ui.buttonReset.setEnabled(True)
        self.ui.buttonUpdate.setEnabled(True)
        self.ui.labelMessage.hide()

    def onUpdate(self):
        date = self.ui.dateTrans.date()
        details = self.ui.editTransDetails.text()
        amount = self.ui.editTransAmount.text()
        head = self.ui.editHead.text()
        account = self.ui.editAccount.text()

        title = 'Update Date'
        msg = ''

        # ###########################  Validating date ##############################
        if date == self.old_trans_date:
            title = 'No change found '
            msg = 'Nothing to update???'
        else:
            date_status = validDate(self, date)
            if date_status != "ok":
                title = f'Incorrect Transaction Date'
                msg = date_status
            else:
                updateTransaction(self, self.records[self.current_index],
                                  date, head, details, account, amount)

                msg = f'Record updated successfully'
                self.ui.labelMessage.setText(msg)
                self.ui.labelMessage.show()
                self.loadRecords()
                self.ui.dateTrans.setFocus()

        MsgBox(title, msg, '&Got it').warn()
        self.navigateRecords(self.current_index)
        self.ui.dateTrans.setFocus()
        return

    def onReset(self):
        self.navigateRecords(self.current_index)

    def onDelete(self):
        if MsgBox("Delete mismatch record",
                         "Do you want to proceed?",
                         "&Delete",
                         "&Cancel").confirm():

            removeTransaction(self, self.records[self.current_index])
            self.ui.labelMessage.setText("Record deleted")
            self.ui.labelMessage.show()
            self.current_index -= 1
            self.loadRecords()

    def navigateRecords(self, index):
        populateMisMatchRecord(self, self.records[index])
        self.configUI()

        if self.record_count == 1:
            self.ui.buttonFirst.setEnabled(False)
            self.ui.buttonPrevious.setEnabled(False)
            self.ui.buttonNext.setEnabled(False)
            self.ui.buttonLast.setEnabled(False)

        elif self.record_count == 2:
            if self.current_index == 0:
                self.ui.buttonFirst.setEnabled(False)
                self.ui.buttonPrevious.setEnabled(False)
                self.ui.buttonLast.setEnabled(True)
                self.ui.buttonNext.setEnabled(True)

            else:
                self.ui.buttonFirst.setEnabled(True)
                self.ui.buttonPrevious.setEnabled(True)
                self.ui.buttonLast.setEnabled(False)
                self.ui.buttonNext.setEnabled(False)

        else:
            if self.current_index == 0:
                self.ui.buttonFirst.setEnabled(False)
                self.ui.buttonPrevious.setEnabled(False)
                self.ui.buttonLast.setEnabled(True)
                self.ui.buttonNext.setEnabled(True)

            elif self.current_index == self.record_count - 1:
                self.ui.buttonFirst.setEnabled(True)
                self.ui.buttonPrevious.setEnabled(True)
                self.ui.buttonLast.setEnabled(False)
                self.ui.buttonNext.setEnabled(False)

            else:
                self.ui.buttonFirst.setEnabled(True)
                self.ui.buttonPrevious.setEnabled(True)
                self.ui.buttonLast.setEnabled(True)
                self.ui.buttonNext.setEnabled(True)

    def onFirst(self):
        self.current_index = 0
        self.navigateRecords(self.current_index)

    def onPrevious(self):
        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = 0

        self.navigateRecords(self.current_index)

    def onLast(self):
        self.current_index = self.record_count - 1
        self.navigateRecords(self.current_index)

    def onNext(self):
        self.current_index += 1

        if self.current_index == self.record_count:
            self.current_index = self.record_count - 1

        self.navigateRecords(self.current_index)

