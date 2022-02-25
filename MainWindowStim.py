"""
Created on Wed Feb 16 09:10:00 2022

@author: Frédérique Leclerc
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
from InstructionWindow import InstructionWindow
from StimulationWindow import StimulationWindow
from Parameters import Parameters
from DangerPopUp import DangerPopUp

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class MainWindowStim(QMainWindow):
    def __init__(self):
        super(MainWindowStim, self).__init__()
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre du menu principal ###
        self.setGeometry(100, 50, SCREEN_WIDTH/1.2, SCREEN_HEIGTH/1.15)
        self.setWindowTitle("Menu principal des stimulations électriques fonctionnelles")
        self.setStyleSheet("background-color: white;")
        ## 1.2. ##
        init_parameters = Parameters()
        self.initUI(init_parameters)
    
    def initUI(self, init_parameters):
        ### 1.3. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.4. Titre du menu principal ###
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Bienvenue au menu principal de l'interface usager des stimulations électriques fonctionnelles")
        self.menu_label.move(200,40)
        self.menu_label.setFont(QFont('Arial', 15, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ## 1.5.  Durée de l'entrainement (possiblement à retirer pour éviter la répétition avec UI du contrôle moteur) ##
        self.stim_training_length_label = QtWidgets.QLabel(self)
        self.stim_training_length_label.setText("Durée de l'entraînement en stimulation (min):")
        self.stim_training_length_label.move(10,150)
        self.stim_training_length_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.stim_training_length_label.adjustSize()
        
        self.stim_training_length_ComboBox = QtWidgets.QComboBox(self)
        self.stim_training_length_ComboBox.addItems(["5", "10", "15", "20", "25", "30"])
        self.stim_training_length_ComboBox.move(450,150)
        self.stim_training_length_ComboBox.setFont(QFont('Arial', 12))
        self.stim_training_length_ComboBox.adjustSize()

        ## 1.5. Définition des muscles à stimuler ##
        self.muscle_label = QtWidgets.QLabel(self)
        self.muscle_label.setText("Veuillez sélectionner les muscles à stimuler et l'électrode correspondante: ")
        self.muscle_label.move(10,200)
        self.muscle_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.muscle_label.adjustSize()

        self.electrode1_label = QtWidgets.QLabel(self)
        self.electrode1_label.setText("Électrode 1 (droite):")
        self.electrode1_label.move(10,250)
        self.electrode1_label.setFont(QFont('Arial', 12))
        self.electrode1_label.adjustSize()

        self.electrode1_ComboBox = QtWidgets.QComboBox(self)
        self.electrode1_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode1_ComboBox.move(200,250)
        self.electrode1_ComboBox.setFont(QFont('Arial', 12))
        self.electrode1_ComboBox.adjustSize()

        self.electrode2_label = QtWidgets.QLabel(self)
        self.electrode2_label.setText("Électrode 2 (droite):")
        self.electrode2_label.move(10,300)
        self.electrode2_label.setFont(QFont('Arial', 12))
        self.electrode2_label.adjustSize()

        self.electrode2_ComboBox = QtWidgets.QComboBox(self)
        self.electrode2_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode2_ComboBox.move(200,300)
        self.electrode2_ComboBox.setFont(QFont('Arial', 12))
        self.electrode2_ComboBox.adjustSize()

        self.electrode3_label = QtWidgets.QLabel(self)
        self.electrode3_label.setText("Électrode 3 (droite):")
        self.electrode3_label.move(10,350)
        self.electrode3_label.setFont(QFont('Arial', 12))
        self.electrode3_label.adjustSize()

        self.electrode3_ComboBox = QtWidgets.QComboBox(self)
        self.electrode3_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode3_ComboBox.move(200,350)
        self.electrode3_ComboBox.setFont(QFont('Arial', 12))
        self.electrode3_ComboBox.adjustSize()

        self.electrode4_label = QtWidgets.QLabel(self)
        self.electrode4_label.setText("Électrode 4 (droite):")
        self.electrode4_label.move(10,400)
        self.electrode4_label.setFont(QFont('Arial', 12))
        self.electrode4_label.adjustSize()
        
        self.electrode4_ComboBox = QtWidgets.QComboBox(self)
        self.electrode4_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode4_ComboBox.move(200,400)
        self.electrode4_ComboBox.setFont(QFont('Arial', 12))
        self.electrode4_ComboBox.adjustSize()

        ## GAUCHE ##
        self.electrode5_label = QtWidgets.QLabel(self)
        self.electrode5_label.setText("Électrode 5 (gauche):")
        self.electrode5_label.move(550,250)
        self.electrode5_label.setFont(QFont('Arial', 12))
        self.electrode5_label.adjustSize()

        self.electrode5_ComboBox = QtWidgets.QComboBox(self)
        self.electrode5_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode5_ComboBox.move(750,250)
        self.electrode5_ComboBox.setFont(QFont('Arial', 12))
        self.electrode5_ComboBox.adjustSize()

        self.electrode6_label = QtWidgets.QLabel(self)
        self.electrode6_label.setText("Électrode 6 (gauche):")
        self.electrode6_label.move(550,300)
        self.electrode6_label.setFont(QFont('Arial', 12))
        self.electrode6_label.adjustSize()

        self.electrode6_ComboBox = QtWidgets.QComboBox(self)
        self.electrode6_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode6_ComboBox.move(750,300)
        self.electrode6_ComboBox.setFont(QFont('Arial', 12))
        self.electrode6_ComboBox.adjustSize()

        self.electrode7_label = QtWidgets.QLabel(self)
        self.electrode7_label.setText("Électrode 7 (gauche):")
        self.electrode7_label.move(550,350)
        self.electrode7_label.setFont(QFont('Arial', 12))
        self.electrode7_label.adjustSize()

        self.electrode7_ComboBox = QtWidgets.QComboBox(self)
        self.electrode7_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode7_ComboBox.move(750,350)
        self.electrode7_ComboBox.setFont(QFont('Arial', 12))
        self.electrode7_ComboBox.adjustSize()

        self.electrode8_label = QtWidgets.QLabel(self)
        self.electrode8_label.setText("Électrode 8 (gauche):")
        self.electrode8_label.move(550,400)
        self.electrode8_label.setFont(QFont('Arial', 12))
        self.electrode8_label.adjustSize()
        
        self.electrode8_ComboBox = QtWidgets.QComboBox(self)
        self.electrode8_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode8_ComboBox.move(750,400)
        self.electrode8_ComboBox.setFont(QFont('Arial', 12))
        self.electrode8_ComboBox.adjustSize()

        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("  Soumettre  ")
        self.submit_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_button.move(1400, 400)
        self.submit_button.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.submit_button.adjustSize()
        self.submit_button.clicked.connect(lambda:self.clicked_more(init_parameters))

        self.param_label = QtWidgets.QLabel(self)
        self.electrode11_label = QtWidgets.QLabel(self)
        self.electrode22_label = QtWidgets.QLabel(self)
        self.electrode33_label = QtWidgets.QLabel(self)
        self.electrode44_label = QtWidgets.QLabel(self)
        self.electrode55_label = QtWidgets.QLabel(self)
        self.electrode66_label = QtWidgets.QLabel(self)
        self.electrode77_label = QtWidgets.QLabel(self)
        self.electrode88_label = QtWidgets.QLabel(self)
        self.amplitude_label = QtWidgets.QLabel(self)
        self.length_imp_label = QtWidgets.QLabel(self)
        self.frequency_label = QtWidgets.QLabel(self)

        self.amplitude_list_int = list(range(0,132,2))
        self.frequency_list_int = list(range(0,55,5)) ## Devrait commencer à 10 mais je dois mettre à zero si jamais electrode pas utilisée. Si personne entre 5 je vais mettre la stim à 0
        self.length_imp_list_int = list(range(0,510,10)) ## Devrait commencer à 20 mais je dois mettre à zero si jamais electrode pas utilisée. Si personne entre 10 je vais mettre la stim à 0
        
        self.amplitude_list1 = map(str,self.amplitude_list_int)
        self.amplitude_list2 = map(str,self.amplitude_list_int)
        self.amplitude_list3 = map(str,self.amplitude_list_int)
        self.amplitude_list4 = map(str,self.amplitude_list_int)
        self.amplitude_list5 = map(str,self.amplitude_list_int)
        self.amplitude_list6 = map(str,self.amplitude_list_int)
        self.amplitude_list7 = map(str,self.amplitude_list_int)
        self.amplitude_list8 = map(str,self.amplitude_list_int)

        self.frequency_list1 = map(str,self.frequency_list_int)
        self.frequency_list2 = map(str,self.frequency_list_int)
        self.frequency_list3 = map(str,self.frequency_list_int)
        self.frequency_list4 = map(str,self.frequency_list_int)
        self.frequency_list5 = map(str,self.frequency_list_int)
        self.frequency_list6 = map(str,self.frequency_list_int)
        self.frequency_list7 = map(str,self.frequency_list_int)
        self.frequency_list8 = map(str,self.frequency_list_int)

        self.length_imp_list1 = map(str,self.length_imp_list_int)
        self.length_imp_list2 = map(str,self.length_imp_list_int)
        self.length_imp_list3 = map(str,self.length_imp_list_int)
        self.length_imp_list4 = map(str,self.length_imp_list_int)
        self.length_imp_list5 = map(str,self.length_imp_list_int)
        self.length_imp_list6 = map(str,self.length_imp_list_int)
        self.length_imp_list7 = map(str,self.length_imp_list_int)
        self.length_imp_list8 = map(str,self.length_imp_list_int)

        self.electrode1_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode2_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode3_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode4_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode5_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode6_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode7_ComboBox_amplitude = QtWidgets.QComboBox(self)
        self.electrode8_ComboBox_amplitude = QtWidgets.QComboBox(self)

        self.electrode1_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode2_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode3_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode4_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode5_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode6_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode7_ComboBox_frequency = QtWidgets.QComboBox(self)
        self.electrode8_ComboBox_frequency = QtWidgets.QComboBox(self)

        self.electrode1_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode2_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode3_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode4_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode5_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode6_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode7_ComboBox_length_imp = QtWidgets.QComboBox(self)
        self.electrode8_ComboBox_length_imp = QtWidgets.QComboBox(self)

        self.submit_final_button = QtWidgets.QPushButton(self)
        

    def clicked_more(self, init_parameters): ## Possiblement regarder si on peut mettre les label inactive si choix de muscle plus haut est aucun "Aucun"
        self.param_label.setText("Veuillez sélectionner les valeurs des paramètres de stimulation: ")
        self.param_label.move(10,450)
        self.param_label.setFont(QFont('Arial', 12, weight = QFont.Bold))
        self.param_label.adjustSize()

        self.electrode11_label.setText("Électrode 1 (droite):")
        self.electrode11_label.move(10,550)
        self.electrode11_label.setFont(QFont('Arial', 12))
        self.electrode11_label.adjustSize()

        self.electrode22_label.setText("Électrode 2 (droite):")
        self.electrode22_label.move(10,600)
        self.electrode22_label.setFont(QFont('Arial', 12))
        self.electrode22_label.adjustSize()

        self.electrode33_label.setText("Électrode 3 (droite):")
        self.electrode33_label.move(10,650)
        self.electrode33_label.setFont(QFont('Arial', 12))
        self.electrode33_label.adjustSize()

        self.electrode44_label.setText("Électrode 4 (droite):")
        self.electrode44_label.move(10,700)
        self.electrode44_label.setFont(QFont('Arial', 12))
        self.electrode44_label.adjustSize()

        self.electrode55_label.setText("Électrode 5 (gauche):")
        self.electrode55_label.move(10,750)
        self.electrode55_label.setFont(QFont('Arial', 12))
        self.electrode55_label.adjustSize()
    
        self.electrode66_label.setText("Électrode 6 (gauche):")
        self.electrode66_label.move(10,800)
        self.electrode66_label.setFont(QFont('Arial', 12))
        self.electrode66_label.adjustSize()

        self.electrode77_label.setText("Électrode 7 (gauche):")
        self.electrode77_label.move(10,850)
        self.electrode77_label.setFont(QFont('Arial', 12))
        self.electrode77_label.adjustSize()

        self.electrode88_label.setText("Électrode 8 (gauche):")
        self.electrode88_label.move(10,900)
        self.electrode88_label.setFont(QFont('Arial', 12))
        self.electrode88_label.adjustSize()

        ## Tous les combos box des paramètres de stimulation ##
        self.amplitude_label.setText("Amplitude (mA):")
        self.amplitude_label.move(400,(500))
        self.amplitude_label.setFont(QFont('Arial', 12))
        self.amplitude_label.adjustSize()

        self.frequency_label.setText("Fréquence (Hz):")
        self.frequency_label.move(750,500)
        self.frequency_label.setFont(QFont('Arial', 12))
        self.frequency_label.adjustSize()

        self.length_imp_label.setText("Durée d'impulsion (μs):")
        self.length_imp_label.move(1200,(500))
        self.length_imp_label.setFont(QFont('Arial', 12))
        self.length_imp_label.adjustSize()

        self.electrode1_ComboBox_amplitude.addItems(self.amplitude_list1)
        self.electrode1_ComboBox_amplitude.move(400,550)
        self.electrode1_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode1_ComboBox_amplitude.adjustSize()

        self.electrode2_ComboBox_amplitude.addItems(self.amplitude_list2)
        self.electrode2_ComboBox_amplitude.move(400,600)
        self.electrode2_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode2_ComboBox_amplitude.adjustSize()

        self.electrode3_ComboBox_amplitude.addItems(self.amplitude_list3)
        self.electrode3_ComboBox_amplitude.move(400,650)
        self.electrode3_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode3_ComboBox_amplitude.adjustSize()

        self.electrode4_ComboBox_amplitude.addItems(self.amplitude_list4)
        self.electrode4_ComboBox_amplitude.move(400,700)
        self.electrode4_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode4_ComboBox_amplitude.adjustSize()

        self.electrode5_ComboBox_amplitude.addItems(self.amplitude_list5)
        self.electrode5_ComboBox_amplitude.move(400,750)
        self.electrode5_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode5_ComboBox_amplitude.adjustSize()

        self.electrode6_ComboBox_amplitude.addItems(self.amplitude_list6)
        self.electrode6_ComboBox_amplitude.move(400,800)
        self.electrode6_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode6_ComboBox_amplitude.adjustSize()

        self.electrode7_ComboBox_amplitude.addItems(self.amplitude_list7)
        self.electrode7_ComboBox_amplitude.move(400,850)
        self.electrode7_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode7_ComboBox_amplitude.adjustSize()

        self.electrode8_ComboBox_amplitude.addItems(self.amplitude_list8)
        self.electrode8_ComboBox_amplitude.move(400,900)
        self.electrode8_ComboBox_amplitude.setFont(QFont('Arial', 12))
        self.electrode8_ComboBox_amplitude.adjustSize()

        self.electrode1_ComboBox_frequency.addItems(self.frequency_list1)
        self.electrode1_ComboBox_frequency.move(750,550)
        self.electrode1_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode1_ComboBox_frequency.adjustSize()

        self.electrode2_ComboBox_frequency.addItems(self.frequency_list2)
        self.electrode2_ComboBox_frequency.move(750,600)
        self.electrode2_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode2_ComboBox_frequency.adjustSize()

        self.electrode3_ComboBox_frequency.addItems(self.frequency_list3)
        self.electrode3_ComboBox_frequency.move(750,650)
        self.electrode3_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode3_ComboBox_frequency.adjustSize()

        self.electrode4_ComboBox_frequency.addItems(self.frequency_list4)
        self.electrode4_ComboBox_frequency.move(750,700)
        self.electrode4_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode4_ComboBox_frequency.adjustSize()

        self.electrode5_ComboBox_frequency.addItems(self.frequency_list5)
        self.electrode5_ComboBox_frequency.move(750,750)
        self.electrode5_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode5_ComboBox_frequency.adjustSize()

        self.electrode6_ComboBox_frequency.addItems(self.frequency_list6)
        self.electrode6_ComboBox_frequency.move(750,800)
        self.electrode6_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode6_ComboBox_frequency.adjustSize()

        self.electrode7_ComboBox_frequency.addItems(self.frequency_list7)
        self.electrode7_ComboBox_frequency.move(750,850)
        self.electrode7_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode7_ComboBox_frequency.adjustSize()

        self.electrode8_ComboBox_frequency.addItems(self.frequency_list8)
        self.electrode8_ComboBox_frequency.move(750,900)
        self.electrode8_ComboBox_frequency.setFont(QFont('Arial', 12))
        self.electrode8_ComboBox_frequency.adjustSize()

        self.electrode1_ComboBox_length_imp.addItems(self.length_imp_list1)
        self.electrode1_ComboBox_length_imp.move(1200,550)
        self.electrode1_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode1_ComboBox_length_imp.adjustSize()

        self.electrode2_ComboBox_length_imp.addItems(self.length_imp_list2)
        self.electrode2_ComboBox_length_imp.move(1200,600)
        self.electrode2_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode2_ComboBox_length_imp.adjustSize()

        self.electrode3_ComboBox_length_imp.addItems(self.length_imp_list3)
        self.electrode3_ComboBox_length_imp.move(1200,650)
        self.electrode3_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode3_ComboBox_length_imp.adjustSize()

        self.electrode4_ComboBox_length_imp.addItems(self.length_imp_list4)
        self.electrode4_ComboBox_length_imp.move(1200,700)
        self.electrode4_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode4_ComboBox_length_imp.adjustSize()

        self.electrode5_ComboBox_length_imp.addItems(self.length_imp_list5)
        self.electrode5_ComboBox_length_imp.move(1200,750)
        self.electrode5_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode5_ComboBox_length_imp.adjustSize()

        self.electrode6_ComboBox_length_imp.addItems(self.length_imp_list6)
        self.electrode6_ComboBox_length_imp.move(1200,800)
        self.electrode6_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode6_ComboBox_length_imp.adjustSize()

        self.electrode7_ComboBox_length_imp.addItems(self.length_imp_list7)
        self.electrode7_ComboBox_length_imp.move(1200,850)
        self.electrode7_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode7_ComboBox_length_imp.adjustSize()

        self.electrode8_ComboBox_length_imp.addItems(self.length_imp_list8)
        self.electrode8_ComboBox_length_imp.move(1200,900)
        self.electrode8_ComboBox_length_imp.setFont(QFont('Arial', 12))
        self.electrode8_ComboBox_length_imp.adjustSize()

        self.submit_final_button.setText("  Soumettre  ")
        self.submit_final_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_final_button.move(1400, 900)
        self.submit_final_button.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.submit_final_button.adjustSize()
        self.submit_final_button.clicked.connect(lambda:self.clicked_next(init_parameters))
    
    def clicked_next(self, init_parameters):
        # 1 - Enregistrer les valeurs des paramètres entrées
        # 1.1 - Temps de stiumulation de l'entrainement (pour le menu de stimulation)
        init_parameters.set_stim_training_length(self.stim_training_length_ComboBox) 
        # 1.2 - Muscles à stimuler à chaque électrode (pour le menu des instructions)
        init_parameters.set_electrode1_muscle(self.electrode1_ComboBox) 
        init_parameters.set_electrode2_muscle(self.electrode2_ComboBox) 
        init_parameters.set_electrode3_muscle(self.electrode3_ComboBox)
        init_parameters.set_electrode4_muscle(self.electrode4_ComboBox) 
        init_parameters.set_electrode5_muscle(self.electrode5_ComboBox) 
        init_parameters.set_electrode6_muscle(self.electrode6_ComboBox) 
        init_parameters.set_electrode7_muscle(self.electrode7_ComboBox) 
        init_parameters.set_electrode8_muscle(self.electrode8_ComboBox) 
        # 1.3 - Amplitude à chaque électrode (pour le menu de stimulation)
        init_parameters.set_electrode1_amplitude(self.electrode1_ComboBox_amplitude)
        init_parameters.set_electrode2_amplitude(self.electrode2_ComboBox_amplitude)
        init_parameters.set_electrode3_amplitude(self.electrode3_ComboBox_amplitude)
        init_parameters.set_electrode4_amplitude(self.electrode4_ComboBox_amplitude)
        init_parameters.set_electrode5_amplitude(self.electrode5_ComboBox_amplitude)
        init_parameters.set_electrode6_amplitude(self.electrode6_ComboBox_amplitude)
        init_parameters.set_electrode7_amplitude(self.electrode7_ComboBox_amplitude)
        init_parameters.set_electrode8_amplitude(self.electrode8_ComboBox_amplitude)
        # 1.4 - Fréquence à chaque électrode (pour le menu de stimulation)
        init_parameters.set_electrode1_frequency(self.electrode1_ComboBox_frequency)
        init_parameters.set_electrode2_frequency(self.electrode2_ComboBox_frequency)
        init_parameters.set_electrode3_frequency(self.electrode3_ComboBox_frequency)
        init_parameters.set_electrode4_frequency(self.electrode4_ComboBox_frequency)
        init_parameters.set_electrode5_frequency(self.electrode5_ComboBox_frequency)
        init_parameters.set_electrode6_frequency(self.electrode6_ComboBox_frequency)
        init_parameters.set_electrode7_frequency(self.electrode7_ComboBox_frequency)
        init_parameters.set_electrode8_frequency(self.electrode8_ComboBox_frequency)
        # 1.5 - Durée de l'impulsion à chaque électrode (pour le menu de stimulation)
        init_parameters.set_electrode1_length_imp(self.electrode1_ComboBox_length_imp)
        init_parameters.set_electrode2_length_imp(self.electrode2_ComboBox_length_imp)
        init_parameters.set_electrode3_length_imp(self.electrode3_ComboBox_length_imp)
        init_parameters.set_electrode4_length_imp(self.electrode4_ComboBox_length_imp)
        init_parameters.set_electrode5_length_imp(self.electrode5_ComboBox_length_imp)
        init_parameters.set_electrode6_length_imp(self.electrode6_ComboBox_length_imp)
        init_parameters.set_electrode7_length_imp(self.electrode7_ComboBox_length_imp)
        init_parameters.set_electrode8_length_imp(self.electrode8_ComboBox_length_imp)
        # 2- vérification que tout est entrée (appel a la fonction is_completed)

        # 3- vérification du danger (appel a la fonction danger_check)

        # 4- Appel au bon menu (DangerPopUp ou InstructionMenu)
        self.instruction_window = InstructionWindow(init_parameters)
        #self.stim_window = StimulationWindow(init_parameters)
        self.close()
        self.instruction_window.show()
        self.update(init_parameters)

    def update(self, init_parameters):
        self.param_label.adjustSize()
        print("Paramètres enregistrés2: ", init_parameters.get_electrode1_amplitude(), "mA", init_parameters.get_stim_training_length(),"min")
        #print("Paramètres enregistrés:",init_parameters.get_electrode1_muscle(), init_parameters.get_electrode2_muscle(), init_parameters.get_electrode3_muscle(),init_parameters.get_electrode4_muscle(),init_parameters.get_electrode5_muscle(), init_parameters.get_electrode6_muscle(), init_parameters.get_electrode7_muscle(),init_parameters.get_electrode8_muscle())
        #print("Amplitudes enregistrées: ", init_parameters.get_electrode1_amplitude(),  init_parameters.get_electrode2_amplitude(),  init_parameters.get_electrode3_amplitude(),  init_parameters.get_electrode4_amplitude(),  init_parameters.get_electrode5_amplitude(), init_parameters.get_electrode6_amplitude(),  init_parameters.get_electrode7_amplitude(),  init_parameters.get_electrode8_amplitude())
        #print("Fréquences enregistrées: ", init_parameters.get_electrode1_frequency(),  init_parameters.get_electrode2_frequency(),  init_parameters.get_electrode3_frequency(),  init_parameters.get_electrode4_frequency(),  init_parameters.get_electrode5_frequency(), init_parameters.get_electrode6_frequency(),  init_parameters.get_electrode7_frequency(),  init_parameters.get_electrode8_frequency())
        #print("Durées d'imp enregistrées: ", init_parameters.get_electrode1_length_imp(),  init_parameters.get_electrode2_length_imp(),  init_parameters.get_electrode3_length_imp(),  init_parameters.get_electrode4_length_imp(),  init_parameters.get_electrode5_length_imp(), init_parameters.get_electrode6_length_imp(),  init_parameters.get_electrode7_length_imp(),  init_parameters.get_electrode8_length_imp())