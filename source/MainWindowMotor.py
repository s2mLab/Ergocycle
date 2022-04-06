# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:39:36 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
# import time
# import sys

from MotorParameters import MotorParameters
from ActivityMenu import ActivityMenu
# from ErrorMenu import ErrorMenu
# from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu
from CommandButton import CommandButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080 - 30

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

# Fenêtre principale qui crée le menu principal pour le contrôle du moteur

class MainWindowMotor(QMainWindow):
    def __init__(self, motor_param):
        super(MainWindowMotor, self).__init__()
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        self.setWindowTitle("Menu Principal")
        self.setStyleSheet("background-color: white;")
        self.button_dictionary = {}
        
        # init_parameters = MotorParameters()
        # self.training_type = "Concentrique"
        # self.speed = "0"
        # self.training_length = "0"
        
        self.initUI(motor_param) # init_parameters
    
    def initUI(self, motor_param):
        #self.layout = QGridLayout()
        
        self.logo_label = QLabel(self)
        self.pixmap = QPixmap('s2m_logo_resized.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        self.logo_label.adjustSize()
        # self.layout.addWidget(self.logo_label, 0, 0, Qt.AlignLeft)
        
        self.menu_label = QLabel(self)
        self.menu_label.setText("Menu Principal")
        self.menu_label.move(175,40)
        self.menu_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.menu_label.adjustSize()
        # self.layout.addWidget(self.menu_label, 0, 1, Qt.AlignHCenter)
        
        self.training_type_label = QtWidgets.QLabel(self)
        self.training_type_label.setText("Type d'entraînement")
        self.training_type_label.move(100,100)
        self.training_type_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.training_type_label.adjustSize()
        # self.layout.addWidget(self.training_type_label, 1 , 0, Qt.AlignRight)
        
        self.training_type_ComboBox = QComboBox(self)
        self.training_type_ComboBox.addItems(["Concentrique", "Excentrique", "Passif"])
        self.training_type_ComboBox.move(300,100)
        self.training_type_ComboBox.setFont(QFont('Arial', 12))
        self.training_type_ComboBox.adjustSize()
        # self.layout.addWidget(self.training_type_ComboBox, 1, 2, Qt.AlignLeft)
        
        self.target_speed_label = QLabel(self)
        self.target_speed_label.setText("Vitesse/Puissance cible")
        self.target_speed_label.move(100,150)
        self.target_speed_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.target_speed_label.adjustSize()
        # self.layout.addWidget(self.target_speed_label, 2, 0, Qt.AlignRight)
        
        self.target_speed_ComboBox = QComboBox(self)
        self.target_speed_ComboBox.addItems(["25", "50", "75", "100"])
        self.target_speed_ComboBox.move(300,150)
        self.target_speed_ComboBox.setFont(QFont('Arial', 12))
        self.target_speed_ComboBox.adjustSize()
        # self.layout.addWidget(self.target_speed_ComboBox, 2, 2, Qt.AlignLeft)
        
        self.training_length_label = QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement")
        self.training_length_label.move(100,200)
        self.training_length_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        # self.layout.addWidget(self.training_length_label, 3, 0, Qt.AlignRight)
        
        self.training_length_ComboBox = QComboBox(self)
        self.training_length_ComboBox.addItems(["5", "10", "15", "20", "25", "30"])
        self.training_length_ComboBox.move(300,200)
        self.training_length_ComboBox.setFont(QFont('Arial', 12))
        self.training_length_ComboBox.adjustSize()
        # self.layout.addWidget(self.training_length_ComboBox, 3, 2, Qt.AlignLeft)
        
        self.submit_button = QtWidgets.QPushButton(self)
        #self.submit_button = CommandButton("Débuter l'entraînement", "start_training")
        self.submit_button.setText("  Débuter  ")
        self.submit_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_button.move(200, 260)
        self.submit_button.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.submit_button.adjustSize()
        # self.layout.addWidget(self.submit_button, 4, 1, Qt.AlignHCenter)
        self.button_dictionary[self.submit_button] = "start_training"
        
        # self.test_button = QtWidgets.QPushButton("Commander amplitude", self)
        # self.test_button.move(300, 260)
        # self.button_dictionary[self.test_button] = "command_amplitude"
        
        #self.layout.addWidget(self.test_button, 9)
        
        #self.setCentralWidget(QWidget(self))
        #self.centralWidget().setLayout(self.layout)
        
        #self.start_application()
    
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
    
    def submit_clicked(self, motor_parameters):
        # self.label.setText("Paramètres enregistrés")
        
        #TODO: envoyer ces paramètres au contrôle du moteur
        
        motor_parameters.set_training_type(self.training_type_ComboBox)
        motor_parameters.set_target_speed(self.target_speed_ComboBox)
        motor_parameters.set_training_length(self.training_length_ComboBox)
        
        self.activity_window = ActivityMenu(motor_parameters)
        self.close()
        self.activity_window.show()
        
        # self.update(init_parameters)
        
    
    # def update(self, init_parameters): # Pourrait être effacée
    #     # self.label.adjustSize()
    #     print("Paramètres enregistrés: ", init_parameters.get_training_type(), ",", str(init_parameters.get_speed()), "RPM ,", init_parameters.get_training_length(),"min.")