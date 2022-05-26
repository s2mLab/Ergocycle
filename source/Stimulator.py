# Stimulator class

# Imports
import crccheck.checksum
import numpy as np
import serial
import time
from colorama import Fore
from constants import *


# channel_stim:   list of active' channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)

# Notes:
# - Revoir les principes d'orienté objet (encapsulation)
# - Indentation : 4 espaces
# TODO: utiliser les channels
# TODO: Faire en sorte qu'à chaque command on check si l'on est toujours connecté, si l'on est plus connecté.
#  On part du principe que le code sera bien utilisé donc tant qu'on est pas rentré dans stop stimulation,
#  on est connecté au rehastim.


class Stimulator:
    # Class variables
    VERSION = 0x01

    START_BYTE = 0xF0
    STOP_BYTE = 0x0F
    STUFFING_BYTE = 0x81
    STUFFING_KEY = 0x55
    MAX_PACKET_BYTES = 69

    BAUD_RATE = 460800

    TYPES = {'Init': 0x01, 'InitAck': 0x02, 'UnknownCommand': 0x03, 'Watchdog': 0x04,
             'GetStimulationMode': 0x0A, 'GetStimulationModeAck': 0x0B,
             'InitChannelListMode': 0x1E, 'InitChannelListModeAck': 0x1F,
             'StartChannelListMode': 0x20, 'StartChannelListModeAck': 0x21,
             'StopChannelListMode': 0x22, 'StopChannelListModeAck': 0x23,
             'SinglePulse': 0x24, 'SinglePulseAck': 0x25, 'StimulationError': 0x26,
             0x01: 'Init', 0x02: 'InitAck', 0x03: 'UnknownCommand', 0x04: 'Watchdog',
             0x0A: 'GetStimulationMode', 0x0B: 'GetStimulationModeAck',
             0x1E: 'InitChannelListMode', 0x1F: 'InitChannelListModeAck',
             0x20: 'StartChannelListMode', 0x21: 'StartChannelListModeAck',
             0x22: 'StopChannelListMode', 0x23: 'StopChannelListModeAck',
             0x24: 'SinglePulse', 0x25: 'SinglePulseAck', 0x26: 'StimulationError'}

    RECEIVE = 0
    SEND = 1
    ERR = 2

    # Constructor
    def __init__(self, StimulationSignal, port_path):  # TODO: Changer ts1 pour 1/StimulationSignal.frequency
        # ---- StimulationSignal = Amplitude, fréquence, durée d'impulsion, le nom du muscle ---- #
        # ---- ts1 = Main stimulation interval                                 ---- #
        # ---- ts2 = Inter pulse interval (use only if use duplet or triplet)  ---- #
        # ---- Mode = Single pulse, duplet or triplet                          ---- #
        # ---- port = open port from port_path                                 ---- #
        # ---- packet_count = initialise the packet count                      ---- #

        self.matrice = StimulationSignal
        self.port = serial.Serial(port_path, self.BAUD_RATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_ONE, timeout=0.1)
        self.packet_count = 0
        self.packet_send_history = []
        self.amplitude = []
        self.ts1 = []
        self.frequency = []
        self.pulse_width = []
        self.muscle = []
        self.electrode_number = 0
        self.idx = []
        self.StimulationSignal = []
        self.reha_connected = 0
        self.time_last_cmd = 0

    def initialise_connection(self):
        while 1:
            if self.port.in_waiting > 0:
                return self.calling_ACK()

    def init_channel(self):
        self.set_stim_param()
        self.set_StimulationSignal(self.StimulationSignal)
        self.send_packet('InitChannelListMode', self.packet_count)
        init_channel_list_mode_ack = self.initialise_connection()
        print(init_channel_list_mode_ack)
        if init_channel_list_mode_ack != 'Stimulation initialized':
            print("Error : InitChannelListMode")  # TODO : ajouter une routine de gestion d'erreur

    def start_channel(self):
        self.send_packet('StartChannelListMode', self.packet_count)
        start_channel_list_mode_ack = self.initialise_connection()
        if start_channel_list_mode_ack != ' Stimulation started':
            print(Fore.LIGHTRED_EX + "Error StartChannelListMode, ack received: %s" % start_channel_list_mode_ack,
                  Fore.WHITE)  # TODO : ajouter une routine de gestion d'erreur

    def set_matrice(self, signals_matrice):
        self.matrice = signals_matrice

    # Function to modify the stimulation's parameters
    def set_StimulationSignal(self, StimulationSignal):
        self.amplitude = []
        self.ts1 = []
        self.frequency = []
        self.pulse_width = []
        self.muscle = []
        for i in range(8 - len(self.idx)):
            self.amplitude.append(StimulationSignal[0][i])
            self.ts1.append(int(1000 / StimulationSignal[1][i] - 1) / 0.5)  # à vérifier si bon indice pour fréquence
            self.frequency.append(StimulationSignal[1][i])
            self.pulse_width.append(StimulationSignal[2][i])  # à vérifier si bon indice
            self.muscle.append(StimulationSignal[3][i])

    def set_stim_param(self):
        self.idx = []
        self.electrode_number = 0
        stim_matrice = np.copy(self.matrice)
        for j in range(np.shape(self.matrice)[1]):
            if self.matrice[3][j] == 2 or self.matrice[3][j] == 4:
                stim_matrice[:, j] = 0

        for i in range(0, 8):
            if stim_matrice[0][i] == 0:
                self.idx.append(i)
            else:
                self.electrode_number += 2 ** i
        stim_matrice = np.delete(stim_matrice, self.idx, 1)
        self.StimulationSignal = stim_matrice

    # "byte stuffing", i.e, xoring with STUFFING_KEY
    @staticmethod
    def stuff_byte(byte):
        return (byte & ~Stimulator.STUFFING_KEY) | (~byte & Stimulator.STUFFING_KEY)
        # return bytes(a ^ b for (a, b) in zip(byte, bitarray(self.STUFFING_KEY)))

    # Construction of each packet
    def packet_construction(self, packet_count, packet_type, *packet_data):
        start_byte = self.START_BYTE
        stop_byte = self.STOP_BYTE
        packet_command = self.TYPES[packet_type]
        packet_payload = [packet_count, packet_command]
        packet_payload = self.stuff_packet_byte(packet_payload)
        if packet_data is not None:
            packet_data = list(packet_data)
            packet_data = self.stuff_packet_byte(packet_data)
            packet_payload += packet_data

        checksum = crccheck.crc.Crc8.calc(packet_payload)
        checksum = self.stuff_byte(checksum)
        data_length = self.stuff_byte(len(packet_payload))

        packet_lead = [start_byte, self.STUFFING_BYTE, checksum, self.STUFFING_BYTE, data_length]
        packet_end = [stop_byte]
        packet = packet_lead + packet_payload + packet_end

        return b''.join([byte.to_bytes(1, 'little') for byte in packet])

    def stuff_packet_byte(self, packet):
        # Stuff the byte equal to 0xf0 (240), 0x0f (15), 0x81(129), 0x55 (85) and 0x0a(10)
        # for more details check : Science_Mode2_Description_Protocol_20121212.pdf, 2.2 PacketStructure
        for i in range(0, len(packet)):
            if packet[i] == 240 or packet[i] == 15 or packet[i] == 129 or packet[i] == 85 or packet[i] == 10:
                packet[i] = self.stuff_byte(packet[i])
        return packet

    # Closes port
    def close_port(self):
        self.port.close()

    # Send packets
    def send_packet(self, cmd, packet_number):
        packet = [-1]
        if cmd == 'InitAck':
            packet = self.init_ACK(packet_number)
            self.port.write(packet)
        elif cmd == 'Watchdog':
            packet = self.watchdog()
            self.port.write(packet)
        elif cmd == 'GetStimulationMode':
            packet = self.getMode()
            self.port.write(packet)
        elif cmd == 'InitChannelListMode':
            packet = self.init_stimulation()
            self.port.write(packet)  # quoi faire avec channel_execution
        elif cmd == 'StartChannelListMode':
            packet = self.start_stimulation()
            self.port.write(packet)
        elif cmd == 'StopChannelListMode':
            packet = self.stop_stimulation()
            self.port.write(packet)

        if DEBUG_REHA_SHOW_COM == 1:
            self.packet_show(packet, self.SEND)

        self.time_last_cmd = time.time()
        self.packet_send_history = packet
        self.packet_count = (self.packet_count + 1) % 256

        if cmd == 'InitAck':
            return 'InitAck'

    # Receives packet
    # Read the received packet
    def read_packets(self):
        # Read port stream
        packet = self.port.readline()
        if DEBUG_REHA_SHOW_COM == 1:
            self.packet_show(packet, self.RECEIVE)
        # If it is a start byte, collect packet
        if packet[0] == self.START_BYTE:
            return packet
        else:
            # Return empty string to avoid hanging
            return b''

    # Creates packet for every command part of dictionary TYPES
    def calling_ACK(self):
        # Call the Ack function
        packet = self.read_packets()
        if len(packet) >= 7:
            if int(packet[6]) == Stimulator.TYPES['Init'] and int(packet[7]) == self.VERSION:
                # print("InitAck")
                self.reha_connected = 1
                return self.send_packet('InitAck', int(packet[5]))
            elif int(packet[6]) == Stimulator.TYPES['UnknownCommand']:
                self.packet_show(self.packet_send_history, self.SEND)
                print(Fore.LIGHTRED_EX + "UnknownCommand" + Fore.WHITE)
                self.packet_show(packet, self.ERR)
                return self.unknown_cmd(packet)
            elif int(packet[6]) == Stimulator.TYPES['GetStimulationModeAck']:
                # print("GetStimulationModeAck")
                return self.getModeACK(packet)
            elif int(packet[6]) == Stimulator.TYPES['InitChannelListModeAck']:
                # print("InitChannelListModeAck")
                return self.init_stimulation_ACK(packet)
            elif int(packet[6]) == Stimulator.TYPES['StopChannelListModeAck']:
                return self.stop_stimulation_ACK(packet)
            elif int(packet[6]) == Stimulator.TYPES['StartChannelListModeAck']:
                # print("StartChannelListModeAck")
                return self.start_stimulation_ACK(packet)
            elif int(packet[6]) == Stimulator.TYPES['StimulationError']:
                return self.stimulation_error(packet)
            else:
                self.packet_show(self.packet_send_history, self.SEND)
                print(Fore.LIGHTRED_EX + "Error packet : not understood")
                self.packet_show(packet, self.ERR)
        else:
            self.packet_show(self.packet_send_history, self.SEND)
            print(Fore.LIGHTRED_EX + "Error packet : packet too short, Packet rec:")
            self.packet_show(packet, self.ERR)

    # Establishes connexion acknowledge
    def init(self, packet_count):
        packet = self.packet_construction(packet_count, 'Init', self.VERSION)
        return packet

    # Establishes connexion acknowledge
    def init_ACK(self, packet_count):
        packet = self.packet_construction(packet_count, 'InitAck', 0)
        return packet

    # Sends message for unknown command
    @staticmethod
    def unknown_cmd(packet):
        return str(packet[7])

    def watchdog(self):
        packet = self.packet_construction(self.packet_count, 'Watchdog')
        return packet

    # Send a watchdog if necessary (automatically check if the last command was send more than 0.6s ago and
    # if the rehastim is connected)
    def send_watchdog(self):
        time_present = time.time()
        if time_present - self.time_last_cmd > 0.6 and self.reha_connected == 1:
            self.send_packet('Watchdog', self.packet_count)
        elif self.reha_connected == 0:
            print(Fore.LIGHTRED_EX + "Error watchdog not send: Rehastim not connected" + Fore.WHITE)

    def wait(self, sec):
        time_start = time.time()
        time_step = time_present = time.time()
        while time_present < time_start + sec:
            if time_present - time_step > 0.6:
                self.send_packet('Watchdog', self.packet_count)
                time_step = time_present
            time_present = time.time()

    def is_connected(self):
        if self.time_last_cmd > 1.2:
            self.reha_connected = 0
            return 0
        else:
            return 1

    # Asking to know which mode has been chosen
    def getMode(self):
        packet = self.packet_construction(self.packet_count, 'GetStimulationMode')
        return packet

    # Sent by RehaStim2 in response to getMode
    @staticmethod
    def getModeACK(packet):
        if str(packet[6] == '0'):
            if str(packet[7]) == '0':
                return 'Start Mode'
            elif str(packet[7]) == '1':
                return 'Stimulation initialized'
            elif str(packet[7]) == '2':
                return 'Stimulation started'
        elif str(packet[6]) == '-1':
            return 'Transfer error'
        elif str(packet[6]) == '-8':
            return 'Busy error'  # add a timer

    # Initialises stimulation
    def init_stimulation(self):
        MSB, LSB = self.MSB_LSB_main_stim()
        packet = self.packet_construction(self.packet_count, 'InitChannelListMode', 0, self.electrode_number, 0, 2, MSB,
                                          LSB,
                                          0)
        # Channel est 1,2,4,8,16,32,64,128 pour chaque et l'addition donne l'activation de plusieurs channels
        return packet

    # Sent by RehaStim2 in response to init_stimulation
    @staticmethod
    def init_stimulation_ACK(packet):
        if str(packet[7]) == '0':
            return 'Stimulation initialized'
        elif str(packet[7]) == '-1':
            return 'Transfer error'
        elif str(packet[7]) == '-2':
            return 'Parameter error'  # Change for please change parameters?
        elif str(packet[7]) == '-3':
            return 'Wrong mode error'
        elif str(packet[7]) == '-8':
            return 'Busy error'  # Add a timer?

    # Starts stimulation and modifies it
    def start_stimulation(self):  # VA PROBABLEMENT CHANGER PULSE_WIDTH ET AMPLITUDE SELON COMMENT RÉCUPÈRE DONNÉES
        # if len(self.pulse_width) == 1:
        MSB_matrix = []
        LSB_matrix = []
        packet = []
        for i in range(len(self.amplitude)):
            MSB, LSB = self.MSB_LSB_pulse_stim(self.pulse_width[i])
            MSB_matrix.append(MSB)
            LSB_matrix.append(LSB)

        if (len(self.amplitude)) == 1:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]))
        if len(self.amplitude) == 2:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]))
        elif len(self.amplitude) == 3:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]))
        elif len(self.amplitude) == 4:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]),
                                              0, int(MSB_matrix[3]), int(LSB_matrix[3]), int(self.amplitude[3]))
        elif len(self.amplitude) == 5:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]),
                                              0, int(MSB_matrix[3]), int(LSB_matrix[3]), int(self.amplitude[3]),
                                              0, int(MSB_matrix[4]), int(LSB_matrix[4]), int(self.amplitude[4]))
        elif len(self.amplitude) == 6:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]),
                                              0, int(MSB_matrix[3]), int(LSB_matrix[3]), int(self.amplitude[3]),
                                              0, int(MSB_matrix[4]), int(LSB_matrix[4]), int(self.amplitude[4]),
                                              0, int(MSB_matrix[5]), int(LSB_matrix[5]), int(self.amplitude[5]))
        elif len(self.amplitude) == 7:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]),
                                              0, int(MSB_matrix[3]), int(LSB_matrix[3]), int(self.amplitude[3]),
                                              0, int(MSB_matrix[4]), int(LSB_matrix[4]), int(self.amplitude[4]),
                                              0, int(MSB_matrix[5]), int(LSB_matrix[5]), int(self.amplitude[5]),
                                              0, int(MSB_matrix[6]), int(LSB_matrix[6]), int(self.amplitude[6]))
        elif len(self.amplitude) == 8:
            packet = self.packet_construction(self.packet_count, 'StartChannelListMode',
                                              0, int(MSB_matrix[0]), int(LSB_matrix[0]), int(self.amplitude[0]),
                                              0, int(MSB_matrix[1]), int(LSB_matrix[1]), int(self.amplitude[1]),
                                              0, int(MSB_matrix[2]), int(LSB_matrix[2]), int(self.amplitude[2]),
                                              0, int(MSB_matrix[3]), int(LSB_matrix[3]), int(self.amplitude[3]),
                                              0, int(MSB_matrix[4]), int(LSB_matrix[4]), int(self.amplitude[4]),
                                              0, int(MSB_matrix[5]), int(LSB_matrix[5]), int(self.amplitude[5]),
                                              0, int(MSB_matrix[6]), int(LSB_matrix[6]), int(self.amplitude[6]),
                                              0, int(MSB_matrix[7]), int(LSB_matrix[7]), int(self.amplitude[7]))
        return packet

    # Sent by RehaStim2 in response to start_stimulation
    @staticmethod
    def start_stimulation_ACK(packet):
        if str(packet[7]) == '0':
            return ' Stimulation started'
        if str(packet[7]) == '-1':
            return ' Transfer error'
        if str(packet[7]) == '-2':
            return ' Parameter error'
        if str(packet[7]) == '-3':
            return ' Wrong mode error'
        if str(packet[7]) == '-8':
            return ' Busy error'

    # Stops stimulation
    def stop_stimulation(self):
        packet = self.packet_construction(self.packet_count, 'StopChannelListMode')
        return packet

    # Sent by RehaStim2 in response to stop_stimulation
    def stop_stimulation_ACK(self, packet):
        if str(packet[7]) == '0':
            self.reha_connected = 0
            return ' Stimulation stopped'
        elif str(packet[7]) == '-1':
            return ' Transfer error'

    @staticmethod
    def stimulation_error(packet):
        if str(packet[7]) == '-1':
            return ' Emergency switch activated/not connected'  # mettre fonction qui affiche message sur interface
        elif str(packet[7]) == '-2':
            return ' Electrode error'
        elif str(packet[7]) == '-3':
            return 'Stimulation module error'

    # Function to command the stimulator with pre-defined commands
    @staticmethod
    def throw_command(command):
        print("(Stimulator) TODO : call the '" + command + "' command")
        # If command type == hexadécimal of certain command, throw associated function.
        # Fonction qui lit le paquet reçu par rehastim et qui l'associe à une commande.

        # command = {'Init':0x01}

    def MSB_LSB_main_stim(self):
        LSB = MSB = -1
        if self.ts1[0] <= 255:
            LSB = self.ts1[0]
            MSB = 0
        elif 256 <= self.ts1[0] <= 511:
            LSB = self.ts1[0] - 256
            MSB = 1
        elif 512 <= self.ts1[0] <= 767:
            LSB = self.ts1[0] - 512
            MSB = 2
        elif 768 <= self.ts1[0] <= 1023:
            LSB = self.ts1[0] - 768
            MSB = 3
        elif 1024 <= self.ts1[0] <= 1279:
            LSB = self.ts1[0] - 1024
            MSB = 4
        elif 1280 <= self.ts1[0] <= 1535:
            LSB = self.ts1[0] - 1280
            MSB = 5
        elif 1536 <= self.ts1[0] <= 1791:
            LSB = self.ts1[0] - 1536
            MSB = 6
        elif 1792 <= self.ts1[0] <= 2047:
            LSB = self.ts1[0] - 1792
            MSB = 7
        elif self.ts1[0] == 2048:
            LSB = 0
            MSB = 8

        return MSB, int(LSB)

    @staticmethod
    def MSB_LSB_pulse_stim(pulse_width):
        LSB = MSB = -1
        if pulse_width <= 255:
            LSB = pulse_width
            MSB = 0
        elif 256 <= pulse_width <= 500:
            LSB = pulse_width - 256
            MSB = 1
        return MSB, LSB

    def packet_show(self, packet, header):  # TODO: remove after debug
        if header == self.SEND:
            print(Fore.LIGHTBLUE_EX + "Packet send, ", end='')
        elif header == self.RECEIVE:
            print(Fore.LIGHTGREEN_EX + "Packet rec, ", end='')
        if len(packet) >= 7:
            print("%s" % self.TYPES[packet[6]], ":")
        for i in range(len(packet)):
            if i == 0:
                print("  Start:%s" % packet[0], end='')
            elif i == 1:
                print(", Stuff:%s" % packet[1], end='')
            elif i == 2:
                print(", Checksum:%s" % packet[2], end='')
            elif i == 3:
                print(", Stuff:%s" % packet[3], end='')
            elif i == 4:
                print(", Data length:%s" % packet[4], end='')
            elif i == 5:
                print(", Number:%s" % packet[5], end='')
            elif i == 6:
                print(", Cmd:%s" % packet[6], end='')
            else:
                print(", packet[%s]" % i, ":%s" % packet[i], end='')
        print(Fore.WHITE)
