# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:41:45 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
from constants import *
# import time
# import sys

# from MainWindowMotor import MainWindowMotor
# from MotorParameters import MotorParameters
# from ActivityMenu import ActivityMenu
# from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class ErrorMenu(QWidget):
    def __init__(self):
        super(ErrorMenu, self).__init__()
        
        self.setGeometry(700, 400, SCREEN_WIDTH/4, SCREEN_HEIGHT/3)
        self.setWindowTitle("Erreur")
        self.setStyleSheet("background-color: white;")
        
        self.button_dictionary = {}
        
        self.initUI()

    def initUI(self):        
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('s2m_logo_resized.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Erreur")
        self.menu_label.move(220,40)
        self.menu_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        
        # while(self.check_error_status == 1):
        #     print("")
        # self.close()
            
        
    def check_error_status(self):
        print("Checking error status...")