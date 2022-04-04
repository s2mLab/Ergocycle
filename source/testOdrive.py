from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math

def test_vitesse (vitesse, carte : odrive):
    carte.axis0.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION 
    carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL #pour démarrer le moteur
    carte.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL #set le mode vitesse
    start = time.time()
    end = time.time()
    count = 0 
    carte.axis0.controller.input_vel = vitesse #set la vitesse normalement en tr/s. scale en 0 et 1 
    while count <= 10 : 
        while (end - start) <= 2 :
            end = time.time()
        count += 1
        start = end  
        vitesse = carte.axis0.encoder.vel_estimate 
        print("vitesse :", vitesse)       
    carte.axis0.controller.input_vel = 0
    print("Test vitesse reussi")
    
    #Pour le test du changement de sens on peut utiliser la meme fonction avec une vitesse negative

def test_couple (couple, carte : odrive):
    carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL #pour démarrer le moteur
    carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL #set le mode torque
    carte.axis0.motor.config.torque_constant = 0.5 
    carte.axis0.controller.input_torque = couple #set le couple normalement en Nm. scale en 0 et 1
    start = time.time()
    end = time.time()
    count = 0  
    while (end - start) <= 30 :
        end = time.time()
        vitesse = carte.axis0.encoder.vel_estimate 
        courant = carte.axis0.motor.current_control.Iq_setpoint  
        if vitesse == 0.0 : 
            carte.axis0.controller.input_torque += 1
        elif vitesse != 0.0 : 
            carte.axis0.controller.input_torque = couple
        print ("le torque est: ", carte.axis0.controller.input_torque)
    
    carte.axis0.controller.input_torque = 0.0


   
    # courant = carte.axis0.motor.current_control.Iq_measured
    # couple_fin = 8.27 * courant/150
    # carte.axis0.controller.input_torque = 0.0
    # if couple_fin != couple :
    #     print("Test torque echec")
    # else :
    #     print("Test torque reussi")
    # print("couple de fin:", couple_fin, ", couple attendu:", couple)

#Test 
# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()
# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

#decommenter pour effectuer les tests
#test_vitesse(1, my_drive)
test_couple (0.5, my_drive)
#my_drive.axis0.requested_state = AXIS_STATE_IDLE
