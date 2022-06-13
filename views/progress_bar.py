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
from PySide6.QtCore import QObject, QThread, Signal, Slot, Qt
from PySide6.QtWidgets import QProgressBar

from modules.module import MsgBox, resize_and_move


class Worker(QObject):
    signal_progress = Signal(int)
    signal_finished = Signal()

    @Slot()
    def progress_counter(self):
        for i in range(101):
            time.sleep(.05)
            self.signal_progress.emit(i)

        self.signal_finished.emit()


class MidMonthProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super(MidMonthProgressBar, self).__init__(parent)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint)
        resize_and_move(self, parent=self.parent, wd=.40, ht=.1)
        self.setStyleSheet("background-color: LightBlue; color: White")

        self.obj = Worker()
        self.thread = QThread()
        self.obj.signal_progress.connect(self.on_value_changed)
        self.obj.moveToThread(self.thread)

        self.obj.signal_finished.connect(self.thread.quit)
        self.obj.signal_finished.connect(self.close_progress_bar)
        self.thread.started.connect(self.obj.progress_counter)

    def on_value_changed(self, value):
        """
        This function will be called as and when the signal_progress is connected
        """
        self.setValue(value)

    def start_progress(self):
        """
        This function will be called from the parent window to show the progress bar
        """
        self.show()
        self.thread.start()

    def close_progress_bar(self, error=False):
        """
        This function will close the progress screen
        """
        self.close()
        title = "Data saved successfully at the following location"
        msg = self.parent.file_path
        MsgBox(title=title,
               msg=f"\n{msg}",
               button_0="&Ok").info()


class MonthEndProgressBar(MidMonthProgressBar):
    def __init__(self, parent=None):
        super(MidMonthProgressBar, self).__init__(parent)
        self.parent = parent
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(150, 150, 500, 60)
        # self.setStyleSheet("background-color: LightGreen")

        self.obj = Worker()
        self.thread = QThread()
        self.obj.signal_progress.connect(self.on_value_changed)
        self.obj.moveToThread(self.thread)

        self.obj.signal_finished.connect(self.thread.quit)
        self.obj.signal_finished.connect(self.close_progress_bar)
        self.thread.started.connect(self.obj.progress_counter)

    def close_progress_bar(self):
        """
        This function will close the progress screen
        """
        self.close()
        msg = self.parent.file_path
        MsgBox(title="Data saved successfully",
               msg=f"\n{msg}",
               button_0="&Ok").info()
        self.parent.close()
