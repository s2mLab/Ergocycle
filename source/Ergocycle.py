# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
from Screen import Screen as Screen
# from StimulationSignal import StimulationSignal
from Stimulator import Stimulator as Stimulator
#import MainWindowStim
#import main_sef
#import InstructionWindow

import threading

"""
Choices for the events:
- Multiple function in Ergocycle (more simple and more organised)
- One function and multiple commands in Ergocycle
"""


class Ergocycle:

    #INIT_TIMER = 0.5

    # Constuctor
    def __init__(self):

        self.assistance_screen = Screen(self.read_assistance_screen)
        #self.crankset = CranksetCommunicator(self.read_crankset)
        # self.motor = Motor('tsdz2', 0 , 0, 0, 0 , 0, 0, 0)
        # self.motor = Motor()
        # For now, we will only use one screen to make the implementation easier
       # self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
        # self.stimulator = Stimulator( 2, main_sef, "COM1")
        # self.usbDriveWriter = CrankserRecorder(self.read_crankset)


        #self.test_timer()

        self.assistance_screen.start_application()

    def read_assistance_screen(self, command):
        if command == "command_amplitude":
            print("(Ergocycle) Commanding amplitude " + str(self.assistance_screen.get_amplitude()))
        elif command == "test_event":
            print("(Ergocycle) TESTING EVENT")
        else:
            print("(Ergocycle) Command " + command + " not found")

    def read_stimulation_screen(self, command):
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

    def command_stimulation_screen(self, command, parameters):
        print("TODO")

    def read_crankset(self, commanded_parameter, value):
    	if commanded_parameter == 1:
            self.motor._force  = value
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