# Main class

# Imports
from StimulationScreen import StimulationScreen as StimulationScreen
from MotorScreen import MotorScreen

from Parameters import Parameters
from TestParameters import TestParameters
from MotorParameters import MotorParameters
from Motor import Motor
from constants import *
from InterfacePyScienceMode2 import *

from pyScienceMode2 import Stimulator as St

import odrive
from odrive.enums import *

from PyQt5.QtWidgets import QApplication
import sys
import threading
import time


"""
Choices for the events:
- Multiple function in Ergocycle (more simple and more organised)
- One function and multiple commands in Ergocycle
"""


class Ergocycle:
    def __init__(self):

        self.paused_stimulation_signal = None
        self.final_time = None

        if not DEBUG_REHA:
            self.application = QApplication([])

            self.motor_parameters = MotorParameters()
            self.assistance_screen = MotorScreen(self.read_assistance_screen)
            self.assistance_screen.manage_active_window(self.motor_parameters)

            self.stim_parameters = Parameters()
            self.stim_test_parameters = TestParameters()
            self.stimulation_screen = StimulationScreen(self.read_stimulation_screen)
            self.stimulation_screen.manage_active_window(self.stim_parameters)

            self.thread_motor_control = threading.Thread(target=self.motor_control_function, args=(1,), daemon=True)
            # self.thread_sensors = threading.Thread(target=self.sensors_function, args=(1,), daemon=True)
            self.thread_stimulation = threading.Thread(target=self.stimulation_function, args=(1,), daemon=True)

        self.stimulation_signal = []
        self.stimulation_time = 0
        self.start_time = 0
        self.stimulator = St.Stimulator(list_channels=[], stimulation_interval=8, port_path=USB_DRIVE_PORT_PATH)

        self.stop_motor = False
        self.stop_sensors = False
        self.stop_stimulation = False
        self.stop_tests = False
        self.pause = True

        self.motor_on = True
        self.stimulation_started = False

        if not DEBUG_REHA:
            self.motor = Motor("tsdz2", 0, 0, 0, 0, 0, 0, 0, 0)
            self.thread_motor_control.start()
            self.start_application()

        # self.assistance_screen.start_application()
        # self.stimulation_screen.start_stimulation_application()

        if DEBUG_REHA:
            self.stimulation_function()

        # sys.exit(self.application.exec_())

    def motor_control_function(self):
        # logging.info("Thread %s: starting", name)
        print("Thread started")
        # carte = self.motor.calibrate_motor()
        # Find a connected ODrive (this will block until you connect one)
        print("finding an odrive...")
        my_drive = odrive.find_any()
        print("odrive found")

        # Calibrate motor and wait for it to finish
        print("starting calibration...")
        my_drive.axis0.requested_state = AxisState.FULL_CALIBRATION_SEQUENCE
        while my_drive.axis0.current_state != AxisState.IDLE:
            time.sleep(0.1)
        self.motor.carte = my_drive

        while not self.motor_on:
            print("Waiting for motor to start...")
            time.sleep(1)
        self.motor.carte.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL  # Start the engine
        # self.motor.carte.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL #set le mode torque
        self.motor.carte.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL  # set le mode speed
        #         self.motor.carte.axis0.motor.config.torque_constant = 0.21
        while not self.stop_motor:
            time.sleep(1)  # TODO: Change the moment at which motor control change +-

            # self.motor._torque = (-1)*(self.motor_parameters.get_target_power() / 10)
            self.motor.set_torque((-1) * self.motor_parameters.get_target_power())
            # self.motor.carte.axis0.controller.input_vel = self.motor._torque  # set torque (Nm) [0,1]
            self.motor.carte.axis0.controller.input_vel = self.motor.get_torque()
            print("(Ergocycle) Adjusting motor control...")

            if self.assistance_screen.window_counter == 1:  # Check if training time is reached
                if int(self.assistance_screen.current_menu.minute) >= self.motor_parameters.get_training_length():
                    pass
                    # self.times_up()
                    # self.final_time = self.assistance_screen.current_menu.current_time_label.text()
                    # self.assistance_screen.window_counter = 3
                    # self.assistance_screen.manage_active_window(self.motor_parameters)
                    # self.stop_motor = True
                    # self.stop_sensors = True
                    # self.stop_stimulation = True

        self.motor.carte.axis0.controller.input_vel = 0.0
        print("(Ergocycle) Stopped motor control thread")
        self.thread_motor_control.join()
        # self.assistance_screen.read_assistance_screen("stop_training")
        # logging.info("Thread %s: finishing", name)

    def stimulation_function(self):
        # logging.info("Thread %s: starting", name)
        array_history = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        if DEBUG_REHA_SHOW_COM:
            self.stimulator.show_log()
            # self.stimulator.show_com()
            # stimulator.show_watchdog()

        if DEBUG_REHA:
            self.stimulation_signal = [
                [10, 0, 10, 0, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10],
                [0, 1, 2, 3, 4, 5, 6, 7],
            ]
        else:
            while np.shape(self.stimulation_signal)[1] == 0:
                time.sleep(0.5)

        self.stimulator.init_channel(
            list_channels=matrix_to_list_channels(self.stimulation_signal),
            stimulation_interval=int(1000 / self.stimulation_signal[1][0]),
        )

        self.start_time = time.time()
        timer = 0
        fin_stimulation = 0
        parameter_stimulation_changed = False
        start_stimulation = False

        if DEBUG_REHA:
            # Set wanted stimulation (electrode 1 and 3 failing)
            self.stimulator.array = [
                [10, 0, 10, 0, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10],
                [0, 1, 2, 3, 4, 5, 6, 7],
            ]
            # Set stimulation time (min)
            self.stimulation_time = 10 / 60
            self.stop_stimulation = False
            self.stop_motor = False
            self.stop_tests = True

        while self.stop_stimulation is False and self.stop_motor is False:
            while timer < self.stimulation_time * 60 and self.stop_stimulation is False:  # and self.pause == True
                if DEBUG_REHA_SHOW_COM:
                    print("Time :", round(timer, 3))

                if not (np.allclose(self.stimulation_signal, array_history)):
                    array_history = self.stimulation_signal
                    parameter_stimulation_changed = True

                if not start_stimulation or parameter_stimulation_changed:
                    if parameter_stimulation_changed:
                        self.stimulator.init_channel(stimulation_interval=self.stimulation_signal[1][0])
                        parameter_stimulation_changed = False
                    self.stimulator.start_stimulation(
                        upd_list_channels=matrix_to_list_channels(self.stimulation_signal)
                    )
                    start_stimulation = True

                time.sleep(1)

                timer = time.time() - self.start_time
                fin_stimulation = 1

            if fin_stimulation == 1:
                print("Stimulation finished")
                self.stimulator.stop_stimulation()
                fin_stimulation = 0
                if DEBUG_REHA:
                    self.stop_stimulation = True

        self.stimulator.disconnect()
        print("(Ergocycle) Stopped stimulations thread")
        # self.thread_stimulation.join()
        # self.stimulation_screen.read_stimulation_screen("stop_stimulation")
        # logging.info("Thread %s: finishing", name)

    def read_assistance_screen(self, command):
        # if command == "command_amplitude":
        #     print("(Ergocycle) Commanding amplitude") # + str(self.assistance_screen.get_amplitude()))

        # elif command == "test_event":
        #     print("(Ergocycle) TESTING EVENT")

        if command == "start_training":
            # self.thread_motor_control.start()
            # self.thread_sensors.start()

            self.motor_on = True

            self.assistance_screen.next_window()
            self.assistance_screen.current_menu.submit_clicked(self.motor_parameters)

            print("(Ergocycle) Beginning training...")
            print("Initial parameters :")
            print(f"Mode : {self.motor_parameters.get_training_type()}")
            print(f"Target power : {self.motor_parameters.get_target_power()} W")
            print(f"Training length : {self.motor_parameters.get_training_length()} min")

            self.assistance_screen.manage_active_window(self.motor_parameters)

            # TODO: Warn the stimulation UI that training must start
            # self.stimulation_screen.flag_ready = True

            # TODO: Activate motor and start training

            # TODO: Start data acquisition

        elif command == "increase_target_power":
            self.motor_parameters.increase_target_power()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Target power increased")

            # TODO: Increase speed/torque

        elif command == "decrease_target_power":
            self.motor_parameters.decrease_target_power()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Target power decreased")

            # TODO: Decrease speed/torque

        elif command == "increase_training_length":
            self.motor_parameters.increase_training_length()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Training length increased")

        elif command == "decrease_training_length":
            self.motor_parameters.decrease_training_length()
            self.assistance_screen.current_menu.update_labels(self.motor_parameters)
            print("(Ergocycle) Training length decreased")

        elif command == "stop_training":
            self.final_time = self.assistance_screen.current_menu.current_time_label.text()

            self.assistance_screen.next_window()
            self.assistance_screen.manage_active_window(self.motor_parameters)
            # self.assistance_screen.current_menu.stop_clicked()
            print("(Ergocycle) Waiting for confirmation to stop...")

        elif command == "continue_training":
            print("(Ergocycle) Continuing training...")

        elif command == "confirmed_stop_training":
            print("(Ergocycle) Stopping training...")
            self.assistance_screen.current_menu.total_length.setText(self.final_time)
            # TODO: Stop motor and stop training
            self.stop_motor = True
            self.motor_on = False

            self.thread_motor_control.join()
            # TODO: Stop data acquisition
            self.stop_sensors = True

            # TODO: Save data in a file

            # TODO: Calculate and display in SummaryMenu average, minimum and maximum power

            self.read_stimulation_screen("stop_stimulation")

        else:
            print("(Ergocycle) Command " + command + " not found")

    def read_stimulation_screen(self, command):
        # if command == "USER CLICKING":
        #     print("(Ergocycle) Commanding a test ") # + str(self.stimulation_screen.get_something()))

        if command == "start_test":
            self.stimulation_screen.window_counter = -1
            self.stimulation_screen.current_menu.get_test_parameters(self.stim_test_parameters)
            self.stimulation_screen.manage_active_window(self.stim_test_parameters)
            print(
                "Ergocycle commanding to get initial test parameters"
            )  # +str(self.stimulation_screen.get_initial_test_parameters)
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"Initial test parameters : {self.stimulation_signal}")
            self.stop_tests = True

        elif command == "increase_amp":
            self.stimulation_screen.current_menu.increase_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")

            if not self.stimulation_started:
                self.thread_stimulation.start()
                self.stimulation_started = True
            self.start_time = time.time()

        elif command == "increase_frequency":
            self.stimulation_screen.current_menu.increase_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test frequency : {self.stim_test_parameters.frequency}")

        elif command == "increase_imp":
            self.stimulation_screen.current_menu.increase_imp(self.stim_test_parameters)
            print("(Ergocycle) Test impulsion increased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test imp : {self.stim_test_parameters.imp}")

        elif command == "decrease_amp":
            self.stimulation_screen.current_menu.decrease_amplitude(self.stim_test_parameters)
            print("(Ergocycle) Test amplitude decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test amplitude : {self.stim_test_parameters.amplitude}")

        elif command == "decrease_frequency":
            self.stimulation_screen.current_menu.decrease_frequency(self.stim_test_parameters)
            print("(Ergocycle) Test frequency decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test frequency : {self.stim_test_parameters.frequency}")

        elif command == "decrease_imp":
            self.stimulation_screen.current_menu.decrease_imp(self.stim_test_parameters)
            print("(Ergocycle) Test impulsion decreased")
            self.stimulation_signal = self.stim_test_parameters.get_test_parameters(
                self.stim_test_parameters.amplitude,
                self.stim_test_parameters.frequency,
                self.stim_test_parameters.imp,
                self.stim_test_parameters.muscle,
            )
            print(f"UPDATED test parameters : {self.stimulation_signal}")
            # print(f"Updated test parameters : {self.stim_test_parameters.imp}")

        elif command == "back_button_clicked":
            # self.thread_stimulation.pause()

            self.stimulation_screen.current_menu.close()
            self.stimulation_screen.next_window()
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            print("(Ergocycle) Done testing")
            self.stimulation_signal = self.stim_test_parameters.set_to_off()
            print(f"Initial test parameters : {self.stimulation_signal}")
            self.stimulator.stop_stimulation()
            self.stop_tests = False

        # elif command == "updated_test_parameters":
        #     print("Ergocycle commanding to get updated test parameters")
        # +str(self.stimulation_screen.get_updated_test_parameters)

        elif command == "start_training":

            self.stimulation_screen.next_window()
            self.stimulation_screen.current_menu.get_test_parameters(self.stim_parameters)
            self.stimulation_screen.manage_active_window(self.stim_parameters)
            print(
                "Ergocycle commanding to go to main menu of stimulations"
            )  # +str(self.stimulation_screen.get_initial_training_parameters)

        # elif command == "updated_training_parameters":
        # print("Ergocycle commanding to get updated training parameters")#+
        #   str(self.stimulation_screen.get_updated_training_parameters)

        elif command == "submit_button_clicked":
            self.stimulation_screen.current_menu.clicked_more(self.stim_parameters)
            print("(Ergocycle) Submit button clicked. Muscles have been chosen by user.")

        elif command == "submit_final_button_clicked":
            self.stimulation_screen.current_menu.clicked_next(self.stim_parameters)
            print("(Ergocycle) Final submit button clicked")
            if self.stimulation_screen.current_menu.is_completed(self.stim_parameters):
                # 4.5.1 Check danger and call right menu(DangerPopUp ou InstructionWindow)
                if self.stimulation_screen.current_menu.danger_check(self.stim_parameters):
                    self.stimulation_screen.window_counter = -2
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    print("(Ergocycle) Verify unsafe parameters")
                else:
                    if self.stimulation_screen.window_counter == -2:
                        self.stimulation_screen.next_window_special()
                    else:
                        self.stimulation_screen.next_window()
                    self.stimulation_screen.manage_active_window(self.stim_parameters)
                    # print("(Ergocycle) Starting stimulation...")
                    self.read_stimulation_screen("show_instructions")

        elif command == "back_to_menu":
            print("(Ergocycle) Waiting for change of parameters...")

        elif command == "continue_to_instructions":
            print("(Ergocycle) Continuing with unsafe parameters...")
            self.read_stimulation_screen("show_instructions")

        elif command == "show_instructions":  # TODO: Needs to be modified
            print("(Ergocycle) Instructions...")

        elif command == "start_stimulation":
            # self.thread_stimulation.start()
            # self.stimulation_screen.current_menu.clicked_start(self.stim_parameters)
            if self.motor_on:
                self.stimulation_screen.current_menu.get_initial_parameters(self.stim_parameters)
                self.stimulation_screen.current_menu.get_training_time(self.stim_parameters)
                self.stimulation_signal = self.stimulation_screen.current_menu.get_initial_parameters(
                    self.stim_parameters
                )
                self.stimulation_time = self.stimulation_screen.current_menu.get_training_time(self.stim_parameters)
                self.stimulation_screen.create_csv_file(self.stimulation_signal)
                self.stimulation_screen.next_window()
                self.stimulation_screen.manage_active_window(self.stim_parameters)
                print("(Ergocycle) Starting stimulation...")
                print(f"Initial training parameters : {self.stimulation_signal}")
                print(f"Training time : {self.stimulation_time}")

                if not self.stimulation_started:
                    self.thread_stimulation.start()
                    self.stimulation_started = True
                self.start_time = time.time()

            else:
                # self.stimulation_screen.current_menu.start_button.setEnabled(False)
                # time.sleep(0.1)
                # self.stimulation_screen.current_menu.start_button.setEnabled(True)
                print("Mettez en marche le moteur")
            # self.thread_stimulation.start()

        elif command == "increase_amplitude1":
            self.stimulation_screen.current_menu.increase_amplitude1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude2":
            self.stimulation_screen.current_menu.increase_amplitude2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude3":
            self.stimulation_screen.current_menu.increase_amplitude3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude4":
            self.stimulation_screen.current_menu.increase_amplitude4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude5":
            self.stimulation_screen.current_menu.increase_amplitude5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude6":
            self.stimulation_screen.current_menu.increase_amplitude6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 6 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude7":
            self.stimulation_screen.current_menu.increase_amplitude7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_amplitude8":
            self.stimulation_screen.current_menu.increase_amplitude8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude1":
            self.stimulation_screen.current_menu.decrease_amplitude1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude2":
            self.stimulation_screen.current_menu.decrease_amplitude2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude3":
            self.stimulation_screen.current_menu.decrease_amplitude3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude4":
            self.stimulation_screen.current_menu.decrease_amplitude4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude5":
            self.stimulation_screen.current_menu.decrease_amplitude5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude6":
            self.stimulation_screen.current_menu.decrease_amplitude6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude7":
            self.stimulation_screen.current_menu.decrease_amplitude7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_amplitude8":
            self.stimulation_screen.current_menu.decrease_amplitude8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Amplitude 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency1":
            self.stimulation_screen.current_menu.increase_frequency1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency2":
            self.stimulation_screen.current_menu.increase_frequency2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency3":
            self.stimulation_screen.current_menu.increase_frequency3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency4":
            self.stimulation_screen.current_menu.increase_frequency4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency5":
            self.stimulation_screen.current_menu.increase_frequency5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency6":
            self.stimulation_screen.current_menu.increase_frequency6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 6 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency7":
            self.stimulation_screen.current_menu.increase_frequency7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_frequency8":
            self.stimulation_screen.current_menu.increase_frequency8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency1":
            self.stimulation_screen.current_menu.decrease_frequency1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")
        elif command == "decrease_frequency2":
            self.stimulation_screen.current_menu.decrease_frequency2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency3":
            self.stimulation_screen.current_menu.decrease_frequency3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency4":
            self.stimulation_screen.current_menu.decrease_frequency4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency5":
            self.stimulation_screen.current_menu.decrease_frequency5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency6":
            self.stimulation_screen.current_menu.decrease_frequency6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency7":
            self.stimulation_screen.current_menu.decrease_frequency7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_frequency8":
            self.stimulation_screen.current_menu.decrease_frequency8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Frequency 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp1":
            self.stimulation_screen.current_menu.increase_imp1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 1 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp2":
            self.stimulation_screen.current_menu.increase_imp2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 2 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp3":
            self.stimulation_screen.current_menu.increase_imp3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 3 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp4":
            self.stimulation_screen.current_menu.increase_imp4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 4 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp5":
            self.stimulation_screen.current_menu.increase_imp5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 5 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp6":
            self.stimulation_screen.current_menu.increase_imp6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 6 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp7":
            self.stimulation_screen.current_menu.increase_imp7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 7 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "increase_imp8":
            self.stimulation_screen.current_menu.increase_imp8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 8 increased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp1":
            self.stimulation_screen.current_menu.decrease_imp1(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 1 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp2":
            self.stimulation_screen.current_menu.decrease_imp2(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 2 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp3":
            self.stimulation_screen.current_menu.decrease_imp3(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 3 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp4":
            self.stimulation_screen.current_menu.decrease_imp4(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 4 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp5":
            self.stimulation_screen.current_menu.decrease_imp5(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 5 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp6":
            self.stimulation_screen.current_menu.decrease_imp6(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 6 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp7":
            self.stimulation_screen.current_menu.decrease_imp7(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 7 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "decrease_imp8":
            self.stimulation_screen.current_menu.decrease_imp8(self.stim_parameters)
            self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_signal = self.stimulation_screen.current_menu.get_updated_parameters(self.stim_parameters)
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print("(Ergocycle) Impulsion 8 decreased")
            print(f"UPDATED training parameters : {self.stimulation_signal}")

        elif command == "pause_stimulation":
            self.stimulation_screen.current_menu.pause(self.stim_parameters)
            print("(Ergocycle) Stimulation paused/restarted...")
            if self.stimulation_signal != []:
                print("(Ergocycle) Stimulation paused")
                self.paused_stimulation_signal = self.stimulation_signal
                self.stimulation_signal = []
                self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
                print(f"PAUSED parameters: {self.stimulation_signal}")
                self.pause = False
            else:
                print("(Ergocycle) Stimulation restarted")
                self.stimulation_signal = self.paused_stimulation_signal
                self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
                print(f"RESTARTED parameters: {self.stimulation_signal}")
                self.pause = True

        elif command == "stop_stimulation":
            # self.stimulation_screen.current_menu.clicked_stop()
            self.stimulation_screen.current_menu.close()  # .next_window()
            # self.stimulation_screen.manage_active_window(self.stim_parameters)
            self.stimulation_signal = []
            self.stimulation_screen.save_data_in_csv_file(self.stimulation_signal)
            print(f"(Ergocycle): Stopping stimulation : {self.stimulation_signal}")
            self.stop_stimulation = True
            time.sleep(1)
            if self.stimulation_started:
                self.thread_stimulation.join()

        else:
            print("(Ergocycle) Command " + command + " not found")

        # print("TODO: Read stimulation screen")

    # def command_stimulator(self):#(self, command)
    # self.stimulator.throw_command("Set frequency to " + self.assistance_screen.get_amplitude() + " volts")

    @staticmethod
    def test_timer():
        print("TEST TIMER")
        # threading.Timer(1, test_timer).start()

    def start_application(self):
        sys.exit(self.application.exec_())
