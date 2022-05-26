
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer, QTime
# import time
# import sys

from ErrorMenu import ErrorMenu
from StopMenu import StopMenu
from constants import *

MIN_SPEED = 0
MAX_SPEED = 200

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class ActivityMenu(QWidget):
    def __init__(self, motor_parameters):
        super(ActivityMenu, self).__init__()
        
        self.setGeometry(SCREEN_WIDTH, 30, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle("Performances")
        self.setStyleSheet("background-color: white;")
        # self.button_dictionary = {}
        
        self.initUI(motor_parameters)

    def initUI(self, current_parameters):
        self.logo_label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image_400.jpg') # Modifier la taille de l'image au besoin
        self.logo_label.setPixmap(self.pixmap)
        # self.logo_label.resize(self.pixmap.width(), self.pixmap.height())
        self.logo_label.adjustSize()
        
        self.menu_label = QtWidgets.QLabel(self)
        self.menu_label.setText("Performances")
        self.menu_label.move(825,100)
        self.menu_label.setFont(QFont('Arial', 32, weight = QFont.Bold))
        self.menu_label.adjustSize()
        
        self.current_power_label = QtWidgets.QLabel(self)
        self.current_power_label.setText("Puissance actuelle (W)")
        self.current_power_label.move(300, 225)
        self.current_power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.current_power_label.adjustSize()
        
        self.measured_power_label = QtWidgets.QLabel(self)
        self.measured_power_label.setText(str(current_parameters.get_current_power()))
        self.measured_power_label.move(1300,225)
        self.measured_power_label.setFont(QFont('Arial', 24))
        self.measured_power_label.adjustSize()
        
        self.target_power_label = QtWidgets.QLabel(self)
        self.target_power_label.setText("Puissance cible (W)")
        self.target_power_label.move(300,350)
        self.target_power_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.target_power_label.adjustSize()
        
        self.current_target_power_label = QtWidgets.QLabel(self)
        self.current_target_power_label.setText(str(current_parameters.get_target_power()))
        self.current_target_power_label.move(1300,350)
        self.current_target_power_label.setFont(QFont('Arial', 24))
        self.current_target_power_label.adjustSize()
        
        self.increase_target_power_button = QtWidgets.QPushButton(self)
        self.increase_target_power_button.setText("     +     ")
        self.increase_target_power_button.move(1100, 348)
        self.increase_target_power_button.setFont(QFont('Arial', 28))
        self.increase_target_power_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.increase_target_power_button.adjustSize()
        # self.increase_speed_button.clicked.connect(lambda:self.increase_speed(current_parameters))  
        # self.button_dictionary[self.increase_target_power_button] = "increase_target_speed"
        
        self.decrease_target_power_button = QtWidgets.QPushButton(self)
        self.decrease_target_power_button.setText("     -     ")
        self.decrease_target_power_button.move(1420, 348)
        self.decrease_target_power_button.setFont(QFont('Arial', 28))
        self.decrease_target_power_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        self.decrease_target_power_button.adjustSize()
        #self.decrease_target_power_button.clicked.connect(lambda:self.decrease_target_power(current_parameters))  
        # self.button_dictionary[self.decrease_target_power_button] = "decrease_target_power"
        
        self.distance_label = QtWidgets.QLabel(self)
        self.distance_label.setText("Distance parcourue (km)")
        self.distance_label.move(300, 475)
        self.distance_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.distance_label.adjustSize()
        
        self.current_distance_label = QtWidgets.QLabel(self)
        self.current_distance_label.setText(str(current_parameters.get_distance()))
        self.current_distance_label.move(1300, 475)
        self.current_distance_label.setFont(QFont('Arial', 24))
        self.current_distance_label.adjustSize()
        
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setText("Temps écoulé")
        self.time_label.move(300, 600)
        self.time_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.time_label.adjustSize()
        
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.MAX_TIME = int(current_parameters.get_training_length())
        self.startWatch = True

        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(100)
        
        self.current_time_label = QtWidgets.QLabel(self)
        self.current_time_label.setText("00:00") # str(current_parameters.get_time()))
        # self.current_time_label.move(1250, 600)
        self.current_time_label.setGeometry(1270, 600, 100, 70)
        self.current_time_label.setFont(QFont('Arial', 12))
        # self.current_time_label.adjustSize()
        # self.motor_parameters.start_time()
        # self.current_time_label.setText(self.motor_parameters.time.toString('hh:mm:ss'))
        
        self.training_length_label = QtWidgets.QLabel(self)
        self.training_length_label.setText("Durée de l'entraînement (min)")
        self.training_length_label.move(300, 725)
        self.training_length_label.setFont(QFont('Arial', 24, weight = QFont.Bold))
        self.training_length_label.adjustSize()
        
        self.current_training_length_label = QtWidgets.QLabel(self)
        self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.move(1300, 725)
        self.current_training_length_label.setFont(QFont('Arial', 24))
        self.current_training_length_label.adjustSize()
        
        self.time_status_label = QtWidgets.QLabel(self)
        self.time_status_label.setText("")
        self.time_status_label.move(625, 800)
        self.time_status_label.setFont(QFont('Arial', 28))
        self.time_status_label.setStyleSheet("color: green")
        # self.time_status_label.adjustSize()
        
        # self.increase_training_length_button = QtWidgets.QPushButton(self)
        # self.increase_training_length_button.setText("     +     ")
        # self.increase_training_length_button.move(1100, 723)
        # self.increase_training_length_button.setFont(QFont('Arial', 28))
        # self.increase_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        # self.increase_training_length_button.adjustSize()
        # self.increase_training_length_button.clicked.connect(lambda:self.increase_training_length(current_parameters))  
        # self.button_dictionary[self.increase_training_length_button] = "increase_training_length"
        
        # self.decrease_training_length_button = QtWidgets.QPushButton(self)
        # self.decrease_training_length_button.setText("     -     ")
        # self.decrease_training_length_button.move(1420, 723)
        # self.decrease_training_length_button.setFont(QFont('Arial', 28))
        # self.decrease_training_length_button.setStyleSheet("background-color: palegreen; border: 2 solid; border-radius: 1")
        # self.decrease_training_length_button.adjustSize()
        # self.decrease_training_length_button.clicked.connect(lambda:self.decrease_training_length(current_parameters)) 
        # self.button_dictionary[self.decrease_training_length_button] = "decrease_training_length"
        
        self.correction_label = QtWidgets.QLabel(self)
        self.correction_label.setText("")
        self.correction_label.setFont(QFont('Arial', 28, weight = QFont.Bold))
        self.correction_label.adjustSize()
        
        self.stop_button = QtWidgets.QPushButton(self)
        self.stop_button.setText("  ARRÊT  ")
        self.stop_button.setStyleSheet("background-color: red; border: 2 solid;")
        self.stop_button.move(1300, 90)
        self.stop_button.setFont(QFont('Arial', 40, weight = QFont.Bold))
        self.stop_button.adjustSize()
        # self.stop_button.clicked.connect(lambda:self.stop_clicked())   
        # self.button_dictionary[self.stop_button] = "stop_training"
        
        # self.error_button = QtWidgets.QPushButton(self) # Effacer cette section quand les erreurs pourront être détectées
        # self.error_button.setText("  ERREUR  ")
        # self.error_button.setStyleSheet("background-color: red; border: 2 solid;")
        # self.error_button.move(250, 850)
        # self.error_button.setFont(QFont('Arial', 44, weight = QFont.Bold))
        # self.error_button.adjustSize()
        # self.error_button.clicked.connect(lambda:self.simulate_error())
        
        self.update_labels(current_parameters)
        
    # def simulate_error(self): # À enlever
    #     self.error_window = ErrorMenu()
    #     self.error_window.show()
      
    def stop_clicked(self):
        self.stop_window = StopMenu()
        self.stop_window.show()
        self.stop_window.confirmation_button.clicked.connect(lambda:self.close())
        # self.button_dictionary[self.stop_button] = "stop_training"
    
    def showCounter(self):
        # Check the value of startWatch  variable to start or stop the Stop Watch
        if self.startWatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min == self.MAX_TIME:
                        # self.close()
                        self.time_status_label.setText("Le temps d'entraînement visé est terminé")
                        self.time_status_label.adjustSize()
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        # Merge the mintue, second and count values
        text = self.minute + ':' + self.second
        # Display the stop watch values in the label
        self.current_time_label.setText('<h1 style="color:black">' + text + '</h1>')
        
    def update_labels(self, current_parameters):
        
        # TODO: Faire la lecture des mesures
        self.measured_power_label.setText(str(current_parameters.get_current_power()))
        self.measured_power_label.adjustSize()
        
        self.current_target_power_label.setText(str(current_parameters.get_target_power()))
        self.current_target_power_label.adjustSize()
        
        self.current_distance_label.setText(str(current_parameters.get_distance()))
        self.current_distance_label.adjustSize()
        
        self.current_training_length_label.setText(str(current_parameters.get_training_length()))
        self.current_training_length_label.adjustSize()
        
        if (current_parameters.get_current_power() > (current_parameters.get_target_power() * 1.1)): # Remplacer 25 par la vitesse cible
            self.measured_power_label.setStyleSheet("color: red")
            self.correction_label.setText("Diminuer votre puissance")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(725,875)
        elif (current_parameters.get_current_power() < (current_parameters.get_target_power() * 0.9)): # Remplacer 25 par la vitesse cible
            self.measured_power_label.setStyleSheet("color: red")
            self.correction_label.setText("Augmenter votre puissance")
            self.correction_label.setStyleSheet("color: red")
            self.correction_label.move(725,875)
        else:
            self.measured_power_label.setStyleSheet("color: green")
            self.correction_label.setText("Maintenez cette puissance")
            self.correction_label.setStyleSheet("color: green")
            self.correction_label.move(725,875)
        self.correction_label.adjustSize()