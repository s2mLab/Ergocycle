
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
# import time
# import sys

from MotorParameters import MotorParameters
from constants import *

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

# Fenêtre principale qui crée le menu principal pour le contrôle du moteur

class MainWindowMotor(QMainWindow):
    def __init__(self, motor_param):
        super(MainWindowMotor, self).__init__()
        self.setGeometry(SCREEN_WIDTH, 30, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle("Menu Principal")
        self.setStyleSheet("background-color: white;")
        # self.button_dictionary = {}
        
        self.initUI(motor_param) # init_parameters
    
    def initUI(self, motor_param):
        
        self.logo_label = QLabel(self)
        self.pixmap = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        # self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        self.logo_label.adjustSize()
        
        self.menu_label = QLabel(self)
        self.menu_label.setText("Menu Principal")
        self.menu_label.move(800,150)
        self.menu_label.setFont(QFont('Arial', 32, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.training_type_label = QtWidgets.QLabel(self)
        self.training_type_label.setText("Type d'entraînement")
        self.training_type_label.move(300,300)
        self.training_type_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.training_type_label.adjustSize()
        
        self.training_type_ComboBox = QComboBox(self)
        self.training_type_ComboBox.addItems(["Concentrique", "Excentrique", "Passif"])
        self.training_type_ComboBox.move(1300,300)
        self.training_type_ComboBox.setFont(QFont('Arial', 24))
        self.training_type_ComboBox.adjustSize()
        
        self.target_power_label = QLabel(self)
        self.target_power_label.setText("Puissance cible (W)")
        self.target_power_label.move(300,500)
        self.target_power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.target_power_label.adjustSize()
        
        self.target_power_ComboBox = QComboBox(self)
        self.target_power_ComboBox.addItems(["5", "10", "15", "20", "25", "30"])
        self.target_power_ComboBox.move(1300,500)
        self.target_power_ComboBox.setFont(QFont('Arial', 24))
        self.target_power_ComboBox.adjustSize()
        
        self.training_length_label = QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement")
        self.training_length_label.move(300,700)
        self.training_length_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        
        self.training_length_ComboBox = QComboBox(self)
        self.training_length_ComboBox.addItems(["1", "5", "10", "15", "20", "25", "30"])
        self.training_length_ComboBox.move(1300,700)
        self.training_length_ComboBox.setFont(QFont('Arial', 24))
        self.training_length_ComboBox.adjustSize()
        
        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("  Débuter  ")
        self.submit_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_button.move(840, 850)
        self.submit_button.setFont(QFont('Arial', 36, weight = QFont.Bold))
        self.submit_button.adjustSize()
        # self.button_dictionary[self.submit_button] = "start_training"
    
    def submit_clicked(self, motor_parameters):
        motor_parameters.set_training_type(self.training_type_ComboBox)
        motor_parameters.set_target_power(self.target_power_ComboBox)
        motor_parameters.set_training_length(self.training_length_ComboBox)
        
        # self.update(init_parameters)
