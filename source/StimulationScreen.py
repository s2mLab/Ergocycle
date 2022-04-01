"""
Created on Wed March 30 11::00 2022

@author: Frédérique Leclerc
"""
from Screen import Screen as Screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
#from Ergocycle.source.StartWindow import StartWindow
from StartWindow import StartWindow
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
        #self.test_button = CommandButton("   Débuter un entraînement   ", "test_event")
        #self.test_button.clicked.connect(lambda : self.event_function(self.test_button.get_command()))
    def start_stimulation_application(self):
        self.win.show()
        sys.exit(self.app.exec_())
    def get_something(self):
        print("SOMETHING")
        #self.InitUI()
    #def InitUI(self):
        #self.app = QApplication(sys.argv)
        #self.win = StartWindow()
        #self.win.show()
        #sys.exit(self.app.exec_())
