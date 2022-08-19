
import numpy as np
import nidaqmx
import keyboard
import time
import csv
from datetime import datetime
from tcpcom import TCPServer
from Crankset import Crankset


IP_PORT = 22000


class SendDataServer(Crankset):
    def __init__(self):
        super().__init__()
        self.server = None
    def sendAngle(self):
        valueangle= self.readangle()
        return valueangle


    def sendForce(self):
        valuef = self.readcard()
        # Find the Force/Torque data Left
        forceL = self.multGU(self.gL, valuef[0:6])
        forceR = self.multGU(self.gR, valuef[6:12])
        vectforce = np.append(forceL, forceR)
        return vectforce

    def onStateChanged(self, state, msg):
        if state == "LISTENING":
            print("Server:-- Listening...")
        elif state == "CONNECTED":
            print("Server:-- Connected to", msg)
        elif state == "MESSAGE":
            print("Server:-- Message received:", msg)
            if msg == "reveiveForce":
                self.server.sendMessage(self.sendForce())
            elif msg=="reveiveAngle":
                self.server.sendMessage(self.sendAngle())

    def startServer(self):
        self.server = TCPServer(IP_PORT, stateChanged=self.onStateChanged)




