# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyAlarm.ui'
#
# Created: Wed Mar 11 11:54:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys
import getpass

from PySide import QtCore, QtGui
from py_alarm import PyAlarm


class Ui_PyAlarmWindow(QtGui.QWidget, PyAlarm):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        PyAlarm.__init__(self)
        self.setupUi(self)

    def setupUi(self, PyAlarmWindow):
        PyAlarmWindow.setObjectName("PyAlarmWindow")
        PyAlarmWindow.resize(320, 240)
        self.pushButton = QtGui.QPushButton(PyAlarmWindow)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.py_alarm_label = QtGui.QLabel(PyAlarmWindow)
        self.py_alarm_label.setGeometry(QtCore.QRect(25, 13, 261, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.py_alarm_label.sizePolicy().hasHeightForWidth())
        self.py_alarm_label.setSizePolicy(sizePolicy)
        self.py_alarm_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(64, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.py_alarm_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(50)
        font.setBold(False)
        self.py_alarm_label.setFont(font)
        self.py_alarm_label.setTextFormat(QtCore.Qt.AutoText)
        self.py_alarm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.py_alarm_label.setObjectName("py_alarm_label")

        self.retranslateUi(PyAlarmWindow)
        QtCore.QMetaObject.connectSlotsByName(PyAlarmWindow)

    def retranslateUi(self, PyAlarmWindow):
        PyAlarmWindow.setWindowTitle(QtGui.QApplication.translate("PyAlarmWindow", "PyAlarm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PyAlarmWindow", "Find Song/Album", None, QtGui.QApplication.UnicodeUTF8))
        self.py_alarm_label.setText(QtGui.QApplication.translate("PyAlarmWindow", "Welcome to PyAlarm!", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton.clicked.connect(self.retrieve_album_location)

    def retrieve_album_location(self):
        current_user = getpass.getuser()
        album_initial_search_location = "/Users/%s/Music/iTunes Media/Music" % current_user

        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        directory = dialog.getExistingDirectory(self, "Choose Album Folder", album_initial_search_location)

        self.create_and_randomize_song_list(directory)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_PyAlarmWindow()
    ex.show()
    sys.exit(app.exec_())
