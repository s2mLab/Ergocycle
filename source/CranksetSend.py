import nidaqmx
import keyboard
import time
import csv
import numpy as np
from datetime import datetime
from crankset import DataCrankset
 
class DataSendCrankset(DataCrankset):

  def __init__(self):
    super().__init__()
    
  def loop(self):
        
    k=0
    
    valuef=self.readcard()
    k= k+1

    #Find the Force/Torque data Left
    forceL = self.multGU(self.gL,valuef[0:6])
    forceR = self.multGU(self.gR, valuef[6:12])
    vectforce = np.append(forceL,forceR)    
    return vectforce   
    
        
