import nidaqmx
import keyboard
import time
import csv
import numpy as np
from datetime import datetime


class Crankset:
    def __init__(self, ergocycle_command_function):
        self.ergocycle_command_function = ergocycle_command_function
        self.vectforce = None
        self.now = datetime.now()

# -------------READ THE NI DQA CARD------------------------

#     --- Settings all the constant ---

    ### Matrice G for left and right pedal ###
    gL = np.array([[-34.38040, -15.98861, 14.85417, 38.92416, 21.79468, -16.54527],
                   [-12.14299, -15.97750, -56.00527, 11.64254, 21.73617, 49.64078],
                   [28.63924, -90.06860, 59.71884, -38.77426, 57.60297, -39.94618],
                   [-2.13145, -1.43975, -0.32197, 0.00206, 1.17651, 1.80420],
                   [-0.88409, -0.76118, 0.18369, 0.63824, -0.17685, 0.41540],
                   [3.28901, 4.22937, -4.23554, -3.80481, -0.39113, -0.63313]])

    gR = np.array([[39.69498, 20.12129, -19.50629, -34.57358, -11.88828, 17.41444],
                   [20.99047, 20.91399, 47.52230, -27.37309, -31.76135, -40.85873],
                   [66.49169, -62.31206, 41.18963, -66.01363, 48.99188, -26.64237],
                   [-0.92049, 1.86258, 1.42483, -1.22487, -1.45979, -0.35540],
                   [-0.02004, 0.18073, -0.12406, 0.24428, -0.16225, 0.34908],
                   [-3.06666, 1.57173, 0.75671, 4.43107, 4.05345, -3.09914]])

#     --- Read one value for each parameters ---

    def readcard(self):

        task1 = nidaqmx.Task()  # creation dune tache pour récupe
        
        # LEFT PEDALS CHANNELS
        # Force
        task1.ai_channels.add_ai_voltage_chan("TC01/ai0")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai1")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai2")
        # Torque
        task1.ai_channels.add_ai_voltage_chan("TC01/ai3")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai4")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai5")

        # RIGHT PEDAL CHANNELS
        # Force
        task1.ai_channels.add_ai_voltage_chan("TC01/ai8")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai10")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai13")
        # Torque
        task1.ai_channels.add_ai_voltage_chan("TC01/ai6")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai15")
        task1.ai_channels.add_ai_voltage_chan("TC01/ai7")

        
        
        # Start the task
        task1.start()
        
        # Get the values 
        val1 = task1.read()
        task1.stop()
        task1.close()

        return val1
    def readangle():

        task2 = nidaqmx.Task() # creation dune tache pour récuper l'angle
        
        # Angle
        task2.ai_channels.ai_pos_rvdt_chan("TC01/ai14")

        # Start the task
        task2.start()
        # Get the values
        val2 = task2.read()
        task2.stop()
        task2.close()

        return val2

#     --- Write in csv file ---


#     --- Find the Force and torque BY F=GU ---

    def multGU(self, mat, vec):
        F = np.matmul(mat, vec)
        return F

#     --- Where the magic happens ---
    def loop(self, Ts):
        pass

    def getAvgMoment(self):
        return -1 if self.vectforce == None else ((self.vectforce[6] + self.vectforce[12]) / 2)

