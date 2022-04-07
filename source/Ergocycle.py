# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
from Screen import Screen as Screen
from StimulationScreen import StimulationScreen as StimulationScreen
from MotorScreen import MotorScreen
# from StimulationSignal import StimulationSignal
#from Stimulator import Stimulator as Stimulator
#import MainWindowStim
#import main_sef
#import InstructionWindow
from MotorParameters import MotorParameters
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

        self.motor_parameters = MotorParameters()
        self.assistance_screen = MotorScreen(self.read_assistance_screen)
        
        self.assistance_screen.manage_active_window(self.motor_parameters)
        # self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
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

        self.assistance_screen.start_application()
        # self.stimulation_screen.start_stimulation_application()

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
            
            # TODO: Augmenter la durée de l'entraînement
        
        elif command == "decrease_training_length":
            self.motor_parameters.decrease_training_length()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Training length decreased")
            
            # TODO: Diminuer la durée de l'entraînement
            
        elif command == "stop_training":
            self.assistance_screen.next_window()
            self.assistance_screen.manage_active_window(self.motor_parameters)
            # self.assistance_screen.current_menu.stop_clicked()
            print("(Ergocycle) Waiting for confirmation...")
        
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
        if command == "USER CLICKING":
            print("(Ergocycle) Commanding a test ") # + str(self.stimulation_screen.get_something()))
        elif command == "start_test":
            print("Ergocycle commanding to get initial test parameters") #+str(self.stimulation_screen.get_initial_test_parameters)
        elif command == "updated_test_parameters":
            print("Ergocycle commanding to get updated test parameters")#+str(self.stimulation_screen.get_updated_test_parameters)
        elif command == "start_training":
            print("Ergocycle commanding to get initial training parameters")#+str(self.stimulation_screen.get_initial_training_parameters)
        elif command == "updated_training_parameters":
            print("Ergocycle commanding to get updated training parameters")#+str(self.stimulation_screen.get_updated_training_parameters)
        elif command == "pause_stimulation":
            print("Ergocycle commanding to pause stimulation")
        elif command == "stop_stimulation":
            print("Ergocycle commanding to stop stimulation")
        else:
            print("(Ergocycle) Commanding initial test parameters NOTHING")
            
        print("TODO: Read stimulation screen")

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
