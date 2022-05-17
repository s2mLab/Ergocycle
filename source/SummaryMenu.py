
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
# import time
# import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

class SummaryMenu(QWidget):
    def __init__(self, motor_parameters):
        super(SummaryMenu, self).__init__()
        
        self.setGeometry(SCREEN_WIDTH, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        self.setWindowTitle("Résumé de la séance")
        self.setStyleSheet("background-color: white;")
        
        self.initUI(motor_parameters)

    def initUI(self, motor_parameters):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Séance terminée")
        self.menu_label.move(780,100)
        self.menu_label.setFont(QFont('Arial', 32, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.summary_label = QtWidgets.QLabel(self)
        self.summary_label.setText("Résumé de la séance")
        self.summary_label.move(790,200)
        self.summary_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.summary_label.adjustSize()
        
        self.max_power_label = QtWidgets.QLabel(self)
        self.max_power_label.setText("Puissance maximale : ")
        self.max_power_label.move(300,400)
        self.max_power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.max_power_label.adjustSize()
        
        self.max_power = QtWidgets.QLabel(self)
        self.max_power.setText(str(motor_parameters.get_max_power()) + " W")
        self.max_power.move(1300,400)
        self.max_power.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.max_power.adjustSize()
        
        self.average_power_label = QtWidgets.QLabel(self)
        self.average_power_label.setText("Puissance moyenne : ")
        self.average_power_label.move(300,500)
        self.average_power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.average_power_label.adjustSize()
        
        self.average_power = QtWidgets.QLabel(self)
        self.average_power.setText(str(motor_parameters.get_average_power()) + " W")
        self.average_power.move(1300,500)
        self.average_power.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.average_power.adjustSize()
        
        self.total_length_label = QtWidgets.QLabel(self)
        self.total_length_label.setText("Durée de l'entraînement : ")
        self.total_length_label.move(300,600)
        self.total_length_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.total_length_label.adjustSize()
        
        self.total_length = QtWidgets.QLabel(self)
        # self.total_length.setText(str(motor_parameters.get_training_length()) + " min")
        self.total_length.setGeometry(1300, 590, 100, 70)
        self.total_length.setFont(QFont('Arial', 12))
        # self.total_length.move(1300,600)
        # self.total_length.setFont(QFont('Arial', 24, weight = QFont.Bold))
        # self.total_length.adjustSize()
        
        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("Nombre d'ajustement du moteur : ")
        # self.label.move(300,600)
        # self.label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        # self.label.adjustSize()