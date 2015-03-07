from datetime import datetime
from subprocess import call
import os
import random
import glob
import time
import sys
import threading

wake_up_song_list = glob.glob("../*.m4a")
random_song = random.randint(0, len(wake_up_song_list) - 1)


def set_volume():
    """
    set_volume()
    changes the volume of the current track
    """
    current_volume = 1
    while current_volume <= 10:
        os.system("sudo osascript -e 'set Volume " + str(current_volume) + "'")
        current_volume += 0.5
        time.sleep(5)


def play_song():
    print("Good morning! It's time to wake up!")
    call(["afplay", wake_up_song_list[random_song]])


def play_default_song_if_argv_has_mistake():
    print("You gotta put in the time you want the alarm to go off! But I'll play a song for you anyways. :)")
    call(["afplay",
          "SomeSong.m4a"])


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
            # play the song!
            play_default_song_if_argv_has_mistake()
            keep_going = False

        time.sleep(25)


# set the system volume to 1
os.system("sudo osascript -e 'set Volume 1'")

# start the main loop that waits for the specified time for the alarm to go off
main_loop()

# reset the system volume to 1
os.system("sudo osascript -e 'set Volume 1'")
