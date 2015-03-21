# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyAlarm.ui'
#
# Created: Sat Mar 21 01:47:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from py_alarm import PyAlarm
import sys
import getpass

class Ui_PyAlarmWindow(QtGui.QWidget, PyAlarm):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        PyAlarm.__init__(self)
        self.setupUi(self)

    def setupUi(self, PyAlarmWindow):
        PyAlarmWindow.setObjectName('PyAlarmWindow')
        PyAlarmWindow.resize(236, 292)
        self.find_album_button = QtGui.QPushButton(PyAlarmWindow)
        self.find_album_button.setGeometry(QtCore.QRect(5, 102, 91, 31))
        self.find_album_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.find_album_button.setToolTip('')
        self.find_album_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.find_album_button.setObjectName('find_album_button')
        self.hour_spinbox = QtGui.QSpinBox(PyAlarmWindow)
        self.hour_spinbox.setGeometry(QtCore.QRect(20, 26, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.hour_spinbox.setFont(font)
        self.hour_spinbox.setWrapping(True)
        self.hour_spinbox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.hour_spinbox.setMaximum(23)
        self.hour_spinbox.setObjectName('hour_spinbox')
        self.hour_label = QtGui.QLabel(PyAlarmWindow)
        self.hour_label.setGeometry(QtCore.QRect(20, 6, 61, 20))
        self.hour_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label.setObjectName('hour_label')
        self.minute_label = QtGui.QLabel(PyAlarmWindow)
        self.minute_label.setGeometry(QtCore.QRect(140, 6, 61, 20))
        self.minute_label.setAlignment(QtCore.Qt.AlignCenter)
        self.minute_label.setObjectName('minute_label')
        self.minute_spinbox = QtGui.QSpinBox(PyAlarmWindow)
        self.minute_spinbox.setGeometry(QtCore.QRect(140, 26, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.minute_spinbox.setFont(font)
        self.minute_spinbox.setWrapping(True)
        self.minute_spinbox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.minute_spinbox.setMaximum(59)
        self.minute_spinbox.setObjectName('minute_spinbox')
        self.colon_label = QtGui.QLabel(PyAlarmWindow)
        self.colon_label.setGeometry(QtCore.QRect(112, 27, 16, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.colon_label.setFont(font)
        self.colon_label.setObjectName('colon_label')
        self.random_song_label = QtGui.QLabel(PyAlarmWindow)
        self.random_song_label.setGeometry(QtCore.QRect(10, 87, 91, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.random_song_label.setFont(font)
        self.random_song_label.setObjectName('random_song_label')
        self.specific_song_label = QtGui.QLabel(PyAlarmWindow)
        self.specific_song_label.setGeometry(QtCore.QRect(135, 87, 91, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.specific_song_label.setFont(font)
        self.specific_song_label.setObjectName('specific_song_label')
        self.find_song_button = QtGui.QPushButton(PyAlarmWindow)
        self.find_song_button.setGeometry(QtCore.QRect(128, 102, 91, 31))
        self.find_song_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.find_song_button.setObjectName('find_song_button')
        self.random_or_specific_song_display_label = QtGui.QLabel(PyAlarmWindow)
        self.random_or_specific_song_display_label.setGeometry(QtCore.QRect(7, 140, 221, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.random_or_specific_song_display_label.setPalette(palette)
        self.random_or_specific_song_display_label.setText('')
        self.random_or_specific_song_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.random_or_specific_song_display_label.setWordWrap(True)
        self.random_or_specific_song_display_label.setObjectName('random_or_specific_song_display_label')
        self.start_alarm_button = QtGui.QPushButton(PyAlarmWindow)
        self.start_alarm_button.setGeometry(QtCore.QRect(9, 250, 110, 32))
        self.start_alarm_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.start_alarm_button.setCheckable(False)
        self.start_alarm_button.setObjectName('start_alarm_button')
        self.stop_alarm_button = QtGui.QPushButton(PyAlarmWindow)
        self.stop_alarm_button.setGeometry(QtCore.QRect(120, 250, 110, 32))
        self.stop_alarm_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.stop_alarm_button.setObjectName('stop_alarm_button')
        self.alarm_display_label = QtGui.QLabel(PyAlarmWindow)
        self.alarm_display_label.setGeometry(QtCore.QRect(15, 202, 211, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.alarm_display_label.setPalette(palette)
        self.alarm_display_label.setText('')
        self.alarm_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.alarm_display_label.setObjectName('alarm_display_label')

        self.retranslateUi(PyAlarmWindow)
        QtCore.QMetaObject.connectSlotsByName(PyAlarmWindow)

    def retranslateUi(self, PyAlarmWindow):
        PyAlarmWindow.setWindowTitle(QtGui.QApplication.translate('PyAlarmWindow', 'PyAlarm', None, QtGui.QApplication.UnicodeUTF8))
        self.find_album_button.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Find Album', None, QtGui.QApplication.UnicodeUTF8))
        self.hour_label.setText(QtGui.QApplication.translate('PyAlarmWindow', 'HOUR', None, QtGui.QApplication.UnicodeUTF8))
        self.minute_label.setText(QtGui.QApplication.translate('PyAlarmWindow', 'MINUTE', None, QtGui.QApplication.UnicodeUTF8))
        self.colon_label.setText(QtGui.QApplication.translate('PyAlarmWindow', ':', None, QtGui.QApplication.UnicodeUTF8))
        self.random_song_label.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Random Song', None, QtGui.QApplication.UnicodeUTF8))
        self.specific_song_label.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Specific Song', None, QtGui.QApplication.UnicodeUTF8))
        self.find_song_button.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Find Song', None, QtGui.QApplication.UnicodeUTF8))
        self.start_alarm_button.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Start Alarm', None, QtGui.QApplication.UnicodeUTF8))
        self.stop_alarm_button.setText(QtGui.QApplication.translate('PyAlarmWindow', 'Stop Alarm', None, QtGui.QApplication.UnicodeUTF8))

        # on click for find_album_button
        self.find_album_button.clicked.connect(self.retrieve_album_location)

        # on click for find_song_button
        self.find_song_button.clicked.connect(self.retrieve_song_location)

        # on click for start_alarm_button
        self.start_alarm_button.clicked.connect(self.start_alarm)

        # on click for stop_alarm_button
        self.stop_alarm_button.clicked.connect(self.stop_alarm)

    def retrieve_album_location(self):
        current_user = getpass.getuser()
        album_initial_search_location = '/Users/%s/Music/iTunes Media/Music' % current_user

        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        directory = dialog.getExistingDirectory(self, 'Choose Album Folder', album_initial_search_location)

        # send album path to py_alarm which will pick a random song from the passed directory
        album_list = self.create_and_randomize_song_list(directory)

        if album_list:
            split_directory = directory.split('/')
            artist_album = split_directory[len(split_directory) - 2] + ' - ' + \
                split_directory[len(split_directory) - 1]

            self.random_or_specific_song_display_label.setText('A random song will be played from ' + artist_album)
            self.start_alarm_button.setEnabled(True)

    def retrieve_song_location(self):
        current_user = getpass.getuser()
        album_initial_search_location = '/Users/%s/Music/iTunes Media/Music' % current_user

        dialog = QtGui.QFileDialog()
        song_path = dialog.getOpenFileName(self, 'Choose Song', album_initial_search_location)

        if song_path:
            split_song_path = str(song_path[0]).split('/')
            artist_album_song_title = split_song_path[len(split_song_path) - 3] + " - " + \
                split_song_path[len(split_song_path) - 2] + ' - ' + \
                split_song_path[len(split_song_path) - 1]

            self.store_specific_song(song_path)
            self.random_or_specific_song_display_label.setText('The song %s will be played' % artist_album_song_title)
            self.start_alarm_button.setEnabled(True)

    def start_alarm(self):
        self.hour_spinbox.setEnabled(False)
        self.minute_spinbox.setEnabled(False)
        self.find_album_button.setEnabled(False)
        self.find_song_button.setEnabled(False)
        self.start_alarm_button.setEnabled(False)
        self.stop_alarm_button.setEnabled(True)

        hour_value = self.hour_spinbox.value()
        minute_value = self.minute_spinbox.value()
        clock_in_twelve_hour_format = self.display_clock_in_twelve_hour_format(hour_value, minute_value)
        self.alarm_display_label.setText('The alarm will go off at %s' % clock_in_twelve_hour_format)
        self.play_song_at_specified_time(hour_value, minute_value)

    def stop_alarm(self):
        self.random_or_specific_song_display_label.setText('')
        self.alarm_display_label.setText('')
        self.hour_spinbox.setEnabled(True)
        self.minute_spinbox.setEnabled(True)
        self.find_album_button.setEnabled(True)
        self.find_song_button.setEnabled(True)
        self.stop_alarm_button.setEnabled(False)
        self.stop_song()

    def display_clock_in_twelve_hour_format(self, hour, minute):
        am_pm_setting = None
        hour = int(hour)
        minute = int(minute)

        # modify hour field to 12 hour format
        if hour < 12:
            if hour == 0:
                hour = 12
            am_pm_setting = 'AM'
        else:
            if hour != 12:
                hour -= 12
            am_pm_setting = 'PM'

        # add a leading zero for single digit numbers
        if minute < 10:
            minute = str(minute)
            minute = '0' + minute

        easy_to_read_format = str(hour) + ':' + str(minute) + ' ' + am_pm_setting
        return easy_to_read_format

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_PyAlarmWindow()
    ex.show()
    sys.exit(app.exec_())
