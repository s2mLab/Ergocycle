"""
Created on Wed March 30 11::00 2022

@author: Frédérique Leclerc
"""
from tracemalloc import start

from numpy import number
from Screen import Screen as Screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
#from Ergocycle.source.StartWindow import StartWindow
from StartWindow import StartWindow
from TestingWindow import TestingWindow
from InstructionWindow import InstructionWindow
from Parameters import Parameters
from StimulationWindow import StimulationWindow
from MainWindowStim import MainWindowStim
from DangerPopUp import DangerPopUp
import sys
import datetime
import time
import csv
from CommandButton import CommandButton as CommandButton

# Take the code from main_sef.py and add getters and setters
#def window():
    #app = QApplication(sys.argv)
    #win = StartWindow()
    #win.show()
    #sys.exit(app.exec_())
#window()
class StimulationScreen(Screen):
    def __init__(self, event_function):
        super(StimulationScreen, self).__init__(event_function)
        self.event_function = event_function
        self.current_menu = 0
        self.danger_menu = 0
        #self.now = datetime.datetime.now()
    
    ### 1.1. Permet de gérer les fenêtre apparaissant sur l'interface. ###
    def manage_active_window(self, stim_parameters):
        
        if self.window_counter == 0:
            self.current_menu = StartWindow()
            self.current_menu.training_button.clicked.connect(lambda : self.event_function("start_training"))
            self.current_menu.test_button.clicked.connect(lambda : self.event_function("start_test"))
            self.current_menu.show()
            # self.connect_buttons(self.current_menu)
            
        elif self.window_counter == -1:
            self.current_menu.close()
            self.current_menu = TestingWindow()
            self.current_menu.increase_amp_button.clicked.connect(lambda : self.event_function("increase_amp"))
            self.current_menu.increase_freq_button.clicked.connect(lambda : self.event_function("increase_frequency"))
            self.current_menu.increase_imp_button.clicked.connect(lambda : self.event_function("increase_imp"))
            self.current_menu.decrease_amp_button.clicked.connect(lambda : self.event_function("decrease_amp"))
            self.current_menu.decrease_freq_button.clicked.connect(lambda : self.event_function("decrease_frequency"))
            self.current_menu.decrease_imp_button.clicked.connect(lambda : self.event_function("decrease_imp"))
            self.current_menu.back_button.clicked.connect(lambda : self.event_function("back_button_clicked"))
            self.current_menu.show()
            
        elif self.window_counter == 1:
            self.current_menu.close()
            self.current_menu = MainWindowStim()
            self.current_menu.submit_button.clicked.connect(lambda : self.event_function("submit_button_clicked"))
            self.current_menu.submit_final_button.clicked.connect(lambda : self.event_function("submit_final_button_clicked"))
            self.current_menu.show()
            
        elif self.window_counter == -2:
            self.danger_menu = DangerPopUp(stim_parameters)
            self.danger_menu.show()
            self.danger_menu.back_to_menu_button.clicked.connect(lambda : self.back_to_menu_button_clicked())
            self.danger_menu.continue_button.clicked.connect(lambda : self.continue_button_clicked(stim_parameters))
            
        elif self.window_counter == 2:
            self.current_menu.close()
            self.current_menu = InstructionWindow(stim_parameters)
            self.current_menu.start_button.clicked.connect(lambda : self.event_function("start_stimulations"))
            self.current_menu.show()
        
        elif self.window_counter == 3:
            self.current_menu.close()
            self.current_menu = StimulationWindow(stim_parameters)
            
            self.current_menu.increase_amplitude1_button.clicked.connect(lambda : self.event_function("increase_amplitude1")) 
            self.current_menu.increase_amplitude2_button.clicked.connect(lambda : self.event_function("increase_amplitude2")) 
            self.current_menu.increase_amplitude3_button.clicked.connect(lambda : self.event_function("increase_amplitude3")) 
            self.current_menu.increase_amplitude4_button.clicked.connect(lambda : self.event_function("increase_amplitude4")) 
            self.current_menu.increase_amplitude5_button.clicked.connect(lambda : self.event_function("increase_amplitude5")) 
            self.current_menu.increase_amplitude6_button.clicked.connect(lambda : self.event_function("increase_amplitude6")) 
            self.current_menu.increase_amplitude7_button.clicked.connect(lambda : self.event_function("increase_amplitude7")) 
            self.current_menu.increase_amplitude8_button.clicked.connect(lambda : self.event_function("increase_amplitude8"))
            
            self.current_menu.decrease_amplitude1_button.clicked.connect(lambda : self.event_function("decrease_amplitude1")) 
            self.current_menu.decrease_amplitude2_button.clicked.connect(lambda : self.event_function("decrease_amplitude2")) 
            self.current_menu.decrease_amplitude3_button.clicked.connect(lambda : self.event_function("decrease_amplitude3")) 
            self.current_menu.decrease_amplitude4_button.clicked.connect(lambda : self.event_function("decrease_amplitude4")) 
            self.current_menu.decrease_amplitude5_button.clicked.connect(lambda : self.event_function("decrease_amplitude5")) 
            self.current_menu.decrease_amplitude6_button.clicked.connect(lambda : self.event_function("decrease_amplitude6")) 
            self.current_menu.decrease_amplitude7_button.clicked.connect(lambda : self.event_function("decrease_amplitude7")) 
            self.current_menu.decrease_amplitude8_button.clicked.connect(lambda : self.event_function("decrease_amplitude8"))
            
            self.current_menu.increase_frequency1_button.clicked.connect(lambda : self.event_function("increase_frequency1"))
            self.current_menu.increase_frequency2_button.clicked.connect(lambda : self.event_function("increase_frequency2"))
            self.current_menu.increase_frequency3_button.clicked.connect(lambda : self.event_function("increase_frequency3"))
            self.current_menu.increase_frequency4_button.clicked.connect(lambda : self.event_function("increase_frequency4"))
            self.current_menu.increase_frequency5_button.clicked.connect(lambda : self.event_function("increase_frequency5"))
            self.current_menu.increase_frequency6_button.clicked.connect(lambda : self.event_function("increase_frequency6"))
            self.current_menu.increase_frequency7_button.clicked.connect(lambda : self.event_function("increase_frequency7"))
            self.current_menu.increase_frequency8_button.clicked.connect(lambda : self.event_function("increase_frequency8"))
            
            self.current_menu.decrease_frequency1_button.clicked.connect(lambda : self.event_function("decrease_frequency1"))
            self.current_menu.decrease_frequency2_button.clicked.connect(lambda : self.event_function("decrease_frequency2"))
            self.current_menu.decrease_frequency3_button.clicked.connect(lambda : self.event_function("decrease_frequency3"))
            self.current_menu.decrease_frequency4_button.clicked.connect(lambda : self.event_function("decrease_frequency4"))
            self.current_menu.decrease_frequency5_button.clicked.connect(lambda : self.event_function("decrease_frequency5"))
            self.current_menu.decrease_frequency6_button.clicked.connect(lambda : self.event_function("decrease_frequency6"))
            self.current_menu.decrease_frequency7_button.clicked.connect(lambda : self.event_function("decrease_frequency7"))
            self.current_menu.decrease_frequency8_button.clicked.connect(lambda : self.event_function("decrease_frequency8"))
            
            self.current_menu.increase_imp1_button.clicked.connect(lambda : self.event_function("increase_imp1")) 
            self.current_menu.increase_imp2_button.clicked.connect(lambda : self.event_function("increase_imp2")) 
            self.current_menu.increase_imp3_button.clicked.connect(lambda : self.event_function("increase_imp3")) 
            self.current_menu.increase_imp4_button.clicked.connect(lambda : self.event_function("increase_imp4")) 
            self.current_menu.increase_imp5_button.clicked.connect(lambda : self.event_function("increase_imp5")) 
            self.current_menu.increase_imp6_button.clicked.connect(lambda : self.event_function("increase_imp6")) 
            self.current_menu.increase_imp7_button.clicked.connect(lambda : self.event_function("increase_imp7")) 
            self.current_menu.increase_imp8_button.clicked.connect(lambda : self.event_function("increase_imp8"))
            
            self.current_menu.decrease_imp1_button.clicked.connect(lambda : self.event_function("decrease_imp1")) 
            self.current_menu.decrease_imp2_button.clicked.connect(lambda : self.event_function("decrease_imp2")) 
            self.current_menu.decrease_imp3_button.clicked.connect(lambda : self.event_function("decrease_imp3")) 
            self.current_menu.decrease_imp4_button.clicked.connect(lambda : self.event_function("decrease_imp4")) 
            self.current_menu.decrease_imp5_button.clicked.connect(lambda : self.event_function("decrease_imp5")) 
            self.current_menu.decrease_imp6_button.clicked.connect(lambda : self.event_function("decrease_imp6")) 
            self.current_menu.decrease_imp7_button.clicked.connect(lambda : self.event_function("decrease_imp7")) 
            self.current_menu.decrease_imp8_button.clicked.connect(lambda : self.event_function("decrease_imp8"))
            
            self.current_menu.pauseWatch.pressed.connect(lambda : self.event_function("pause_stimulation"))
            
            self.current_menu.stop_button.clicked.connect(lambda : self.event_function("stop_stimulation")) 
            
            self.current_menu.show()
            
        else:
            self.current_menu.close()
            
    def back_to_menu_button_clicked(self):
        self.danger_menu.close()
        # self.manage_active_window(stim_parameters)
        self.event_function("back_to_menu")
        
    def continue_button_clicked(self, stim_parameters):
        self.window_counter = 2
        self.manage_active_window(stim_parameters)
        self.danger_menu.close()
        self.event_function("continue_to_instructions")
    
    ### 1.2. Création d'un fichier CSV lors de l'entraînement afin d'enregistrer les données de stimulations ###
    def create_csv_file(self, matrice):
        self.now = datetime.datetime.now()
        file = (self.now.strftime("%m-%d-%Y, %H;%M;%S"))
        path = "\\home\\pi\\Downloads\\stimulation_data_" # à commenter si vous travaillez sur votre ordinateur
        name_of_file = path+file+".csv" # à commenter si vous travaillez sur votre ordi
        #name_of_file = (self.now.strftime("%m-%d-%Y, %H;%M;%S"))+" stimulations_data.csv" # à décommenter si vous travaillez sur votre ordinateur
        with open(name_of_file, 'w',newline='') as f:
            fieldnames = ['Date and time', 'Electrode', 'Amplitude(mA)','Frequence(Hz)', 'Durée dimpulsion(us)', 'muscle']
            thewriter = csv.DictWriter(f,fieldnames)
            thewriter.writeheader()
            now = datetime.datetime.now()
            date_time = now.strftime("%m-%d-%Y,%H:%M:%S")
            for i in range(8):
                muscle_name = self.get_muscle_traduction(matrice[3,i])
                thewriter.writerow({'Date and time' : date_time, 'Electrode': str(i+1), 'Amplitude(mA)': str(matrice[0,i]) ,'Frequence(Hz)': str(matrice[1,i]), 'Durée dimpulsion(us)': str(matrice[2,i]), 'muscle': muscle_name})
            f.close
    
    ### 1.3. Ajouter les modification des paramètres d'entraînement au même fichier CSV ###
    def save_data_in_csv_file(self, matrice):
        file = self.now.strftime("%m-%d-%Y, %H;%M;%S")
        path = "\\home\\pi\\Downloads\\stimulation_data_" # à commenter si vous travaillez sur votre ordi
        name_of_file = path+file+".csv" # à commenter si vous travaillez sur votre ordi
        #name_of_file = (self.now.strftime("%m-%d-%Y, %H;%M;%S"))+" stimulations_data.csv" # à décommenter si vous travaillez sur votre ordi
        with open(name_of_file, 'a+',newline='') as f:
            fieldnames = ['Date and time', 'Electrode', 'Amplitude(mA)','Frequence(Hz)', 'Durée dimpulsion(us)', 'muscle']
            thewriter = csv.DictWriter(f,fieldnames)
            new_now = datetime.datetime.now()
            date_time = new_now.strftime("%m-%d-%Y,%H:%M:%S")
            if matrice == []:
                for i in range(8):
                    thewriter.writerow({'Date and time' : date_time, 'Electrode': str(i+1), 'Amplitude(mA)': str(0) ,'Frequence(Hz)': str(0), 'Durée dimpulsion(us)': str(0), 'muscle': str(0)})
            else:
                for i in range(8):
                    muscle_name = self.get_muscle_traduction(matrice[3,i])
                    thewriter.writerow({'Date and time' : date_time, 'Electrode': str(i+1), 'Amplitude(mA)': str(matrice[0,i]) ,'Frequence(Hz)': str(matrice[1,i]), 'Durée dimpulsion(us)': str(matrice[2,i]), 'muscle': muscle_name})
            f.close
    
    ### 1.4. Traduit les muscles de chiffre à nom pour l'enregistrements des données ###
    def get_muscle_traduction(self, muscle_number):
        if muscle_number == 0:
            muscle = "Aucun"
        if muscle_number == 1:
            muscle = "Biceps Brachii"
        if muscle_number== 2:
            muscle = "Triceps Brachii"
        if muscle_number == 3:
            muscle = "Deltoide Postérieur"
        if muscle_number == 4:
            muscle = "Deltoide Antérieur"
        return(muscle)
