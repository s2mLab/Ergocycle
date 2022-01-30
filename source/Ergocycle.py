# Main class

# Imports
from Crankset import Crankset
from Menu import Menu
from Motor import Motor
from Screen import Screen
from StimulationSignal import StimulationSignal
from Stimulator import Stimulator

class Ergocycle:

    # Constuctor
    def __init__(self):
        self.assistance_screen = Screen()
        self.crankset = Crankset()
        self.crankset_measures = {}
        self.motor = Motor()
        self.stimulation_screen = Screen()
        self.stimulator = Stimulator()

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
