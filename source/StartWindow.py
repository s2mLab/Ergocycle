"""
Created on Wed March 24 11:15:00 2022

@author: Frédérique Leclerc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import numpy
import datetime
#from Ergocycle.source.TestingWindow import TestingWindow
from TestingWindow import TestingWindow
from MainWindowStim import MainWindowStim 
from PIL import Image
from numpy import *

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

class StartWindow(QWidget):
    def __init__(self): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
    #def __init__(self, event_function): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        #super(StartWindow, self).__init__(event_function) ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        super(StartWindow, self).__init__() ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre des instructions ###
        self.setGeometry(300, 300, SCREEN_WIDTH/1.7, SCREEN_HEIGTH/1.8)
        self.setWindowTitle("Interface usager des stimulations électriques fonctionnelles")
        self.setStyleSheet("background-color: white;")
        self.initUI()
    def initUI(self):  
        ### 1.2. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.3. Titre menu des instructions ###
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setText("Bienvenue dans l'interface usager des stimulations électriques \nfonctionnelles")
        self.title_label.move(200,40)
        self.title_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.title_label.adjustSize()
        self.question_label = QtWidgets.QLabel(self)
        self.question_label.setText("Désirez-vous débuter un entraînement en stimulation ou effectuer des tests?")
        self.question_label.move(150,200)
        self.question_label.setFont(QFont('Arial', 15))
        self.question_label.adjustSize()
        ### 1.4. Bouton pour débuter l'entraînement ###
        self.training_button = QtWidgets.QPushButton(self)
        self.training_button.setText("   Débuter un entraînement   ")
        self.training_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.training_button.move(200, 400)
        self.training_button.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.training_button.adjustSize()
        self.training_button.clicked.connect(lambda:self.clicked_training())
        ### 1.5. Bouton pour faire des tests ###
        self.test_button = QtWidgets.QPushButton(self)
        self.test_button.setText("  Effectuer des tests  ")
        self.test_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.test_button.move(700, 400)
        self.test_button.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.test_button.adjustSize()
        self.test_button.clicked.connect(lambda:self.clicked_test())
    def clicked_training(self): 
        self.main_menu = MainWindowStim()
        self.main_menu.show()
        self.close()
        self.update()
    def clicked_test(self): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        self.test_menu = TestingWindow() ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        self.test_menu.setWindowModality(2)
        self.test_menu.show()
        self.get_initial_test_parameters()
        self.update()
    def get_initial_test_parameters(self):
        self.test_parameters = numpy.array([0,30,200])
        #print(self.test_parameters)
        return(self.test_parameters)