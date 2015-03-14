from datetime import datetime
import subprocess
from subprocess import Popen, call
import multiprocessing
import os
import random
import glob
import time
import sys
import threading
import getpass

test = None

class PyAlarm(object):
    """
    album_list, random_song -> used for playing a random song
    in a selected album
    specific_song -> used for playing a specific selected song
    """
    album_list = None
    random_song = None
    specific_song = None
    play_specific_song_process = multiprocessing.Process()

    def create_and_randomize_song_list(self, user_selected_directory):
        if user_selected_directory:
            song_types = (user_selected_directory + "/*.mp3", user_selected_directory + "/*.m4a")
            songs_from_user_selected_directory = []

            for songs in song_types:
                songs_from_user_selected_directory.extend(glob.glob(songs))

            # set class variables
            self.album_list = songs_from_user_selected_directory
            self.random_song = random.randint(0, len(self.album_list) - 1)
            self.play_specific_song_process = multiprocessing.Process(target=self.play_song)
            self.specific_song = None

            # return string of random album name for label on PyAlarm window
            return user_selected_directory

    def store_specific_song(self, user_selected_song):
        self.specific_song = user_selected_song
        # self.play_specific_song_process = multiprocessing.Process(target=self.play_song)
        self.album_list = None
        self.random_song = None
        self.play_song()

    def play_song(self):
        global test
        if self.album_list and self.random_song:
            call(["afplay", self.album_list[self.random_song]])
        elif self.specific_song:
            test = Popen(["afplay", str(self.specific_song[0])])

    def start_separate_process_to_play_song(self):
        self.play_specific_song_process.start()

    def stop_separate_process_to_play_song(self):
        # pid_of_song_process = self.play_specific_song_process.pid + 1
        # self.play_specific_song_process.terminate()
        test.terminate()
        # call(["kill", str(pid_of_song_process)])
