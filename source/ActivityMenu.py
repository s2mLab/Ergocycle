# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:41:31 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
# import time
# import sys

# from MainWindowMotor import MainWindowMotor
# from MotorParameters import MotorParameters
from ErrorMenu import ErrorMenu
from StopMenu import StopMenu
# from SummaryMenu import SummaryMenu

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class ActivityMenu(QWidget):
    def __init__(self, init_parameters):
        super(ActivityMenu, self).__init__()
        
        self.setGeometry(700, 400, SCREEN_WIDTH/4, SCREEN_HEIGTH/3)
        self.setWindowTitle("Performances")
        self.setStyleSheet("background-color: white;")
        
        current_parameters = init_parameters
        
        # measured = MotorParameters()
        
        self.initUI(current_parameters)

    def initUI(self, current_parameters):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('s2m_logo_resized.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Performances")
        self.menu_label.move(175,40)
        self.menu_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.power_label = QtWidgets.QLabel(self)
        self.power_label.setText("Puissance")
        self.power_label.move(75,100)
        self.power_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.power_label.adjustSize()
        
        self.current_power_label = QtWidgets.QLabel(self)
        self.current_power_label.setText(str(current_parameters.get_speed()))
        self.current_power_label.move(350,100)
        self.current_power_label.setFont(QFont('Arial', 12))
        self.current_power_label.adjustSize()
        
        self.speed_label = QtWidgets.QLabel(self)
        self.speed_label.setText("Vitesse/RPM")
        self.speed_label.move(75,150)
        self.speed_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.speed_label.adjustSize()
        
        self.current_speed_label = QtWidgets.QLabel(self)
        # self.current_speed_label.setText(str(current_parameters.get_speed()))
        self.current_speed_label.move(350,150)
        self.current_speed_label.setFont(QFont('Arial', 12))
        # self.current_speed_label.adjustSize()
        
        self.increase_speed_button = QtWidgets.QPushButton(self)
        self.increase_speed_button.setText("     +     ")
        self.increase_speed_button.move(270, 148)
        self.increase_speed_button.setFont(QFont('Arial', 14))
        self.increase_speed_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_speed_button.adjustSize()
        self.increase_speed_button.clicked.connect(lambda:self.increase_speed(current_parameters))  
        
        self.decrease_speed_button = QtWidgets.QPushButton(self)
        self.decrease_speed_button.setText("     -     ")
        self.decrease_speed_button.move(385, 148)
        self.decrease_speed_button.setFont(QFont('Arial', 14))
        self.decrease_speed_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_speed_button.adjustSize()
        self.decrease_speed_button.clicked.connect(lambda:self.decrease_speed(current_parameters))  
        
        self.distance_label = QtWidgets.QLabel(self)
        self.distance_label.setText("Distance parcourue")
        self.distance_label.move(75,200)
        self.distance_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.distance_label.adjustSize()
        
        self.current_distance_label = QtWidgets.QLabel(self)
        # self.current_distance_label.setText(str(current_parameters.get_training_length()))
        self.current_distance_label.move(350,200)
        self.current_distance_label.setFont(QFont('Arial', 12))
        # self.current_distance_label.adjustSize()
        
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setText("Temps écoulé")
        self.time_label.move(75,250)
        self.time_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.time_label.adjustSize()
        
        self.current_time_label = QtWidgets.QLabel(self)
        self.current_time_label.setText(str(current_parameters.get_training_length()))
        self.current_time_label.move(350,250)
        self.current_time_label.setFont(QFont('Arial', 12))
        # self.current_time_label.adjustSize()
        
        self.training_length_label = QtWidgets.QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement")
        self.training_length_label.move(75,300)
        self.training_length_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        
        self.current_training_length_label = QtWidgets.QLabel(self)
        # self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.move(350,300)
        self.current_training_length_label.setFont(QFont('Arial', 12))
        # self.current_training_length_label.adjustSize()
        
        self.increase_training_length_button = QtWidgets.QPushButton(self)
        self.increase_training_length_button.setText("     +     ")
        self.increase_training_length_button.move(270, 300)
        self.increase_training_length_button.setFont(QFont('Arial', 14))
        self.increase_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_training_length_button.adjustSize()
        self.increase_training_length_button.clicked.connect(lambda:self.increase_training_length(current_parameters))  
        
        self.decrease_training_length_button = QtWidgets.QPushButton(self)
        self.decrease_training_length_button.setText("     -     ")
        self.decrease_training_length_button.move(385, 300)
        self.decrease_training_length_button.setFont(QFont('Arial', 14))
        self.decrease_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_training_length_button.adjustSize()
        self.decrease_training_length_button.clicked.connect(lambda:self.decrease_training_length(current_parameters)) 
        
        self.correction_label = QtWidgets.QLabel(self)
        self.correction_label.setText("")
        self.correction_label.setFont(QFont('Arial', 14, weight = QFont.Bold))
        self.correction_label.adjustSize()
        
        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setText("  ARRÊT  ")
        self.stop_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.stop_button.move(330, 34)
        self.stop_button.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.stop_button.adjustSize()
        self.stop_button.clicked.connect(lambda:self.stop_clicked())   
        
        self.error_button = QtWidgets.QPushButton(self) # Effacer cette section quand les erreurs pourront être détectées
        self.error_button.setText("  ERREUR  ")
        self.error_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.error_button.move(170, 370)
        self.error_button.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.error_button.adjustSize()
        self.error_button.clicked.connect(lambda:self.simulate_error())
        
        self.update_labels(current_parameters)
        
    def simulate_error(self):
        self.error_window = ErrorMenu()
        self.error_window.show()

    def get_current_speed(self, current_parameters): # Peut-être à enlever
        return current_parameters.get_speed()

    def increase_speed(self, current_parameters):
        if (current_parameters.speed < MAX_SPEED):
            current_parameters.speed += 1
            self.update_labels(current_parameters)

    def decrease_speed(self, current_parameters):
        if (current_parameters.speed > MIN_SPEED):
            current_parameters.speed -= 1
            self.update_labels(current_parameters)

    def get_current_training_length(self, current_parameters): # Peut-être à enlever
        return current_parameters.training_length
        self.update_labels(current_parameters)

    def increase_training_length(self, current_parameters):
        if(current_parameters.training_length < MAX_TRAINING_LENGTH):
            current_parameters.training_length += 1
            self.update_labels(current_parameters)

    def decrease_training_length(self, current_parameters):
        if(current_parameters.training_length > MIN_TRAINING_LENGTH):
            current_parameters.training_length -= 1
            self.update_labels(current_parameters)
      
    def stop_clicked(self):
        self.stop_window = StopMenu()
        self.stop_window.show()
        self.stop_window.confirmation_button.clicked.connect(lambda:self.close())
        
    def update_labels(self, current_parameters):
        self.current_speed_label.setText(str(current_parameters.get_speed()))
        self.current_speed_label.adjustSize()
        
        # self.update_measures(measured)
        
        self.current_distance_label.setText(str(current_parameters.get_training_length()))
        self.current_distance_label.adjustSize()
        
        self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.adjustSize()
        
        if (current_parameters.get_speed() > (25 * 1.1)): # Remplacer 25 par la vitesse cible
            self.current_speed_label.setStyleSheet("color: red")
            self.correction_label.setText("Ralentissez")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(190,330)
        elif (current_parameters.get_speed() < (25 * 0.9)): # Remplacer 25 par la vitesse cible
            self.current_speed_label.setStyleSheet("color: red")
            self.correction_label.setText("Accélérez")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(190,330)
        else:
            self.current_speed_label.setStyleSheet("color: green")
            self.correction_label.setText("Maintenez cette vitesse")
            self.correction_label.setStyleSheet("color: green")
            self.correction_label.move(130,330)
        self.correction_label.adjustSize()
        
    # def update_measures(self, measured):
        # measured.set_speed(20) # Modifier
        # Mettre à jour les mesures ici