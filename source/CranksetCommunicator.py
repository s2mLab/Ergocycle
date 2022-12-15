import numpy as np
from tcpcom import TCPServer
from Crankset import Crankset


IP_PORT = 22000


class SendDataServer(Crankset):
    def __init__(self):
        super().__init__()  # TODO: Complete the parameter needed
        self.server = None

    def send_angle(self):
        return self.read_angle()

    def send_force(self):
        force_value = self.read_card()
        # Find the Force/Torque data Left
        force_left = self.multiple_gu(self.gL, force_value[0:6])
        force_right = self.multiple_gu(self.gR, force_value[6:12])
        force_vector = np.append(force_left, force_right)
        return force_vector

    def on_state_changed(self, state, msg):
        if state == "LISTENING":
            print("Server:-- Listening...")
        elif state == "CONNECTED":
            print("Server:-- Connected to", msg)
        elif state == "MESSAGE":
            print("Server:-- Message received:", msg)
            if msg == "receiveForce":
                self.server.sendMessage(self.send_force())
            elif msg == "receiveAngle":
                self.server.sendMessage(self.send_angle())

    def start_server(self):
        self.server = TCPServer(IP_PORT, stateChanged=self.on_state_changed)
