from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QPixmap
from constants import *

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120  # TODO: Needs to be modified


class ErrorMenu(QWidget):
    def __init__(self):
        super(ErrorMenu, self).__init__()

        self.menu_label = None
        self.pixmap = None
        self.logo_label = None

        self.setGeometry(700, 400, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 3)
        self.setWindowTitle("Erreur")
        self.setStyleSheet("background-color: white;")

        self.button_dictionary = {}

        self.init_ui()

    def init_ui(self):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap("s2m_logo_resized.jpg")
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.resize(self.pixmap.width(), self.pixmap.height())

        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Erreur")
        self.menu_label.move(220, 40)
        self.menu_label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        self.menu_label.adjustSize()

    @staticmethod
    def check_error_status():
        print("Checking error status...")
