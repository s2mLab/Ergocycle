"""
Created on Wed Feb 23 14:10:00 2022

@author: Frédérique Leclerc
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
#import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

class DangerPopUp(QWidget):
    def __init__(self, init_parameters):
        super(DangerPopUp, self).__init__()
         ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre PopUp ###
        self.setGeometry(600, 300, SCREEN_WIDTH/3, SCREEN_HEIGTH/3)
        self.setWindowTitle("Averitissement")
        self.setStyleSheet("background-color: white;")
        self.initUI(self)
    def initUI(self, init_parameters):  
        ### 1.3. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save('image_400.jpg')
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())