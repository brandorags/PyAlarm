"""
PyAlarm: An alarm clock written in Python
Copyright (C) 2015 Brandon Ragsdale

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from datetime import datetime
from subprocess import Popen, call
import os
import random
import glob
import time
import threading

song_subprocess = None  # this subprocess will play the alarm sound/song
hour_minute_checker = None
volume_level = None


class PyAlarm(object):
    """
    album_list, random_song -> used for playing a random song
      in a selected album
    specific_song -> used for playing a specific selected song
    stop_volume_increase -> used to stop set_volume from increasing
      the volume in the background after the user has already turned
      off the alarm
    """
    album_list = None
    random_song = None
    specific_song = None
    stop_volume_increase = False

    def create_and_randomize_song_list(self, user_selected_directory):
        if user_selected_directory:
            song_types = (user_selected_directory + '/*.mp3',
                          user_selected_directory + '/*.m4a',
                          user_selected_directory + '/*.m4p',
                          user_selected_directory + '/*.aiff',
                          user_selected_directory + '/*.flac',
                          user_selected_directory + '/*.ogg',
                          user_selected_directory + '/*.wav')

            songs_from_user_selected_directory = []

            for songs in song_types:
                songs_from_user_selected_directory.extend(glob.glob(songs))

            if not songs_from_user_selected_directory:
                call(['cd', user_selected_directory])
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

    def check_for_hour_and_minute(self, hour, minute):
        global song_subprocess
        keep_going = True
        self.stop_volume_increase = False

        while keep_going:
            global volume_level
            now = datetime.now()

            if hour == now.hour and minute == now.minute:
                if self.album_list and self.random_song:
                    volume_level = threading.Timer(0.5, self.set_volume)
                    volume_level.daemon = True
                    volume_level.start()

                    song_subprocess = Popen(['afplay', self.album_list[self.random_song]])
                    keep_going = False
                elif self.specific_song:
                    volume_level = threading.Timer(0.5, self.set_volume)
                    volume_level.daemon = True
                    volume_level.start()

                    song_subprocess = Popen(['afplay', str(self.specific_song[0])])
                    keep_going = False

            time.sleep(25)

    def play_song_at_specified_time(self, hour, minute):
        global hour_minute_checker

        hour_minute_checker = threading.Timer(0.5, self.check_for_hour_and_minute,
                                              args=(hour, minute))
        hour_minute_checker.daemon = True
        hour_minute_checker.start()

    def stop_song(self):
        global song_subprocess
        global hour_minute_checker
        global volume_level

        if song_subprocess:
            song_subprocess.terminate()

        if hour_minute_checker.is_alive():
            hour_minute_checker.cancel()

        try:
            if volume_level.is_alive():
                volume_level.cancel()
                os.system("osascript -e 'set Volume 0'")
                self.stop_volume_increase = True
        except:
            os.system("osascript -e 'set Volume 0'")

    def set_volume(self):
        current_volume = 1
        while current_volume <= 10 and self.stop_volume_increase is False:
            os.system("osascript -e 'set Volume " + str(current_volume) + "'")
            current_volume += 0.5
            time.sleep(5)
