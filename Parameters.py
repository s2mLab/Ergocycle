"""
Created on Wed Feb 23 22:02:00 2022

@author: Frédérique Leclerc
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class Parameters():
    def __init__(self):
        super(Parameters, self).__init__()
        
        #self.stim_training_length = 0
        #self.electrode1_muscle = "vide"
        #self.electrode2_muscle = "vide"
        #self.electrode3_muscle = "vide"
        #self.electrode4_muscle = "vide"
        #self.electrode5_muscle = "vide"
        #self.electrode6_muscle = "vide"
        #self.electrode7_muscle = "vide"
        #self.electrode8_muscle = "vide"
        #self.electrode1_amplitude = 0
        #self.electrode2_amplitude = 0
        #self.electrode3_amplitude = 0
        #self.electrode4_amplitude = 0
        #self.electrode5_amplitude = 0
        #self.electrode6_amplitude = 0
        #self.electrode7_amplitude = 0
        #self.electrode8_amplitude = 0
        #self.electrode1_frequency = 0
        #self.electrode2_frequency = 0
        #self.electrode3_frequency = 0
        #self.electrode4_frequency = 0
        #self.electrode5_frequency = 0
        #self.electrode6_frequency = 0
        #self.electrode7_frequency = 0
        #self.electrode8_frequency = 0
        #self.electrode1_length_imp = 0
        #self.electrode2_length_imp = 0
        #self.electrode3_length_imp = 0
        #self.electrode4_length_imp = 0
        #self.electrode5_length_imp = 0
        #self.electrode6_length_imp = 0
        #self.electrode7_length_imp = 0
        #self.electrode8_length_imp = 0
        
    
    ## Aller chercher les valeurs d'amplitudes pour chaque électrode ##
    def get_electrode1_amplitude(self):
        return self.electrode1_amplitude
    
    def set_electrode1_amplitude(self, combo_box):
        self.electrode1_amplitude = combo_box.currentText()

    def get_electrode2_amplitude(self):
        return self.electrode2_amplitude
    
    def set_electrode2_amplitude(self, combo_box):
        self.electrode2_amplitude = combo_box.currentText()

    def get_electrode3_amplitude(self):
        return self.electrode3_amplitude
    
    def set_electrode3_amplitude(self, combo_box):
        self.electrode3_amplitude = combo_box.currentText()
    
    def get_electrode4_amplitude(self):
        return self.electrode4_amplitude
    
    def set_electrode4_amplitude(self, combo_box):
        self.electrode4_amplitude = combo_box.currentText()
    
    def get_electrode5_amplitude(self):
        return self.electrode5_amplitude

    def set_electrode5_amplitude(self, combo_box):
        self.electrode5_amplitude = combo_box.currentText()

    def get_electrode6_amplitude(self):
        return self.electrode6_amplitude
    
    def set_electrode6_amplitude(self, combo_box):
        self.electrode6_amplitude = combo_box.currentText()

    def get_electrode7_amplitude(self):
        return self.electrode7_amplitude
    
    def set_electrode7_amplitude(self, combo_box):
        self.electrode7_amplitude = combo_box.currentText()
    
    def get_electrode8_amplitude(self):
        return self.electrode8_amplitude
    
    def set_electrode8_amplitude(self, combo_box):
        self.electrode8_amplitude = combo_box.currentText()

    ## Aller chercher les valeurs des fréquences pour chaque électrode ##
    def get_electrode1_frequency(self):
        return self.electrode1_frequency
    
    def set_electrode1_frequency(self, combo_box):
        self.electrode1_frequency = combo_box.currentText()

    def get_electrode2_frequency(self):
        return self.electrode2_frequency
    
    def set_electrode2_frequency(self, combo_box):
        self.electrode2_frequency = combo_box.currentText()

    def get_electrode3_frequency(self):
        return self.electrode3_frequency
    
    def set_electrode3_frequency(self, combo_box):
        self.electrode3_frequency= combo_box.currentText()
    
    def get_electrode4_frequency(self):
        return self.electrode4_frequency
    
    def set_electrode4_frequency(self, combo_box):
        self.electrode4_frequency = combo_box.currentText()
    
    def get_electrode5_frequency(self):
        return self.electrode5_frequency

    def set_electrode5_frequency(self, combo_box):
        self.electrode5_frequency = combo_box.currentText()

    def get_electrode6_frequency(self):
        return self.electrode6_frequency
    
    def set_electrode6_frequency(self, combo_box):
        self.electrode6_frequency = combo_box.currentText()

    def get_electrode7_frequency(self):
        return self.electrode7_frequency
    
    def set_electrode7_frequency(self, combo_box):
        self.electrode7_frequency = combo_box.currentText()
    
    def get_electrode8_frequency(self):
        return self.electrode8_frequency
    
    def set_electrode8_frequency(self, combo_box):
        self.electrode8_frequency = combo_box.currentText()

    ## Aller chercher les valeurs des durées d'impulsions pour chaque électrode ##
    def get_electrode1_length_imp(self):
        return self.electrode1_length_imp
    
    def set_electrode1_length_imp(self, combo_box):
        self.electrode1_length_imp = combo_box.currentText()

    def get_electrode2_length_imp(self):
        return self.electrode2_length_imp
    
    def set_electrode2_length_imp(self, combo_box):
        self.electrode2_length_imp = combo_box.currentText()

    def get_electrode3_length_imp(self):
        return self.electrode3_length_imp
    
    def set_electrode3_length_imp(self, combo_box):
        self.electrode3_length_imp= combo_box.currentText()
    
    def get_electrode4_length_imp(self):
        return self.electrode4_length_imp
    
    def set_electrode4_length_imp(self, combo_box):
        self.electrode4_length_imp = combo_box.currentText()
    
    def get_electrode5_length_imp(self):
        return self.electrode5_length_imp

    def set_electrode5_length_imp(self, combo_box):
        self.electrode5_length_imp = combo_box.currentText()

    def get_electrode6_length_imp(self):
        return self.electrode6_length_imp
    
    def set_electrode6_length_imp(self, combo_box):
        self.electrode6_length_imp = combo_box.currentText()

    def get_electrode7_length_imp(self):
        return self.electrode7_length_imp
    
    def set_electrode7_length_imp(self, combo_box):
        self.electrode7_length_imp = combo_box.currentText()
    
    def get_electrode8_length_imp(self):
        return self.electrode8_length_imp
    
    def set_electrode8_length_imp(self, combo_box):
        self.electrode8_length_imp = combo_box.currentText()

    ## Aller chercher les muscles à stimuler pour chaque électrodes ##
    def get_electrode1_muscle(self):
        return self.electrode1_muscle
    def set_electrode1_muscle(self,combo_box):
        self.electrode1_muscle = combo_box.currentText()
    
    def get_electrode2_muscle(self):
        return self.electrode2_muscle
    def set_electrode2_muscle(self,combo_box):
        self.electrode2_muscle = combo_box.currentText()

    def get_electrode3_muscle(self):
        return self.electrode3_muscle
    def set_electrode3_muscle(self,combo_box):
        self.electrode3_muscle = combo_box.currentText()

    def get_electrode4_muscle(self):
        return self.electrode4_muscle
    def set_electrode4_muscle(self,combo_box):
        self.electrode4_muscle = combo_box.currentText()

    def get_electrode5_muscle(self):
        return self.electrode5_muscle
    def set_electrode5_muscle(self,combo_box):
        self.electrode5_muscle = combo_box.currentText()
    
    def get_electrode6_muscle(self):
        return self.electrode6_muscle
    def set_electrode6_muscle(self,combo_box):
        self.electrode6_muscle = combo_box.currentText()

    def get_electrode7_muscle(self):
        return self.electrode7_muscle
    def set_electrode7_muscle(self,combo_box):
        self.electrode7_muscle = combo_box.currentText()

    def get_electrode8_muscle(self):
        return self.electrode8_muscle
    def set_electrode8_muscle(self,combo_box):
        self.electrode8_muscle = combo_box.currentText()
    
    ## Aller chercher le temps de stimulation de l'entrainement 
    def get_stim_training_length(self):
        return self.stim_training_length    
    def set_stim_training_length(self, combo_box):
        self.stim_training_length = int(combo_box.currentText())
