from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
#from Ergocycle.source.StartWindow import StartWindow
from StartWindow import StartWindow
from MainWindowStim import MainWindowStim
import sys

def window():
    app = QApplication(sys.argv)
    win = MainWindowStim()
    win = StartWindow()
    win.show()
    sys.exit(app.exec_())
window()