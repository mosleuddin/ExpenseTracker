
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

from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox


class CustomButton(QPushButton):
    """
    This is a class inherited from QPushButton to make a custom button used in loadData()
    function of ShowUsers class in credentials.py file
    """

    def __init__(self):
        super(CustomButton, self).__init__()
        self.setIcon(QIcon("src/icons/reset.png"))
        self.setStyleSheet("background-color:rgb(255, 100, 100)")
        self.user_name = ''


class CustomButtonBalance(QPushButton):
    """
    This is a class inherited from QPushButton to make a custom button used in loadData()
    function of ShowOpeningBalance class in opening_balance.py file
    """

    def __init__(self):
        super(CustomButtonBalance, self).__init__()
        self.setIcon(QIcon("src/icons/edit.png"))
        self.account_number = None


class MsgBox(QMessageBox):
    """
       This is a class inherited from QMessageBox to make 4 types of messages
       used in different parts of the application
    """

    def __init__(self,
                 title='Title',
                 msg='Message',
                 button_0='&Ok',
                 button_1='&Cancel'):
        super(MsgBox, self).__init__()

        self.title = title
        self.msg = f"\n\n\n{msg}\n\n\n"
        self.button0 = button_0
        self.button1 = button_1

        self.setWindowTitle(self.title)
        self.setText(self.msg)

        self.setStyleSheet('background-color: #10141b; color:rgba(255, 255, 255, 0.60)')

        self.acceptButton = QPushButton(icon=QIcon('./src/icons/ok.png'), text=self.button0)
        self.rejectButton = QPushButton(icon=QIcon('./src/icons/cancel.png'), text=self.button1)

        button_style = """
                         QPushButton{
                            background-color: #10141b; 
                            color:rgba(255, 255, 255, 0.60);
                            width: 100px;
                            height: 20px;
                            text-align: center;
                            padding: 5px, 10px;
                            border: 1px solid #264BF6;
                            border-radius: 10px;
                            }
                    
                         QPushButton:hover{
                            background-color: rgba(0, 0, 255, 0.50);
                            }
                      """

        self.acceptButton.setStyleSheet(button_style)
        self.rejectButton.setStyleSheet(button_style)

        self.addButton(self.acceptButton, QMessageBox.AcceptRole)

    def confirm(self):
        self.addButton(self.rejectButton, QMessageBox.RejectRole)
        self.setDefaultButton(self.rejectButton)

        self.setIcon(QMessageBox.Question)
        self.exec()

        if self.clickedButton() == self.acceptButton:
            return True
        else:
            return False

    def info(self):
        self.setIcon(QMessageBox.Information)
        self.exec()

    def warn(self):
        self.setIcon(QMessageBox.Warning)
        self.exec()

    def danger(self):
        self.setIcon(QMessageBox.Critical)
        self.exec()


def custom_font(widget=None, font_size=12, bold=False, underline=False):
    """
        The function makes custom font using the parameters.
        *However the function has not been used by the application.
    """
    font = QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    font.setUnderline(underline)
    widget.setFont(font)


def resize_and_move(self, parent=None, wd=None, ht=None):
    """
    The function helps for resizing and positioning a window
    """
    geometry = QApplication.primaryScreen().availableGeometry()
    screen_wd = geometry.width()
    screen_ht = geometry.height()

    # when resizing and moving to be done with reference to the parent size
    if parent is not None and wd is not None and ht is not None:
        width = int(parent.width() * wd)
        height = int(parent.height() * ht)
        self.setFixedSize(width, height)

    # when resizing to be done with reference to the screen size
    if parent is None and wd is not None and ht is not None:
        width = int(screen_wd * wd)
        height = int(screen_ht * ht)
        self.setFixedSize(width, height)

    # no resizing done only move with reference to the screen size
    else:
        width = self.width()
        height = self.height()

    # move window
    x = int((screen_wd - width) / 2)
    y = int((screen_ht - height) / 3)
    self.move(x, y)


# make widgets read only
def read_only(bg, *args):
    """
    The function makes one or more QLineEdit(s) or QDateEdit(s) readonly
    and also changes the background colors of the widget(s)
    """
    for obj in args:
        obj.setReadOnly(True)
        # obj.setFrame(False)
        obj.setStyleSheet(bg)


# validation
def valid_char(text, allowed_spl_chars=None):
    """
    The function checks whether the text entered in a widget is valid or not
    """
    if allowed_spl_chars is None:
        allowed_spl_chars = [' ']
    if all(char.isalpha() or char in allowed_spl_chars for char in text):
        return True
    else:
        return False


def valid_space(text):
    """
    The function checks whether the space(s) entered by the user is valid or not
    """
    space = 0
    for char in text:
        if char == ' ':
            space = space + 1
            if space > 1:
                return False
        else:
            space = 0
    return True


def showMismatchMessage(parent, title=None, button=None):
    """
    The function shows a message to the users if transaction mismatch found
    """
    message_title = title
    message_button = button

    if message_title is None:
        message_title = "Attention please!!!"

    if message_button is None:
        message_button = "&Ok"

    char = "_"
    width = 55

    horizontal_line = " ".rjust(width, char)

    msg1 = " ".ljust(28, " ") + "For rectification go to....."
    msg1 = msg1 + "\n" + horizontal_line

    msg2 = " ".ljust(28, " ") + "File ---> Period Mismatch"

    msg3 = " ".ljust(28, " ") + "Receipt ---> Edit Receipt"

    msg4 = " ".ljust(28, " ") + "Payment ---> Edit  Payment"

    msg_or = " ".ljust(48, " ") + "OR"

    messages = [msg1, msg2, msg_or, msg3, msg_or, msg4]

    # now configure message
    message = "\nTransaction Date not matching with Transaction Period\n"
    message = message + "\n" + horizontal_line

    for msg in messages:
        message = message + "\n\n" + msg

    message = message + "\n\n" + horizontal_line + "\n\n"

    MsgBox(message_title, message, message_button).warn()
