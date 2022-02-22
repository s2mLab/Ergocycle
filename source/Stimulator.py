# Stimulator class

# Imports
from StimulationSignal import StimulationSignal
import crccheck.checksum
import numpy as np

# channel_stim:   list of active channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)

  

class Stimulator:
    
        # Constuctor
<<<<<<< HEAD
       
           TYPES = {'Init': 0x01, 'InitAck': 0x02, 'Unknown': 0x03, 'Watchdog': 0x04,
             'GetStimulationMode': 0x0A, 'GetStimulationModeAck': 0x0B,
             'InitChannelListMode': 0x1E, 'InitChannelListModeAck': 0x1F,
             'StartChannelListMode': 0x20, 'StartChannelListModeAck': 0x21,
             'StopChannelListMode': 0x22, 'StopChannelListModeAck': 0x23,
             'SinglePulse': 0x24, 'SinglePulseAck': 0x25, 'StimulationError': 0x26}
  
  
           VERSION = 0x01

              INITACK_RESULT_OK = 0x00
              INITACK_RESULT_ERR = -0x05
          
            START_BYTE = 0xF0
            STOP_BYTE  = 0x0F
            STUFFING_BYTE = 0x81
            STUFFING_KEY = 0x55
            MAX_PACKET_BYTES = 69 
  
        # fonction pour appeler une commande (avec son numéro)
        def throw_command(command):
            #if command type == hexadécimal of certain command, throw associated function.
            

=======
        #command = {'Init':0x01}
        version_number = 0x01
>>>>>>> 174e83765c2b5b7576b9d3842dc9b111eb84a904

        def __init__(self, channel_stim, freq, ts1, ts2, mode, pulse_width, amplitude):
            self.channel_stim = channel_stim
            self.freq = freq
            self.ts1 = ts1
            self.ts2 = ts2
            self.mode = mode
            self.pulse_width = pulse_width
            self.amplitude = amplitude
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
           packet_data = [command, packet_number, version_number]
           return packet_data
            
        # Establishes connexion acknowlege
        def init_ACK():
            print("TODO")
        
    
        # Sends message for unknown command
        def unknown_cmd():
            print("TODO")
        
            
        # Error signal (inactivity ends connexion)    
        def watchdog():
            print("TODO")
        
            
        # Returns chosen mode
        def getMode():
            print("TODO")
        
            
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
  

#Essai
a = Stimulator.init()
print(a)
    