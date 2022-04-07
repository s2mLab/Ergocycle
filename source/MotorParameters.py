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

# from Observable import Observable

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class MotorParameters():
    def __init__(self):
        super(MotorParameters, self).__init__()
        
        self.training_type = "Concentrique"
        self.current_speed = 0
        self.training_length = 0
        self.target_speed = 0
        self.distance = 0
        
    def get_training_type(self):
        return self.training_type
    
    def set_training_type(self, combo_box):
        self.training_type = combo_box.currentText()
    
    def get_current_speed(self):
        return self.current_speed
    
    def get_target_speed(self):
        return self.target_speed
    
    def set_target_speed(self, combo_box):
        self.target_speed = int(combo_box.currentText())
        
    def get_training_length(self):
        return self.training_length    
    
    def set_training_length(self, combo_box):
        self.training_length = int(combo_box.currentText())
        
    def increase_target_speed(self):
        self.target_speed += 1
        
    def decrease_target_speed(self):
        self.target_speed -= 1
    
    def increase_training_length(self):
        if(self.training_length < MAX_TRAINING_LENGTH):
            self.training_length += 1
    
    def decrease_training_length(self):
        if(self.training_length > MIN_TRAINING_LENGTH):
            self.training_length -= 1
    
    def get_distance(self):
        return self.distance