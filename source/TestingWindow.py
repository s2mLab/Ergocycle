"""
Created on Wed March 23 13:58:00 2022

@author: Frédérique Leclerc
"""
import numpy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
from numpy import *
from CommandButton import CommandButton as CommandButton
#from StartWindow import StartWindow
#from MainWindowStim import MainWindowStim
#from Stimulator import Stimulator

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080 - 30
MAX_AMPLITUDE = 130
MIN_AMPLITUDE = 0
MAX_FREQ = 50
MIN_FREQ = 0
MAX_IMP = 500
MIN_IMP = 0

class TestingWindow(QWidget):
    def __init__(self): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
    #def __init__(self, event_function): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        #super(TestingWindow, self).__init__(event_function) ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        super(TestingWindow, self).__init__() ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre des instructions ###
        # self.SCREEN_WIDTH = 1920
        # self.SCREEN_HEIGTH = 1080 - 30
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        # self.setFixedWidth(self.SCREEN_WIDTH)
        # self.setFixedHeight(self.SCREEN_HEIGTH)
        #self.setGeometry(300, 300, SCREEN_WIDTH/1.7, SCREEN_HEIGTH/1.8)
        self.setWindowTitle("Test des stimulations")
        self.setStyleSheet("background-color: white;")
        self.button_dictionary = {}
        self.initUI()
    #def initUI(self, event_function): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
    def initUI(self): ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        ### 1.2. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.3. Titre menu des instructions ###
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Veuillez tester les paramètres de stimulation à l'aide des boutons + et  - . Lorsque terminé, veuillez cliquer\nsur tests complétés pour débuter l'entraînment en stimulation. ")
        self.menu_label.move(200,60)
        self.menu_label.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ### 1.4 - Initialiser les labels pour les 3 paramètres ###
        ### 1.4.1 - Layout des labels de la fenêtre de stimulation ###
        self.amplitude_label = QtWidgets.QLabel(self)
        self.amplitude_label.setText("Amplitude (mA):")
        self.amplitude_label.move(500,350)
        self.amplitude_label.setFont(QFont('Arial', 16))
        self.amplitude_label.adjustSize()

        self.frequency_label = QtWidgets.QLabel(self)
        self.frequency_label.setText("Fréquence (Hz):")
        self.frequency_label.move(500,450)
        self.frequency_label.setFont(QFont('Arial', 16))
        self.frequency_label.adjustSize()

        self.length_imp_label = QtWidgets.QLabel(self)
        self.length_imp_label.setText("Durée d'impulsion (μs):")
        self.length_imp_label.move(500,550)
        self.length_imp_label.setFont(QFont('Arial', 16))
        self.length_imp_label.adjustSize()
        ### 1.4.2 - Valeur initiales ### 
        self.amplitude = 0
        self.frequency = 30
        self.imp = 200
        self.test_amplitude_label = QtWidgets.QLabel(self)
        self.test_amplitude_label.setText(str(self.amplitude))
        self.test_amplitude_label.move(1000,350)
        self.test_amplitude_label.setFont(QFont('Arial', 16))
        self.test_amplitude_label.adjustSize()
        self.test_frequency_label = QtWidgets.QLabel(self)
        self.test_frequency_label.setText(str(self.frequency))
        self.test_frequency_label.move(1000,450)
        self.test_frequency_label.setFont(QFont('Arial', 16))
        self.test_frequency_label.adjustSize()
        self.test_imp_label = QtWidgets.QLabel(self)
        self.test_imp_label.setText(str(self.imp))
        self.test_imp_label.move(1000,550)
        self.test_imp_label.setFont(QFont('Arial', 16))
        self.test_imp_label.adjustSize()
        ### 1.4.3 - Boutons "+" ###
        self.increase_amp_button = QtWidgets.QPushButton(self)
        self.button_dictionary[self.increase_amp_button] = "USER CLICKING"
        self.increase_amp_button.setText(" + ")
        self.increase_amp_button.move(1150,350)
        self.increase_amp_button.setFont(QFont('Arial', 25))
        self.increase_amp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_amp_button.adjustSize()
        # self.increase_amp_button.clicked.connect(lambda:self.increase_amplitude()) ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
        #self.increase_amp_button.clicked.connect(lambda:self.increase_amplitude(event_function)) ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION

        self.increase_freq_button = QtWidgets.QPushButton(self)
        self.increase_freq_button.setText(" + ")
        self.increase_freq_button.move(1150,450)
        self.increase_freq_button.setFont(QFont('Arial', 25))
        self.increase_freq_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_freq_button.adjustSize()
        # self.increase_freq_button.clicked.connect(lambda:self.increase_frequency()) 

        self.increase_imp_button = QtWidgets.QPushButton(self)
        self.increase_imp_button.setText(" + ")
        self.increase_imp_button.move(1150,550)
        self.increase_imp_button.setFont(QFont('Arial', 25))
        self.increase_imp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_imp_button.adjustSize()
        # self.increase_imp_button.clicked.connect(lambda:self.increase_imp()) 
        ### 1.4.4 - Boutons "-" ###
        self.decrease_amp_button = QtWidgets.QPushButton(self)
        self.decrease_amp_button.setText("  -  ")
        self.decrease_amp_button.move(850,350)
        self.decrease_amp_button.setFont(QFont('Arial', 25))
        self.decrease_amp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_amp_button.adjustSize()
        # self.decrease_amp_button.clicked.connect(lambda:self.decrease_amplitude())
        
        self.decrease_freq_button = QtWidgets.QPushButton(self)
        self.decrease_freq_button.setText("  -  ")
        self.decrease_freq_button.move(850,450)
        self.decrease_freq_button.setFont(QFont('Arial', 25))
        self.decrease_freq_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_freq_button.adjustSize()
        # self.decrease_freq_button.clicked.connect(lambda:self.decrease_frequency()) 

        self.decrease_imp_button = QtWidgets.QPushButton(self)
        self.decrease_imp_button.setText("  -  ")
        self.decrease_imp_button.move(850,550)
        self.decrease_imp_button.setFont(QFont('Arial', 25))
        self.decrease_imp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_imp_button.adjustSize()
        # self.decrease_imp_button.clicked.connect(lambda:self.decrease_imp()) 
        
        ### 1.5. Bouton pour retourner au menu initial ###
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setText("     Tests complétés     ")
        self.back_button.setStyleSheet("background-color: red; border: 1 solid;")
        self.back_button.move(850, 750)
        self.back_button.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.back_button.adjustSize()
        # self.back_button.clicked.connect(lambda:self.clicked_back())
    
    def clicked_back(self):
        self.close()

    def increase_amplitude(self, test_parameters):
        # if (self.amplitude) < MAX_AMPLITUDE:
        #     self.amplitude = self.amplitude + 2
        #     self.test_amplitude_label.setText(str(self.amplitude))
        #     self.test_amplitude_label.adjustSize()
        #     self.get_updated_test_parameters()
        if (test_parameters.amplitude) < MAX_AMPLITUDE:
            test_parameters.amplitude += 2
            self.test_amplitude_label.setText(str(test_parameters.amplitude))
            self.test_amplitude_label.adjustSize()
            self.get_updated_test_parameters(test_parameters)
        
            #self.increase_amp_command_button = CommandButton(" + ","command_test")
            #self.increase_amp_command_button.clicked.connect(lambda : self.increase_amp_command_button.get_command())
            #event_function("command_new_test_parameters") ## PROBLÈME PASSAGE DE PARAMÈTRES EVENT_FUNCTION
    def increase_frequency(self, test_parameters):
        # if (self.frequency) < MAX_FREQ:
        #     if (self.frequency) == 0:
        #         self.frequency = 10
        #     else:
        #         self.frequency = self.frequency + 5
        #     self.test_frequency_label.setText(str(self.frequency))
        #     self.test_frequency_label.adjustSize()
        #     self.get_updated_test_parameters(test_parameters)
        if (test_parameters.frequency) < MAX_FREQ:
            if (test_parameters.frequency) == 0:
                test_parameters.frequency = 10
            else:
                test_parameters.frequency += 5
            self.test_frequency_label.setText(str(test_parameters.frequency))
            self.test_frequency_label.adjustSize()
            self.get_updated_test_parameters(test_parameters)
        
    def increase_imp(self, test_parameters):
        # if (self.imp) < MAX_IMP:
        #     if (self.imp) == 0:
        #         self.imp = 20
        #     else:
        #         self.imp = self.imp + 10
        #     self.test_imp_label.setText(str(self.imp))
        #     self.test_imp_label.adjustSize()
        #     self.get_updated_test_parameters()
        if (test_parameters.imp) < MAX_IMP:
            if (test_parameters.imp) == 0:
                test_parameters.imp = 20
            else:
                test_parameters.imp += 10
            self.test_imp_label.setText(str(test_parameters.imp))
            self.test_imp_label.adjustSize()
            self.get_updated_test_parameters(test_parameters)
            
    def decrease_amplitude(self, test_parameters):
        # if (self.amplitude) > MIN_AMPLITUDE:
        #     self.amplitude = self.amplitude - 2
        #     self.test_amplitude_label.setText(str(self.amplitude))
        #     self.test_amplitude_label.adjustSize()
        #     self.get_updated_test_parameters()
        if (test_parameters.amplitude) > MIN_AMPLITUDE:
            test_parameters.amplitude -= 2
            self.test_amplitude_label.setText(str(test_parameters.amplitude))
            self.test_amplitude_label.adjustSize()
            self.get_updated_test_parameters(test_parameters)
            
    def decrease_frequency(self, test_parameters):
        # if self.frequency > MIN_FREQ:
        #     if self.frequency == 10:
        #         self.frequency = 0
        #     else: 
        #         self.frequency  = self.frequency - 5
        #     self.test_frequency_label.setText(str(self.frequency))
        #     self.test_frequency_label.adjustSize()
            
        #     self.get_updated_test_parameters()
        if test_parameters.frequency > MIN_FREQ:
            if test_parameters.frequency == 10:
                test_parameters.frequency = 0
            else: 
                test_parameters.frequency -= 5
            self.test_frequency_label.setText(str(test_parameters.frequency))
            self.test_frequency_label.adjustSize()
            
            self.get_updated_test_parameters(test_parameters)
            
    def decrease_imp(self, test_parameters):
        # if self.imp > MIN_IMP:
        #     if self.imp == 20:
        #         self.imp = 0
        #     else: 
        #         self.imp  = self.imp - 10
        #     self.test_imp_label.setText(str(self.imp))
        #     self.test_imp_label.adjustSize()
        #     self.get_updated_test_parameters()
        if test_parameters.imp > MIN_IMP:
            if test_parameters.imp == 20:
                test_parameters.imp = 0
            else: 
                test_parameters.imp  -= 10
            self.test_imp_label.setText(str(test_parameters.imp))
            self.test_imp_label.adjustSize()
            self.get_updated_test_parameters(test_parameters)
            
    def get_updated_test_parameters(self, test_parameters):
        #self.event_function("New_test_parameters") ## MAIS JE NE COMPRENDS PAS OU ON DÉFINI event_function?
        #self.send_test_parameters_button = CommandButton("command_augmente_amplitude")
        #self.send_test_parameters_button.clicked.connect(lambda : self.event_function(self.send_test_parameters_button.get_command()))
        test_parameters = numpy.array([test_parameters.amplitude,test_parameters.frequency,test_parameters.imp])
        # print(test_parameters)
        # return(self.test_parameters)

        
