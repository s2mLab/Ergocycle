"""
Created on Wed Feb 23 14:10:00 2022

@author: Frédérique Leclerc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import numpy
import datetime 
from StimulationWindow import StimulationWindow
from PIL import Image
from numpy import *
#import sys
from constants import *

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier


class InstructionWindow(QWidget):
    def __init__(self, init_parameters):
        super(InstructionWindow, self).__init__()
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle("Instructions d'installation des électrodes")
        self.setStyleSheet("background-color: white;")
        self.com_start_feedback = True 
        self.initUI(init_parameters)
    def initUI(self, init_parameters):  
        ### 1.1. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.2. Titre menu des instructions ###
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Veuillez intaller les électrodes sur le patient tel qu'indiqué ci-dessous. Lorsque terminé, veuillez appuyer sur \nle bouton continuer pour commencer la stimulation.\nNote: Vous pourrez uniquement commencer la stimulation lorsque l'ergocycle sera en marche.")
        self.menu_label.move(200,40)
        self.menu_label.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ### 1.3. Information d'installation ###
        self.electrode1_label = QtWidgets.QLabel(self)
        self.electrode1_label.setText("Électrode 1 (droite):")
        self.electrode1_label.move(10,200)
        self.electrode1_label.setFont(QFont('Arial', 16))
        self.electrode1_label.adjustSize()

        self.muscle1_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle1_label.setText(init_parameters.get_electrode1_muscle())
        self.muscle1_label.move(350,200)
        self.muscle1_label.setFont(QFont('Arial', 16))
        self.muscle1_label.adjustSize()

        self.electrode2_label = QtWidgets.QLabel(self)
        self.electrode2_label.setText("Électrode 2 (droite):")
        self.electrode2_label.move(10,300)
        self.electrode2_label.setFont(QFont('Arial', 16))
        self.electrode2_label.adjustSize()

        self.muscle2_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle2_label.setText(init_parameters.get_electrode2_muscle())
        self.muscle2_label.move(350,300)
        self.muscle2_label.setFont(QFont('Arial', 16))
        self.muscle2_label.adjustSize()
        
        self.electrode3_label = QtWidgets.QLabel(self)
        self.electrode3_label.setText("Électrode 3 (droite):")
        self.electrode3_label.move(10,400)
        self.electrode3_label.setFont(QFont('Arial', 16))
        self.electrode3_label.adjustSize()

        self.muscle3_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle3_label.setText(init_parameters.get_electrode3_muscle())
        self.muscle3_label.move(350,400)
        self.muscle3_label.setFont(QFont('Arial', 16))
        self.muscle3_label.adjustSize()

        self.electrode4_label = QtWidgets.QLabel(self)
        self.electrode4_label.setText("Électrode 4 (droite):")
        self.electrode4_label.move(10,500)
        self.electrode4_label.setFont(QFont('Arial', 16))
        self.electrode4_label.adjustSize()

        self.muscle4_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle4_label.setText(init_parameters.get_electrode4_muscle())
        self.muscle4_label.move(350,500)
        self.muscle4_label.setFont(QFont('Arial', 16))
        self.muscle4_label.adjustSize()

        self.electrode5_label = QtWidgets.QLabel(self)
        self.electrode5_label.setText("Électrode 5 (gauche):")
        self.electrode5_label.move(10,600)
        self.electrode5_label.setFont(QFont('Arial', 16))
        self.electrode5_label.adjustSize()

        self.muscle5_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle5_label.setText(init_parameters.get_electrode5_muscle())
        self.muscle5_label.move(350,600)
        self.muscle5_label.setFont(QFont('Arial', 16))
        self.muscle5_label.adjustSize()

        self.electrode6_label = QtWidgets.QLabel(self)
        self.electrode6_label.setText("Électrode 6 (gauche):")
        self.electrode6_label.move(10,700)
        self.electrode6_label.setFont(QFont('Arial', 16))
        self.electrode6_label.adjustSize()

        self.muscle6_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle6_label.setText(init_parameters.get_electrode6_muscle())
        self.muscle6_label.move(350,700)
        self.muscle6_label.setFont(QFont('Arial', 16))
        self.muscle6_label.adjustSize()

        self.electrode7_label = QtWidgets.QLabel(self)
        self.electrode7_label.setText("Électrode 7 (gauche):")
        self.electrode7_label.move(10,800)
        self.electrode7_label.setFont(QFont('Arial', 16))
        self.electrode7_label.adjustSize()

        self.muscle7_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle7_label.setText(init_parameters.get_electrode7_muscle())
        self.muscle7_label.move(350,800)
        self.muscle7_label.setFont(QFont('Arial', 16))
        self.muscle7_label.adjustSize()

        self.electrode8_label = QtWidgets.QLabel(self)
        self.electrode8_label.setText("Électrode 8 (gauche):")
        self.electrode8_label.move(10,900)
        self.electrode8_label.setFont(QFont('Arial', 16))
        self.electrode8_label.adjustSize()

        self.muscle8_label = QtWidgets.QLabel(self) ## Faire la même chose pour tous les électrodes ##
        self.muscle8_label.setText(init_parameters.get_electrode8_muscle())
        self.muscle8_label.move(350,900)
        self.muscle8_label.setFont(QFont('Arial', 16))
        self.muscle8_label.adjustSize()

        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setText("  Continuer vers la stimulation  ")
        self.start_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.start_button.move(1100, 900)
        self.start_button.setFont(QFont('Arial', 30, weight = QFont.Bold))
        self.start_button.adjustSize()

    ### 1.4. Chercher les valeurs des menus déroulants entrés par l'utilisateur à MainWindowStim.py pour l'envoyer au module de communication ###
        self.start_parameters = numpy.empty([4,8], dtype=int)
    def get_initial_parameters(self, init_parameters):
        #self.start_parameters = numpy.empty([4,8], dtype=int)
        for i in range(len(self.start_parameters)):
                if i==0:
                    self.start_parameters[i,:]=[init_parameters.get_electrode1_amplitude(), init_parameters.get_electrode2_amplitude(), init_parameters.get_electrode3_amplitude(),init_parameters.get_electrode4_amplitude(),init_parameters.get_electrode5_amplitude(),init_parameters.get_electrode6_amplitude(),init_parameters.get_electrode7_amplitude(),init_parameters.get_electrode8_amplitude()]
                if i==1:
                    self.start_parameters[i,:]=[init_parameters.get_electrode1_frequency(), init_parameters.get_electrode2_frequency(), init_parameters.get_electrode3_frequency(),init_parameters.get_electrode4_frequency(),init_parameters.get_electrode5_frequency(),init_parameters.get_electrode6_frequency(),init_parameters.get_electrode7_frequency(),init_parameters.get_electrode8_frequency()]
                if i==2:
                    self.start_parameters[i,:]=[init_parameters.get_electrode1_length_imp(),init_parameters.get_electrode2_length_imp(), init_parameters.get_electrode3_length_imp(), init_parameters.get_electrode4_length_imp(), init_parameters.get_electrode5_length_imp(), init_parameters.get_electrode6_length_imp(), init_parameters.get_electrode7_length_imp(),init_parameters.get_electrode8_length_imp()]
                if i==3:
                    self.start_parameters[i,:]=init_parameters.get_muscle_number()
        return(self.start_parameters)
    ### 1.5. Chercher la valeur du menu déroulant de temps d'entrainement entré par l'utilisateur à MainWindowStim.py pour l'envoyer au module de communication ###
    def get_training_time(self, init_parameters):
        self.training_time = init_parameters.get_stim_training_length()
        return(self.training_time)
    
    


