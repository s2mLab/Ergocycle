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
#from CommandButton import CommandButton as CommandButton
#from StartWindow import StartWindow
#from MainWindowStim import MainWindowStim
#from Stimulator import Stimulator

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080
MAX_AMPLITUDE = 130
MIN_AMPLITUDE = 0
MAX_FREQ = 50
MIN_FREQ = 0
MAX_IMP = 500
MIN_IMP = 0

class TestingWindow(QWidget):
    def __init__(self):
        super(TestingWindow, self).__init__()
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre des instructions ###
        self.setGeometry(300, 300, SCREEN_WIDTH/1.7, SCREEN_HEIGTH/1.8)
        self.setWindowTitle("Test des stimulations")
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
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Veuillez tester les paramètres de stimulation à l'aide des boutons + et  - .\nLorsque terminé, veuillez cliquer sur tests complétés pour débuter\nl'entraînment en stimulation. ")
        self.menu_label.move(200,60)
        self.menu_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ### 1.4 - Initialiser les labels pour les 3 paramètres ###
        ### 1.4.1 - Layout des labels de la fenêtre de stimulation ###
        self.amplitude_label = QtWidgets.QLabel(self)
        self.amplitude_label.setText("Amplitude (mA):")
        self.amplitude_label.move(250,200)
        self.amplitude_label.setFont(QFont('Arial', 12))
        self.amplitude_label.adjustSize()

        self.frequency_label = QtWidgets.QLabel(self)
        self.frequency_label.setText("Fréquence (Hz):")
        self.frequency_label.move(250,250)
        self.frequency_label.setFont(QFont('Arial', 12))
        self.frequency_label.adjustSize()

        self.length_imp_label = QtWidgets.QLabel(self)
        self.length_imp_label.setText("Durée d'impulsion (μs):")
        self.length_imp_label.move(250,300)
        self.length_imp_label.setFont(QFont('Arial', 12))
        self.length_imp_label.adjustSize()
        ### 1.4.2 - Valeur initiales ### 
        self.amplitude = 0
        self.frequency = 30
        self.imp = 200
        self.test_amplitude_label = QtWidgets.QLabel(self)
        self.test_amplitude_label.setText(str(self.amplitude))
        self.test_amplitude_label.move(600,200)
        self.test_amplitude_label.setFont(QFont('Arial', 12))
        self.test_amplitude_label.adjustSize()
        self.test_frequency_label = QtWidgets.QLabel(self)
        self.test_frequency_label.setText(str(self.frequency))
        self.test_frequency_label.move(600,250)
        self.test_frequency_label.setFont(QFont('Arial', 12))
        self.test_frequency_label.adjustSize()
        self.test_imp_label = QtWidgets.QLabel(self)
        self.test_imp_label.setText(str(self.imp))
        self.test_imp_label.move(600,300)
        self.test_imp_label.setFont(QFont('Arial', 12))
        self.test_imp_label.adjustSize()
        ### 1.4.3 - Boutons "+" ###
        self.increase_amp_button = QtWidgets.QPushButton(self)
        self.increase_amp_button.setText(" + ")
        self.increase_amp_button.move(650,200)
        self.increase_amp_button.setFont(QFont('Arial', 14))
        self.increase_amp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_amp_button.adjustSize()
        self.increase_amp_button.clicked.connect(lambda:self.increase_amplitude()) 

        self.increase_freq_button = QtWidgets.QPushButton(self)
        self.increase_freq_button.setText(" + ")
        self.increase_freq_button.move(650,250)
        self.increase_freq_button.setFont(QFont('Arial', 14))
        self.increase_freq_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_freq_button.adjustSize()
        self.increase_freq_button.clicked.connect(lambda:self.increase_frequency()) 

        self.increase_imp_button = QtWidgets.QPushButton(self)
        self.increase_imp_button.setText(" + ")
        self.increase_imp_button.move(650,300)
        self.increase_imp_button.setFont(QFont('Arial', 14))
        self.increase_imp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_imp_button.adjustSize()
        self.increase_imp_button.clicked.connect(lambda:self.increase_imp()) 
        ### 1.4.4 - Boutons "-" ###
        self.decrease_amp_button = QtWidgets.QPushButton(self)
        self.decrease_amp_button.setText("  - ")
        self.decrease_amp_button.move(550,200)
        self.decrease_amp_button.setFont(QFont('Arial', 14))
        self.decrease_amp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_amp_button.adjustSize()
        self.decrease_amp_button.clicked.connect(lambda:self.decrease_amplitude())
        
        self.decrease_freq_button = QtWidgets.QPushButton(self)
        self.decrease_freq_button.setText("  - ")
        self.decrease_freq_button.move(550,250)
        self.decrease_freq_button.setFont(QFont('Arial', 14))
        self.decrease_freq_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_freq_button.adjustSize()
        self.decrease_freq_button.clicked.connect(lambda:self.decrease_frequency()) 

        self.decrease_imp_button = QtWidgets.QPushButton(self)
        self.decrease_imp_button.setText("  - ")
        self.decrease_imp_button.move(550,300)
        self.decrease_imp_button.setFont(QFont('Arial', 14))
        self.decrease_imp_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_imp_button.adjustSize()
        self.decrease_imp_button.clicked.connect(lambda:self.decrease_imp()) 
        ### 1.5. Bouton pour retourner au menu initial ###
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setText("     Tests complétés     ")
        self.back_button.setStyleSheet("background-color: red; border: 1 solid;")
        self.back_button.move(450, 450)
        self.back_button.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.back_button.adjustSize()
        self.back_button.clicked.connect(lambda:self.clicked_back())
        ### 1.6. Bouton pour retourner au menu principal ###
        #self.stim_button = QtWidgets.QPushButton(self)
        #self.stim_button.setText("   Tests complétés   ")
        #self.stim_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        #self.stim_button.move(700, 450)
        #self.stim_button.setFont(QFont('Arial', 12, weight = QFont.Bold))
        #self.stim_button.adjustSize()
        #self.stim_button.clicked.connect(lambda:self.clicked_stim())
    
    def clicked_back(self):
        #self.start_menu = StartWindow()
        #self.start_menu.show()
        self.close()
        #self.update()

    #def clicked_stim(self):
        #self.main_menu = MainWindowStim()
        #self.main_menu.show()
        #self.close()
        #self.update()

    def increase_amplitude(self):
        if (self.amplitude) < MAX_AMPLITUDE:
            self.amplitude = self.amplitude + 2
            self.test_amplitude_label.setText(str(self.amplitude))
            self.test_amplitude_label.adjustSize()
            self.get_updated_test_parameters()
    def increase_frequency(self):
        if (self.frequency) < MAX_FREQ:
            if (self.frequency) == 0:
                self.frequency = 10
            else:
                self.frequency = self.frequency + 5
            self.test_frequency_label.setText(str(self.frequency))
            self.test_frequency_label.adjustSize()
            self.get_updated_test_parameters()
    def increase_imp(self):
        if (self.imp) < MAX_IMP:
            if (self.imp) == 0:
                self.imp = 20
            else:
                self.imp = self.imp + 10
            self.test_imp_label.setText(str(self.imp))
            self.test_imp_label.adjustSize()
            self.get_updated_test_parameters()
    def decrease_amplitude(self):
        if (self.amplitude) > MIN_AMPLITUDE:
            self.amplitude = self.amplitude - 2
            self.test_amplitude_label.setText(str(self.amplitude))
            self.test_amplitude_label.adjustSize()
            self.get_updated_test_parameters()
    def decrease_frequency(self):
        if self.frequency > MIN_FREQ:
            if self.frequency == 10:
                self.frequency = 0
            else: 
                self.frequency  = self.frequency - 5
            self.test_frequency_label.setText(str(self.frequency))
            self.test_frequency_label.adjustSize()
            self.get_updated_test_parameters()
    def decrease_imp(self):
        if self.imp > MIN_IMP:
            if self.imp == 20:
                self.imp = 0
            else: 
                self.imp  = self.imp - 10
            self.test_imp_label.setText(str(self.imp))
            self.test_imp_label.adjustSize()
            self.get_updated_test_parameters()
    def get_updated_test_parameters(self):
        #self.event_function("New_test_parameters") ## MAIS JE NE COMPRENDS PAS OU ON DÉFINI event_function?
        #self.send_test_parameters_button = CommandButton("command_augmente_amplitude")
        #self.send_test_parameters_button.clicked.connect(lambda : self.event_function(self.send_test_parameters_button.get_command()))
        self.test_parameters = numpy.array([self.amplitude,self.frequency,self.imp])
        print(self.test_parameters)
        return(self.test_parameters)

        
