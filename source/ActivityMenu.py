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
    def __init__(self, motor_parameters):
        super(ActivityMenu, self).__init__()
        
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        self.setWindowTitle("Performances")
        self.setStyleSheet("background-color: white;")
        self.button_dictionary = {}
        
        self.initUI(motor_parameters)

    def initUI(self, current_parameters):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        # self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        self.logo_label.adjustSize()
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Performances")
        self.menu_label.move(825,100)
        self.menu_label.setFont(QFont('Arial', 32, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.power_label = QtWidgets.QLabel(self)
        self.power_label.setText("Puissance")
        self.power_label.move(300, 250)
        self.power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.power_label.adjustSize()
        
        self.current_power_label = QtWidgets.QLabel(self)
        self.current_power_label.setText(str(current_parameters.get_target_speed()))
        self.current_power_label.move(1300,250)
        self.current_power_label.setFont(QFont('Arial', 24))
        self.current_power_label.adjustSize()
        
        self.current_speed_label = QtWidgets.QLabel(self)
        self.current_speed_label.setText("Vitesse/RPM")
        self.current_speed_label.move(300,400)
        self.current_speed_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.current_speed_label.adjustSize()
        
        self.current_speed_label = QtWidgets.QLabel(self)
        self.current_speed_label.setText(str(current_parameters.get_current_speed()))
        self.current_speed_label.move(1300,400)
        self.current_speed_label.setFont(QFont('Arial', 24))
        self.current_speed_label.adjustSize()
        
        self.increase_speed_button = QtWidgets.QPushButton(self)
        self.increase_speed_button.setText("     +     ")
        self.increase_speed_button.move(1100, 248)
        self.increase_speed_button.setFont(QFont('Arial', 28))
        self.increase_speed_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_speed_button.adjustSize()
        # self.increase_speed_button.clicked.connect(lambda:self.increase_speed(current_parameters))  
        self.button_dictionary[self.increase_speed_button] = "increase_target_speed"
        
        self.decrease_speed_button = QtWidgets.QPushButton(self)
        self.decrease_speed_button.setText("     -     ")
        self.decrease_speed_button.move(1420, 248)
        self.decrease_speed_button.setFont(QFont('Arial', 28))
        self.decrease_speed_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_speed_button.adjustSize()
        #self.decrease_speed_button.clicked.connect(lambda:self.decrease_speed(current_parameters))  
        self.button_dictionary[self.decrease_speed_button] = "decrease_target_speed"
        
        self.distance_label = QtWidgets.QLabel(self)
        self.distance_label.setText("Distance parcourue")
        self.distance_label.move(300, 500)
        self.distance_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.distance_label.adjustSize()
        
        self.current_distance_label = QtWidgets.QLabel(self)
        self.current_distance_label.setText(str(current_parameters.get_distance()))
        self.current_distance_label.move(1300, 500)
        self.current_distance_label.setFont(QFont('Arial', 24))
        self.current_distance_label.adjustSize()
        
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setText("Temps écoulé")
        self.time_label.move(300, 650)
        self.time_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.time_label.adjustSize()
        
        self.current_time_label = QtWidgets.QLabel(self)
        self.current_time_label.setText(str(current_parameters.get_training_length()))
        self.current_time_label.move(1300, 650)
        self.current_time_label.setFont(QFont('Arial', 24))
        self.current_time_label.adjustSize()
        
        self.training_length_label = QtWidgets.QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement")
        self.training_length_label.move(300, 800)
        self.training_length_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        
        self.current_training_length_label = QtWidgets.QLabel(self)
        self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.move(1300, 800)
        self.current_training_length_label.setFont(QFont('Arial', 24))
        self.current_training_length_label.adjustSize()
        
        self.increase_training_length_button = QtWidgets.QPushButton(self)
        self.increase_training_length_button.setText("     +     ")
        self.increase_training_length_button.move(1100, 798)
        self.increase_training_length_button.setFont(QFont('Arial', 28))
        self.increase_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_training_length_button.adjustSize()
        # self.increase_training_length_button.clicked.connect(lambda:self.increase_training_length(current_parameters))  
        self.button_dictionary[self.increase_training_length_button] = "increase_training_length"
        
        self.decrease_training_length_button = QtWidgets.QPushButton(self)
        self.decrease_training_length_button.setText("     -     ")
        self.decrease_training_length_button.move(1420, 798)
        self.decrease_training_length_button.setFont(QFont('Arial', 28))
        self.decrease_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_training_length_button.adjustSize()
        # self.decrease_training_length_button.clicked.connect(lambda:self.decrease_training_length(current_parameters)) 
        self.button_dictionary[self.decrease_training_length_button] = "decrease_training_length"
        
        self.correction_label = QtWidgets.QLabel(self)
        self.correction_label.setText("")
        self.correction_label.setFont(QFont('Arial', 28, weight = QFont.Bold))
        self.correction_label.adjustSize()
        
        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setText("  ARRÊT  ")
        self.stop_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.stop_button.move(1300, 90)
        self.stop_button.setFont(QFont('Arial', 40, weight = QFont.Bold))
        self.stop_button.adjustSize()
        # self.stop_button.clicked.connect(lambda:self.stop_clicked())   
        self.button_dictionary[self.stop_button] = "stop_training"
        
        self.error_button = QtWidgets.QPushButton(self) # Effacer cette section quand les erreurs pourront être détectées
        self.error_button.setText("  ERREUR  ")
        self.error_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.error_button.move(250, 875)
        self.error_button.setFont(QFont('Arial', 42, weight = QFont.Bold))
        self.error_button.adjustSize()
        self.error_button.clicked.connect(lambda:self.simulate_error())
        
        self.update_labels(current_parameters)
        
    def simulate_error(self):
        self.error_window = ErrorMenu()
        self.error_window.show()

    # def get_current_speed(self, current_parameters): # Prendre les mesures des capteurs
    #     return current_parameters.get_target_speed()

    # def increase_speed(self, current_parameters): # Envoyer la commande au contrôle du moteur
    #     if (current_parameters.target_speed < MAX_SPEED):
    #         current_parameters.target_speed += 1
    #         self.update_labels(current_parameters)

    # def decrease_speed(self, current_parameters):  # Envoyer la commande au contrôle du moteur
    #     if (current_parameters.target_speed > MIN_SPEED):
    #         current_parameters.target_speed -= 1
    #         self.update_labels(current_parameters)

    # def get_current_training_length(self, current_parameters): # Peut-être à enlever
    #     return current_parameters.training_length
    #     self.update_labels(current_parameters)

    # def increase_training_length(self, current_parameters): # Peut-être à enlever
    #     if(current_parameters.training_length < MAX_TRAINING_LENGTH):
    #         current_parameters.training_length += 1
    #         self.update_labels(current_parameters)

    # def decrease_training_length(self, current_parameters): # Peut-être à enlever
    #     if(current_parameters.training_length > MIN_TRAINING_LENGTH):
    #         current_parameters.training_length -= 1
    #         self.update_labels(current_parameters)
      
    def stop_clicked(self):
        self.stop_window = StopMenu()
        self.stop_window.show()
        self.stop_window.confirmation_button.clicked.connect(lambda:self.close())
        # self.button_dictionary[self.stop_button] = "stop_training"
        
        
    def update_labels(self, current_parameters):
        self.current_speed_label.setText(str(current_parameters.get_target_speed()))
        self.current_speed_label.adjustSize()
        
        # self.update_measures(measured)
        
        #TODO: faire la lecture des mesures
        
        self.current_distance_label.setText(str(current_parameters.get_training_length()))
        self.current_distance_label.adjustSize()
        
        self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.adjustSize()
        
        if (current_parameters.get_current_speed() > (25 * 1.1)): # Remplacer 25 par la vitesse cible
            self.current_speed_label.setStyleSheet("color: red")
            self.correction_label.setText("Ralentissez")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(850,875)
        elif (current_parameters.get_current_speed() < (25 * 0.9)): # Remplacer 25 par la vitesse cible
            self.current_speed_label.setStyleSheet("color: red")
            self.correction_label.setText("Accélérez")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(875,875)
        else:
            self.current_speed_label.setStyleSheet("color: green")
            self.correction_label.setText("Maintenez cette vitesse")
            self.correction_label.setStyleSheet("color: green")
            self.correction_label.move(850,875)
        self.correction_label.adjustSize()
        
    # def update_measures(self, measured):
        # measured.set_speed(20) # Modifier
        # Mettre à jour les mesures ici