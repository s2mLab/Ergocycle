# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:22:48 2022

@author: nicol
"""
from Screen import Screen as Screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image
from MainWindowMotor import MainWindowMotor
from ActivityMenu import ActivityMenu
from MotorParameters import MotorParameters
import sys
from CommandButton import CommandButton as CommandButton

class MotorScreen(Screen):
    def __init__(self, event_function):
        super(MotorScreen, self).__init__(event_function)
        self.event_function = event_function
        self.app = QApplication(sys.argv)
        
        self.motor_parameters = MotorParameters()
        # self.main_window_motor
        
        # self.connect_buttons(self.main_window_motor)
        self.window_counter = 0
        self.current_menu = 0
        self.manage_active_window()
        
    
    def manage_active_window(self):
        if self.window_counter == 0:
            self.current_menu = MainWindowMotor(self.motor_parameters)
            self.connect_buttons(self.current_menu)
        elif self.window_counter == 1:
            self.current_menu.close()
            self.current_menu = ActivityMenu(self.motor_parameters)
        
        
        
    def connect_buttons(self, window):
    # Connect before the show or the exec
        print(f"{len(window.button_dictionary)} Buttons:")
        for button in window.button_dictionary:
            #print(widget)
            #print(type(widget))
            button.clicked.connect(lambda : self.event_function(window.button_dictionary[button]))
            self.event_function(window.button_dictionary[button])
                
            print(f"CONNECTED BUTTON {window.button_dictionary[button]} TO ERGOCYCLE")
        
        # print(f"{window.layout.count()} Widgets:")
        # for i in range(0, window.layout.count()):
        #     widget = window.layout.itemAt(i).widget()
        #     #print(widget)
        #     #print(type(widget))
        #     if type(widget) is CommandButton:

        #         widget.clicked.connect(lambda : self.event_function(widget.get_command()))
                
        #         print(f"CONNECTED BUTTON {widget.get_command()} TO ERGOCYCLE")
    
    # def start_motor_application(self):
    #     self.win.show()
    #     sys.exit(self.app.exec_())