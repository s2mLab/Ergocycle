"""
Created on Wed Feb 16 09:10:00 2022

@author: Frédérique Leclerc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
from MainWindowStim import MainWindowStim
import sys

def window():
    app = QApplication(sys.argv)
    win = MainWindowStim()
    win.show()
    sys.exit(app.exec_())
window()