import nidaqmx
import keyboard
import time
import csv
import numpy as np
from datetime import datetime

class Crankset:
    def __init__(self, ergocycle_command_function)
        self.ergocycle_command_function = ergocycle_command_function
        self.vectforce = None

#-------------READ THE NI DQA CARD------------------------

#     --- Settings all the constant ---

        ### Matrice G for left and right pedal ###
    gL=np.array([[-34.38040, -15.98861, 14.85417, 38.92416, 21.79468, -16.54527],
            [-12.14299, -15.97750, -56.00527, 11.64254, 21.73617, 49.64078],
            [28.63924, -90.06860, 59.71884, -38.77426, 57.60297, -39.94618],
            [-2.13145, -1.43975, -0.32197, 0.00206, 1.17651, 1.80420],
            [-0.88409, -0.76118, 0.18369, 0.63824, -0.17685, 0.41540],
            [3.28901, 4.22937, -4.23554, -3.80481, -0.39113, -0.63313]])

    gR=np.array([[39.69498,20.12129,-19.50629,-34.57358,-11.88828,17.41444],
             [20.99047, 20.91399, 47.52230, -27.37309, -31.76135, -40.85873],
             [66.49169, -62.31206, 41.18963, -66.01363, 48.99188, -26.64237],
             [-0.92049, 1.86258, 1.42483, -1.22487, -1.45979, -0.35540],
             [-0.02004, 0.18073, -0.12406, 0.24428, -0.16225, 0.34908],
             [-3.06666, 1.57173, 0.75671, 4.43107, 4.05345, -3.09914]])

        ### Flag inital Value ###
    thick = 0

        ### To mark the time the csv file was created ###

    now = datetime.now()
#     --- Start and Stop the program ---

    def flagChanger(self):#Function to change the value of the flag
        global thick
        thick = 1

    keyboard.add_hotkey('s', flagChanger)


#     --- Read one value for each parameters ---
    def readcard(self):


        task = nidaqmx.Task() # creation dune tache

        #LEFT PEDALS CHANNELS
        #Force
        task.ai_channels.add_ai_voltage_chan("TC01/ai0")
        task.ai_channels.add_ai_voltage_chan("TC01/ai1")
        task.ai_channels.add_ai_voltage_chan("TC01/ai2")
        #Torque
        task.ai_channels.add_ai_voltage_chan("TC01/ai3")
        task.ai_channels.add_ai_voltage_chan("TC01/ai4")
        task.ai_channels.add_ai_voltage_chan("TC01/ai5")

        #RIGHT PEDAL CHANNELS
        #Force
        task.ai_channels.add_ai_voltage_chan("TC01/ai8")
        task.ai_channels.add_ai_voltage_chan("TC01/ai10")
        task.ai_channels.add_ai_voltage_chan("TC01/ai13")
        #Torque
        task.ai_channels.add_ai_voltage_chan("TC01/ai6")
        task.ai_channels.add_ai_voltage_chan("TC01/ai15")
        task.ai_channels.add_ai_voltage_chan("TC01/ai7")


        task.start()


        val=task.read()
        task.stop()
        task.close()

        return val

#     --- Write in csv file ---

    def writef(self,t,x):
        timestr=now.strftime("%m_%d_%Y, %H;%M;%S")
        file = open(timestr + " force.csv","a") # Open the csv file


        # time = str(t)
        value=np.append(t,x)

        #create the csv writter
        writer= csv.writer(file)

        #write a row to the csv file
        writer.writerow(map(lambda y: [y], value))

      # file.write(time+ "\t" + value)
        # file.write("\n")

        #Close the csv file
        file.close()

#     --- Find the Force and torque BY F=GU ---

    def multGU(self,mat,vec):
        F=np.matmul(mat,vec)
        return F

#     --- Where the magic happens ---
    def loop(self,Ts):
        pass

    def getAvgMoment(self):
	       return -1 if self.vectforce == None else ((self.vectforce[3] + self.vectforce[9]) / 2)
