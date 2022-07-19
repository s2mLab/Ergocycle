from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math

# import Motor


def test_vitesse(speed, carte: odrive):
    carte.axis0.requested_state = AxisState.ENCODER_OFFSET_CALIBRATION
    carte.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL  # pour démarrer le moteur
    carte.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL  # set le mode speed
    start = time.time()
    end = time.time()
    count = 0
    carte.axis0.controller.input_vel = speed  # set la speed normalement en tr/s. scale en 0 et 1
    while count <= 10:
        while (end - start) <= 2:
            end = time.time()
        count += 1
        start = end
        speed = carte.axis0.encoder.vel_estimate
        print("speed :", speed)
    carte.axis0.controller.input_vel = 0
    print("Test speed reussi")

    # Pour le test du changement de sens on peut utiliser la meme fonction avec une speed negative


def test_torque(torque, carte: odrive):
    carte.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL  # pour démarrer le moteur
    carte.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL  # set le mode torque
    carte.axis0.motor.config.torque_constant = 0.21
    carte.axis0.controller.input_torque = torque  # set le torque normalement en Nm. scale en 0 et 1
    start = time.time()
    end = time.time()
    count = 0
    while (end - start) <= 30:
        end = time.time()
        speed = carte.axis0.encoder.vel_estimate
        courant = carte.axis0.motor.current_control.Iq_setpoint
        if speed == 0.0:
            carte.axis0.controller.input_torque += 0.5
        elif speed != 0.0:
            carte.axis0.controller.input_torque = torque
        print("le torque est: ", carte.axis0.controller.input_torque)
        print("speed :", speed)

    carte.axis0.controller.input_torque = 0.0


def passif_mode(torque, carte: odrive):
    start = time.time()
    end = time.time()
    while (end - start) <= 30:
        end = time.time()
    new_time = time.time()
    new_end_time = time.time()
    carte.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL  # pour démarrer le moteur
    carte.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL  # set le mode torque
    carte.axis0.motor.config.torque_constant = 0.21
    carte.axis0.controller.input_torque = torque  # set le torque normalement en Nm. scale en 0 et 1
    while (new_end_time - new_time) <= 30:
        new_end_time = time.time()
        speed = carte.axis0.encoder.vel_estimate
        courant = carte.axis0.motor.current_control.Iq_setpoint
        puissance = torque * speed
        print("puissance en watt :", puissance)

    carte.axis0.controller.input_torque = 0.0


# courant = carte.axis0.motor.current_control.Iq_measured
# torque_fin = 8.27 * courant/150
# carte.axis0.controller.input_torque = 0.0
# if torque_fin != torque :
#     print("Test torque echec")
# else :
#     print("Test torque reussi")
# print("torque de fin:", torque_fin, ", torque attendu:", torque)

# Test
# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()
# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AxisState.IDLE:
    time.sleep(0.1)

passif_mode(-1, my_drive)
# moteur = Motor('tsdz2', 0.1 , 0.5, 0.1, 0.5 , 50, 35, -35, 1, my_drive)
# moteur._torque_user = 8
# moteur.concentric_mode()
# decommenter pour effectuer les tests
# test_vitesse(1, my_drive)
# test_torque (-1, my_drive)
# test_torque (0.5, my_drive)
# my_drive.axis0.requested_state = AxisState.IDLE
