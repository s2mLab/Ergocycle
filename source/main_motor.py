# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import sys

from MainWindowMotor import MainWindowMotor
from MotorParameters import MotorParameters

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120


def window():
    app = QApplication([])  # sys.argv
    motor_param = MotorParameters()
    win = MainWindowMotor(motor_param)
    win.show()
    sys.exit(app.exec_())


window()
