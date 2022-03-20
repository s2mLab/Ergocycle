# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:40:36 2022

@author: Nicolas Pelletier-Côté
"""

# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.QtGui import QFont, QPixmap
# import time
# import sys

# from MainWindowMotor import MainWindowMotor
# from ActivityMenu import ActivityMenu
# from ErrorMenu import ErrorMenu
# from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class MotorParameters():
    def __init__(self):
        super(MotorParameters, self).__init__()
        
        self.training_type = "Concentrique"
        self.speed = 0
        self.training_length = 0
        
    def get_training_type(self):
        return self.training_type
    
    def set_training_type(self, combo_box):
        self.training_type = combo_box.currentText()
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, combo_box):
        self.speed = int(combo_box.currentText())
        
    def get_training_length(self):
        return self.training_length    
    
    def set_training_length(self, combo_box):
        self.training_length = int(combo_box.currentText())