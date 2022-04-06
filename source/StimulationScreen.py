"""
Created on Wed March 30 11::00 2022

@author: Frédérique Leclerc
"""
from tracemalloc import start
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
import sys
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
        self.app = QApplication(sys.argv)
        self.win = StartWindow()
        #parameters = Parameters()
        #start_win = StartWindow()
        #testing_win = TestingWindow()
        #instruction_win = InstructionWindow()
        #stim_win = StimulationWindow

        #self.test_button = CommandButton("   Débuter un entraînement   ", "test_event")
        #self.test_button.clicked.connect(lambda : self.event_function(self.test_button.get_command()))
    def start_stimulation_application(self):
        self.win.show()
        sys.exit(self.app.exec_())
    def get_initial_test_parameters(self):
        self.get_initial_test_parameters = "USER CLICKING"
        #self.initial_test_parameters = start_win.get_initial_test_parameters()
        return(self.initial_test_parameters)
    def get_updated_test_parameters(self, testing_win):
        self.updated_test_parameters = testing_win.get_updated_test_parameters()
        return(self.updated_test_parameters)
    def get_initial_training_parameters(self, instruction_win):
        self.initial_training_parameters = instruction_win.get_initial_parameters(Parameters)
        return(self.initial_training_parameters)
    def get_updated_training_parameters(self):
        self.updated_training_parameters = self.get_initial_parameters(Parameters)
        return(self.updated_test_parameters)  
    def get_something(self):
        print("USER CLICKING")
        #self.InitUI()
    #def InitUI(self):
        #self.app = QApplication(sys.argv)
        #self.win = StartWindow()
        #self.win.show()
        #sys.exit(self.app.exec_())
