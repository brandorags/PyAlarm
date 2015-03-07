"""
Name: py_alarm_window.py
Author: Brandon Ragsdale
Description: This file generates the main window that
will house the main logic of PyAlarm.
"""

import tkinter
import getpass
import py_alarm as PyAlarm

from tkinter import Frame
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror


class PyAlarmWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("PyAlarm")
        self.master.geometry("{}x{}".format(300, 200))
        self.initialize_window()

    def initialize_window(self):
        self.grid()

        self.song_path = tkinter.StringVar()
        self.song_path_textbox = tkinter.Entry(self, textvariable=self.song_path)
        self.song_path_textbox.grid(column=0, row=0, sticky="EW")
        self.song_path_textbox.bind("<Return>", self.on_press_enter)

        find_song_button = tkinter.Button(self, text="Find song",
                                          command=self.return_song_location)
        find_song_button.grid(column=1, row=0)

        # self.label_variable = Tkinter.StringVar()
        # label = Tkinter.Label(self, textvariable=self.label_variable, anchor="w", fg="white", bg="blue")
        # label.grid(column=0, row=2, columnspan=2, sticky="EW")
        # self.label_variable.set(u"Hello!")

        self.grid_columnconfigure(0, weight=1)
        self.update()

    # def on_button_click(self):
    #     self.label_variable.set(self.entry_variable.get() + " (You clicked the button)")
    #
    # def on_press_enter(self, event):
    #     self.label_variable.set(self.entry_variable.get() + " (You pressed ENTER)")

    def return_song_location(self):
        current_user = getpass.getuser()
        song_file = askopenfile(mode='r', initialdir="/Users/%s/Music" % current_user)

        if song_file:
            try:
                self.entry_variable.set(song_file.name)
            except:
                showerror("Find Song", "Could not find the song\n %s" % song_file.name)


if __name__ == "__main__":
    py_alarm_app = PyAlarmWindow()
    py_alarm_app.mainloop()