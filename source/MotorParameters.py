# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:40:36 2022

@author: Nicolas Pelletier-Côté
"""

from PyQt5.QtCore import QTimer, QTime

# from Observable import Observable

MIN_TARGET_POWER = 0
MAX_TARGET_POWER = 100

MIN_TRAINING_LENGTH = 1
MAX_TRAINING_LENGTH = 120 # À modifier

class MotorParameters():
    def __init__(self):
        super(MotorParameters, self).__init__()
        
        self.training_type = "Concentrique"
        self.current_power = 0
        self.target_power = 0
        self.training_length = 0
        self.distance = 0
        
        
    def get_training_type(self):
        return self.training_type
    
    def set_training_type(self, combo_box):
        self.training_type = combo_box.currentText()
    
    def get_current_power(self):
        # TODO: Ajouter la commande pour aller chercher les mesures de puissance
        return self.current_power
    
    def get_target_power(self):
        return self.target_power
    
    def set_target_power(self, combo_box):
        self.target_power = int(combo_box.currentText())
        
    def get_training_length(self):
        return self.training_length    
    
    def set_training_length(self, combo_box):
        self.training_length = int(combo_box.currentText())
        
    def increase_target_power(self):
        if(self.target_power < MAX_TARGET_POWER):
            self.target_power += 1
            # TODO : Communiquer avec le moteur
        
    def decrease_target_power(self):
        if(self.target_power > MIN_TARGET_POWER):
            self.target_power -= 1
            # TODO : Communiquer avec le moteur
    
    def increase_training_length(self):
        if(self.training_length < MAX_TRAINING_LENGTH):
            self.training_length += 1
    
    def decrease_training_length(self):
        if(self.training_length > MIN_TRAINING_LENGTH):
            self.training_length -= 1
            # TODO : Vérifier que la durée actuelle est inférieure à la nouvelle durée
    
    def get_distance(self):
        return self.distance