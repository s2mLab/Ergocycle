"""
Created on Wed Feb 23 17:20:00 2022

@author: Frédérique Leclerc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
#from Parameters import Parameters
#import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080


class StimulationWindow(QWidget):
    def __init__(self, init_parameters):
        super(StimulationWindow, self).__init__()
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre des instructions ###
        self.setGeometry(100, 50, SCREEN_WIDTH/1.2, SCREEN_HEIGTH/1.15)
        self.setWindowTitle("Menu des stimulations")
        self.setStyleSheet("background-color: white;")
        current_parameters = init_parameters
        self.initUI(current_parameters)
        #self.initUI(init_parameters)
    def initUI(self, current_parameters):  
        ### 1.3. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())
        ### 1.4. Titre menu des instructions ###
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Stimulations en cours...")
        self.menu_label.move(650,100)
        self.menu_label.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ### 1.5. Bouton d'arrêt ##
        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setText("  ARRÊT  ")
        self.stop_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.stop_button.move(1300, 50)
        self.stop_button.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.stop_button.adjustSize()
        self.stop_button.clicked.connect(lambda:self.clicked_stop()) 
        ### 1.6. Label d'amplitude, fréquence et durée d'impulsion ##
        self.amplitude_label = QtWidgets.QLabel(self)
        self.amplitude_label.setText("Amplitude (mA):")
        self.amplitude_label.move(400,300)
        self.amplitude_label.setFont(QFont('Arial', 12))
        self.amplitude_label.adjustSize()

        self.frequency_label = QtWidgets.QLabel(self)
        self.frequency_label.setText("Fréquence (Hz):")
        self.frequency_label.move(800,300)
        self.frequency_label.setFont(QFont('Arial', 12))
        self.frequency_label.adjustSize()

        self.length_imp_label = QtWidgets.QLabel(self)
        self.length_imp_label.setText("Durée d'impulsion (μs):")
        self.length_imp_label.move(1200,(300))
        self.length_imp_label.setFont(QFont('Arial', 12))
        self.length_imp_label.adjustSize()
        ### 1.7. Label d'électrode ##
        self.electrode1_label = QtWidgets.QLabel(self)
        self.electrode1_label.setText("Électrode 1 (droite):")
        self.electrode1_label.move(75,375)
        self.electrode1_label.setFont(QFont('Arial', 12))
        self.electrode1_label.adjustSize()

        self.electrode2_label = QtWidgets.QLabel(self)
        self.electrode2_label.setText("Électrode 2 (droite):")
        self.electrode2_label.move(75,450)
        self.electrode2_label.setFont(QFont('Arial', 12))
        self.electrode2_label.adjustSize()

        self.electrode3_label = QtWidgets.QLabel(self)
        self.electrode3_label.setText("Électrode 3 (droite):")
        self.electrode3_label.move(75,525)
        self.electrode3_label.setFont(QFont('Arial', 12))
        self.electrode3_label.adjustSize()

        self.electrode4_label = QtWidgets.QLabel(self)
        self.electrode4_label.setText("Électrode 4 (droite):")
        self.electrode4_label.move(75,600)
        self.electrode4_label.setFont(QFont('Arial', 12))
        self.electrode4_label.adjustSize()

        self.electrode5_label = QtWidgets.QLabel(self)
        self.electrode5_label.setText("Électrode 5 (gauche):")
        self.electrode5_label.move(75,675)
        self.electrode5_label.setFont(QFont('Arial', 12))
        self.electrode5_label.adjustSize()

        self.electrode6_label = QtWidgets.QLabel(self)
        self.electrode6_label.setText("Électrode 6 (gauche):")
        self.electrode6_label.move(75,750)
        self.electrode6_label.setFont(QFont('Arial', 12))
        self.electrode6_label.adjustSize()

        self.electrode7_label = QtWidgets.QLabel(self)
        self.electrode7_label.setText("Électrode 7 (gauche):")
        self.electrode7_label.move(75,825)
        self.electrode7_label.setFont(QFont('Arial', 12))
        self.electrode7_label.adjustSize()

        self.electrode8_label = QtWidgets.QLabel(self)
        self.electrode8_label.setText("Électrode 8 (gauche):")
        self.electrode8_label.move(75,900)
        self.electrode8_label.setFont(QFont('Arial', 12))
        self.electrode8_label.adjustSize()
        #print("Amplitudes enregistrées: ", current_parameters.get_electrode1_amplitude(),  current_parameters.get_electrode2_amplitude(),  current_parameters.get_electrode3_amplitude(),  current_parameters.get_electrode4_amplitude(),  current_parameters.get_electrode5_amplitude(), current_parameters.get_electrode6_amplitude(),  current_parameters.get_electrode7_amplitude(),  current_parameters.get_electrode8_amplitude())
        #print("Fréquences enregistrées: ", init_parameters.get_electrode1_frequency(),  init_parameters.get_electrode2_frequency(),  init_parameters.get_electrode3_frequency(),  init_parameters.get_electrode4_frequency(),  init_parameters.get_electrode5_frequency(), init_parameters.get_electrode6_frequency(),  init_parameters.get_electrode7_frequency(),  init_parameters.get_electrode8_frequency())
        #print("Durées d'imp enregistrées: ", init_parameters.get_electrode1_length_imp(),  init_parameters.get_electrode2_length_imp(),  init_parameters.get_electrode3_length_imp(),  init_parameters.get_electrode4_length_imp(),  init_parameters.get_electrode5_length_imp(), init_parameters.get_electrode6_length_imp(),  init_parameters.get_electrode7_length_imp(),  init_parameters.get_electrode8_length_imp())
        
        ### 1.8. Placer toutes les amplitudes selon l'électrode ###
        self.current_amplitude1_label = QtWidgets.QLabel(self)
        self.current_amplitude1_label.setText(str(current_parameters.get_electrode1_amplitude()))
        self.current_amplitude1_label.move(450,375)
        self.current_amplitude1_label.setFont(QFont('Arial', 12))
        self.current_amplitude1_label.adjustSize()

        self.current_amplitude2_label = QtWidgets.QLabel(self)
        self.current_amplitude2_label.setText(str(current_parameters.get_electrode2_amplitude()))
        self.current_amplitude2_label.move(450,450)
        self.current_amplitude2_label.setFont(QFont('Arial', 12))
        self.current_amplitude2_label.adjustSize()

        self.current_amplitude3_label = QtWidgets.QLabel(self)
        self.current_amplitude3_label.setText(str(current_parameters.get_electrode3_amplitude()))
        self.current_amplitude3_label.move(450,525)
        self.current_amplitude3_label.setFont(QFont('Arial', 12))
        self.current_amplitude3_label.adjustSize()

        self.current_amplitude4_label = QtWidgets.QLabel(self)
        self.current_amplitude4_label.setText(str(current_parameters.get_electrode4_amplitude()))
        self.current_amplitude4_label.move(450,600)
        self.current_amplitude4_label.setFont(QFont('Arial', 12))
        self.current_amplitude4_label.adjustSize()

        self.current_amplitude5_label = QtWidgets.QLabel(self)
        self.current_amplitude5_label.setText(str(current_parameters.get_electrode5_amplitude()))
        self.current_amplitude5_label.move(450,675)
        self.current_amplitude5_label.setFont(QFont('Arial', 12))
        self.current_amplitude5_label.adjustSize()

        self.current_amplitude6_label = QtWidgets.QLabel(self)
        self.current_amplitude6_label.setText(str(current_parameters.get_electrode6_amplitude()))
        self.current_amplitude6_label.move(450,750)
        self.current_amplitude6_label.setFont(QFont('Arial', 12))
        self.current_amplitude6_label.adjustSize()

        self.current_amplitude7_label = QtWidgets.QLabel(self)
        self.current_amplitude7_label.setText(str(current_parameters.get_electrode7_amplitude()))
        self.current_amplitude7_label.move(450,825)
        self.current_amplitude7_label.setFont(QFont('Arial', 12))
        self.current_amplitude7_label.adjustSize()

        self.current_amplitude8_label = QtWidgets.QLabel(self)
        self.current_amplitude8_label.setText(str(current_parameters.get_electrode8_amplitude()))
        self.current_amplitude8_label.move(450,900)
        self.current_amplitude8_label.setFont(QFont('Arial', 12))
        self.current_amplitude8_label.adjustSize()

        ### 1.9. Placer toutes les fréquences selon l'électrode ###
        self.current_frequency1_label = QtWidgets.QLabel(self)
        self.current_frequency1_label.setText(str(current_parameters.get_electrode1_frequency()))
        self.current_frequency1_label.move(850,375)
        self.current_frequency1_label.setFont(QFont('Arial', 12))
        self.current_frequency1_label.adjustSize()

        self.current_frequency2_label = QtWidgets.QLabel(self)
        self.current_frequency2_label.setText(str(current_parameters.get_electrode2_frequency()))
        self.current_frequency2_label.move(850,450)
        self.current_frequency2_label.setFont(QFont('Arial', 12))
        self.current_frequency2_label.adjustSize()

        self.current_frequency3_label = QtWidgets.QLabel(self)
        self.current_frequency3_label.setText(str(current_parameters.get_electrode3_frequency()))
        self.current_frequency3_label.move(850,525)
        self.current_frequency3_label.setFont(QFont('Arial', 12))
        self.current_frequency3_label.adjustSize()

        self.current_frequency4_label = QtWidgets.QLabel(self)
        self.current_frequency4_label.setText(str(current_parameters.get_electrode4_frequency()))
        self.current_frequency4_label.move(850,600)
        self.current_frequency4_label.setFont(QFont('Arial', 12))
        self.current_frequency4_label.adjustSize()

        self.current_frequency5_label = QtWidgets.QLabel(self)
        self.current_frequency5_label.setText(str(current_parameters.get_electrode5_frequency()))
        self.current_frequency5_label.move(850,675)
        self.current_frequency5_label.setFont(QFont('Arial', 12))
        self.current_frequency5_label.adjustSize()

        self.current_frequency6_label = QtWidgets.QLabel(self)
        self.current_frequency6_label.setText(str(current_parameters.get_electrode6_frequency()))
        self.current_frequency6_label.move(850,750)
        self.current_frequency6_label.setFont(QFont('Arial', 12))
        self.current_frequency6_label.adjustSize()

        self.current_frequency7_label = QtWidgets.QLabel(self)
        self.current_frequency7_label.setText(str(current_parameters.get_electrode7_frequency()))
        self.current_frequency7_label.move(850,825)
        self.current_frequency7_label.setFont(QFont('Arial', 12))
        self.current_frequency7_label.adjustSize()

        self.current_frequency8_label = QtWidgets.QLabel(self)
        self.current_frequency8_label.setText(str(current_parameters.get_electrode8_frequency()))
        self.current_frequency8_label.move(850,900)
        self.current_frequency8_label.setFont(QFont('Arial', 12))
        self.current_frequency8_label.adjustSize()

        ### 1.10. Placer toutes les durée impulsion selon l'électrode ###
        self.current_imp_label1_label = QtWidgets.QLabel(self)
        self.current_imp_label1_label.setText(str(current_parameters.get_electrode1_length_imp()))
        self.current_imp_label1_label.move(1275,375)
        self.current_imp_label1_label.setFont(QFont('Arial', 12))
        self.current_imp_label1_label.adjustSize()

        self.current_imp_label2_label = QtWidgets.QLabel(self)
        self.current_imp_label2_label.setText(str(current_parameters.get_electrode2_length_imp()))
        self.current_imp_label2_label.move(1275,450)
        self.current_imp_label2_label.setFont(QFont('Arial', 12))
        self.current_imp_label2_label.adjustSize()

        self.current_imp_label3_label = QtWidgets.QLabel(self)
        self.current_imp_label3_label.setText(str(current_parameters.get_electrode3_length_imp()))
        self.current_imp_label3_label.move(1275,525)
        self.current_imp_label3_label.setFont(QFont('Arial', 12))
        self.current_imp_label3_label.adjustSize()

        self.current_imp_label4_label = QtWidgets.QLabel(self)
        self.current_imp_label4_label.setText(str(current_parameters.get_electrode4_length_imp()))
        self.current_imp_label4_label.move(1275,600)
        self.current_imp_label4_label.setFont(QFont('Arial', 12))
        self.current_imp_label4_label.adjustSize()

        self.current_imp_label5_label = QtWidgets.QLabel(self)
        self.current_imp_label5_label.setText(str(current_parameters.get_electrode5_length_imp()))
        self.current_imp_label5_label.move(1275,675)
        self.current_imp_label5_label.setFont(QFont('Arial', 12))
        self.current_imp_label5_label.adjustSize()

        self.current_imp_label6_label = QtWidgets.QLabel(self)
        self.current_imp_label6_label.setText(str(current_parameters.get_electrode6_length_imp()))
        self.current_imp_label6_label.move(1275,750)
        self.current_imp_label6_label.setFont(QFont('Arial', 12))
        self.current_imp_label6_label.adjustSize()

        self.current_imp_label7_label = QtWidgets.QLabel(self)
        self.current_imp_label7_label.setText(str(current_parameters.get_electrode7_length_imp()))
        self.current_imp_label7_label.move(1275,825)
        self.current_imp_label7_label.setFont(QFont('Arial', 12))
        self.current_imp_label7_label.adjustSize()

        self.current_imp_label8_label = QtWidgets.QLabel(self)
        self.current_imp_label8_label.setText(str(current_parameters.get_electrode8_length_imp()))
        self.current_imp_label8_label.move(1275,900)
        self.current_imp_label8_label.setFont(QFont('Arial', 12))
        self.current_imp_label8_label.adjustSize()
    def clicked_stop(self):
        self.close()
