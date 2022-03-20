# Stimulator class

# Imports
#from StimulationSignal import StimulationSignal
import crccheck.checksum
import numpy as np
import serial
import time

# channel_stim:   list of active channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)

# Notes:
# - Revoir les principes d'orienté objet (encapsulation)
# - Indentation : 4 espaces

class Stimulator:

    # Class variables
    VERSION = 0x01

    INIT_REPETITION_TIME = 0.5
    

    START_BYTE = 0xF0
    STOP_BYTE  = 0x0F
    STUFFING_BYTE = 0x81
    STUFFING_KEY = 0x55
    MAX_PACKET_BYTES = 69

    BAUD_RATE = 460800

    TYPES = {'Init': 0x01, 'InitAck': 0x02, 'UnknownCommand': 0x03, 'Watchdog': 0x04,
             'GetStimulationMode': 0x0A, 'GetStimulationModeAck': 0x0B,
             'InitChannelListMode': 0x1E, 'InitChannelListModeAck': 0x1F,
             'StartChannelListMode': 0x20, 'StartChannelListModeAck': 0x21,
             'StopChannelListMode': 0x22, 'StopChannelListModeAck': 0x23,
             'SinglePulse': 0x24, 'SinglePulseAck': 0x25, 'StimulationError': 0x26}
    

    # Constuctor
    def __init__(self, ts2, StimulationSignal, port_path): #Changer ts1 pour 1/StimulationSignal.frequency
    # ---- StimulationSignal = Contient les infos d'amplitude, de fréquence, de durée d'impulsion et le nom du muscle pour chaque électrode ---- #
    # ---- ts1 = Main stimulation interval                                 ---- #
    # ---- ts2 = Inter pulse interval (use only if use duplet or triplet)  ---- #
    # ---- Mode = Single pulse, duplet or triplet                          ---- #
    # ---- port = open port from port_path                                 ---- #
    # ---- packet_count = initialise the packet count                      ---- #
    
        self.StimulationSignal = StimulationSignal
        self.amplitude = StimulationSignal[0] #à vérifier si bon indice
        self.ts1 = 1/StimulationSignal[1] #à vérifier si bon indice pour fréquence
        self.pulse_width = StimulationSignal[2] #à vérifier si bon indice
        self.muscle = StimulationSignal[3]
        self.ts2 = ts2 
        self.port = serial.Serial(port_path, self.BAUD_RATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)
        self.packet_count = 0
        
        while True:
            received_packet= self.read_packets()
            self.init_ACK(received_packet)
            time.sleep(self.INIT_REPETITION_TIME)
        return 
    
    # Function to modify the stimulation's parameters
    def set_StimulationSignal(self,StimulationSignal):
        self.StimulationSignal = StimulationSignal
        self.amplitude = StimulationSignal[0] #à vérifier si bon indice
        self.ts1 = 1/StimulationSignal[1] #à vérifier si bon indice pour avoir fréquence
        self.pulse_width = StimulationSignal[2] #à vérifier si bon indice
        self.muscle = StimulationSignal[3]
        
    # Function to modify the time between pulses if doublet or triplet are chose
    def set_t2(self,t2):
        self.t2 = t2
    

    # "byte stuffing", i.e, xoring with STUFFING_KEY
    def stuff_byte(byte):
        return ((byte & ~Stimulator.STUFFING_KEY) | (~byte & Stimulator.STUFFING_KEY))

    # Construction of each packet
    def packet_construction(self,packet_count, packet_type, *packet_data):
        packet_command = self.TYPES[packet_type]
        packet_payload = [self.packet_count, packet_command]
        if packet_data!= None:
            for i in packet_data:
                packet_payload.append(i)
        checksum = self.stuff_byte(crccheck.crc.Crc8.calc(packet_payload))
        data_length = self.stuff_byte(len(packet_payload))
        packet_lead = [self.START_BYTE, self.STUFFING_BYTE, checksum, self.STUFFING_BYTE, data_length]
        packet_end = [self.STOP_BYTE]
        packet = packet_lead + packet_payload + packet_end
        return b''.join([byte.to_bytes(1, 'little') for byte in packet])


# Closes port
    def close_port(self):
        self.port.close()

# Send packets
    def send_packet(self, cmd):
        if cmd == 'InitACK':
            self.port.write(self.initACK(self.packet_count))
        elif cmd == 'Watchdog':
            self.port.write(self.watchdog(self.packet_count))
        elif cmd == 'GetStimulationMode':
            self.port.write(self.getMode(self.packet_count))
        elif cmd == 'InitChannelListMode':
            self.port.write(self.init_stimulation(self.packet_count, None, len(self.StimulationSignal.electrodes), None, self.ts2, self.ts1, 0)) #quoi faire avec channel_execution
        elif cmd == 'StartChannelListMode':
            self.port.write(self.start_stimulation(self.packet_count, self.mode, self.StimulationSignal.pulse_width, self.StimulationSignal.amplitude))
        elif cmd == 'StopChannelListMode':
            self.port.write(self.stop_stimulation(self.packet_count))
        # Update packet count
        self.packet_count = (self.packet_count + 1) % 256

# Receives packet
    # Read the received packet
    def read_packets(self):
        
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
            # Call the right ACK function
            if(str(packet[5]) == Stimulator.TYPES['Init']):
                return Stimulator.init()
            elif(str(packet[5]) == Stimulator.TYPES['UnknownCommand']):
                return Stimulator.unknown_cmd()
            elif(str(packet[5]) == Stimulator.TYPES['GetStimulationModeAck']):
                return Stimulator.getmodeACK(packet)
            elif(str(packet[5]) == Stimulator.TYPES['InitChannelListModeAck']):
                return Stimulator.init_stimulation_ACK(packet)
            elif(str(packet[5]) == Stimulator.TYPES['StartChannelListMode']):
                return Stimulator.start_stimulation_ACK(packet)
            elif(str(packet[5]) == Stimulator.TYPES['StopChannelListModeAck']):
                return Stimulator.stop_stimulation_ACK(packet)
            elif(str(packet[5]) == Stimulator.TYPES['StartChannelListModeAck']):
                return Stimulator.error_stimulation_ACK(packet)
        else:
            # Return empty string to avoid hanging
            return b''

# Creates packet for every command part of dictionary TYPES

    # Establishes connexion acknowlege
    def init(self, packet):
       return str(packet[6])

    # Establishes connexion acknowlege
    def init_ACK(self, packet):
        if (packet[6] == self.VERSION):
            result = '0'
            return self.packet_construction(self.packet_count, 'InitACK', result)
        else :
            return 'Version number is incompatible'


    # Sends message for unknown command
    def unknown_cmd(self, packet):
        return str(packet[6])


    # Error signal (inactivity ends connexion)  VERIFY IF IT HAVE TO BE SEND EVERY <1200MS OR SEND IF ONLY NOTHING SEND AFTER 120MS
    def watchdog(self, packet_count):
        packet = self.packet_construction(self.packet_count,'Watchdog')
        return packet


    # Asking to know which mode has been chosen
    def getMode(self, packet_count):
        packet = self.packet_construction(self.packet_count, 'GetStimulationMode')
        return packet


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
    def init_stimulation(self, packet_count, low_freq_factor): 
        max_frequency = max(self.StimulationSignal[1])
        max_frequency_electrode = np.where(self.StimulationSignal[1]==max_frequency)
        low_frequency_electrode = np.where(self.StimulationSignal[1]!=max_frequency)
        packet = self.packet_construction(self.packet_count,'InitChannelListMode', low_freq_factor, max_frequency_electrode, low_frequency_electrode, self.ts2, 1/max_frequency, None, 0 )
        return packet
        

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
    def start_stimulation(self,packet_count, mode): #VA PROBABLEMENT CHANGER PULSE_WIDTH ET AMPLITUDE SELON COMMENT RÉCUPÈRE DONNÉES
        if len(self.pulse_width) == 1:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode', 
                                              mode, self.pulse_width, None, self.amplitude)
        elif len(self.pulse_width) == 2:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0], 
                                              mode[1], self.pulse_width[1], None, self.amplitude[1])
        elif len(self.pulse_width) == 3:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2])
        elif len(self.pulse_width) == 4:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2],
                                              mode[3], self.pulse_width[3], None, self.amplitude[3])
        elif len(self.pulse_width) == 5:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2],
                                              mode[3], self.pulse_width[3], None, self.amplitude[3],
                                              mode[4], self.pulse_width[4], None, self.amplitude[4])
        elif len(self.pulse_width) == 6:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2],
                                              mode[3], self.pulse_width[3], None, self.amplitude[3],
                                              mode[4], self.pulse_width[4], None, self.amplitude[4],
                                              mode[5], self.pulse_width[5], None, self.amplitude[5])
        elif len(self.pulse_width) == 7:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2],
                                              mode[3], self.pulse_width[3], None, self.amplitude[3],
                                              mode[4], self.pulse_width[4], None, self.amplitude[4],
                                              mode[5], self.pulse_width[5], None, self.amplitude[5],
                                              mode[6], self.pulse_width[6], None, self.amplitude[6])
        elif len(self.pulse_width) == 8:
            packet = self.packet_construction(self.packet_count,'StartChannelListMode',
                                              mode[0], self.pulse_width[0], None, self.amplitude[0],
                                              mode[1], self.pulse_width[1], None, self.amplitude[1],
                                              mode[2], self.pulse_width[2], None, self.amplitude[2],
                                              mode[3], self.pulse_width[3], None, self.amplitude[3],
                                              mode[4], self.pulse_width[4], None, self.amplitude[4],
                                              mode[5], self.pulse_width[5], None, self.amplitude[5],
                                              mode[6], self.pulse_width[6], None, self.amplitude[6],
                                              mode[7], self.pulse_width[7], None, self.amplitude[7])
        
        return packet

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
    def stop_stimulation(self, packet_count):
        packet = self.packet_construction(self.packet_count,'StopChannelListMode')
        return packet


    # Sent by RehaStim2 in response to stop_stimulation
    def stop_stimulation_ACK(self, packet):

        if(str(packet[6]) == '0'):
            return ' Stimulation stopped'
        elif(str(packet[6]) == '-1'):
            return ' Transfer error'
        
        
    def stimulation_error(self, packet):
        
        if(str(packet[6]) == '-1'):
            return ' Emergency switch activated/not conencted' #mettre fonction qui affiche message sur interface
        elif(str(packet[6]) == '-2'):
            return ' Electrode error'
        elif(str(packet[6]) == '-3'):
            return 'Stimulation module error'
      
    
    def testing_stimulation(self): # lié avec +- courant
        self.ts1 = 3
        self.send_packet('InitChannelListMode')
        received_packet=self.read_packets()
        if (received_packet == 'Stimulation initialized'):
            self.send_packet('StartChannelListMode')
            received_packet = self.read_packets()
            if (received_packet == 'busy error'):
                while():
                    time.sleep(10)
                self.send_packet('StartChannelListMode')
            elif (received_packet == 'transfer error'):
                self.send_packet('StartChannelListMode')
            #elif (received_packet == 'Wrong mode error'):
                #self.mode ==
            #elif (received_packet == 'Parameter error'):
                
    def control_stimulation(self): #lié avec bouton start stim/update            
        self.send_packet('InitChannelListMode')
        received_packet=self.read_packets()
        if (received_packet == 'Stimulation initialized'):
            self.send_packet('StartChannelListMode')
            received_packet = self.read_packets()
            if (received_packet == 'busy error'):
                while():
                    time.sleep(10)
                self.send_packet('StartChannelListMode')
            elif (received_packet == 'transfer error'):
                self.send_packet('StartChannelListMode')
            #elif (received_packet == 'Wrong mode error'):
                #self.mode ==
            #elif (received_packet == 'Parameter error'):
                
    
      # Function to command the stimulator with pre-defined commands
    def throw_command(self, command):
        print("(Stimulator) TODO : call the '" + command + "' command")

        #if command type == hexadécimal of certain command, throw associated function.
        #fonction qui lit le paquet reçu par rehastim et qui l'associe à une commande.

        #command = {'Init':0x01}      
        
        
    '''
    if (InstructionWindow.clicked_started()): #changer pour ouverture 
            Stimulator.send_packet('Init')
            Stimulator.read_packets()
        if (Stimulator.read_packets() == 'Connexion established'):
            Stimulator.send_packet('InitChannelListMode')
            if(Stimulator.read_packets() == 'Stimulation initialized'):
                if()
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
