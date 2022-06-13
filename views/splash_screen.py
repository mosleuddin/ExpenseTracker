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

import time

from PySide6.QtCore import QObject, Signal, Slot, Qt, QThread
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen
from design.ui_splash import Ui_SplashScreen
from views.login import Login


class Worker(QObject):
    signal_progress = Signal(int)
    signal_finished = Signal()

    @Slot()
    def progress_counter(self):
        for i in range(101):
            time.sleep(.05)
            self.signal_progress.emit(i)

        self.signal_finished.emit()


class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.dlg = None
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        pixmap = QPixmap("src/icons/flash.jpg")

        self.setPixmap(pixmap)
        self.showMessage("Loading window. Please wait ......",
                         Qt.AlignVCenter| Qt.AlignCenter,
                         Qt.blue)

        self.ui.progressBar.setTextVisible(0)

        self.obj = Worker()
        self.thread = QThread()
        self.obj.signal_progress.connect(self.on_value_changed)
        self.obj.moveToThread(self.thread)

        self.obj.signal_finished.connect(self.thread.quit)
        self.obj.signal_finished.connect(self.close_splash_window)
        self.thread.started.connect(self.obj.progress_counter)

    def on_value_changed(self, value):
        """
        This function will be called as and when the signal_progress is connected
        """
        self.ui.progressBar.setValue(value)

    def start_progress(self):
        """
        This function will be called from main to open Login window and show flash screen
        """
        self.thread.start()
        self.show()
        self.dlg = Login()

    def close_splash_window(self):
        self.close()

        self.dlg.show()
