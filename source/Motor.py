# Motor class
from __future__ import print_function

import odrive
from odrive.enums import *

import time


class Motor:
    def __init__(self, nom, kp, ki, t, torque, speed, val_max, val_min, time_ent):  # , carte : odrive) :
        self._nom = nom
        self.carte = None
        self._kp = kp
        self._ki = ki
        self._torque = torque
        self._speed = speed
        self._dt = t
        self._val_max = val_max
        self._val_min = val_min
        self._is_concentric = True
        self._is_eccentric = False
        self._torque_user = 0
        self._duration = time_ent
        print("moteur construit")

    def __del__(self):
        print("moteur detruit")

    @staticmethod
    def calibrate_motor():
        # Find a connected ODrive (this will block until you connect one)
        print("finding an odrive...")
        my_drive = odrive.find_any()
        print("odrive found")

        # Calibrate motor and wait for it to finish
        print("starting calibration...")
        my_drive.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
        while my_drive.axis0.current_state != AxisState.IDLE:
            time.sleep(0.1)
        return my_drive

    def concentric_mode(self):
        self.carte.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL  # start engine
        self.carte.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL  # set mode to torque control
        self.carte.axis0.motor.config.torque_constant = 0.21
        self.carte.axis0.controller.input_torque = self._torque
        start = time.time()
        end = time.time()

        # PI
        # Modification de la condition du while
        # variation_torque_user = self.torque_cible - self._torque_user
        # threshold_acceptabilite = 0.1*self.torque_cible
        compte = 0
        # Asservissement
        start = time.time()
        end = time.time()
        while (end - start) <= self._duration:
            seconde = end - start
            end = time.time()
            # while abs(variation_torque_user) >= threshold_accceptabilite and self._is_concentric
            print("Dans la boucle du temps")
            while abs(erreur) >= 5 and self._is_concentric:
                end = time.time()
                seconde = end - start
                erreur = self._torque_user - self._torque
                P_o = self._kp * erreur
                integral = erreur * self._dt
                I_o = self._ki * integral
                controller = P_o + I_o
                if controller > self._val_max:
                    controller = self._val_max
                elif controller < self._val_min:
                    controller = self._val_min
                self._torque += controller
                compte += 1
                print("torque", compte)
                print(self._torque)
                # self.carte.axis0.controller.input_torque = self._force
                if (end - start) >= self._duration:
                    break
        print("mode concentrique")

    def eccentric_mode(self):
        # initialisation du projet
        self.carte.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
        while self.carte.axis0.current_state != AXIS_STATE_IDLE:
            time.sleep(0.1)
        self.carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL
        self.carte.axis0.motor.config.torque_constant = 8.23 / 150
        self.carte.axis0.controller.input_vel = self._speed
        self.carte.axis0.controller.input_torque = self._force

        # PI
        # Asservissement
        erreur_excentrique = self._force_user - self._force
        compte = 0
        while erreur_excentrique <= -5 and self._is_eccentric:
            erreur_excentrique = self._force_user - self._force
            P_o = self._kp * erreur_excentrique
            integral = erreur_excentrique * self._dt
            I_o = self._ki * integral
            controller = P_o + I_o
            if controller > self._val_max:
                controller = self._val_max
            elif controller < self._val_min:
                controller = self._val_min
            self._force += controller
            compte += 1
            print("torque", compte)
            print(self._force)
            # self.carte.axis0.controller.input_torque = self._force
        print("mode excentrique")

    def passif_mode(self):
        start = time.time()
        end = time.time()
        while (end - start) <= 30:
            end = time.time()
        new_time = time.time()
        new_end_time = time.time()
        self.carte.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL  # pour démarrer le moteur
        self.carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL  # set le mode torque
        self.carte.axis0.motor.config.torque_constant = 0.21
        self.carte.axis0.controller.input_torque = self._torque  # set le torque normalement en Nm. scale en 0 et 1
        while (new_end_time - new_time) <= 30:
            new_end_time = time.time()
            speed = self.carte.axis0.encoder.vel_estimate
            courant = self.carte.axis0.motor.current_control.Iq_setpoint
            puissance = self._torque * speed
            print("puissance en watt :", puissance)

        self.carte.axis0.controller.input_torque = 0.0

    def get_torque(self):
        return self._torque

    def set_torque(self, new_torque):
        self._torque = new_torque

# test
# moteur = Motor('tsdz2', 0.1 , 0.5, 0.1, 3 , 50, 35, -35, 30)
# type = moteur._nom
# print ("force user debut: " , moteur._torque_user)
# #print("le moteur  est de type", type)
# moteur._torque_user = 25
# #print ("force user apres: ", moteur._force_user)
# #print ("test")
# # erreur_test = moteur._force - moteur._force_user
# # print(erreur_test)
# moteur.concentric_mode()
# a = moteur._force_user
# moteur.get_force_user()
# b = moteur._force_user
# print(a)
# print(b)
# moteur.concentric_mode()
