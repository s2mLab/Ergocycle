import nidaqmx
import keyboard
import time
import csv
import numpy as np
from datetime import datetime
from crankset import DataCrankset

class CranksetRecorder(DataCrankset):

    def __init__(self, ergocycle_command_function):
        super().__init__(ergocycle_command_function)

    def loop(self,Ts):
        #Ts is the sampling time
        k=0
        while True:
            valuef=readcard()
            k= k+1


            #Find the Force/Torque data Left
            forceL = multGU(gL,valuef[0:6])
            forceR = multGU(gR, valuef[6:12])
            self.vectforce = np.append(forceL,forceR)
            self.ergocycle_command_function(1, self.getAvgMoment())
            writef(k*Ts,vectforce)
            print("valeurk",vectforce[0],k)

            #To stop the while
            if thick == 1:
                print("You stop the acquisition")
                break

            time.sleep(Ts)
