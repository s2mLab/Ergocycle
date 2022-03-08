# Screen class

# Imports (libraries)
import sys
import math
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

# Imports (classes)
from Menu import Menu

class Screen:

    # Constuctor
    def __init__(self, function_dictionary):
        print("THIS IS A TEST")

        self.width = 640
        self.height = 480

        self.speed = 100

        self.application = QApplication([])

        self.window = QWidget()
        self.window.setWindowTitle('Test interface graphique')
        self.window.setFixedWidth(self.width)
        self.window.setFixedHeight(self.height)

        layout = QHBoxLayout()
        layout.addWidget(QLabel('Vitesse:'))
        layout.addWidget(QLineEdit())
        self.send_button = QPushButton('Modifier / Envoyer')
        layout.addWidget(self.send_button)

        # Connect before the show or the exec
        print("Widgets:")
        for i in range(0, layout.count()):
            widget = layout.itemAt(i).widget()
            #print(widget)
            #print(type(widget))
            if type(widget) is QPushButton:
                # print the push buttons labels
                #print(widget.text())
                label = widget.text()
                if label in function_dictionary:
                    widget.clicked.connect(function_dictionary[label])
                    print("CONNECTED")

        self.window.setLayout(layout)
        self.window.show()


    def start_application(self):
        #sys.exit(self.app.exec_())
        self.application.exec_()

    def get_speed():
        return self.speed

    def get_send_button():
        return self.send_button
