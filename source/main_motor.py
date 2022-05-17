# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.QtGui import QFont, QPixmap
# import time
import sys

from MainWindowMotor import MainWindowMotor
from MotorParameters import MotorParameters
# from ActivityMenu import ActivityMenu
# from ErrorMenu import ErrorMenu
# from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

def window():
    app = QApplication([]) #sys.argv
    motor_param = MotorParameters()
    win = MainWindowMotor(motor_param)
    win.show()
    sys.exit(app.exec_())
    
window()