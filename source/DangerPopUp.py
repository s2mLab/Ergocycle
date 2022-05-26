"""
Created on Wed Feb 23 14:10:00 2022

@author: Frédérique Leclerc
"""
from inspect import Parameter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
#from Ergocycle.source.MainWindowStim import MainWindowStim
from InstructionWindow import InstructionWindow
from PIL import Image
#import sys
from constants import *

class DangerPopUp(QWidget):
    def __init__(self, init_parameters):
        super(DangerPopUp, self).__init__()
         ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre PopUp ###
        self.setGeometry(300, 300, SCREEN_WIDTH/1.7, SCREEN_HEIGHT/1.8)
        self.setWindowTitle("Averitissement")
        self.setStyleSheet("background-color: white;")
        self.initUI(init_parameters)
    def initUI(self, init_parameters):  
        ### 1.2. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.3. Message d'erreur ###
        self.attention_label = QtWidgets.QLabel(self)
        self.attention_label.setText("Attention.")
        self.attention_label.move(200,40)
        self.attention_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.attention_label.adjustSize()
        self.message_label = QtWidgets.QLabel(self)
        self.message_label.setText("L'une ou plusieurs valeurs que vous avez entrées \n ne sont pas recommandées. Assurez-vous que pour chaque électrode: \n - une amplitude supérieure à 60mA n'est pas couplée à une fréquence supérieure à 40 Hz \n - une amplitude supérieure à 60mA n'est pas couplée à une durée d'impulsion supérieure à 250μs \n - une durée d'impulsion supérieure à 250μs n'est pas couplée à une fréquence supérieure à 40 Hz")
        self.message_label.move(200,60)
        self.message_label.setFont(QFont('Arial', 12))
        self.message_label.adjustSize()
        self.problem_label = QtWidgets.QLabel(self)
        self.problem_label.setText("Nombre de problèmes rencontrés pour chaqun des couples dangereux :")
        self.problem_label.move(10,200)
        self.problem_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.problem_label.adjustSize()
        ### 1.4. Détermination du problème au client ###
        self.i=init_parameters.couple_amplitude_frequency_check()
        self.j=init_parameters.couple_amplitude_imp_check()
        self.k=init_parameters.couple_frequency_imp_check()
        self.couple_amplitude_frequency_label = QtWidgets.QLabel(self)
        self.couple_amplitude_frequency_label.setText("Couple Amplitude/Fréquence : ")
        self.couple_amplitude_frequency_label.move(10,250)
        self.couple_amplitude_frequency_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.couple_amplitude_frequency_label.adjustSize()
        self.i_label = QtWidgets.QLabel(self)
        self.i_label.setText(str(init_parameters.couple_amplitude_frequency_check()))
        self.i_label.move(400,250)
        self.i_label.setFont(QFont('Arial', 12))
        self.i_label.adjustSize()
        self.couple_amplitude_imp_label = QtWidgets.QLabel(self)
        self.couple_amplitude_imp_label.setText("Couple Amplitude/Durée d'impulsion : ")
        self.couple_amplitude_imp_label.move(10,300)
        self.couple_amplitude_imp_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.couple_amplitude_imp_label.adjustSize()
        self.j_label = QtWidgets.QLabel(self)
        self.j_label.setText(str(init_parameters.couple_amplitude_imp_check()))
        self.j_label.move(400,300)
        self.j_label.setFont(QFont('Arial', 12))
        self.j_label.adjustSize()
        self.couple_frequency_imp_label = QtWidgets.QLabel(self)
        self.couple_frequency_imp_label.setText("Couple Fréquence/Durée d'impulsion : ")
        self.couple_frequency_imp_label.move(10,350)
        self.couple_frequency_imp_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.couple_frequency_imp_label.adjustSize()
        self.k_label = QtWidgets.QLabel(self)
        self.k_label.setText(str(init_parameters.couple_frequency_imp_check()))
        self.k_label.move(400,350)
        self.k_label.setFont(QFont('Arial', 12))
        self.question_label = QtWidgets.QLabel(self)
        self.question_label.setText("Souhaiteriez-vous changer les valeurs des paramètres d'entraînement?")
        self.question_label.move(200,450)
        self.question_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.question_label.adjustSize()
        self.question_label.adjustSize()
        ### 1.5. Bouton pour retourner au menu principal ###
        self.back_to_menu_button = QtWidgets.QPushButton(self)
        self.back_to_menu_button.setText("   Modifier les paramètres   ")
        self.back_to_menu_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.back_to_menu_button.move(200, 500)
        self.back_to_menu_button.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.back_to_menu_button.adjustSize()
        ### 1.6. Bouton pour poursuivre quand même ###
        self.continue_button = QtWidgets.QPushButton(self)
        self.continue_button.setText("   Poursuivre quand même   ")
        self.continue_button.setStyleSheet("background-color: red; border: 1 solid;")
        self.continue_button.move(600, 500)
        self.continue_button.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.continue_button.adjustSize()
    ### 1.7. Retour au MainWindowStim.py ###
    def clicked_back(self):
        self.close()
    ### 1.8. Envoie au InstructionWindow.py ###
    def clicked_instruction(self, init_parameters):
        self.instruction_window = InstructionWindow(init_parameters)
        self.instruction_window.show()
        self.close()