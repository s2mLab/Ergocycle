# Main class

# Imports
# from Crankset import Crankset
# from Menu import Menu
# from Motor import Motor
from Screen import Screen
# from StimulationSignal import StimulationSignal
# from Stimulator import Stimulator

import threading

class Ergocycle:

    # Constuctor
    def __init__(self):

        # Dictionary that matches events to functions to be called
        function_dictionary = {
            "Modifier / Envoyer" : self.test_event
        }

        self.assistance_screen = Screen(function_dictionary)
        # self.crankset = Crankset()
        # self.crankset_measures = {}
        # self.motor = Motor()
        # For now, we will only use one screen to make the implementation easier
        # self.stimulation_screen = Screen()
        # self.stimulator = Stimulator()

        self.test_timer()


    def test_event(self):
        print("TEST EVENT")

    def test_timer(self):
        print("TEST TIMER")
        # threading.Timer(1, test_timer).start()

    def command_assistance_screen(self, command, parameters):
        print("TODO")

    def command_motor(self, commanded_parameter, value):
        print("TODO")

    def command_stimulation_screen(self, command, parameters):
        print("TODO")

    def command_stimulator(self, command, parameters):
        print("TODO")

    def read_crankset(self):
        print("TODO")
