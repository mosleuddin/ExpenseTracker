from PySide6.QtGui import QFont, QIcon
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QApplication, QPushButton


class CustomButton(QPushButton):
    def __init__(self):
        super(CustomButton, self).__init__()
        self.setIcon(QIcon("src/icons/reset.png"))
        self.setStyleSheet("background-color:rgb(255, 100, 100)")
        self.user_name = ''


# set custom font
def custom_font(widget=None, font_size=12, bold=False, underline=False):
    font = QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    font.setUnderline(underline)
    widget.setFont(font)


# set window size and position
def resize_and_move(self, parent=None, wd=None, ht=None):
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
    for obj in args:
        obj.setReadOnly(True)
        # obj.setFrame(False)
        obj.setStyleSheet(bg)


# validation
def valid_char(text, allowed_spl_chars=None):
    if allowed_spl_chars is None:
        allowed_spl_chars = [' ']
    if all(char.isalpha() or char in allowed_spl_chars for char in text):
        return True
    else:
        return False


def valid_space(text):
    space = 0
    for char in text:
        if char == ' ':
            space = space + 1
            if space > 1:
                return False
        else:
            space = 0
    return True

