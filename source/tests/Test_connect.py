import sys
import socket
import numpy as np
import serial
sys.path.append("c:/Users/Victorine/Documents/GitHub/Ergocycle/source")

from Stimulator import Stimulator as Stimulator
from StimulationSignal import StimulationSignal as Stimulation_Signal



''' test= [240, 129, 121, 86, 3, 1, 1, 1, 15]
a = b' '.join([byte.to_bytes(1, 'little') for byte in test])

print (a) '''
#signal_test = Stimulation_Signal(1, 6, 5, 360, 4, 1)
signal_test = np.array([[0,0,0,0,0,0,0,130],[0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,50],[0,0,0,0,0,0,0,2]])
#StimulationSignal_test = signal_test.set_stimulation_signal()

#port_path = serial.Serial('COM4', baudrate = 460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)

rehastim = Stimulator(3,signal_test,'COM6')



#fonc_1=rehastim.init(1)

#test = rehastim.send_packet('InitAck',4)

#test=rehastim.start_stimulation(1, signal_test.pulse_width, signal_test.amplitude)

#print(rehastim.packet_construction())

#Stimulator(100,0,,COM2)