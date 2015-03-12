from datetime import datetime
from subprocess import call
import os
import random
import glob
import time
import sys
import threading


class PyAlarm(object):
    def hello(self):
        print("Hello!")

cool = PyAlarm()
cool.hello()