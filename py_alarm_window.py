"""
Name: py_alarm_window.py
Author: Brandon Ragsdale
Description: This file generates the main window that
will house the main logic of PyAlarm.
"""


import tkinter


class PyAlarmWindow(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize_window()

    def initialize_window(self):
        pass


if __name__ == "__main__":
    py_alarm_app = PyAlarmWindow(None)
    py_alarm_app.title("PyAlarm")
    py_alarm_app.mainloop()
