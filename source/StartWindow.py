from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import numpy

from PIL import Image
from constants import *


class StartWindow(QWidget):
    def __init__(self):
        super(StartWindow, self).__init__()

        self.test_button = None
        self.training_button = None
        self.question_label = None
        self.title_label = None
        self.logo_jpg = None
        self.logo_label = None
        self.petite_imageS2M = None
        self.imageS2M = None

        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGHT)
        # 1.1. Initialise the window
        self.setWindowTitle("Interface usager des stimulations électriques fonctionnelles")
        self.setStyleSheet("background-color: white;")
        self.button_dictionary = {}

        self.init_ui()

    def init_ui(self):
        # 1.2. Put the logo in the left corner of the window
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save("image_400.jpg")
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_jpg = QPixmap("image_400.jpg")  # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())

        # 1.3. Menu title of instructions
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setText("Bienvenue dans l'interface usager des stimulations électriques fonctionnelles")
        self.title_label.move(400, 75)
        self.title_label.setFont(QFont("Arial", 20, weight=QFont.Bold))
        self.title_label.adjustSize()
        self.question_label = QtWidgets.QLabel(self)
        self.question_label.setText("Désirez-vous débuter un entraînement en stimulation ou effectuer des tests?")
        self.question_label.move(500, 300)
        self.question_label.setFont(QFont("Arial", 16))
        self.question_label.adjustSize()

        # 1.4. Start training button
        self.training_button = QtWidgets.QPushButton(self)
        self.training_button.setText("   Débuter un entraînement   ")
        self.training_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.training_button.move(150, 600)
        self.training_button.setFont(QFont("Arial", 30, weight=QFont.Bold))
        self.training_button.adjustSize()

        # 1.5. Test button
        self.test_button = QtWidgets.QPushButton(self)
        self.test_button.setText("  Effectuer des tests  ")
        self.test_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.test_button.move(1150, 600)
        self.test_button.setFont(QFont("Arial", 30, weight=QFont.Bold))
        self.test_button.adjustSize()

    def get_test_parameters(self, stim_parameters):
        stim_parameters = numpy.array([0, 30, 200])
        # print(self.test_parameters)
        # return(self.test_parameters)
