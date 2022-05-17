# Motor class
from __future__ import print_function

import odrive
#import numpy 
from odrive.enums import *
import time
import math
# from abc import ABC, abstractmethod

# from sqlalchemy import false 

class Motor():
    # Constuctor
    def __init__(self, nom, kp, ki, T, couple, vitesse, val_max, val_min, duree_ent): #, carte : odrive) :
        self._nom = nom
        self._carte = []
        self._kp = kp
        self._ki = ki
        self._couple = couple
        self._vitesse = vitesse 
        self._dt = T
        self._val_max = val_max
        self._val_min = val_min
        self._est_concentrique = True
        self._est_excentrique = False
        self._couple_usager = 0
        self._duree = duree_ent
        print("moteur construit")
    def __del__(self):
        print("moteur detruit")
    
    def calibratre_motor(self):
        # Find a connected ODrive (this will block until you connect one)
        print("finding an odrive...")
        my_drive = odrive.find_any()
        print("odrive found")
        
        # Calibrate motor and wait for it to finish
        print("starting calibration...")
        my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
        while my_drive.axis0.current_state != AXIS_STATE_IDLE:
            time.sleep(0.1)
        return my_drive
    
    def get_force_usager (self):
        self._force_usager += 1  #récupération du torque de l'usager 

    def concentric_mode(self):
        self._carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL #pour démarrer le moteur
        self._carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL #set le mode torque
        self._carte.axis0.motor.config.torque_constant = 0.21 
        self._carte.axis0.controller.input_torque = self._couple #set le couple normalement en Nm.
        start = time.time()
        end = time.time()
       
        #PI
        erreur = self._couple_usager - self._couple 
        #Modification de la condition du while
        #variation_couple_usager = self.couple_cible - self._couple_usager
        #seuil_acceptabilite = 0.1*self.couple_cible 
        compte = 0
        #Asservissement 
        start = time.time()
        end = time.time()        
        while (end - start) <= self._duree :
            seconde = end - start
            end = time.time()
            #while abs(variation_couple_usager) >= seuil_accceptabilite and self._est_concentrique
            print("Dans la boucle du temps") 
            while abs(erreur) >= 5 and self._est_concentrique : 
                end = time.time()
                seconde = end - start
                erreur = self._couple_usager - self._couple  
                P_o = self._kp*erreur
                integral = erreur*self._dt
                I_o = self._ki * integral
                controller = P_o + I_o
                if controller > self._val_max :
                    controller = self._val_max   
                elif controller < self._val_min :
                    controller = self._val_min
                self._couple += controller 
                compte += 1 
                print("torque", compte)
                print(self._couple)           
                #self._carte.axis0.controller.input_torque = self._force                 
                if (end - start) >= self._duree :
                    break
        print("mode concentrique")

    def eccentric_mode(self):
        #initialisation du projet 
        self._carte.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
        while self._carte.axis0.current_state != AXIS_STATE_IDLE:
              time.sleep(0.1)
        self._carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL 
        self._carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
        self._carte.axis0.motor.config.torque_constant = 8.23 / 150
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

    def passif_mode(self) :    
        start = time.time() 
        end = time.time()  
        while (end - start) <= 30 : 
            end = time.time()
        new_time = time.time() 
        new_end_time = time.time() 
        self._carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL #pour démarrer le moteur
        self._carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL #set le mode torque
        self._carte.axis0.motor.config.torque_constant = 0.21  
        self._carte.axis0.controller.input_torque = self._couple #set le couple normalement en Nm. scale en 0 et 1        
        while (new_end_time - new_time) <= 30 :
            new_end_time = time.time()
            vitesse = self._carte.axis0.encoder.vel_estimate
            courant = self._carte.axis0.motor.current_control.Iq_setpoint 
            puissance = self._couple * vitesse  
            print("puissance en watt :", puissance)

        self._carte.axis0.controller.input_torque = 0.0




#test 
# moteur = Motor('tsdz2', 0.1 , 0.5, 0.1, 3 , 50, 35, -35, 30)
# type = moteur._nom 
# print ("force usager debut: " , moteur._couple_usager)
# #print("le moteur  est de type", type)
# moteur._couple_usager = 25
# #print ("force usager apres: ", moteur._force_usager)
# #print ("test")
# # erreur_test = moteur._force - moteur._force_usager
# # print(erreur_test)
# moteur.concentric_mode()
#a = moteur._force_usager
#moteur.get_force_usager()
#b = moteur._force_usager
#print(a)
#print(b)
#moteur.concentric_mode() 
