"""
Name: py_alarm_window.py
Author: Brandon Ragsdale
Description: This file generates the main window that
will house the main logic of PyAlarm.
"""

import tkinter as tk
import getpass

from tkinter import Frame
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror


class PyAlarmWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("PyAlarm")
        self.master.geometry("{}x{}".format(500, 400))
        self.initialize_window()

    def initialize_window(self):
        self.grid()

        # song/album directory location settings
        find_song_button = tk.Button(self, text="Find Song",
                                     command=self.return_song_location)
        find_song_button.grid(column=0, row=0, sticky="EW")

        self.song_path = tk.StringVar()
        self.song_path_textbox = tk.Entry(self, width=30, textvariable=self.song_path)
        self.song_path_textbox.grid(column=1, row=0, sticky="EW")
        self.song_path_textbox.bind("<Return>", self.song_path_textbox_on_press_enter)

        # hour settings
        self.hour_label = tk.StringVar()
        hour_label = tk.Label(self, text="Hour:", anchor="w")
        hour_label.grid(column=0, row=1, sticky="EW")

        hour_spinbox = tk.Spinbox(self, from_=0, to=24, width=3, wrap=True)
        hour_spinbox.grid(column=0, row=1, sticky="E")

        # minute settings
        self.minute_label = tk.StringVar()
        minute_label = tk.Label(self, text="Minute:", anchor="w")
        minute_label.grid(column=1, row=1, sticky="EW")

        minute_spinbox_list = tk.Spinbox(self, from_=00, to=59, width=3, wrap=True)
        minute_spinbox_list.grid(column=1, row=1, sticky="N")

        # set alarm button settings
        set_alarm_button = tk.Button(self, text="Set Alarm",
                                     command=self.return_song_location)
        set_alarm_button.grid(column=1, row=1, sticky="E")

        self.grid_columnconfigure(0, weight=1)
        self.update()

    # def on_button_click(self):
    #     self.label_variable.set(self.entry_variable.get() + " (You clicked the button)")
    #
    def song_path_textbox_on_press_enter(self, event):
        self.return_song_location()

    def return_song_location(self):
        current_user = getpass.getuser()
        song_file = askopenfile(mode='r', initialdir="/Users/%s/Music" % current_user)

        if song_file:
            try:
                self.song_path.set(song_file.name)
            except:
                showerror("Find Song", "Could not find the song\n %s" % song_file.name)


if __name__ == "__main__":
    py_alarm_app = PyAlarmWindow()
    py_alarm_app.mainloop()