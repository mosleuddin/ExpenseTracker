from PySide6.QtGui import QFont, QIcon
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QApplication, QPushButton


class CustomButton(QPushButton):
    def __init__(self):
        super(CustomButton, self).__init__()
        self.setIcon(QIcon("src/icons/reset.png"))
        self.setStyleSheet("background-color:rgb(255, 100, 100)")
        self.user_name = ''


# set window size and position
def resizeMove(self, parent=None, wd=None, ht=None):
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


# set font
def custom_font(widget=None, font_size=12, bold=False, underline=False):
    font = QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    font.setUnderline(underline)
    widget.setFont(font)


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


def min_length(length, min_len):
    if length >= min_len:
        return True
    else:
        return False


def is_unique(tbl, search_field, display_field, pk_field,
              search_field_value, pk_field_value=None):
    """
    This function will check a value entered by the user in a field of a
    table to ensure whether it's value is unique in the table or not

    :param tbl: The name of the table to which the field belongs

    :param search_field: The name of the field which value to be checked

    :param display_field: The value of this field will be shown to the user
     as a reference of the duplicate record found, if any

    :param pk_field: The name of the Primary Key field of the table

    :param search_field_value: The current value of the search field. It is to be
    ensured this value dies not exist in the table.

    :param pk_field_value: The current value of the Primary Key. The record holding
    this value will not be considered to check.

    :return:  returns a tuple of two element

             First element  -->  True or False

             Second element -->  If duplicate found:
                                    value of display_field of the record which holds the duplicate value
                                 else:
                                    an empty string
    """

    result = (True, '')
    query = QSqlQuery()
    if pk_field_value is None:
        # while inserting record to the table
        query.prepare(f"SELECT {pk_field}, {display_field}, {search_field} FROM {tbl}")

    else:
        # while updating an existing record in the table
        query.prepare(f"""SELECT {pk_field}, {display_field}, {search_field} FROM {tbl}
                          WHERE  {pk_field} != :current_rec_pk_field_value
                      """)
        query.bindValue(":current_rec_pk_field_value", pk_field_value)

    query.exec()

    while query.next():
        display_value = query.value(1)
        search_value = query.value(2)
        if search_value == search_field_value:
            result = (False, display_value)
            return result
    return result
