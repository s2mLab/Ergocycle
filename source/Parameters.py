import string
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import numpy
from numpy import *


class Parameters():
    def __init__(self):
        super(Parameters, self).__init__()
    # Aller chercher les valeurs d'amplitudes pour chaque électrode ##
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

    # Aller chercher les valeurs des fréquences pour chaque électrode ##
    def get_electrode1_frequency(self):
        return self.electrode1_frequency
    
    def set_electrode1_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode1_frequency = str(10)
        else: 
            self.electrode1_frequency = combo_box.currentText()
        

    def get_electrode2_frequency(self):
        return self.electrode2_frequency
    
    def set_electrode2_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode2_frequency = str(10)
        else: 
            self.electrode2_frequency = combo_box.currentText()

    def get_electrode3_frequency(self):
        return self.electrode3_frequency
    
    def set_electrode3_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode3_frequency = str(10)
        else: 
            self.electrode3_frequency= combo_box.currentText()
    
    def get_electrode4_frequency(self):
        return self.electrode4_frequency
    
    def set_electrode4_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode4_frequency = str(10)
        else: 
            self.electrode4_frequency = combo_box.currentText()
    
    def get_electrode5_frequency(self):
        return self.electrode5_frequency

    def set_electrode5_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode5_frequency = str(10)
        else: 
            self.electrode5_frequency = combo_box.currentText()

    def get_electrode6_frequency(self):
        return self.electrode6_frequency
    
    def set_electrode6_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode6_frequency = str(10)
        else: 
            self.electrode6_frequency = combo_box.currentText()

    def get_electrode7_frequency(self):
        return self.electrode7_frequency
    
    def set_electrode7_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode7_frequency = str(10)
        else: 
            self.electrode7_frequency = combo_box.currentText()
    
    def get_electrode8_frequency(self):
        return self.electrode8_frequency
    
    def set_electrode8_frequency(self, combo_box):
        if combo_box.currentText() == str(5):
            self.electrode8_frequency = str(10)
        else: 
            self.electrode8_frequency = combo_box.currentText()

    # Aller chercher les valeurs des durées d'impulsions pour chaque électrode ##
    def get_electrode1_length_imp(self):
        return self.electrode1_length_imp
    
    def set_electrode1_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode1_length_imp = str(20)
        else: 
            self.electrode1_length_imp = combo_box.currentText()

    def get_electrode2_length_imp(self):
        return self.electrode2_length_imp
    
    def set_electrode2_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode2_length_imp = str(20)
        else: 
            self.electrode2_length_imp = combo_box.currentText()

    def get_electrode3_length_imp(self):
        return self.electrode3_length_imp
    
    def set_electrode3_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode3_length_imp = str(20)
        else: 
            self.electrode3_length_imp= combo_box.currentText()
    
    def get_electrode4_length_imp(self):
        return self.electrode4_length_imp
    
    def set_electrode4_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode4_length_imp = str(20)
        else: 
            self.electrode4_length_imp = combo_box.currentText()
    
    def get_electrode5_length_imp(self):
        return self.electrode5_length_imp

    def set_electrode5_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode5_length_imp = str(20)
        else: 
            self.electrode5_length_imp = combo_box.currentText()

    def get_electrode6_length_imp(self):
        return self.electrode6_length_imp
    
    def set_electrode6_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode6_length_imp = str(20)
        else: 
            self.electrode6_length_imp = combo_box.currentText()

    def get_electrode7_length_imp(self):
        return self.electrode7_length_imp
    
    def set_electrode7_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode7_length_imp = str(20)
        else: 
            self.electrode7_length_imp = combo_box.currentText()
    
    def get_electrode8_length_imp(self):
        return self.electrode8_length_imp
    
    def set_electrode8_length_imp(self, combo_box):
        if combo_box.currentText() == str(10):
            self.electrode8_length_imp = str(20)
        else: 
            self.electrode8_length_imp = combo_box.currentText()

    # Aller chercher les muscles à stimuler pour chaque électrodes ##
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

    # Transformer les muscles en numeros ##
    def get_muscle_number(self):
        self.muscle_number = numpy.empty([1,8], dtype=int)
        self.muscle=[self.get_electrode1_muscle(),self.get_electrode2_muscle(), self.get_electrode3_muscle(), self.get_electrode4_muscle(), self.get_electrode5_muscle(), self.get_electrode6_muscle(), self.get_electrode7_muscle(),self.get_electrode8_muscle()]
        for i in range(len(self.muscle)):
            if self.muscle[i] == "Aucun":
                self.muscle_number[0,i] = 0
            if self.muscle[i] == "Biceps Brachii":
                self.muscle_number[0,i] = 1
            if self.muscle[i] == "Triceps Brachii":
                self.muscle_number[0,i] = 2
            if self.muscle[i] == "Deltoide Postérieur":
                self.muscle_number[0,i] = 3
            if self.muscle[i] == "Deltoide Antérieur":
                self.muscle_number[0,i] = 4
            #if self.muscle[i] == "Grand pectoral": ## Conservé si vous désirer ajouter des muscles à stimuler
                #self.muscle_number[0,i] = 5
            #if self.muscle[i] =="Trapezius descendens":
                #self.muscle_number[0,i] = 6
            #if self.muscle[i] == "Infraspinatus":
                #self.muscle_number[0,i] = 7
            #if self.muscle[i] == "Supraspinatus":
                #self.muscle_number[0,i] = 8
            #if self.muscle[i] == "Subscapularis":
                #self.muscle_number[0,i] = 9
            #if self.muscle[i] == "Brachioradialis":
                #self.muscle_number[0,i] = 10
            #if self.muscle[i] =="Faisceau supérieur du trapeze":
                #self.muscle_number[0,i] = 11
            #if self.muscle[i] == "Flexor carpi radialis":
                #self.muscle_number[0,i] = 12
            #if self.muscle[i] == "Extensor carpi ulnaris":
                #self.muscle_number[0,i] = 13
            #if self.muscle[i] == "M. rectus abdominis":
                #self.muscle_number[0,i] = 14
        return(self.muscle_number)

    # Déterminer les couples dangereux ##
    def couple_amplitude_frequency_check(self):
        i = 0
        self.seuil_amplitude = 60
        self.seuil_frequency = 40
        if int(self.get_electrode1_amplitude()) > self.seuil_amplitude and int(self.get_electrode1_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode2_amplitude()) > self.seuil_amplitude and int(self.get_electrode2_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode3_amplitude()) > self.seuil_amplitude and int(self.get_electrode3_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode4_amplitude()) > self.seuil_amplitude and int(self.get_electrode4_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode5_amplitude()) > self.seuil_amplitude and int(self.get_electrode5_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode6_amplitude()) > self.seuil_amplitude and int(self.get_electrode6_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode7_amplitude()) > self.seuil_amplitude and int(self.get_electrode7_frequency())>self.seuil_frequency:
            i += 1
        elif int(self.get_electrode8_amplitude()) > self.seuil_amplitude and int(self.get_electrode8_frequency())>self.seuil_frequency:
            i += 1
        return i

    def couple_amplitude_imp_check(self):
        self.seuil_amplitude = 60
        self.seuil_imp = 250
        j=0
        if int(self.get_electrode1_amplitude()) > self.seuil_amplitude and int(self.get_electrode1_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode2_amplitude()) > self.seuil_amplitude and int(self.get_electrode2_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode3_amplitude()) > self.seuil_amplitude and int(self.get_electrode3_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode4_amplitude()) > self.seuil_amplitude and int(self.get_electrode4_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode5_amplitude()) > self.seuil_amplitude and int(self.get_electrode5_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode6_amplitude()) > self.seuil_amplitude and int(self.get_electrode6_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode7_amplitude()) > self.seuil_amplitude and int(self.get_electrode7_length_imp())>self.seuil_imp:
            j += 1
        elif int(self.get_electrode8_amplitude()) > self.seuil_amplitude and int(self.get_electrode8_length_imp())>self.seuil_imp:
            j += 1
        return j

    def couple_frequency_imp_check(self):  
        self.seuil_frequency = 40
        self.seuil_imp = 250
        k=0
        if int(self.get_electrode1_frequency()) > self.seuil_frequency and int(self.get_electrode1_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode2_frequency()) > self.seuil_frequency and int(self.get_electrode2_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode3_frequency()) > self.seuil_frequency and int(self.get_electrode3_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode4_frequency()) > self.seuil_frequency and int(self.get_electrode4_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode5_frequency()) > self.seuil_frequency and int(self.get_electrode5_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode6_frequency()) > self.seuil_frequency and int(self.get_electrode6_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode7_frequency()) > self.seuil_frequency and int(self.get_electrode7_length_imp())>self.seuil_imp:
            k += 1
        elif int(self.get_electrode8_frequency()) > self.seuil_frequency and int(self.get_electrode8_length_imp())>self.seuil_imp:
            k += 1
        return k

    # Aller chercher le temps de stimulation de l'entrainement
    def get_stim_training_length(self):
        return self.stim_training_length

    def set_stim_training_length(self, combo_box):
        self.stim_training_length = int(combo_box.currentText())
