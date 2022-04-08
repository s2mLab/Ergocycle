# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
from Screen import Screen as Screen
from StimulationScreen import StimulationScreen as StimulationScreen
from MotorScreen import MotorScreen

from Parameters import Parameters
from TestParameters import TestParameters
from MotorParameters import MotorParameters

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
        #self.crankset = CranksetCommunicator(self.read_crankset)
        # self.motor = Motor('tsdz2', 0 , 0, 0, 0 , 0, 0, 0)
        # self.motor = Motor()
        # For now, we will only use one screen to make the implementation easier
        # self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
        # self.stimulator = Stimulator( 2, main_sef, "COM1")
        # self.usbDriveWriter = CrankserRecorder(self.read_crankset)
        # self.motor_parameters = MotorParameters()
        # self.motor_parameters.register_observer(self)


        #self.test_timer()
        
        self.start_application()

        # self.assistance_screen.start_application()
        # self.stimulation_screen.start_stimulation_application()
        
        # sys.exit(self.application.exec_())

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
            self.stimulation_screen.current_menu.get_initial_test_parameters(self.stim_test_parameters)
            self.stimulation_screen.manage_active_window(self.stim_test_parameters)
            print("Ergocycle commanding to get initial test parameters") # +str(self.stimulation_screen.get_initial_test_parameters)
            print(f"Initial test parameters : {self.stim_test_parameters}")
            
        elif command == "increase_amp":
            self.stimulation_screen.current_menu.increase_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude increased")
            print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")
            
        elif command == "increase_frequency":
            self.stimulation_screen.current_menu.increase_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency increased")
            print(f"Updated test frequency : {self.stim_test_parameters.frequency}")
            
        elif command == "increase_imp":
            self.stimulation_screen.current_menu.increase_imp(self.stim_test_parameters)
            print("(Ergocycle) Test imp increased")
            print(f"Updated test imp : {self.stim_test_parameters.imp}")
        
        elif command == "decrease_amp":
            self.stimulation_screen.current_menu.decrease_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude decreased")
            print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")
            
        elif command == "decrease_frequency":
            self.stimulation_screen.current_menu.decrease_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency decreased")
            print(f"Updated test frequency : {self.stim_test_parameters.frequency}")
            
        elif command == "decrease_imp":
            self.stimulation_screen.current_menu.decrease_imp(self.stim_test_parameters)
            print("(Ergocycle) Test imp decreased")
            print(f"Updated test parameters : {self.stim_test_parameters.imp}")
            
        elif command == "back_button_clicked":
            self.stimulation_screen.current_menu.close()
            self.stimulation_screen.next_window()
            self.stimulation_screen.manage_active_window(self.stim_parameters)
        
        # elif command == "updated_test_parameters":
        #     print("Ergocycle commanding to get updated test parameters") # +str(self.stimulation_screen.get_updated_test_parameters)
            
        elif command == "start_training":
            self.stimulation_screen.next_window()
            self.stimulation_screen.current_menu.get_initial_test_parameters(self.stim_parameters)
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            print("Ergocycle commanding to get initial training parameters") # +str(self.stimulation_screen.get_initial_training_parameters)
            
        # elif command == "updated_training_parameters":
        #     print("Ergocycle commanding to get updated training parameters")#+str(self.stimulation_screen.get_updated_training_parameters)
        
        elif command == "submit_button_clicked":
            self.stimulation_screen.current_menu.clicked_more(self.stim_parameters)
            print("(Ergocycle) Submit button clicked")
            
        elif command == "submit_final_button_clicked":
            self.stimulation_screen.current_menu.clicked_next(self.stim_parameters)
            print("(Ergocycle) Final submit button clicked")
            if self.stimulation_screen.current_menu.is_completed(self.stim_parameters) == True:
                ### 4.5.1 - Vérification du danger et appel au bon menu (DangerPopUp ou InstructionWindow) ###
                if self.stimulation_screen.current_menu.danger_check(self.stim_parameters) == True:
                    # self.stimulation_screen.current_menu.danger_pop_up_window = DangerPopUp(self.stim_parameters)
                    # self.stimulation_screen.current_menu.danger_pop_up_window.setWindowModality(2) ## Bloque les inputs des autres fenêtres
                    # self.stimulation_screen.current_menu.danger_pop_up_window.show()
                    # self.stimulation_screen.current_menu.update()
                    self.stimulation_screen.window_counter = -2
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    print("Danger")
                else:
                    # self.instruction_window = InstructionWindow(init_parameters)
                    # self.close()
                    # self.instruction_window.show()
                    # self.update()
                    self.stimulation_screen.next_window()
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    print("All good")
            
            
        elif command == "pause_stimulation":
            print("Ergocycle commanding to pause stimulation")
            
        elif command == "stop_stimulation":
            print("Ergocycle commanding to stop stimulation")
            
        else:
            print("(Ergocycle) Commanding initial test parameters NOTHING")
            
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
'''
    def initialise_stimulation(self):
        if(MainWindowStim.InitUI): #changer pour que ce soit évènement lié  l'ouverture du UI
          Stimulator.call_init()

       

        #self.stimulator.testing_stimulation() à lier avec +- de la nouvelle fenêtre pour tester

        #Possible de lier commande en-dessous avec MainWindowStim.submit_button?
        parameters = InstructionWindow.get_initial_parameters(MainWindowStim.init_parameter)

        for i in range (len(parameters)):
            if(MainWindowStim.submit_button.clicked.connect() and (parameters[4][i] == 0 or 2) and read_crankset == 40 ): #where 0 = biceps et 2 = post. deltoide, 40 if in degrees
                Stimulator.control_stimulation(i)
                if(read_crankset == 190 ):
                    Stimulator.send_packet('StopChannelListMode', i)

            if(MainWindowStim.submit_button.clicked.connect() and (parameters[4][i] == 1 or 3) and read_crankset == 200 ): #where 1 = triceps et 3 = ant. deltoide, 200 if in degrees
                Stimulator.control_stimulation(i)
                if(read_crankset == 360 ):
                    Stimulator.send_packet('StopChannelListMode', i)
'''
