# Stimulator class

# Imports
#from StimulationSignal import StimulationSignal
from cgi import print_arguments
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

# Generate an error
        self.ts1 = 1/StimulationSignal[1] #à vérifier si bon indice pour fréquence

        self.pulse_width = StimulationSignal[2] #à vérifier si bon indice
        self.muscle = StimulationSignal[3]
        self.ts2 = ts2
        self.port = serial.Serial(port_path, self.BAUD_RATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=0.1)
        self.packet_count = 0

        """
        while True:
            received_packet= self.read_packets()
            self.init_ACK(received_packet)
            time.sleep(self.INIT_REPETITION_TIME)
        return"""
        while (1):
            if (self.port.in_waiting>0):
                self.calling_ACK()
        
        
        
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
        self.packet_count = packet_count
        self.packet_type = packet_type
        packet_command = self.TYPES[packet_type]
        packet_payload = [packet_count, packet_command]    
        if packet_data!= None:
            packet_data = str(packet_data).strip("()")
            packet_data = list(packet_data.replace(",",""))
            for i in range (0, len(packet_data)):
                packet_payload.append(int(packet_data[i]))  
        print(packet_payload, "packet_payload")   
        checksum = crccheck.crc.Crc8.calc(packet_payload)
        print(checksum, "checksum")
        data_length = len(packet_payload)       
        packet_lead = [self.START_BYTE, self.STUFFING_BYTE, int(checksum), self.STUFFING_BYTE, data_length]
        packet_end = [self.STOP_BYTE]
        packet = packet_lead + packet_payload + packet_end
        return b''.join([byte.to_bytes(1, 'little') for byte in packet])


# Closes port
    def close_port(self):
        self.port.close()

# Send packets
    def send_packet(self, cmd, electrode_number, packet_number):
        if cmd == 'InitAck':
            self.port.write(self.init_ACK(packet_number))
        elif cmd == 'Watchdog':
            self.port.write(self.watchdog())
        elif cmd == 'GetStimulationMode':
            self.port.write(self.getMode())
        elif cmd == 'InitChannelListMode':
            self.port.write(self.init_stimulation(electrode_number)) #quoi faire avec channel_execution
        elif cmd == 'StartChannelListMode':
            self.port.write(self.start_stimulation( self.mode, electrode_number))
        elif cmd == 'StopChannelListMode':
            self.port.write(self.stop_stimulation())
        # Update packet count
        self.packet_count = (self.packet_count + 1) % 256

# Receives packet
    # Read the received packet
    def read_packets(self):

        # Read port stream
        packet = self.port.readline()
        print(packet, "Cequ'on reçoit")
        # If it is a start byte, collect packet
        if packet[0] == self.START_BYTE:
            # Collect header bytes
            ''' for i in range(4):
                packet += self.port.read()
            # Collect data bytes
            datalength = packet[-1]
            for i in range(datalength):
                packet += self.port.read()
            # Collect stop byte
            packet += self.port.read()
            # Call the right ACK function '''
            return packet
        else:
            # Return empty string to avoid hanging
            return b''

# Creates packet for every command part of dictionary TYPES
    def calling_ACK(self):
            #Call the Ack function
        packet = self.read_packets()
        if(int(packet[6]) == Stimulator.TYPES['Init'] and int(packet[7]) == self.VERSION):
            print(int(packet[2]))
            return Stimulator.send_packet(self, 'InitAck', 1, int(packet[5]))
        elif(str(packet[6]) == Stimulator.TYPES['UnknownCommand']):
            return Stimulator.unknown_cmd()
        elif(str(packet[6]) == Stimulator.TYPES['GetStimulationModeAck']):
            return Stimulator.getmodeACK(packet)
        elif(str(packet[6]) == Stimulator.TYPES['InitChannelListModeAck']):
            return Stimulator.init_stimulation_ACK(packet)
        elif(str(packet[6]) == Stimulator.TYPES['StartChannelListMode']):
            return Stimulator.start_stimulation_ACK(packet)
        elif(str(packet[6]) == Stimulator.TYPES['StopChannelListModeAck']):
            return Stimulator.stop_stimulation_ACK(packet)
        elif(str(packet[6]) == Stimulator.TYPES['StartChannelListModeAck']):
            return Stimulator.error_stimulation_ACK(packet)
    # Establishes connexion acknowlege
    def init(self, packet_count):
        packet = self.packet_construction(packet_count,'Init', self.VERSION )
        return packet

    # Establishes connexion acknowlege
    def init_ACK(self, packet_count):
        packet = self.packet_construction(packet_count, 'InitAck', 0)
        print (packet, "Ce qu'on renvoie")
        return packet



    # Sends message for unknown command
    def unknown_cmd(self, packet):
        return str(packet[6])


    # Error signal (inactivity ends connexion)  VERIFY IF IT HAVE TO BE SEND EVERY <1200MS OR SEND IF ONLY NOTHING SEND AFTER 120MS
    def watchdog(self):
        packet = self.packet_construction(self.packet_count,Stimulator.TYPES['Watchdog'])
        return packet


    # Asking to know which mode has been chosen
    def getMode(self):
        packet = self.packet_construction(self.packet_count, Stimulator.TYPES['GetStimulationMode'])
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
    def init_stimulation(self, electrode_number):
        #max_frequency = max(self.StimulationSignal[1])
       # max_frequency_electrode = np.where(self.StimulationSignal[1]==max_frequency)
       # low_frequency_electrode = np.where(self.StimulationSignal[1]!=max_frequency)
        packet = self.packet_construction(self.packet_count,Stimulator.TYPES['InitChannelListMode'], 0, electrode_number-1, 0, self.ts2, 1/self.frequency[electrode_number-1], None, 0 )
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
    def stop_stimulation(self):
        packet = self.packet_construction(self.packet_count,Stimulator.TYPES['StopChannelListMode'])
        return packet


    # Sent by RehaStim2 in response to stop_stimulation
    def stop_stimulation_ACK(self, packet):

        if(str(packet[6]) == '0'):
            return ' Stimulation stopped'
        elif(str(packet[6]) == '-1'):
            return ' Transfer error'


    def stimulation_error(self, packet):

        if(str(packet[6]) == '-1'):
            return ' Emergency switch activated/not connected' #mettre fonction qui affiche message sur interface
        elif(str(packet[6]) == '-2'):
            return ' Electrode error'
        elif(str(packet[6]) == '-3'):
            return 'Stimulation module error'


    def testing_stimulation(self, electrode_number): # lié avec +- courant
        self.ts1 = 3 #à vérifier
        self.send_packet('InitChannelListMode', electrode_number)
        received_packet=self.read_packets()
        if (received_packet == 'Stimulation initialized'):
            self.send_packet('StartChannelListMode', electrode_number)
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

    def control_stimulation(self, electrode_number): #lié avec bouton start stim/update ET position pédalier
        self.send_packet('InitChannelListMode', electrode_number)
        received_packet=self.read_packets()

        if (received_packet == 'Stimulation initialized'):
            self.send_packet('StartChannelListMode', electrode_number)
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
