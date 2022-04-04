import sys
import socket
import numpy as np
import serial
sys.path.append("c:/Users/izqui/Downloads/École/Automne_2021/ELE8080/Code/Ergocycle/source")
from Stimulator import Stimulator as Stimulator
from StimulationSignal import StimulationSignal as Stimulation_Signal



''' test= [240, 129, 121, 86, 3, 1, 1, 1, 15]
a = b' '.join([byte.to_bytes(1, 'little') for byte in test])

print (a) '''
''' signal_test = Stimulation_Signal(1, 6, 5, 360, 4, 1)
StimulationSignal_test = signal_test.set_stimulation_signal()

#port_path = serial.Serial('COM4', baudrate = 460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)

rehastim = Stimulator(3,StimulationSignal_test,"COM5") '''

test = np.array([[2, 0, 0, 0, 6, 0, 0, 8],[10, 0, 0, 0, 6, 0, 0, 10],[20, 0, 0, 0, 6, 0, 0, 3],[4, 0, 0, 0, 6, 0, 0, 2]])
idx = []
electrodes = []
test_2=0
for i in range(0,8):
    if test[0][i]==0:
        idx.append(i)
    else:
        test_2 += (2)**(i)
        
test = np.delete(test, idx, 1)          

#fonc_1=rehastim.init(1)

#test = rehastim.send_packet('InitAck',4)

#test=rehastim.start_stimulation(1, signal_test.pulse_width, signal_test.amplitude)

#print(rehastim.packet_construction())

#Stimulator(100,0,,COM2)