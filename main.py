import sys

from PySide6.QtWidgets import QApplication
from views.login import Login


def main():
    app = QApplication(sys.argv)
    win = Login()
    app.exec()
    sys.exit()


if __name__ == "__main__":
    main()
