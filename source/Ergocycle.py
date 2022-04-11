# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
import numpy
from Screen import Screen as Screen
from StimulationScreen import StimulationScreen as StimulationScreen
from MotorScreen import MotorScreen

from Parameters import Parameters
from TestParameters import TestParameters
from MotorParameters import MotorParameters

# from ReceiveDataClient import ReceiveDataClient

from PyQt5.QtWidgets import QApplication

import sys
# from StimulationSignal import StimulationSignal
#from Stimulator import Stimulator as Stimulator
#import MainWindowStim
#import main_sef
#import InstructionWindow
#from Observer import Observer
#from Observable import Observable

import threading
import logging
import time

"""
Choices for the events:
- Multiple function in Ergocycle (more simple and more organised)
- One function and multiple commands in Ergocycle
"""



class Ergocycle():

    #INIT_TIMER = 0.5

    # Constuctor
    def __init__(self):
        
        self.application = QApplication([])

        self.motor_parameters = MotorParameters()
        self.assistance_screen = MotorScreen(self.read_assistance_screen)
        self.assistance_screen.manage_active_window(self.motor_parameters)
        
        self.stim_parameters = Parameters()
        self.stim_test_parameters = TestParameters()
        self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
        self.stimulation_screen.manage_active_window(self.stim_parameters)
        self.stimulation_signal = []
        
        self.thread_motor_control = threading.Thread(target=self.motor_control_function, args=(1,))
        self.thread_sensors = threading.Thread(target=self.sensors_function, args=(1,))
        self.thread_stimulations = threading.Thread(target=self.stimulations_function, args=(1,))
        
        self.stop_motor = False
        self.stop_stimulations = False
        
        self.thread_motor_control.start()
        self.thread_sensors.start()
        self.thread_stimulations.start()
        
        #self.crankset = CranksetCommunicator(self.read_crankset)
        # self.motor = Motor('tsdz2', 0 , 0, 0, 0 , 0, 0, 0)
        # self.motor = Motor()
        # For now, we will only use one screen to make the implementation easier
        # self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
        # self.stimulator = Stimulator( 2, main_sef, "COM1")
        # self.usbDriveWriter = CrankserRecorder(self.read_crankset)
        # self.motor_parameters = MotorParameters()
        # self.motor_parameters.register_observer(self)
        
        # self.data = ReceiveDataClient()
        # TODO: Déplacer les deux lignes suivantes dans une boucle pour faire la prise de données
        # self.data.receiveForce() # Stock un vecteur de 12 éléments dans data.message (pas de return)
        # force = self.data.message


        #self.test_timer()
        
        self.start_application()

        # self.assistance_screen.start_application()
        # self.stimulation_screen.start_stimulation_application()
        
        # sys.exit(self.application.exec_())
    
    def motor_control_function(self, name):
        # logging.info("Thread %s: starting", name)
        while(self.stop_motor == False):
            time.sleep(1)
            print("Adjusting motor control...")
        print("Stopped motor control")
        # logging.info("Thread %s: finishing", name)
        
    def sensors_function(self, name):
        # logging.info("Thread %s: starting", name)
        while(self.stop_motor == False or self.stop_stimulations == False):
            time.sleep(0.1)
            # self.data.receiveForce() # Stock un vecteur de 12 éléments dans data.message (pas de return)
            # force = self.data.message
            print("Receiving data from sensors...")
        print("Stopped receiveing data from sensors")
        # logging.info("Thread %s: finishing", name)
    
    def stimulations_function(self, name):
        # logging.info("Thread %s: starting", name)
        while(self.stop_stimulations == False):
            time.sleep(0.1)
            print("Sending new stimulation data...")
        print("Stopped stimulations")
        # logging.info("Thread %s: finishing", name)

    def read_assistance_screen(self, command):
        # if command == "command_amplitude":
        #     print("(Ergocycle) Commanding amplitude") # + str(self.assistance_screen.get_amplitude()))
            
        # elif command == "test_event":
        #     print("(Ergocycle) TESTING EVENT")
            
        if command == "start_training":
            self.assistance_screen.next_window()
            self.assistance_screen.current_menu.submit_clicked(self.motor_parameters)
            
            print("(Ergocycle) Beginning training...")
            print("Initial parameters :")
            print(f"Mode : {self.motor_parameters.get_training_type()}")
            print(f"Target power : {self.motor_parameters.get_target_power()} W")
            print(f"Training length : {self.motor_parameters.get_training_length()} min")
            
            self.assistance_screen.manage_active_window(self.motor_parameters)
            
            # TODO: Prévenir le UI de stimulation que le training doit commencer
            # self.stimulation_screen.flag_ready = True
            
            # TODO: Activer le moteur et démarrer l'entraînement
            
            # TODO: Démarrer la prise de données
            
        elif command == "increase_target_power":
            self.motor_parameters.increase_target_power()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Target power increased")
            
            # TODO: Augmenter la vitesse/torque du moteur
        
        elif command == "decrease_target_power":
            self.motor_parameters.decrease_target_power()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Target power decreased")
            
            # TODO: Diminuer la vitesse/torque du moteur
            
        elif command == "increase_training_length":
            self.motor_parameters.increase_training_length()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Training length increased")
        
        elif command == "decrease_training_length":
            self.motor_parameters.decrease_training_length()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Training length decreased")
            
        elif command == "stop_training":
            self.assistance_screen.next_window()
            self.assistance_screen.manage_active_window(self.motor_parameters)
            # self.assistance_screen.current_menu.stop_clicked()
            print("(Ergocycle) Waiting for confirmation to stop...")
        
        elif command == "continue_training":
            print("(Ergocycle) Continuing training...")
        
        elif command == "confirmed_stop_training":
            print("(Ergocycle) Stopping training...")
            self.stop_motor = True
            
            # TODO: Éteindre le moteur et arrêter l'entraînement
            
            # TODO: Arrêter la prise de données
            
            # TODO: Enregistrer les données dans un fichier
            
        else:
            print("(Ergocycle) Command " + command + " not found")

    def read_stimulation_screen(self, command):
        
        # if command == "USER CLICKING":
        #     print("(Ergocycle) Commanding a test ") # + str(self.stimulation_screen.get_something()))
        
        if command == "start_test":
            self.stimulation_screen.window_counter = -1
            self.stimulation_screen.current_menu.get_test_parameters(self.stim_test_parameters)
            self.stimulation_screen.manage_active_window(self.stim_test_parameters)
            print("Ergocycle commanding to get initial test parameters") # +str(self.stimulation_screen.get_initial_test_parameters)
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"Initial test parameters : {self.stimulation_signal}")
            
        elif command == "increase_amp":
            self.stimulation_screen.current_menu.increase_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")
            
        elif command == "increase_frequency":
            self.stimulation_screen.current_menu.increase_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test frequency : {self.stim_test_parameters.frequency}")
            
        elif command == "increase_imp":
            self.stimulation_screen.current_menu.increase_imp(self.stim_test_parameters)
            print("(Ergocycle) Test impulsion increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test imp : {self.stim_test_parameters.imp}")
        
        elif command == "decrease_amp":
            self.stimulation_screen.current_menu.decrease_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")
            
        elif command == "decrease_frequency":
            self.stimulation_screen.current_menu.decrease_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test frequency : {self.stim_test_parameters.frequency}")
            
        elif command == "decrease_imp":
            self.stimulation_screen.current_menu.decrease_imp(self.stim_test_parameters)
            print("(Ergocycle) Test impulsion decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(self.stim_test_parameters.amplitude, self.stim_test_parameters.frequency,self.stim_test_parameters.imp,self.stim_test_parameters.muscle)
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            #print(f"Updated test parameters : {self.stim_test_parameters.imp}")
            
        elif command == "back_button_clicked":
            self.stimulation_screen.current_menu.close()
            self.stimulation_screen.next_window()
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            print("(Ergocycle) Done testing")
            self.stimulation_signal = self.stim_test_parameters.set_to_off()
            print(f"Initial test parameters : {self.stimulation_signal}")
        
        # elif command == "updated_test_parameters":
        #     print("Ergocycle commanding to get updated test parameters") # +str(self.stimulation_screen.get_updated_test_parameters)
            
        elif command == "start_training":
            self.stimulation_screen.next_window()
            self.stimulation_screen.current_menu.get_test_parameters(self.stim_parameters)
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            print("Ergocycle commanding to go to main menu of stimulations") # +str(self.stimulation_screen.get_initial_training_parameters)
            
        # elif command == "updated_training_parameters":
        #     print("Ergocycle commanding to get updated training parameters")#+str(self.stimulation_screen.get_updated_training_parameters)
        
        elif command == "submit_button_clicked":
            self.stimulation_screen.current_menu.clicked_more(self.stim_parameters)
            print("(Ergocycle) Submit button clicked. Muscles have been chosen by user.")
            
        elif command == "submit_final_button_clicked":
            self.stimulation_screen.current_menu.clicked_next(self.stim_parameters)
            print("(Ergocycle) Final submit button clicked")
            if self.stimulation_screen.current_menu.is_completed(self.stim_parameters) == True:
                ### 4.5.1 - Vérification du danger et appel au bon menu (DangerPopUp ou InstructionWindow) ###
                if self.stimulation_screen.current_menu.danger_check(self.stim_parameters) == True:
                    self.stimulation_screen.window_counter = -2
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    print("(Ergocycle) Verify unsafe parameters")
                else:
                    if self.stimulation_screen.window_counter == -2:
                        self.stimulation_screen.next_window_special()
                    else:
                        self.stimulation_screen.next_window()
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    #print("(Ergocycle) Starting stimulations...")
                    self.read_stimulation_screen("show_instructions")
            
        elif command == "back_to_menu":
            print("(Ergocycle) Waiting for change of parameters...")
            
        elif command == "continue_to_instructions":
            print("(Ergocycle) Continuing with unsafe parameters...")
            self.read_stimulation_screen("show_instructions")
        
        elif command == "show_instructions": # À modifier ou effacer
            print("(Ergocycle) Instructions...")
        
        elif command == "start_stimulations":
            # self.stimulation_screen.current_menu.clicked_start(self.stim_parameters)
            if self.stimulation_screen.current_menu.com_start_feedback == True:
                self.stimulation_screen.current_menu.get_initial_parameters(self.stim_parameters)
                self.stimulation_signal = self.stimulation_screen.current_menu.get_initial_parameters(self.stim_parameters)
                self.stimulation_screen.next_window()
                self.stimulation_screen.manage_active_window(self.stim_parameters)
                print("(Ergocycle) Starting stimulations...")
                print(f"Initial training parameters : {self.stimulation_signal}")
            else:
                self.stimulation_screen.current_menu.start_button.setEnabled(False)
        
        elif command == "increase_amplitude1":
            self.stimulation_screen.current_menu.increase_amplitude1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
            # TODO : Lire la nouvelle matrice?
        elif command == "increase_amplitude2":
            self.stimulation_screen.current_menu.increase_amplitude2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude3":
            self.stimulation_screen.current_menu.increase_amplitude3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude4":
            self.stimulation_screen.current_menu.increase_amplitude4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude5":
            self.stimulation_screen.current_menu.increase_amplitude5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude6":
            self.stimulation_screen.current_menu.increase_amplitude6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 6 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude7":
            self.stimulation_screen.current_menu.increase_amplitude7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_amplitude8":
            self.stimulation_screen.current_menu.increase_amplitude8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
            
        elif command == "decrease_amplitude1":
            self.stimulation_screen.current_menu.decrease_amplitude1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude2":
            self.stimulation_screen.current_menu.decrease_amplitude2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude3":
            self.stimulation_screen.current_menu.decrease_amplitude3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude4":
            self.stimulation_screen.current_menu.decrease_amplitude4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude5":
            self.stimulation_screen.current_menu.decrease_amplitude5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude6":
            self.stimulation_screen.current_menu.decrease_amplitude6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude7":
            self.stimulation_screen.current_menu.decrease_amplitude7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_amplitude8":
            self.stimulation_screen.current_menu.decrease_amplitude8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Amplitude 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
            
        elif command == "increase_frequency1":
            self.stimulation_screen.current_menu.increase_frequency1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency2":
            self.stimulation_screen.current_menu.increase_frequency2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency3":
            self.stimulation_screen.current_menu.increase_frequency3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency4":
            self.stimulation_screen.current_menu.increase_frequency4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency5":
            self.stimulation_screen.current_menu.increase_frequency5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency6":
            self.stimulation_screen.current_menu.increase_frequency6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 6 increased")
        elif command == "increase_frequency7":
            self.stimulation_screen.current_menu.increase_frequency7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_frequency8":
            self.stimulation_screen.current_menu.increase_frequency8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        
        elif command == "decrease_frequency1":
            self.stimulation_screen.current_menu.decrease_frequency1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency2":
            self.stimulation_screen.current_menu.decrease_frequency2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency3":
            self.stimulation_screen.current_menu.decrease_frequency3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency4":
            self.stimulation_screen.current_menu.decrease_frequency4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency5":
            self.stimulation_screen.current_menu.decrease_frequency5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency6":
            self.stimulation_screen.current_menu.decrease_frequency6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency7":
            self.stimulation_screen.current_menu.decrease_frequency7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency8":
            self.stimulation_screen.current_menu.decrease_frequency8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Frequency 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
            
        elif command == "increase_imp1":
            self.stimulation_screen.current_menu.increase_imp1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp2":
            self.stimulation_screen.current_menu.increase_imp2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp3":
            self.stimulation_screen.current_menu.increase_imp3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp4":
            self.stimulation_screen.current_menu.increase_imp4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp5":
            self.stimulation_screen.current_menu.increase_imp5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp6":
            self.stimulation_screen.current_menu.increase_imp6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 6 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp7":
            self.stimulation_screen.current_menu.increase_imp7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "increase_imp8":
            self.stimulation_screen.current_menu.increase_imp8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        
        elif command == "decrease_imp1":
            self.stimulation_screen.current_menu.decrease_imp1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp2":
            self.stimulation_screen.current_menu.decrease_imp2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp3":
            self.stimulation_screen.current_menu.decrease_imp3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp4":
            self.stimulation_screen.current_menu.decrease_imp4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp5":
            self.stimulation_screen.current_menu.decrease_imp5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp6":
            self.stimulation_screen.current_menu.decrease_imp6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp7":
            self.stimulation_screen.current_menu.decrease_imp7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_imp8":
            self.stimulation_screen.current_menu.decrease_imp8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            print("(Ergocycle) Impulsion 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        
        elif command == "pause_stimulation":
            self.stimulation_screen.current_menu.pause()
            print("(Ergocycle) Stimulations paused...")
            
            # TODO : Passer le temps en paramètre si on prend le temps d'Ergocycle
            
        elif command == "stop_stimulation":
            self.stimulation_screen.current_menu.clicked_stop()
            self.stimulation_screen.next_window()
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            self.stop_stimulations = True
            print("(Ergocycle) Stopping stimulations...")
            
        else:
            print("(Ergocycle) Command " + command + " not found")
            
        # print("TODO: Read stimulation screen")

    #def command_stimulator(self):#(self, command)
        #self.stimulator.throw_command("Set frequency to " + self.assistance_screen.get_amplitude() + " volts")

    def test_timer(self):
        print("TEST TIMER")
        # threading.Timer(1, test_timer).start()

    def command_assistance_screen(self, command, parameters):
        print("TODO")

    #si command_parameter est egal a 1 , on modifie la force en fonction du vecteur force genere dans crankset
    def command_motor(self):
    	print("TODO")
        
    def start_application(self):
        sys.exit(self.application.exec_())
    
    #def command_stimulation_screen(self, command, parameters):
        #print("TODO")

    #def read_crankset(self, commanded_parameter, value):
    	#if commanded_parameter == 1:
            #self.motor._force  = value