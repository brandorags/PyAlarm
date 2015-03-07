"""
Name: py_alarm_window.py
Author: Brandon Ragsdale
Description: This file generates the main window that
will house the main logic of PyAlarm.
"""


import Tkinter


class PyAlarmWindow(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize_window()

    def initialize_window(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, row=0, sticky='EW')


if __name__ == "__main__":
    py_alarm_app = PyAlarmWindow(None)
    py_alarm_app.title("PyAlarm")
    py_alarm_app.mainloop()
