from pyparsing import null_debug_action
from tcpcom import TCPClient
import time
IP_ADDRESS = "192.168.0.17"
IP_PORT = 22000


class ReceiveDataClient():
    def __init__(self):
        self.message = None
        self.rc = None
        self.client = None

    def copymsg(self, msg):
        self.message = msg

    def onStateChanged(self, state, msg):
        global isConnected
        if state == "CONNECTING":
            print("Client:-- Waiting for connection...")
        elif state == "CONNECTED":
            print("Client:-- Connection estabished.")
        elif state == "DISCONNECTED":
            print("Client:-- Connection lost.")
            isConnected = False
        elif state == "MESSAGE":
            print("Client:-- Received data:", msg)
            self.copymsg(msg)


def startClient(self):
    self.client = TCPClient(IP_ADDRESS, IP_PORT,
                            stateChanged=self.onStateChanged)
    self.rc = self.client.connect()


def receiveForce(self):

    if self.rc:
        isConnected = True
        print("We send the command: reveiveForce")
        self.message = None
        self.client.sendMessage("reveiveForce")

    else:
        print("The connection has failed")

def receiveAngle(self):

    if self.rc:
        isConnected = True
        print("We send the command: reveiveAngle")
        self.message = None
        self.client.sendMessage("reveiveAngle")
        
    else:
        print("The connection has failed")
