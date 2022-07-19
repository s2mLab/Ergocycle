from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

# from Ergocycle.source.MainWindowStim import MainWindowStim
from InstructionWindow import InstructionWindow
from PIL import Image

from constants import *


class DangerPopUp(QWidget):
    def __init__(self, init_parameters):
        super(DangerPopUp, self).__init__()  # TODO: Complete the parameter needed

        self.continue_button = None
        self.instruction_window = None
        self.back_to_menu_button = None
        self.question_label = None
        self.k_label = None
        self.torque_frequency_imp_label = None
        self.j_label = None
        self.torque_amplitude_imp_label = None
        self.i_label = None
        self.torque_amplitude_frequency_label = None
        self.k = None
        self.j = None
        self.i = None
        self.problem_label = None
        self.message_label = None
        self.attention_label = None
        self.logo_jpg = None
        self.logo_label = None
        self.petite_imageS2M = None
        self.imageS2M = None

        # 1.1. Set size, background color and title of the popup window
        self.setGeometry(300, 300, SCREEN_WIDTH / 1.7, SCREEN_HEIGHT / 1.8)
        self.setWindowTitle("Avertissement")
        self.setStyleSheet("background-color: white;")
        self.init_ui(init_parameters)

    def init_ui(self, init_parameters):
        # 1.2. Place the S2M logo in the left corner of the window
        self.imageS2M = Image.open("img_S2M_JPG.jpg")
        self.petite_imageS2M = self.imageS2M.resize((200, 150))
        self.petite_imageS2M.save("image_400.jpg")
        self.logo_label = QtWidgets.QLabel(self)  # TODO: Check type parameter
        self.logo_jpg = QPixmap("image_400.jpg")  # Modify picture size if needed
        self.logo_label.setPixmap(self.logo_jpg)
        self.logo_label.resize(self.logo_jpg.width(), self.logo_jpg.height())

        # 1.3. Error message
        self.attention_label = QtWidgets.QLabel(self)
        self.attention_label.setText("Attention.")
        self.attention_label.move(200, 40)
        self.attention_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.attention_label.adjustSize()
        self.message_label = QtWidgets.QLabel(self)
        self.message_label.setText(
            "L'une ou plusieurs valeurs que vous avez entrées \n ne sont pas recommandées. Assurez-vous que pour "
            "chaque électrode: \n - une amplitude supérieure à 60mA n'est pas couplée à une fréquence supérieure à "
            "40 Hz \n - une amplitude supérieure à 60mA n'est pas couplée à une durée d'impulsion supérieure à 250μs"
            "\n - une durée d'impulsion supérieure à 250μs n'est pas couplée à une fréquence supérieure à 40 Hz"
        )
        self.message_label.move(200, 60)
        self.message_label.setFont(QFont("Arial", 12))
        self.message_label.adjustSize()
        self.problem_label = QtWidgets.QLabel(self)
        self.problem_label.setText("Nombre de problèmes rencontrés pour chaqun des couples dangereux :")
        self.problem_label.move(10, 200)
        self.problem_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.problem_label.adjustSize()

        # 1.4. Setting the issue to client
        self.i = init_parameters.torque_amplitude_frequency_check()
        self.j = init_parameters.torque_amplitude_imp_check()
        self.k = init_parameters.torque_frequency_imp_check()
        self.torque_amplitude_frequency_label = QtWidgets.QLabel(self)
        self.torque_amplitude_frequency_label.setText("Couple Amplitude/Fréquence : ")
        self.torque_amplitude_frequency_label.move(10, 250)
        self.torque_amplitude_frequency_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.torque_amplitude_frequency_label.adjustSize()
        self.i_label = QtWidgets.QLabel(self)
        self.i_label.setText(str(init_parameters.torque_amplitude_frequency_check()))
        self.i_label.move(400, 250)
        self.i_label.setFont(QFont("Arial", 12))
        self.i_label.adjustSize()
        self.torque_amplitude_imp_label = QtWidgets.QLabel(self)
        self.torque_amplitude_imp_label.setText("Couple Amplitude/Durée d'impulsion : ")
        self.torque_amplitude_imp_label.move(10, 300)
        self.torque_amplitude_imp_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.torque_amplitude_imp_label.adjustSize()
        self.j_label = QtWidgets.QLabel(self)
        self.j_label.setText(str(init_parameters.torque_amplitude_imp_check()))
        self.j_label.move(400, 300)
        self.j_label.setFont(QFont("Arial", 12))
        self.j_label.adjustSize()
        self.torque_frequency_imp_label = QtWidgets.QLabel(self)
        self.torque_frequency_imp_label.setText("Couple Fréquence/Durée d'impulsion : ")
        self.torque_frequency_imp_label.move(10, 350)
        self.torque_frequency_imp_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.torque_frequency_imp_label.adjustSize()
        self.k_label = QtWidgets.QLabel(self)
        self.k_label.setText(str(init_parameters.torque_frequency_imp_check()))
        self.k_label.move(400, 350)
        self.k_label.setFont(QFont("Arial", 12))
        self.question_label = QtWidgets.QLabel(self)
        self.question_label.setText("Souhaiteriez-vous changer les valeurs des paramètres d'entraînement?")
        self.question_label.move(200, 450)
        self.question_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.question_label.adjustSize()
        self.question_label.adjustSize()

        # 1.5. Button back to main menu
        self.back_to_menu_button = QtWidgets.QPushButton(self)
        self.back_to_menu_button.setText("   Modifier les paramètres   ")
        self.back_to_menu_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.back_to_menu_button.move(200, 500)
        self.back_to_menu_button.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.back_to_menu_button.adjustSize()

        # 1.6. Button forced continue
        self.continue_button = QtWidgets.QPushButton(self)
        self.continue_button.setText("   Poursuivre quand même   ")
        self.continue_button.setStyleSheet("background-color: red; border: 1 solid;")
        self.continue_button.move(600, 500)
        self.continue_button.setFont(QFont("Arial", 12, weight=QFont.Bold))
        self.continue_button.adjustSize()

    # 1.7. Back to MainWindowStim.py
    def clicked_back(self):
        self.close()

    # 1.8. Send to InstructionWindow.py
    def clicked_instruction(self, init_parameters):
        self.instruction_window = InstructionWindow(init_parameters)
        self.instruction_window.show()
        self.close()
