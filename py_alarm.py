from datetime import datetime
from subprocess import Popen, call
import multiprocessing
import os
import random
import glob
import time
import sys
import threading
import getpass

# this subprocess will play the alarm sound/song
song_subprocess = None

class PyAlarm(object):
    """
    album_list, random_song -> used for playing a random song
    in a selected album
    specific_song -> used for playing a specific selected song
    """
    album_list = None
    random_song = None
    specific_song = None

    def create_and_randomize_song_list(self, user_selected_directory):
        if user_selected_directory:
            song_types = (user_selected_directory + "/*.mp3", user_selected_directory + "/*.m4a")
            songs_from_user_selected_directory = []

            for songs in song_types:
                songs_from_user_selected_directory.extend(glob.glob(songs))

            if not songs_from_user_selected_directory:
                call(["cd", user_selected_directory])
                songs_from_user_selected_directory.extend(glob.glob(user_selected_directory))

            # set class variables
            self.album_list = songs_from_user_selected_directory
            self.random_song = random.randint(0, len(self.album_list) - 1)
            self.specific_song = None

            # return string of random album name for label on PyAlarm window
            return user_selected_directory

    def store_specific_song(self, user_selected_song):
        self.specific_song = user_selected_song
        self.album_list = None
        self.random_song = None

    def play_song(self):
        global song_subprocess
        if self.album_list and self.random_song:
            song_subprocess = Popen(["afplay", self.album_list[self.random_song]])
        elif self.specific_song:
            song_subprocess = Popen(["afplay", str(self.specific_song[0])])

    def stop_song(self):
        global song_subprocess
        song_subprocess.terminate()
