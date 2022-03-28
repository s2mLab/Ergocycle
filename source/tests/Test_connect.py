import sys
import socket
import serial
sys.path.append("c:/Users/izqui/Downloads/École/Automne_2021/ELE8080/Code/Ergocycle/source")
from Stimulator import Stimulator as Stimulator
from StimulationSignal import StimulationSignal as Stimulation_Signal



''' test= [240, 129, 121, 129, 3, 1, 1, 1, 15]
a = " ".join([hex(byte) for byte in test])
print (a) '''
signal_test = Stimulation_Signal(4, 6, 5, 360, 4, 1)
StimulationSignal_test = signal_test.set_stimulation_signal()

#port_path = serial.Serial('COM4', baudrate = 460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)

rehastim = Stimulator(3,StimulationSignal_test,"COM6")

#fonc_1=rehastim.init(1)

test = rehastim.send_packet('InitAck',4)

#test=rehastim.start_stimulation(1, signal_test.pulse_width, signal_test.amplitude)

#print(rehastim.packet_construction())

#Stimulator(100,0,,COM2)