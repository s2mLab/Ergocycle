# Screen class

# Imports (libraries)
import sys
import math
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from CommandButton import CommandButton as CommandButton

# Imports (classes)
from Menu import Menu

class Screen:

    # Constuctor
    def __init__(self, event_function):
        print("THIS IS A TEST")

        self.event_function = event_function

        self.width = 640
        self.height = 480

        self.speed = 100

        self.application = QApplication([])

        self.window = QWidget()
        self.window.setWindowTitle('Test interface graphique')
        self.window.setFixedWidth(self.width)
        self.window.setFixedHeight(self.height)

        layout = QHBoxLayout()
        layout.addWidget(QLabel('Amplitude:'))
        self.amplitude_edit = QLineEdit()
        layout.addWidget(self.amplitude_edit)
        self.send_button = CommandButton("Commander amplitude", "command_amplitude")
        self.send_button.clicked.connect(lambda : self.event_function(self.send_button.get_command()))
        layout.addWidget(self.send_button)
        self.test_button = CommandButton("Tester événements", "test_event")
        self.test_button.clicked.connect(lambda : self.event_function(self.test_button.get_command()))
        layout.addWidget(self.test_button)

        # Connect before the show or the exec
        """
        print("Widgets:")
        for i in range(0, layout.count()):
            widget = layout.itemAt(i).widget()
            #print(widget)
            #print(type(widget))
            if type(widget) is CommandButton:

                widget.clicked.connect(lambda : self.event_function(widget.get_command()))

                print("CONNECTED BUTTON TO ERGOCYCLE")
        """
        self.window.setLayout(layout)
        #self.window.show()



    def start_application(self):
        #sys.exit(self.app.exec_())
        self.window.show() ## était avant a la ligne 61
        self.application.exec_()

#    def clicked(self):


    def get_amplitude(self):
        return self.amplitude_edit.text()
