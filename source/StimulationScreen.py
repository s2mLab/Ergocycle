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
        # self.app= QApplication(sys.argv)
        # self.win = StartWindow()
        # self.window_counter = 0
        self.current_menu = 0
        # self.manage_active_window()
        #self.manage_active_window()
        #parameters = Parameters()
        #start_win = StartWindow()
        #testing_win = TestingWindow()
        #instruction_win = InstructionWindow()
        #stim_win = StimulationWindow

        #self.test_button = CommandButton("   Débuter un entraînement   ", "test_event")
        #self.test_button.clicked.connect(lambda : self.event_function(self.test_button.get_command()))
    #def start_stimulation_application(self):
        #self.win.show()
        #sys.exit(self.app.exec_())
        
    def get_initial_test_parameters(self, start_win):
        self.initial_test_parameters = start_win.get_initial_test_parameters()
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
        self.get_smth = "Ca fonctionne!"
        return(self.get_smth)
    
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
            self.current_menu.increase_amp_button.clicked.connect(lambda:self.event_function("increase_amp"))
            self.current_menu.increase_freq_button.clicked.connect(lambda:self.event_function("increase_frequency"))
            self.current_menu.increase_imp_button.clicked.connect(lambda:self.event_function("increase_imp"))
            self.current_menu.decrease_amp_button.clicked.connect(lambda:self.event_function("decrease_amp"))
            self.current_menu.decrease_freq_button.clicked.connect(lambda:self.event_function("decrease_frequency"))
            self.current_menu.decrease_imp_button.clicked.connect(lambda:self.event_function("decrease_imp"))
            self.current_menu.back_button.clicked.connect(lambda:self.event_function("back_button_clicked"))
            self.current_menu.show()
            
        elif self.window_counter == 1:
            self.current_menu.close()
            self.current_menu = MainWindowStim()
            self.current_menu.submit_button.clicked.connect(lambda:self.event_function("submit_button_clicked"))
            self.current_menu.submit_final_button.clicked.connect(lambda:self.event_function("submit_final_button_clicked"))
            self.current_menu.show()
            
        elif self.window_counter == -2:
            print("Danger Pop Up")
            
        elif self.window_counter == 2:
            print(".")
            
    # def connect_buttons(self, window):
    #     print(f"{len(window.button_dictionary)} Buttons:")
    #     for button in window.button_dictionary:
    #         button.clicked.connect(lambda:self.event_function(window.button_dictionary[button]))
    #         print(f"CONNECTED BUTTON {window.button_dictionary[button]} TO ERGOCYCLE.")
        #self.InitUI()
    #def InitUI(self):
        #self.app = QApplication(sys.argv)
        #self.win = StartWindow()
        #self.win.show()
        #sys.exit(self.app.exec_())
