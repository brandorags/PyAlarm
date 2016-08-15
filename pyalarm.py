"""
PyAlarm: An alarm clock written in Python
Copyright (C) 2016 Brandon Ragsdale

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
from subprocess import call, check_output
from pathlib import Path
import os
import random
import time
import sys
import threading


"""
CONSOLE ARGUMENT CHECKING SECTION
"""
# display help message if no alarm time and artist was given
# or if user inputs the help parameter
if len(sys.argv) < 4:
    print("Usage: alarm [hour] [minute] [artist name] [album name (optional)]")
    exit()
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Usage: alarm [hour] [minute] [artist name] [album name (optional)]")
    exit()


"""
ALBUM DIRECTORY PATH SETUP
"""
# retrieve current user's username
current_username = str(check_output("whoami"))

# retrieve args
# if user didn't specify
# an album, continue with just
# artist name in except block
user_selected_artist = sys.argv[3]

try:
    album = sys.argv[4]

    # set up path to selected artist
    path_to_artist = "/Users/Brando/Music/iTunes/iTunes Media/Music/" + user_selected_artist + "/" + \
                     album + "/"
except:
    # set up path to selected artist
    path_to_artist = "/Users/Brando/Music/iTunes/iTunes Media/Music/" + user_selected_artist + "/"


"""
SONG GENERATION FUNCTIONS
"""
def generate_song_list():
    # generate list of songs from user selected artist
    song_list = []

    for song in Path(path_to_artist).glob("**/*.m4a"):
        song_list.append(song)

    return song_list


def generate_random_song(song_list):
    return random.randint(0, len(song_list) - 1)


"""
SONG PLAYING SECTION
"""
def set_volume():
    """
    set_volume()
    changes the volume of the current track
    """
    current_volume = 1
    while current_volume <= 10:
        os.system("osascript -e 'set Volume " + str(current_volume) + "'")
        current_volume += 0.2
        time.sleep(5)


def play_song():
    print("Good morning! It's time to wake up!")
    print(str(wake_up_song_list[random_song]))
    call(["afplay", str(wake_up_song_list[random_song])])


def play_default_beep_if_song_has_mistake():
    default_beep_tones = []
    for beep in Path("/System/Library/Sounds").glob("**/*.aiff"):
        default_beep_tones.append(beep)

    random_beep = random.randint(0, len(default_beep_tones) - 1)

    print("Good morning! It's time to wake up!")

    time.sleep(5)

    beeps = 1000
    for i in range(0, beeps):
        # TODO for now, play specific beep that's loud enough to wake someone up
        # call(["afplay", str(default_beep_tones[random_beep])])
        call(["afplay", "/System/Library/Sounds/Glass.aiff"])

"""
MAIN LOOP SECTION
"""
def main_loop():
    keep_going = True
    while keep_going:
        now = datetime.now()

        try:
            if now.hour == int(sys.argv[1]) and now.minute == int(sys.argv[2]):
                # create thread that will increase the volume while the track is playing
                volume_level = threading.Timer(0.5, set_volume)
                volume_level.daemon = True
                volume_level.start()

                # play the song!
                play_song()
                keep_going = False
        except:
            # create thread that will increase the volume while the track is playing
            volume_level = threading.Timer(0.5, set_volume)
            volume_level.daemon = True
            volume_level.start()

            # play the beep!
            play_default_beep_if_song_has_mistake()
            keep_going = False

        time.sleep(25)


try:
    wake_up_song_list = generate_song_list()
    random_song = generate_random_song(wake_up_song_list)
except:
    print("Cant find artist or album!")
    exit()

# set the system volume to 1
os.system("osascript -e 'set Volume 1'")

# start the main loop that waits for the specified time for the alarm to go off
main_loop()

# reset the system volume to 1
os.system("osascript -e 'set Volume 1'")
