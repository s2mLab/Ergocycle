# Stimulator class

# Imports
from StimulationSignal import StimulationSignal
import crccheck.checksum
import numpy as np
import serial #might need to do pip install serial

# channel_stim:   list of active channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)

port = serial.Serial(
    baudrate=460800,
    timeout=0.1, 
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS 
)
port.open()

class Stimulator:
        # Constuctor
        #command = {'Init':0x01}
        version_number = 0x01

        def __init__(self, channel_stim, freq, ts1, ts2, mode, pulse_width, amplitude, force):
            self.channel_stim = channel_stim
            self.freq = freq
            self.ts1 = ts1
            self.ts2 = ts2
            self.mode = mode
            self.pulse_width = pulse_width
            self.amplitude = amplitude
            self.force = force
            #self.baud_rate = 460800
            #self.start_byte = 0xF0
            #self.stop_byte = 0x0F
            #self.stuffing_byte = 0x81
            #self.stuffing_key = 0x55
            
        
        #print("TODO")
        '''
        def first_bytes(self):
            baud_rate = 460800
            start_byte = 0xF0
            stop_byte = 0x0F
            stuffing_byte = 0x81
            stuffing_key = 0x55
            packet = []
            
            packet.append(start_byte)
            packet.append(stuffing_byte)
            checksum = crccheck.crc. Crc8
            
         '''
    # Checksum of each packet
        def checksum(self, packet_data):
            checksum = crccheck.crc.Crc8.calc(packet_data)
            return checksum
    
    # Length of the data part in packet    
        def data_length(self, packet_data):
            data_length = len(packet_data)
            return data_length
        
    # Establishes connexion acknowlege
        def init(self, version_number):
           command = bytearray.fromhex(0x01)
           packet_number = np.zeros(255)
           for i in 255:
               packet_number.append(i)
           
           version_number = bytearray.fromhex(version_number)
           packet_data = []
           packet_data = [ packet_number, command, version_number]
           return packet_data
            
        # Establishes connexion acknowlege
        def init_ACK(self):
            packet = self.port.read
            if packet == bytearray.fromhex(0xF0):
                # Collect header bytes
                for i in range(4):
                    packet += self.port.read()
                # Collect data bytes
                datalength = Stimulator.data_length(packet_data) # vérifier je comprends pas trop comment ils ont fait
                for i in range(datalength):
                    packet += self.port.read()
                # Collect stop byte
                packet += self.port.read()
                # Return packet as byte string
            return packet
        
    
        # Sends message for unknown command
        def unknown_cmd():
            print("TODO")
        
            
        # Error signal (inactivity ends connexion)    
        def watchdog(self):
            command = bytearray.fromhex(0x04)
            packet_number = np.zeros(255)
            for i in 255:
               packet_number.append(i)
            packet_data = []
            packet_data = [packet_number, command]
            return packet_data
        
            
        # Returns chosen mode
        def get_mode():
            command = bytearray.fromhex(0X0A)
            packet_number = np.zeros(255)
            for i in 255:
               packet_number.append(i)
            packet_data = []
            packet_data = [packet_number, command]
            return packet_data
        
            
        # Sent by RehaStim2 in response to getMode
        def getModeACK():
            print("TODO")
        
    
        # Initialises stimulation
        def init_stimulation(channel_stim, ts1, ts2):
            print("TODO")
        
        
        # Sent by RehaStim2 in response to init_stimulation
        def init_stimulation_ACK():
            print("TODO")
        
            
        # Starts stimulation and modifies it
        def start_stimulation(mode, pulse_width, amplitude):
            print("TODO")
        
    
            
        # Sent by RehaStim2 in response to start_stimulation
        def start_stimulation_ACK():    
            print("TODO")
        
        
        # Stops stimulation
        def stop_stimulation():
            print("TODO")
        
            
        # Sent by RehaStim2 in response to stop_stimulation
        def stop_stimulation_ACK():
            print("TODO")
        
        
        # Sends a unique impulsion
        def single_pulse():
            print("TODO")
        
            
        # Sent by RehaStim2 in response to single_pulse
        def single_pulse_ACK():
            print("TODO")
        
        
        # Error message sent by RehaStim2 
        def error():
            print("TODO")
            
        #Emergency stop
        def emergency_stop(self, force):
            if force == 0:
                port.close()
                
            
            
  

#Essai
a = Stimulator.init()
print(a)
    