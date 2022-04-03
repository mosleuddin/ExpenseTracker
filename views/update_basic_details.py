from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog

from db.table_balance import getOpeningBalance, updateOpeningBalance
from db.table_basic_details import getOwner, getPeriod, updateOwner, updatePeriod, validPeriod
from modules.module import valid_char, valid_space, CustomMessage, resize_and_move
from design.ui_basic_details import Ui_BasicDetailsWindow


class UpdateBasicDetails(QDialog):
    def __init__(self, parent):
        super(UpdateBasicDetails, self).__init__(parent=parent)
        # create UI

        self.ui = Ui_BasicDetailsWindow()
        self.ui.setupUi(self)

        self.initUI()  # set up ui and other related tasks
        self.ui.lblMsg.hide()
        self.show()

    def initUI(self):
        resize_and_move(self, wd=.7, ht=.6)
        # self.setFixedSize(500, 400)
        self.ui.lblHead.setText("Change Basic Details")
        self.ui.editCashBalance.setValidator(QIntValidator())

        # disable LineEdits
        self.ui.editName.setEnabled(False)
        self.ui.editAddress.setEnabled(False)
        self.ui.editCashBalance.setEnabled(False)
        self.ui.editMonth.setEnabled(False)
        self.ui.editYear.setEnabled(False)

        # get owner details
        owner_name, owner_address = getOwner()

        # get period details
        active_month, active_year = getPeriod()

        if not active_year.isnumeric():
            active_year = "0"

        # get cash balance
        cash_balance = getOpeningBalance(account_number="Cash")
        cash_balance = cash_balance[-1].strip()
        if not cash_balance.isnumeric():
            cash_balance = "0"

        # put received data from database into respective widgets
        self.ui.editName.setText(owner_name)
        self.ui.editAddress.setText(owner_address)
        self.ui.editMonth.setText(active_month)
        self.ui.editYear.setText(active_year)
        self.ui.editCashBalance.setText(cash_balance)

    def onReturnPressed(self):
        sender = self.sender()
        if sender == self.ui.editName:
            self.ui.editAddress.setFocus()
        elif sender == self.ui.editAddress:
            self.ui.editCashBalance.setFocus()

        elif sender == self.ui.editMonth:
            self.ui.editYear.setFocus()

        else:
            self.ui.btnSubmit.setFocus()

    def onTextEdited(self, text):
        if text:
            self.ui.btnSubmit.setEnabled(True)
        else:
            self.ui.btnSubmit.setEnabled(False)

        self.ui.lblMsg.hide()

    def onLockUnlock(self):
        sender = self.sender()
        if sender == self.ui.btnName:
            if self.ui.editName.isEnabled():
                self.ui.editName.setEnabled(False)
                self.ui.btnName.setText("Unlock")
            else:
                self.ui.editName.setEnabled(True)
                self.ui.editName.setFocus()
                self.ui.btnName.setText("Lock")

        elif sender == self.ui.btnAddress:
            if self.ui.editAddress.isEnabled():
                self.ui.editAddress.setEnabled(False)
                self.ui.btnAddress.setText("Unlock")
            else:
                self.ui.editAddress.setEnabled(True)
                self.ui.editAddress.setFocus()
                self.ui.btnAddress.setText("Lock")

        elif sender == self.ui.btnCashBalance:
            if self.ui.editCashBalance.isEnabled():
                self.ui.editCashBalance.setEnabled(False)
                self.ui.btnCashBalance.setText("Unlock")
            else:
                self.ui.editCashBalance.setEnabled(True)
                self.ui.editCashBalance.setFocus()
                self.ui.btnCashBalance.setText("Lock")

        elif sender == self.ui.btnMonth:
            if self.ui.editMonth.isEnabled():
                self.ui.editMonth.setEnabled(False)
                self.ui.btnMonth.setText("Unlock")
            else:
                self.ui.editMonth.setEnabled(True)
                self.ui.editMonth.setFocus()
                self.ui.btnMonth.setText("Lock")

        elif sender == self.ui.btnYear:
            if self.ui.editYear.isEnabled():
                self.ui.editYear.setEnabled(False)
                self.ui.btnYear.setText("Unlock")
            else:
                self.ui.editYear.setEnabled(True)
                self.ui.editYear.setFocus()
                self.ui.btnYear.setText("Lock")

    def onSubmit(self):
        name = self.ui.editName.text().strip()
        address = self.ui.editAddress.text().strip()
        month = self.ui.editMonth.text().strip().capitalize()
        year = self.ui.editYear.text().strip()
        balance = self.ui.editCashBalance.text().strip()

        title = 'Basic Details'
        msg = 'Record updated successfully'
        obj = None
        name_chars = [' ', '-']
        address_chars = [' ', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # ###########################  Validating Owner Name ##############################
        if len(name) < 3:
            obj = self.ui.editName
            title = 'Invalid Owner Name'
            msg = 'Minimum 3 characters required'

        elif not valid_char(name, name_chars):
            obj = self.ui.editName
            title = 'Invalid Owner Name'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(name):
            obj = self.ui.editName
            title = 'Invalid Owner Name'
            msg = 'Only single space between to characters is allowed'

            # ###########################  Validating Owner Address ##############################
        elif len(address) < 3:
            obj = self.ui.editAddress
            title = 'Invalid Owner Address'
            msg = 'Minimum 3 characters required'

        elif not valid_char(address, address_chars):
            obj = self.ui.editAddress
            title = 'Invalid Owner Address'
            msg = 'Only Alphabet, space and hyphen are allowed'

        elif not valid_space(address):
            obj = self.ui.editAddress
            title = 'Invalid Owner Address'
            msg = 'Only single space between to characters is allowed'

     # ###########################  Validating Cash Balance ##############################
        elif len(balance) < 1:
            obj = self.ui.editCashBalance
            title = 'Invalid Cash Balance'
            msg = 'Please enter opening cash balance'

        else:
            # ###########################  Validating period ##############################
            result = validPeriod(month_arg=month, year_arg=year)
            if result[0]:
                # if period is valid
                updateOwner(name, address)
                updatePeriod(month, year)
                updateOpeningBalance(self, "Cash", balance)

                self.close()
                return
            else:
                # in case of invalid period
                obj = result[1]
                if obj == "month":
                    obj = self.ui.editMonth
                else:
                    obj = self.ui.editYear

                title = result[2]
                msg = result[3]

        CustomMessage().warn(title, msg, '&Got it')
        self.ui.btnSubmit.setEnabled(False)
        obj.setFocus()
        obj.end(False)
        return

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        event.accept()
