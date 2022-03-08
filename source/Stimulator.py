# Stimulator class

# Imports
#from StimulationSignal import StimulationSignal
import crccheck.checksum
import numpy as np
import serial

# channel_stim:   list of active channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)

  

class Stimulator:
    
        # Constuctor


       
      
  
        VERSION = 0x01

        INITACK_RESULT_OK = 0x00
        INITACK_RESULT_ERR = -0x05
          
        START_BYTE = 0xF0
        STOP_BYTE  = 0x0F
        STUFFING_BYTE = 0x81
        STUFFING_KEY = 0x55
        MAX_PACKET_BYTES = 69 
  
        # fonction pour appeler une commande (avec son numéro)
        # def throw_command(command):


        #if command type == hexadécimal of certain command, throw associated function.
        #fonction qui lit le paquet reçu par rehastim et qui l'associe à une commande.  

        #command = {'Init':0x01}
        version_number = 0x01


        #def __init__(self, channel_stim, freq, ts1, ts2, mode, pulse_width, amplitude):

        def __init__(self, channel_stim, freq, ts1, ts2, mode, pulse_width, amplitude, port_path):

            self.channel_stim = channel_stim
            self.freq = freq
            self.ts1 = ts1
            self.ts2 = ts2
            self.mode = mode
            self.pulse_width = pulse_width
            self.amplitude = amplitude
            # Save device path
            #self.port_path = port_path
            # Create serial port
            #self.port = serial.Serial(Stimulator.port_path)
            # Configure serial port
            #self.port.apply_settings(Stimulator.SETTINGS)
            # Initialize packet count
            #self.packet_count = 0
            
        TYPES = {'Init': 0x01, 'InitAck': 0x02, 'UnknownCommand': 0x03, 'Watchdog': 0x04,
                 'GetStimulationMode': 0x0A, 'GetStimulationModeAck': 0x0B,
                 'InitChannelListMode': 0x1E, 'InitChannelListModeAck': 0x1F,
                 'StartChannelListMode': 0x20, 'StartChannelListModeAck': 0x21,
                 'StopChannelListMode': 0x22, 'StopChannelListModeAck': 0x23,
                 'SinglePulse': 0x24, 'SinglePulseAck': 0x25, 'StimulationError': 0x26}
        '''
        SETTINGS = {
                'bytesize': serial.EIGHTBITS,
                'baudrate': 460800,
                'stopbits': serial.STOPBITS_ONE,
                'timeout': 0.1,
                'parity': serial.PARITY_EVEN
               }
        '''
        #Create serial port
        def init_port(self, port_path):
            
            port=serial.Serial(port_path, 460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)
            return port
        
        
        VERSION = 0x01
    
        INITACK_RESULT_OK = 0x00
        INITACK_RESULT_ERR = -0x05
              
        START_BYTE = 0xF0
        STOP_BYTE  = 0x0F
        STUFFING_BYTE = 0x81
        STUFFING_KEY = 0x55
        MAX_PACKET_BYTES = 69
        version_number = 0x01
  
        # fonction pour appeler une commande (avec son numéro)
        #def throw_command(command):


        #if command type == hexadécimal of certain command, throw associated function.
        #fonction qui lit le paquet reçu par rehastim et qui l'associe à une commande.  

        #command = {'Init':0x01}
            
        
        #print("TODO")
       
    # Checksum of each packet
        def checksum(self, packet_data):
            checksum = crccheck.crc.Crc8.calc(packet_data)
            return checksum
    
    # Length of the data part in packet    
        def data_length(self, packet_data):
            data_length = len(packet_data)
            return data_length
        
    # "byte stuffing", i.e, xoring with STUFFING_KEY
        def stuff_byte(byte):
            return ((byte & ~Stimulator.STUFFING_KEY) | (~byte & Stimulator.STUFFING_KEY)) 
      
   # Construction of each packet
        def packet_construction(self,packet_number, packet_type, packet_data):
            packet_command = self.TYPES[packet_type]
            packet_payload = [packet_number, packet_command] + packet_data 
            checksum = self.checksum(packet_payload)
            data_length = self.data_length(packet_payload)
            packet_lead = [self.START_BYTE, self.STUFFING_BYTE, checksum, self.STUFFING_BYTE, data_length]
            packet_end = [self.STOP_BYTE]
            return packet_lead + packet_payload + packet_end

            

    # Opens port

    # Closes port

    # Send packets

    # Receives packet

    # Creates packet for every command part of dictionary TYPES
   
  
        # Read the received packet
        def read_packets(self):
            #for type in Stimulator.TYPES:
               # if Stimulator.TYPES[type] == command:
                   # return type
             
            # Read port stream
            packet = self.port.read()
            # If it is a start byte, collect packet
            if packet == self.START_BYTE.to_bytes(1,byteorder='little'):
                # Collect header bytes
                for i in range(4):
                    packet += self.port.read()
                # Collect data bytes
                datalength = self.stuff_byte(packet[-1])
                for i in range(datalength):
                    packet += self.port.read()
                # Collect stop byte
                packet += self.port.read()
                # Return packet as byte string
                return packet
            else:
                # Return empty string to avoid hanging
                return b''
            
        # choose the right function for the received packet
        def function_call_received_packet(self,packet):
            if(str(packet[5]) == Stimulator.TYPES['InitACK']):
                return Stimulator.init_ACK()
            elif(str(packet[5]) == Stimulator.TYPES['UnknownCommand']):
                return Stimulator.unknown_cmd()
            elif(str(packet[5]) == Stimulator.TYPES['GetStimulationModeAck']):
                return Stimulator.getmodeACK()
            elif(str(packet[5]) == Stimulator.TYPES['InitChannelListModeAck']):
                return Stimulator.init_stimulation_ACK()
            elif(str(packet[5]) == Stimulator.TYPES['StartChannelListModeAck']):
                return Stimulator.start_stimulation_ACK()
            elif(str(packet[5]) == Stimulator.TYPES['StopChannelListModeAck']):
                return Stimulator.stop_stimulation_ACK()
            
            
        # Establishes connexion acknowlege
        def init(self, packet_number):
           packet = self.packet_construction(packet_number,'Init', self.VERSION )
           packet_byte = packet.to_bytes(1, 'little')
           return packet_byte   
            
        # Establishes connexion acknowlege
        def init_ACK(self, packet):
            if (str(packet[6]) == '0'):
                return 'Connexion established'
            elif (str(packet[6]) == '-5'):
                return 'Version number is incompatible'
                
    
        # Sends message for unknown command
        def unknown_cmd(self, packet):
            return str(packet[6])
        
            
        # Error signal (inactivity ends connexion)  VERIFY IF IT HAVE TO BE SEND EVERY <1200MS OR SEND IF ONLY NOTHING SEND AFTER 120MS   
        def watchdog(self, packet_number): 
            packet_payload = [packet_number, Stimulator.TYPES['Watchdog']]
            checksum = self.checksum(packet_payload)
            data_length = self.data_length(packet_payload)
            packet_lead = [self.START_BYTE, self.STUFFING_BYTE, checksum, self.STUFFING_BYTE, data_length]
            packet_end = [self.STOP_BYTE]
            packet = packet_lead + packet_payload + packet_end
            packet_byte = packet.to_bytes(1, 'little')
            return packet_byte
            
        
            
        # Asking to know which mode has been chosen
        def getMode(self, packet_number):
            packet_payload = [packet_number, Stimulator.TYPES['GetStimulationMode']]
            checksum = self.checksum(packet_payload)
            data_length = self.data_length(packet_payload)
            packet_lead = [self.START_BYTE, self.STUFFING_BYTE, checksum, self.STUFFING_BYTE, data_length]
            packet_end = [self.STOP_BYTE]
            packet = packet_lead + packet_payload + packet_end
            packet_byte = packet.to_bytes(1, 'little')
            return packet_byte
        
            
        # Sent by RehaStim2 in response to getMode
        def getModeACK(self, packet):
            
            if(str(packet[6] == '0')):
                if(str(packet[7]) == '0'):
                    return 'Start Mode'
                elif(str(packet[7]) == '1'):
                    return 'Stimulation initialized'
                elif(str(packet[7]) == '2'):
                    return 'Stimulation started'
            elif(str(packet[6]) == '-1'):
                return 'Transfer error'
            elif(str(packet[6]) == '-8'):
                return 'Busy error' #add a timer
    
        # Initialises stimulation
        def init_stimulation(channel_stim, ts1, ts2):
            print("TODO")
        
        
        # Sent by RehaStim2 in response to init_stimulation
        def init_stimulation_ACK(self, packet):
            
                if(str(packet[6]) == '0'):
                    return 'Stimulation initialized'
                elif(str(packet[6]) == '-1'):
                    return 'Transfer error'
                elif(str(packet[6]) == '-2'):
                    return 'Parameter error' #Change for please change parameters?
                elif(str(packet[6]) == '-3'):
                    return 'Wrong mode error'
                elif(str(packet[6]) == '-8'):
                    return 'Busy error' # Add a timer?
                
        # Starts stimulation and modifies it
        def start_stimulation(mode, pulse_width, amplitude):
            print("TODO")
            
        # Sent by RehaStim2 in response to start_stimulation
        def start_stimulation_ACK(self, packet):    
            
            if(str(packet[6]) == '0'):
                return ' Stimulation started'
            if(str(packet[6]) == '-1'):
                return ' Transfer error'
            if(str(packet[6]) == '-2'):
                return ' Parameter error'
            if(str(packet[6]) == '-3'):
                return ' Wrong mode error'
            if(str(packet[6]) == '-8'):
                return ' Busy error'
        
        
        # Stops stimulation
        def stop_stimulation():
            print("TODO")
        
            
        # Sent by RehaStim2 in response to stop_stimulation
        def stop_stimulation_ACK(self, packet):
    
            if(str(packet[6]) == '0'):
                return ' Stimulation stopped'
            if(str(packet[6]) == '-1'):
                return ' Transfer error'
        '''
        Vérifier si utile pour nous ou si décide de le faire pour plus tard
        
        # Sends a unique impulsion
        def single_pulse():
            print("TODO")
        
            
        # Sent by RehaStim2 in response to single_pulse
        def single_pulse_ACK():
            print("TODO")
        
        POSSIBLEMENT PAS UNE COMMANDE EN SOI
        
        # Error message sent by RehaStim2 
        def error():
            print("TODO")
            
        '''


    