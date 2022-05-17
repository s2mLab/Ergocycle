
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
from InstructionWindow import InstructionWindow
from StimulationWindow import StimulationWindow
from Parameters import Parameters
from DangerPopUp import DangerPopUp

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080 - 30

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 

N_ELECTRODES = 8

class MainWindowStim(QMainWindow):
    def __init__(self):
        super(MainWindowStim, self).__init__()
        ### 1.1. Instaurer la taille, la couleur de fond et le titre du de la fenêtre des tests ###
        self.setGeometry(0, 30, SCREEN_WIDTH, SCREEN_HEIGTH)
        self.setWindowTitle("Menu principal des stimulations électriques fonctionnelles")
        self.setStyleSheet("background-color: white;")
        init_parameters = Parameters()
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
        ### 1.3. Titre du menu principal ###
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Bienvenue au menu principal de l'interface usager des stimulations électriques fonctionnelles")
        self.menu_label.move(200,40)
        self.menu_label.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.menu_label.adjustSize()
        ## 1.4.  Durée de l'entrainement (possiblement à retirer pour éviter la répétition avec UI du contrôle moteur) ##
        self.stim_training_length_label = QtWidgets.QLabel(self)
        self.stim_training_length_label.setText("Durée de l'entraînement en stimulation (min):")
        self.stim_training_length_label.move(10,150)
        self.stim_training_length_label.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.stim_training_length_label.adjustSize()

        self.stim_training_length_ComboBox = QtWidgets.QComboBox(self)
        self.stim_training_length_ComboBox.addItems(["1","5", "10", "15", "20", "25", "30"])
        self.stim_training_length_ComboBox.move(650,150)
        self.stim_training_length_ComboBox.setFont(QFont('Arial', 20))
        self.stim_training_length_ComboBox.adjustSize()

        ## 1.5. Définition des muscles à stimuler ##
        ### Droite ###

        """
        Ici, voici simplement une suggestion d'écriture du code plus optimale que celle utilisée présentement.

        self.electrode_first_labels = []
        self.electrode_ComboBoxes = []
        self.electrode_second_labels = []

        self.amplitude_lists = []
        self.frequency_lists = []
        self.length_imp_lists = []

        self.electrode_ComboBox_amplitudes = []
        self.electrode_ComboBox_frequencies = []
        self.electrode_ComboBox_length_imps = []

        for i in range (0, N_ELECTRODES):

            if (i < 4):
                electrode_side = "(droite):"
            else:
                electrode_side = "(gauche):"

            electrode_first_label = QtWidgets.QLabel(self))
            electrode_first_label.setText("Électrode " + str(i + 1) + " " + electrode_side)
            electrode_first_label.move(10, 250 + 50 * i)
            electrode_first_label.setFont(QFont('Arial', 12))
            electrode_first_label.adjustSize()

            self.electrode_first_labels.append(electrode_label)

            electrode_ComboBox = QtWidgets.QComboBox(self)
            electrode_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
            electrode_ComboBox.move(200, 250 + 50 * i)
            electrode_ComboBox.setFont(QFont('Arial', 12))
            electrode_ComboBox.adjustSize()

            self.electrode_ComboBoxes.append(electrode_ComboBox)

            self.electrodes_second_labels.append(QtWidgets.QLabel(self))

            self.amplitude_lists.append(map(str,self.amplitude_list_int))
            self.frequency_lists.append(map(str,self.frequency_list_int))
            self.length_imp_lists.append(map(str,self.length_imp_list_int))

            self.electrode_ComboBox_amplitudes.append(QtWidgets.QComboBox(self))
            self.electrode_ComboBox_frequencies.append(QtWidgets.QComboBox(self))
            self.electrode_ComboBox_length_imps.append(QtWidgets.QComboBox(self))

        """

        self.muscle_label = QtWidgets.QLabel(self)
        self.muscle_label.setText("Veuillez sélectionner les muscles à stimuler et l'électrode correspondante: ")
        self.muscle_label.move(10,200)
        self.muscle_label.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.muscle_label.adjustSize()

        self.electrode1_label = QtWidgets.QLabel(self)
        self.electrode1_label.setText("Électrode 1 (droite):")
        self.electrode1_label.move(10,250)
        self.electrode1_label.setFont(QFont('Arial', 16))
        self.electrode1_label.adjustSize()

        self.electrode1_ComboBox = QtWidgets.QComboBox(self)
        self.electrode1_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode1_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode1_ComboBox.move(275,250)
        self.electrode1_ComboBox.setFont(QFont('Arial', 20))
        self.electrode1_ComboBox.adjustSize()

        self.electrode2_label = QtWidgets.QLabel(self)
        self.electrode2_label.setText("Électrode 2 (droite):")
        self.electrode2_label.move(10,300)
        self.electrode2_label.setFont(QFont('Arial', 16))
        self.electrode2_label.adjustSize()

        self.electrode2_ComboBox = QtWidgets.QComboBox(self)
        self.electrode2_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode2_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode2_ComboBox.move(275,300)
        self.electrode2_ComboBox.setFont(QFont('Arial', 20))
        self.electrode2_ComboBox.adjustSize()

        self.electrode3_label = QtWidgets.QLabel(self)
        self.electrode3_label.setText("Électrode 3 (droite):")
        self.electrode3_label.move(10,350)
        self.electrode3_label.setFont(QFont('Arial', 16))
        self.electrode3_label.adjustSize()

        self.electrode3_ComboBox = QtWidgets.QComboBox(self)
        self.electrode3_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode3_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode3_ComboBox.move(275,350)
        self.electrode3_ComboBox.setFont(QFont('Arial', 20))
        self.electrode3_ComboBox.adjustSize()

        self.electrode4_label = QtWidgets.QLabel(self)
        self.electrode4_label.setText("Électrode 4 (droite):")
        self.electrode4_label.move(10,400)
        self.electrode4_label.setFont(QFont('Arial', 16))
        self.electrode4_label.adjustSize()

        self.electrode4_ComboBox = QtWidgets.QComboBox(self)
        self.electrode4_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode4_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode4_ComboBox.move(275,400)
        self.electrode4_ComboBox.setFont(QFont('Arial', 20))
        self.electrode4_ComboBox.adjustSize()

        ## GAUCHE ##
        self.electrode5_label = QtWidgets.QLabel(self)
        self.electrode5_label.setText("Électrode 5 (gauche):")
        self.electrode5_label.move(600,250)
        self.electrode5_label.setFont(QFont('Arial', 16))
        self.electrode5_label.adjustSize()

        self.electrode5_ComboBox = QtWidgets.QComboBox(self)
        self.electrode5_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode5_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode5_ComboBox.move(875,250)
        self.electrode5_ComboBox.setFont(QFont('Arial', 20))
        self.electrode5_ComboBox.adjustSize()

        self.electrode6_label = QtWidgets.QLabel(self)
        self.electrode6_label.setText("Électrode 6 (gauche):")
        self.electrode6_label.move(600,300)
        self.electrode6_label.setFont(QFont('Arial', 16))
        self.electrode6_label.adjustSize()

        self.electrode6_ComboBox = QtWidgets.QComboBox(self)
        self.electrode6_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode6_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode6_ComboBox.move(875,300)
        self.electrode6_ComboBox.setFont(QFont('Arial', 20))
        self.electrode6_ComboBox.adjustSize()

        self.electrode7_label = QtWidgets.QLabel(self)
        self.electrode7_label.setText("Électrode 7 (gauche):")
        self.electrode7_label.move(600,350)
        self.electrode7_label.setFont(QFont('Arial', 16))
        self.electrode7_label.adjustSize()

        self.electrode7_ComboBox = QtWidgets.QComboBox(self)
        self.electrode7_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode7_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode7_ComboBox.move(875,350)
        self.electrode7_ComboBox.setFont(QFont('Arial', 20))
        self.electrode7_ComboBox.adjustSize()

        self.electrode8_label = QtWidgets.QLabel(self)
        self.electrode8_label.setText("Électrode 8 (gauche):")
        self.electrode8_label.move(600,400)
        self.electrode8_label.setFont(QFont('Arial', 16))
        self.electrode8_label.adjustSize()

        self.electrode8_ComboBox = QtWidgets.QComboBox(self)
        self.electrode8_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur"])
        #self.electrode8_ComboBox.addItems(["Aucun","Biceps Brachii", "Triceps Brachii", "Deltoide Postérieur", "Deltoide Antérieur","Grand pectoral","Trapezius descendens","Infraspinatus", "Supraspinatus","Subscapularis","Brachioradialis","Faisceau supérieur du trapeze", "Flexor carpi radialis","Extensor carpi ulnaris","M. rectus abdominis"])
        self.electrode8_ComboBox.move(875,400)
        self.electrode8_ComboBox.setFont(QFont('Arial', 20))
        self.electrode8_ComboBox.adjustSize()

        ### 1.6. Définition du bouton soummettre qui permet de voir la suite. ###
        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("  Soumettre  ")
        self.submit_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_button.move(1600, 400) # originalement 1400, 400 (devrait être mis a 1000,400)
        self.submit_button.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.submit_button.adjustSize()

        ### 1.7. Définition des labels, des boutons et des menus déroulants pour la définition des paramètres de stimulation ###
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

        self.error_label = QtWidgets.QLabel(self)

        self.amplitude_list_int = list(range(0,132,2))
        self.frequency_list_int = list(range(0,55,5))
        self.length_imp_list_int = list(range(0,510,10))

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

    def clicked_more(self, init_parameters):

        """
        Ici, voici simplement une suggestion d'écriture du code plus optimale que celle utilisée présentement. 

        for i in range (0, N_ELECTRODES):

            if (i < 4):
                electrode_side = "(droite):"
            else:
                electrode_side = "(gauche):"

            self.electrode_ComboBoxes[i].setEnabled(False)

            self.electrode_second_labels[i].setText("Électrode " + str(i + 1) + " " + electrode_side)
            self.electrode_second_labels[i].move(10, 550 + 50 * i)
            self.electrode_second_labels[i].setFont(QFont('Arial', 12))
            self.electrode_second_labels[i].adjustSize()

            self.electrode_ComboBox_amplitudes[i].addItems(self.amplitude_lists[i])
            self.electrode_ComboBox_amplitudes[i].move(400, 550 + 50 * i)
            self.electrode_ComboBox_amplitudes[i].setFont(QFont('Arial', 12))
            self.electrode_ComboBox_amplitudes[i].adjustSize()

            self.electrode_ComboBox_frequencies[i].addItems(self.frequency_lists[i])
            self.electrode_ComboBox_frequencies[i].move(750,550)
            self.electrode_ComboBox_frequencies[i].setFont(QFont('Arial', 12))
            self.electrode_ComboBox_frequencies[i].adjustSize()

            self.electrode_ComboBox_length_imps[i].addItems(self.length_imp_lists[i])
            self.electrode_ComboBox_length_imps[i].move(1200,550 + 50 * i)
            self.electrode_ComboBox_length_imps[i].setFont(QFont('Arial', 12))
            self.electrode_ComboBox_length_imps[i].adjustSize()

        """

        ### 2.1 - Mettre les ComboBox des muscles à utiliser et la durée de l'entrâinement en stimulation inactifs à la suite de l'appui du premier bouton "Soumettre" ###
        self.stim_training_length_ComboBox.setEnabled(False)
        self.electrode1_ComboBox.setEnabled(False)
        self.electrode2_ComboBox.setEnabled(False)
        self.electrode3_ComboBox.setEnabled(False)
        self.electrode4_ComboBox.setEnabled(False)
        self.electrode5_ComboBox.setEnabled(False)
        self.electrode6_ComboBox.setEnabled(False)
        self.electrode7_ComboBox.setEnabled(False)
        self.electrode8_ComboBox.setEnabled(False)

        ### 2.2 - Ajout du titre de l'instruction ###
        self.param_label.setText("Veuillez sélectionner les valeurs des paramètres de stimulation: ")
        self.param_label.move(10,450)
        self.param_label.setFont(QFont('Arial', 16, weight = QFont.Bold))
        self.param_label.adjustSize()

        self.electrode11_label.setText("Électrode 1 (droite):")
        self.electrode11_label.move(10,550)
        self.electrode11_label.setFont(QFont('Arial', 16))
        self.electrode11_label.adjustSize()

        self.electrode22_label.setText("Électrode 2 (droite):")
        self.electrode22_label.move(10,600)
        self.electrode22_label.setFont(QFont('Arial', 16))
        self.electrode22_label.adjustSize()

        self.electrode33_label.setText("Électrode 3 (droite):")
        self.electrode33_label.move(10,650)
        self.electrode33_label.setFont(QFont('Arial', 16))
        self.electrode33_label.adjustSize()

        self.electrode44_label.setText("Électrode 4 (droite):")
        self.electrode44_label.move(10,700)
        self.electrode44_label.setFont(QFont('Arial', 16))
        self.electrode44_label.adjustSize()

        self.electrode55_label.setText("Électrode 5 (gauche):")
        self.electrode55_label.move(10,750)
        self.electrode55_label.setFont(QFont('Arial', 16))
        self.electrode55_label.adjustSize()

        self.electrode66_label.setText("Électrode 6 (gauche):")
        self.electrode66_label.move(10,800)
        self.electrode66_label.setFont(QFont('Arial', 16))
        self.electrode66_label.adjustSize()

        self.electrode77_label.setText("Électrode 7 (gauche):")
        self.electrode77_label.move(10,850)
        self.electrode77_label.setFont(QFont('Arial', 16))
        self.electrode77_label.adjustSize()

        self.electrode88_label.setText("Électrode 8 (gauche):")
        self.electrode88_label.move(10,900)
        self.electrode88_label.setFont(QFont('Arial', 16))
        self.electrode88_label.adjustSize()

        ## 2.3 - Tous les menus déroulants des paramètres de stimulation ##
        self.amplitude_label.setText("Amplitude (mA):")
        self.amplitude_label.move(400,(500))
        self.amplitude_label.setFont(QFont('Arial', 16))
        self.amplitude_label.adjustSize()

        self.frequency_label.setText("Fréquence (Hz):")
        self.frequency_label.move(750,500)
        self.frequency_label.setFont(QFont('Arial', 16))
        self.frequency_label.adjustSize()

        self.length_imp_label.setText("Durée d'impulsion (μs):")
        self.length_imp_label.move(1200,(500))
        self.length_imp_label.setFont(QFont('Arial', 16))
        self.length_imp_label.adjustSize()

        self.electrode1_ComboBox_amplitude.addItems(self.amplitude_list1)
        self.electrode1_ComboBox_amplitude.move(400,550)
        self.electrode1_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode1_ComboBox_amplitude.adjustSize()

        self.electrode2_ComboBox_amplitude.addItems(self.amplitude_list2)
        self.electrode2_ComboBox_amplitude.move(400,600)
        self.electrode2_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode2_ComboBox_amplitude.adjustSize()

        self.electrode3_ComboBox_amplitude.addItems(self.amplitude_list3)
        self.electrode3_ComboBox_amplitude.move(400,650)
        self.electrode3_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode3_ComboBox_amplitude.adjustSize()

        self.electrode4_ComboBox_amplitude.addItems(self.amplitude_list4)
        self.electrode4_ComboBox_amplitude.move(400,700)
        self.electrode4_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode4_ComboBox_amplitude.adjustSize()

        self.electrode5_ComboBox_amplitude.addItems(self.amplitude_list5)
        self.electrode5_ComboBox_amplitude.move(400,750)
        self.electrode5_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode5_ComboBox_amplitude.adjustSize()

        self.electrode6_ComboBox_amplitude.addItems(self.amplitude_list6)
        self.electrode6_ComboBox_amplitude.move(400,800)
        self.electrode6_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode6_ComboBox_amplitude.adjustSize()

        self.electrode7_ComboBox_amplitude.addItems(self.amplitude_list7)
        self.electrode7_ComboBox_amplitude.move(400,850)
        self.electrode7_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode7_ComboBox_amplitude.adjustSize()

        self.electrode8_ComboBox_amplitude.addItems(self.amplitude_list8)
        self.electrode8_ComboBox_amplitude.move(400,900)
        self.electrode8_ComboBox_amplitude.setFont(QFont('Arial', 24))
        self.electrode8_ComboBox_amplitude.adjustSize()

        self.electrode1_ComboBox_frequency.addItems(self.frequency_list1)
        self.electrode1_ComboBox_frequency.move(750,550)
        self.electrode1_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode1_ComboBox_frequency.adjustSize()

        self.electrode2_ComboBox_frequency.addItems(self.frequency_list2)
        self.electrode2_ComboBox_frequency.move(750,600)
        self.electrode2_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode2_ComboBox_frequency.adjustSize()

        self.electrode3_ComboBox_frequency.addItems(self.frequency_list3)
        self.electrode3_ComboBox_frequency.move(750,650)
        self.electrode3_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode3_ComboBox_frequency.adjustSize()

        self.electrode4_ComboBox_frequency.addItems(self.frequency_list4)
        self.electrode4_ComboBox_frequency.move(750,700)
        self.electrode4_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode4_ComboBox_frequency.adjustSize()

        self.electrode5_ComboBox_frequency.addItems(self.frequency_list5)
        self.electrode5_ComboBox_frequency.move(750,750)
        self.electrode5_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode5_ComboBox_frequency.adjustSize()

        self.electrode6_ComboBox_frequency.addItems(self.frequency_list6)
        self.electrode6_ComboBox_frequency.move(750,800)
        self.electrode6_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode6_ComboBox_frequency.adjustSize()

        self.electrode7_ComboBox_frequency.addItems(self.frequency_list7)
        self.electrode7_ComboBox_frequency.move(750,850)
        self.electrode7_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode7_ComboBox_frequency.adjustSize()

        self.electrode8_ComboBox_frequency.addItems(self.frequency_list8)
        self.electrode8_ComboBox_frequency.move(750,900)
        self.electrode8_ComboBox_frequency.setFont(QFont('Arial', 24))
        self.electrode8_ComboBox_frequency.adjustSize()

        self.electrode1_ComboBox_length_imp.addItems(self.length_imp_list1)
        self.electrode1_ComboBox_length_imp.move(1200,550)
        self.electrode1_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode1_ComboBox_length_imp.adjustSize()

        self.electrode2_ComboBox_length_imp.addItems(self.length_imp_list2)
        self.electrode2_ComboBox_length_imp.move(1200,600)
        self.electrode2_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode2_ComboBox_length_imp.adjustSize()

        self.electrode3_ComboBox_length_imp.addItems(self.length_imp_list3)
        self.electrode3_ComboBox_length_imp.move(1200,650)
        self.electrode3_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode3_ComboBox_length_imp.adjustSize()

        self.electrode4_ComboBox_length_imp.addItems(self.length_imp_list4)
        self.electrode4_ComboBox_length_imp.move(1200,700)
        self.electrode4_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode4_ComboBox_length_imp.adjustSize()

        self.electrode5_ComboBox_length_imp.addItems(self.length_imp_list5)
        self.electrode5_ComboBox_length_imp.move(1200,750)
        self.electrode5_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode5_ComboBox_length_imp.adjustSize()

        self.electrode6_ComboBox_length_imp.addItems(self.length_imp_list6)
        self.electrode6_ComboBox_length_imp.move(1200,800)
        self.electrode6_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode6_ComboBox_length_imp.adjustSize()

        self.electrode7_ComboBox_length_imp.addItems(self.length_imp_list7)
        self.electrode7_ComboBox_length_imp.move(1200,850)
        self.electrode7_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode7_ComboBox_length_imp.adjustSize()

        self.electrode8_ComboBox_length_imp.addItems(self.length_imp_list8)
        self.electrode8_ComboBox_length_imp.move(1200,900)
        self.electrode8_ComboBox_length_imp.setFont(QFont('Arial', 24))
        self.electrode8_ComboBox_length_imp.adjustSize()

        ### 2.4 - Bloquer les menus déroulants des électrodes non-utilisées (exigence de sécurité) ###
        self.set_electrode_off(init_parameters)

        ### 2.5 - Initialisation du bouton soumettre ###
        self.submit_final_button.setText("  Soumettre  ")
        self.submit_final_button.setStyleSheet("background-color: palegreen; border: 1 solid;")
        self.submit_final_button.move(1600, 900) # 1400, 900 originalement, devrait etre a (1000, 900)
        self.submit_final_button.setFont(QFont('Arial', 20, weight = QFont.Bold))
        self.submit_final_button.adjustSize()
        # self.submit_final_button.clicked.connect(lambda:self.clicked_next(init_parameters))

    def set_electrode_off(self, init_parameters):
        ### 3.1 - Enregistrer les valeurs des paramètres entrées pour les électrodes utilisées ###
        init_parameters.set_electrode1_muscle(self.electrode1_ComboBox)
        init_parameters.set_electrode2_muscle(self.electrode2_ComboBox)
        init_parameters.set_electrode3_muscle(self.electrode3_ComboBox)
        init_parameters.set_electrode4_muscle(self.electrode4_ComboBox)
        init_parameters.set_electrode5_muscle(self.electrode5_ComboBox)
        init_parameters.set_electrode6_muscle(self.electrode6_ComboBox)
        init_parameters.set_electrode7_muscle(self.electrode7_ComboBox)
        init_parameters.set_electrode8_muscle(self.electrode8_ComboBox)
        ### 3.2 - Empêcher l'utilisateur de mettre des valeurs non-nulles à des électrodes pas utilisées lors de l'entraînement ###
        if (init_parameters.get_electrode1_muscle() == "Aucun"):
            self.electrode1_ComboBox_amplitude.setEnabled(False)
            self.electrode1_ComboBox_frequency.setEnabled(False)
            self.electrode1_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode2_muscle() == "Aucun"):
            self.electrode2_ComboBox_amplitude.setEnabled(False)
            self.electrode2_ComboBox_frequency.setEnabled(False)
            self.electrode2_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode3_muscle() == "Aucun"):
            self.electrode3_ComboBox_amplitude.setEnabled(False)
            self.electrode3_ComboBox_frequency.setEnabled(False)
            self.electrode3_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode4_muscle() == "Aucun"):
            self.electrode4_ComboBox_amplitude.setEnabled(False)
            self.electrode4_ComboBox_frequency.setEnabled(False)
            self.electrode4_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode5_muscle() == "Aucun"):
            self.electrode5_ComboBox_amplitude.setEnabled(False)
            self.electrode5_ComboBox_frequency.setEnabled(False)
            self.electrode5_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode6_muscle() == "Aucun"):
            self.electrode6_ComboBox_amplitude.setEnabled(False)
            self.electrode6_ComboBox_frequency.setEnabled(False)
            self.electrode6_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode7_muscle() == "Aucun"):
            self.electrode7_ComboBox_amplitude.setEnabled(False)
            self.electrode7_ComboBox_frequency.setEnabled(False)
            self.electrode7_ComboBox_length_imp.setEnabled(False)
        if (init_parameters.get_electrode8_muscle() == "Aucun"):
            self.electrode8_ComboBox_amplitude.setEnabled(False)
            self.electrode8_ComboBox_frequency.setEnabled(False)
            self.electrode8_ComboBox_length_imp.setEnabled(False)

    def clicked_next(self, init_parameters):
        ### Enregistrer les valeurs des paramètres entrées ###
        ### 4.1 - Temps de stiumulation de l'entrainement (pour le menu de stimulation) ###
        init_parameters.set_stim_training_length(self.stim_training_length_ComboBox)
        ### 4.2 - Amplitude à chaque électrode (pour le menu de stimulation) ###
        init_parameters.set_electrode1_amplitude(self.electrode1_ComboBox_amplitude)
        init_parameters.set_electrode2_amplitude(self.electrode2_ComboBox_amplitude)
        init_parameters.set_electrode3_amplitude(self.electrode3_ComboBox_amplitude)
        init_parameters.set_electrode4_amplitude(self.electrode4_ComboBox_amplitude)
        init_parameters.set_electrode5_amplitude(self.electrode5_ComboBox_amplitude)
        init_parameters.set_electrode6_amplitude(self.electrode6_ComboBox_amplitude)
        init_parameters.set_electrode7_amplitude(self.electrode7_ComboBox_amplitude)
        init_parameters.set_electrode8_amplitude(self.electrode8_ComboBox_amplitude)
        ### 4.3 - Fréquence à chaque électrode (pour le menu de stimulation) ###
        init_parameters.set_electrode1_frequency(self.electrode1_ComboBox_frequency)
        init_parameters.set_electrode2_frequency(self.electrode2_ComboBox_frequency)
        init_parameters.set_electrode3_frequency(self.electrode3_ComboBox_frequency)
        init_parameters.set_electrode4_frequency(self.electrode4_ComboBox_frequency)
        init_parameters.set_electrode5_frequency(self.electrode5_ComboBox_frequency)
        init_parameters.set_electrode6_frequency(self.electrode6_ComboBox_frequency)
        init_parameters.set_electrode7_frequency(self.electrode7_ComboBox_frequency)
        init_parameters.set_electrode8_frequency(self.electrode8_ComboBox_frequency)
        ### 4.4 - Durée de l'impulsion à chaque électrode (pour le menu de stimulation) ###
        init_parameters.set_electrode1_length_imp(self.electrode1_ComboBox_length_imp)
        init_parameters.set_electrode2_length_imp(self.electrode2_ComboBox_length_imp)
        init_parameters.set_electrode3_length_imp(self.electrode3_ComboBox_length_imp)
        init_parameters.set_electrode4_length_imp(self.electrode4_ComboBox_length_imp)
        init_parameters.set_electrode5_length_imp(self.electrode5_ComboBox_length_imp)
        init_parameters.set_electrode6_length_imp(self.electrode6_ComboBox_length_imp)
        init_parameters.set_electrode7_length_imp(self.electrode7_ComboBox_length_imp)
        init_parameters.set_electrode8_length_imp(self.electrode8_ComboBox_length_imp)
        ### 4.5 - Vérification que toutes les informations sont entrées (appel a la fonction is_completed) ###
        ## Maintenant contrôler dans Ergocycle.py ###
        # if self.is_completed(init_parameters) == True:
        #     ### 4.5.1 - Vérification du danger et appel au bon menu (DangerPopUp ou InstructionWindow) ###
        #     if self.danger_check(init_parameters) == True:
        #         self.danger_pop_up_window = DangerPopUp(init_parameters)
        #         self.danger_pop_up_window.setWindowModality(2) ## Bloque les inputs des autres fenêtres
        #         self.danger_pop_up_window.show()
        #         self.update()
        #     else:
        #         self.instruction_window = InstructionWindow(init_parameters)
        #         self.close()
        #         self.instruction_window.show()
        #         self.update()
        ### 4.6 - S'il manque des information, on affiche un message d'erreur ###
        # else:
        if self.is_completed(init_parameters) == False:
            self.error_label.setText("Attention! Assurez-vous d'entrer trois valeurs de paramètres pour chaque électrode utilisées. Réessayer.")
            self.error_label.move(200,100)
            self.error_label.setFont(QFont('Arial', 20, weight = QFont.Bold))
            self.error_label.setStyleSheet("background-color: red")
            self.error_label.adjustSize()
            self.error_label.setText

    def e1_is_completed(self, init_parameters):
        if (init_parameters.get_electrode1_muscle() != "Aucun" and int(init_parameters.get_electrode1_amplitude()) != 0 and int(init_parameters.get_electrode1_frequency())!=0 and int(init_parameters.get_electrode1_length_imp())!=0) or (init_parameters.get_electrode1_muscle() == "Aucun" and int(init_parameters.get_electrode1_amplitude()) == 0 and int(init_parameters.get_electrode1_frequency())==0 and int(init_parameters.get_electrode1_length_imp())==0):
            self.reponse1 = True
        else:
            self.reponse1 = False
        return(self.reponse1)
    def e2_is_completed(self, init_parameters):
        if (init_parameters.get_electrode2_muscle() != "Aucun" and int(init_parameters.get_electrode2_amplitude()) != 0 and int(init_parameters.get_electrode2_frequency())!=0 and int(init_parameters.get_electrode2_length_imp())!=0) or (init_parameters.get_electrode2_muscle() == "Aucun" and int(init_parameters.get_electrode2_amplitude()) == 0 and int(init_parameters.get_electrode2_frequency())==0 and int(init_parameters.get_electrode2_length_imp())==0):
            self.reponse2 = True
        else:
            self.reponse2 = False
        return(self.reponse2)
    def e3_is_completed(self, init_parameters):
        if (init_parameters.get_electrode3_muscle() != "Aucun" and int(init_parameters.get_electrode3_amplitude()) != 0 and int(init_parameters.get_electrode3_frequency())!=0 and int(init_parameters.get_electrode3_length_imp())!=0) or (init_parameters.get_electrode3_muscle() == "Aucun" and int(init_parameters.get_electrode3_amplitude()) == 0 and int(init_parameters.get_electrode3_frequency())==0 and int(init_parameters.get_electrode3_length_imp())==0):
            self.reponse3 = True
        else:
            self.reponse3 = False
        return(self.reponse3)
    def e4_is_completed(self, init_parameters):
        if (init_parameters.get_electrode4_muscle() != "Aucun" and int(init_parameters.get_electrode4_amplitude()) != 0 and int(init_parameters.get_electrode4_frequency())!=0 and int(init_parameters.get_electrode4_length_imp())!=0) or (init_parameters.get_electrode4_muscle() == "Aucun" and int(init_parameters.get_electrode4_amplitude()) == 0 and int(init_parameters.get_electrode4_frequency())==0 and int(init_parameters.get_electrode4_length_imp())==0):
            self.reponse4 = True
        else:
            self.reponse4 = False
        return(self.reponse4)

    def e5_is_completed(self, init_parameters):
        if (init_parameters.get_electrode5_muscle() != "Aucun" and int(init_parameters.get_electrode5_amplitude()) != 0 and int(init_parameters.get_electrode5_frequency())!=0 and int(init_parameters.get_electrode5_length_imp())!=0) or (init_parameters.get_electrode5_muscle() == "Aucun" and int(init_parameters.get_electrode5_amplitude()) == 0 and int(init_parameters.get_electrode5_frequency())==0 and int(init_parameters.get_electrode5_length_imp())==0):
            self.reponse5 = True
        else:
            self.reponse5 = False
        return(self.reponse5)
    def e6_is_completed(self, init_parameters):
        if (init_parameters.get_electrode6_muscle() != "Aucun" and int(init_parameters.get_electrode6_amplitude()) != 0 and int(init_parameters.get_electrode6_frequency())!=0 and int(init_parameters.get_electrode6_length_imp())!=0) or (init_parameters.get_electrode6_muscle() == "Aucun" and int(init_parameters.get_electrode6_amplitude()) == 0 and int(init_parameters.get_electrode6_frequency())==0 and int(init_parameters.get_electrode6_length_imp())==0):
            self.reponse6 = True
        else:
            self.reponse6 = False
        return(self.reponse6)
    def e7_is_completed(self, init_parameters):
        if (init_parameters.get_electrode7_muscle() != "Aucun" and int(init_parameters.get_electrode7_amplitude()) != 0 and int(init_parameters.get_electrode7_frequency())!=0 and int(init_parameters.get_electrode7_length_imp())!=0) or (init_parameters.get_electrode7_muscle() == "Aucun" and int(init_parameters.get_electrode7_amplitude()) == 0 and int(init_parameters.get_electrode7_frequency())==0 and int(init_parameters.get_electrode7_length_imp())==0):
            self.reponse7 = True
        else:
            self.reponse7 = False
        return(self.reponse7)
    def e8_is_completed(self, init_parameters):
        if (init_parameters.get_electrode8_muscle() != "Aucun" and int(init_parameters.get_electrode8_amplitude()) != 0 and int(init_parameters.get_electrode8_frequency())!=0 and int(init_parameters.get_electrode8_length_imp())!=0) or (init_parameters.get_electrode8_muscle() == "Aucun" and int(init_parameters.get_electrode8_amplitude()) == 0 and int(init_parameters.get_electrode8_frequency())==0 and int(init_parameters.get_electrode8_length_imp())==0):
            self.reponse8 = True
        else:
            self.reponse8 = False
        return(self.reponse8)
        
    def is_completed(self, init_parameters):
        self.rep1 = self.e1_is_completed(init_parameters)
        self.rep2 = self.e2_is_completed(init_parameters)
        self.rep3 = self.e3_is_completed(init_parameters)
        self.rep4 = self.e4_is_completed(init_parameters)
        self.rep5 = self.e5_is_completed(init_parameters)
        self.rep6 = self.e6_is_completed(init_parameters)
        self.rep7 = self.e7_is_completed(init_parameters)
        self.rep8 = self.e8_is_completed(init_parameters)
        if self.rep1 == True and self.rep2 == True and self.rep3 == True and self.rep4 == True and self.rep5 == True and self.rep6 == True and self.rep7 == True and self.rep8 == True:
            self.global_reponse = True
        else:
            self.global_reponse = False
        return(self.global_reponse)

    def update(self):
        self.param_label.adjustSize()

    def danger_check(self, init_parameters):
        self.i=init_parameters.couple_amplitude_frequency_check()
        self.j=init_parameters.couple_amplitude_imp_check()
        self.k=init_parameters.couple_frequency_imp_check()
        if self.i!=0 or self.j!=0 or self.k!=0:
            self.danger = True
        else:
            self.danger = False
        return(self.danger)
