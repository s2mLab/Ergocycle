# Motor class
from __future__ import print_function

import odrive
#import numpy 
from odrive.enums import *
import time
import math
from abc import ABC, abstractmethod

from sqlalchemy import false 

class Motor():
    # Constuctor
    def __init__(self, nom, kp, ki, T, force, vitesse, val_max, val_min) :
        self._nom = nom
        #self._carte = carte
        self._kp = kp
        self._ki = ki
        self._force = force
        self._vitesse = vitesse 
        self._dt = T
        self._val_max = val_max
        self._val_min = val_min
        self._est_concentrique = True
        self._est_excentrique = false
        self._force_usager = 0
        print("moteur construit")
    def __del__(self):
        print("moteur detruit")
    
    def get_force_usager (self):
        self._force_usager += 1  #récupération du torque de l'usager 

    def concentric_mode(self):
        #initialisation du projet 
        # self._carte.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
        # while self._carte.axis0.current_state != AXIS_STATE_IDLE:
        #       time.sleep(0.1)
        # self._carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL 
        # self._carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
        # self._carte.axis0.controller.input_vel = self._vitesse
        # self._carte.axis0.controller.input_torque = self._force
       
        #PI
        erreur = self._force_usager - self._force  
        compte = 0
        #Asservissement 
        while abs(erreur) >= 5 and self._est_concentrique : 
             erreur = self._force_usager - self._force  
             P_o = self._kp*erreur
             integral = erreur*self._dt
             I_o = self._ki * integral
             controller = P_o + I_o
             if controller > self._val_max :
                controller = self._val_max   
             elif controller < self._val_min :
                 controller = self._val_min
             self._force += controller 
             compte += 1 
             print("torque", compte)
             print(self._force)           
            #self._carte.axis0.controller.input_torque = self._force 


        print("mode concentrique")

    def eccentric_mode(self):
        #initialisation du projet 
        self._carte.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
        while self._carte.axis0.current_state != AXIS_STATE_IDLE:
              time.sleep(0.1)
        self._carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL 
        self._carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
        self._carte.axis0.controller.input_vel = self._vitesse
        self._carte.axis0.controller.input_torque = self._force

        #PI
        #Asservissement 
        erreur_excentrique = self._force_usager - self._force  
        compte = 0
        while erreur_excentrique <= -5 and self._est_excentrique : 
             erreur_excentrique = self._force_usager - self._force  
             P_o = self._kp*erreur_excentrique
             integral = erreur_excentrique*self._dt
             I_o = self._ki * integral
             controller = P_o + I_o
             if controller > self._val_max :
                controller = self._val_max   
             elif controller < self._val_min :
                 controller = self._val_min
             self._force += controller 
             compte += 1 
             print("torque", compte)
             print(self._force)     
             #self._carte.axis0.controller.input_torque = self._force    
        

        print("mode excentrique")


#test 
moteur = Motor('tsdz2', 0.1 , 0.5, 0.1, 3 , 50, 35, -35)
type = moteur._nom 
print ("force usager debut: " , moteur._force_usager)
#print("le moteur  est de type", type)
moteur._force_usager = 25
print ("force usager apres: " , moteur._force_usager)
print ("test")
# erreur_test = moteur._force - moteur._force_usager
# print(erreur_test)
moteur.concentric_mode()
#a = moteur._force_usager
#moteur.get_force_usager()
#b = moteur._force_usager
#print(a)
#print(b)
#moteur.concentric_mode() 

