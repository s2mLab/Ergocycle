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

MIN_TARGET_POWER = 0
MAX_TARGET_POWER = 100

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class MotorParameters():
    def __init__(self):
        super(MotorParameters, self).__init__()
        
        self.training_type = "Concentrique"
        self.current_power = 0
        self.target_power = 0
        self.training_length = 0
        self.distance = 0
        self.time = 0
        
    def get_training_type(self):
        return self.training_type
    
    def set_training_type(self, combo_box):
        self.training_type = combo_box.currentText()
    
    def get_current_power(self):
        return self.current_power
    # TODO: Ajouter la commande pour aller chercher les mesures de puissance
    
    def get_target_power(self):
        return self.target_power
    
    def set_target_power(self, combo_box):
        self.target_power = int(combo_box.currentText())
        
    def get_training_length(self):
        return self.training_length    
    
    def set_training_length(self, combo_box):
        self.training_length = int(combo_box.currentText())
        
    def increase_target_power(self):
        if(self.target_power < MAX_TARGET_POWER):
            self.target_power += 1
        
    def decrease_target_power(self):
        if(self.target_power > MIN_TARGET_POWER):
            self.target_power -= 1
    
    def increase_training_length(self):
        if(self.training_length < MAX_TRAINING_LENGTH):
            self.training_length += 1
    
    def decrease_training_length(self):
        if(self.training_length > MIN_TRAINING_LENGTH):
            self.training_length -= 1
    
    def get_distance(self):
        return self.distance
    
    def get_time(self):
        return self.time