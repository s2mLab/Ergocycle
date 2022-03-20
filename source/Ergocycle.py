# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
from Screen import Screen as Screen
# from StimulationSignal import StimulationSignal
from Stimulator import Stimulator as Stimulator
import MainWindowStim

import threading

"""
Choices for the events:
- Multiple function in Ergocycle (more simple and more organised)
- One function and multiple commands in Ergocycle
"""


class Ergocycle:

    INIT_TIMER = 0.5

    # Constuctor
    def __init__(self):

        self.assistance_screen = Screen(self.read_assistance_screen)
        # self.crankset = Crankset()
        # self.crankset_measures = {}
        # self.motor = Motor()
        # For now, we will only use one screen to make the implementation easier
        # self.stimulation_screen = Screen(self.read_stimulation_screen)
        # self.stimulator = Stimulator("a ts2", "a StimulationSignal", "a port path")
        # self.usbDriveWriter = UsbDriveWriter()


        #self.test_timer()

        self.assistance_screen.start_application()

    def read_assistance_screen(self, command):
        if command == "command_amplitude":
            print("(Ergocycle) Commanding amplitude " + str(self.assistance_screen.get_amplitude()))
        elif command == "test_event":
            print("(Ergocycle) TESTING EVENT")
        else:
            print("(Ergocycle) Command " + command + " not found")

    def read_stimulation_screen(self):
        print("TODO: Read stimulation screen")

    #def command_stimulator(self):#(self, command)
        #self.stimulator.throw_command("Set frequency to " + self.assistance_screen.get_amplitude() + " volts")

    def test_timer(self):
        print("TEST TIMER")
        # threading.Timer(1, test_timer).start()

    def command_assistance_screen(self, command, parameters):
        print("TODO")

    def command_motor(self, commanded_parameter, value):
        print("TODO")

    def command_stimulation_screen(self, command, parameters):
        print("TODO")

    def read_crankset(self):
        print("TODO")

    def initialise_stimulation(self):
        if(MainWindowStim.InitUI): #changer pour que ce soit évènement lié  l'ouverture du UI
          Stimulator.call_init()
