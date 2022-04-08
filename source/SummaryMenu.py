# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:43:34 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
# import time
# import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080

class SummaryMenu(QWidget):
    def __init__(self):
        super(SummaryMenu, self).__init__()
        
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        self.setWindowTitle("Résumé de la séance")
        self.setStyleSheet("background-color: white;")
        
        self.initUI()

    def initUI(self):        
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Séance terminée")
        self.menu_label.move(825,100)
        self.menu_label.setFont(QFont('Arial', 32, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.summary_label = QtWidgets.QLabel(self)
        self.summary_label.setText("Résumé de la séance:")
        self.summary_label.move(300,200)
        self.summary_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.summary_label.adjustSize()
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Ajouter les données que l'on veut afficher")
        self.label.move(300,300)
        self.label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.label.adjustSize()
        
        # TODO: Déterminer quelles données on veut afficher