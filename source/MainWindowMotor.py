# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:39:36 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
# import time
# import sys

from MotorParameters import MotorParameters
from ActivityMenu import ActivityMenu
# from ErrorMenu import ErrorMenu
# from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

# Fenêtre principale qui crée le menu principal pour le contrôle du moteur

class MainWindowMotor(QMainWindow):
    def __init__(self):
        super(MainWindowMotor, self).__init__()
        self.setGeometry(700, 400, SCREEN_WIDTH/4, SCREEN_HEIGTH/3)
        self.setWindowTitle("Menu Principal")
        self.setStyleSheet("background-color: white;")
        
        init_parameters = MotorParameters()
        # self.training_type = "Concentrique"
        # self.speed = "0"
        # self.training_length = "0"
        
        self.initUI(init_parameters)
    
    def initUI(self, init_parameters):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('s2m_logo_resized.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Menu Principal")
        self.menu_label.move(175,40)
        self.menu_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.training_type_label = QtWidgets.QLabel(self)
        self.training_type_label.setText("Type d'entraînement")
        self.training_type_label.move(100,100)
        self.training_type_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.training_type_label.adjustSize()
        
        self.training_type_ComboBox = QtWidgets.QComboBox(self)
        self.training_type_ComboBox.addItems(["Concentrique", "Excentrique", "Passif"])
        self.training_type_ComboBox.move(300,100)
        self.training_type_ComboBox.setFont(QFont('Arial', 12))
        self.training_type_ComboBox.adjustSize()
        
        self.speed_label = QtWidgets.QLabel(self)
        self.speed_label.setText("Vitesse/Puissance cible")
        self.speed_label.move(100,150)
        self.speed_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.speed_label.adjustSize()
        
        self.speed_ComboBox = QtWidgets.QComboBox(self)
        self.speed_ComboBox.addItems(["25", "50", "75", "100"])
        self.speed_ComboBox.move(300,150)
        self.speed_ComboBox.setFont(QFont('Arial', 12))
        self.speed_ComboBox.adjustSize()
        
        self.training_length_label = QtWidgets.QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement")
        self.training_length_label.move(100,200)
        self.training_length_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        
        self.training_length_ComboBox = QtWidgets.QComboBox(self)
        self.training_length_ComboBox.addItems(["5", "10", "15", "20", "25", "30"])
        self.training_length_ComboBox.move(300,200)
        self.training_length_ComboBox.setFont(QFont('Arial', 12))
        self.training_length_ComboBox.adjustSize()
        
        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("  Débuter  ")
        self.submit_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_button.move(200, 260)
        self.submit_button.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.submit_button.adjustSize()
        self.submit_button.clicked.connect(lambda:self.submit_clicked(init_parameters))
    
    # def get_training_type(self):
    #     return self.training_type
    
    # def set_training_type(self, combo_box):
    #     self.training_type = combo_box.currentText()
    
    # def get_speed(self):
    #     return self.speed
    
    # def set_speed(self, combo_box):
    #     self.speed = combo_box.currentText()
        
    # def get_training_length(self):
    #     return self.training_length    
    
    # def set_training_length(self, combo_box):
    #     self.training_length = combo_box.currentText()
    
    def submit_clicked(self, init_parameters):
        # self.label.setText("Paramètres enregistrés")
        init_parameters.set_training_type(self.training_type_ComboBox)
        init_parameters.set_speed(self.speed_ComboBox)
        init_parameters.set_training_length(self.training_length_ComboBox)
        self.activity_window = ActivityMenu(init_parameters)
        self.close()
        self.activity_window.show()
        # self.update(init_parameters)
        
    
    # def update(self, init_parameters): # Pourrait être effacée
    #     # self.label.adjustSize()
    #     print("Paramètres enregistrés: ", init_parameters.get_training_type(), ",", str(init_parameters.get_speed()), "RPM ,", init_parameters.get_training_length(),"min.")