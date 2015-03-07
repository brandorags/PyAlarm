"""
Name: py_alarm_window.py
Author: Brandon Ragsdale
Description: This file generates the main window that
will house the main logic of PyAlarm.
"""

import tkinter
import getpass

from tkinter import Frame
from tkinter import filedialog


class PyAlarmWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("PyAlarm")
        self.master.geometry("{}x{}".format(300, 200))
        self.initialize_window()

    def initialize_window(self):
        self.grid()

        self.entry_variable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entry_variable)
        self.entry.grid(column=0, row=0, sticky="EW")
        self.entry.bind("<Return>", self.on_press_enter)

        button = tkinter.Button(self, text="Find song",
                                command=self.on_button_click)
        button.grid(column=1, row=0)

        # self.label_variable = Tkinter.StringVar()
        # label = Tkinter.Label(self, textvariable=self.label_variable, anchor="w", fg="white", bg="blue")
        # label.grid(column=0, row=2, columnspan=2, sticky="EW")
        # self.label_variable.set(u"Hello!")

        self.grid_columnconfigure(0, weight=1)
        self.update()

    def on_button_click(self):
        self.label_variable.set(self.entry_variable.get() + " (You clicked the button)")

    def on_press_enter(self, event):
        self.label_variable.set(self.entry_variable.get() + " (You pressed ENTER)")

    def return_song_location(self):
        current_user = getpass.getuser()
        song_file = tkinter


if __name__ == "__main__":
    py_alarm_app = PyAlarmWindow()
    py_alarm_app.mainloop()