# Screen class

# Imports (libraries)
# import sys
# import math
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QHBoxLayout
# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import QLineEdit
# from CommandButton import CommandButton as CommandButton
# from Ergocycle import read_assistance_screen

from MainWindowMotor import MainWindowMotor
from MotorParameters import MotorParameters

from PyQt5.QtCore import QTimer, QTime

# Imports (classes)
from Menu import Menu

SCREEN_WIDTH = 1920
SCREEN_HEIGTH = 1080


class Screen:

    # Constuctor
    def __init__(self, event_function): # , menu
        #print("THIS IS A TEST")

        self.event_function = event_function

        # self.width = SCREEN_WIDTH
        # self.height = SCREEN_HEIGTH

        #self.speed = 100
        self.window_counter = 0

        # self.application = QApplication([])
        # self.stim_application = QApplication([])

        #self.window = QWidget()
        #self.window.setWindowTitle("Titre")
        #self.window.setFixedWidth(self.width)
        #self.window.setFixedHeight(self.height)

        # self.layout = QHBoxLayout()
        # if window_title == "stimulation":
        #     print("stimulaiton window")
        # layout.addWidget(QLabel('Amplitude:'))
        # self.amplitude_edit = QLineEdit()
        # layout.addWidget(self.amplitude_edit)
        # self.send_button = CommandButton("Commander amplitude", "command_amplitude")
        # self.send_button.clicked.connect(lambda : self.send_button.get_command())
        # layout.addWidget(self.send_button)
        # self.test_button = CommandButton("Tester événements", "test_event")
        # self.test_button.clicked.connect(lambda : self.test_button.get_command())
        # layout.addWidget(self.test_button)
        
        # if (menu == "main"):
        #     self.motor_parameters = MotorParameters()
        #     self.main_window_motor = MainWindowMotor(self.motor_parameters)
        #     self.connect_buttons(self.main_window_motor)
        # elif(menu == "activity"):
        #     self.activity_menu = ActivityMenu()
        
        #self.window.show()
        # self.connect_buttons(self.main_window_motor)

    # def connect_buttons(self, window):
    # # Connect before the show or the exec
    
    #     print(f"{window.layout.count()} Widgets:")
    #     for i in range(0, window.layout.count()):
    #         widget = window.layout.itemAt(i).widget()
    #         #print(widget)
    #         #print(type(widget))
    #         if type(widget) is CommandButton:

    #             widget.clicked.connect(lambda : self.event_function(widget.get_command()))
                
    #             print(f"CONNECTED BUTTON {widget.get_command()} TO ERGOCYCLE")
        
        #self.window.setLayout(layout)
        

    # def start_stimulation_application(self):
        # self.current_menu.show()
        # sys.exit(self.application.exec_())

    # def start_application(self):
        #sys.exit(self.application.exec_())
        #self.motor_menu_window.show() ## était avant a la ligne 61
        #self.application.exec_()
        # self.current_menu.show()
        # sys.exit(self.application.exec_())
        # print("")

#    def clicked(self):

    def next_window(self):
        self.window_counter += 1
        # print(self.window_counter)

    def next_window_special(self):
        self.window_counter += 4
        # print(self.window_counter)

    def get_amplitude(self):
        return self.amplitude_edit.text()
