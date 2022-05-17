
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image

from InstructionWindow import InstructionWindow as InstructionWindow
from MainWindowStim import MainWindowStim as MainWindowStim
from StimulationWindow import StimulationWindow as StimulationWindow
from DangerPopUp import DangerPopUp as DangerPopUp

import sys

windows_list = ["InstructionWindow", "MainWindowStim", "StimulationWindow", "DangerPopUp"]

print("Liste:")
for w in windows_list:
    print(w)
print("")
choix = input("Choisissez votre menu: ")

app = QApplication(sys.argv)

if choix == "InstructionWindow":
    win = InstructionWindow()
elif choix == "MainWindowStim":
    win = MainWindowStim()
elif choix == "StimulationWindow":
    win = StimulationWindow()
elif choix == "DangerPopUp":
    win = DangerPopUp()
else:
    sys.exit()

win.show()
sys.exit(app.exec_())
