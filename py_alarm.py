from datetime import datetime
from subprocess import call
import os
import random
import glob
import time
import sys
import threading
import getpass


class PyAlarm(object):
    album_list = None
    random_song = None

    def create_and_randomize_song_list(self, user_selected_directory):
        if user_selected_directory:
            song_types = (user_selected_directory + "/*.mp3", user_selected_directory + "/*.m4a")
            songs_from_user_selected_directory = []

            for songs in song_types:
                songs_from_user_selected_directory.extend(glob.glob(songs))

            # set class variables
            self.album_list = songs_from_user_selected_directory
            self.random_song = random.randint(0, len(self.album_list) - 1)

            # return string of random album name for label on PyAlarm window
            return user_selected_directory


