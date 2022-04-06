# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:50:57 2022

@author: Nicolas Pelletier-Côté
"""

# Test de l'interface usager du moteur

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

def test_window():
    app = QApplication([]) #sys.argv
    motor_param = MotorParameters()
    win = MainWindowMotor(motor_param)
    win.show()
    sys.exit(app.exec_())
    
test_window()
