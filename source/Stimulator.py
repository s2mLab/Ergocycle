# Stimulator class

# Imports
import usb
from StimulationSignal import StimulationSignal


# channel_stim:   list of active channels
# freq:           main stimulation frequency in Hz (NOTE: this overrides ts1)
# ts1:            main stimulation period in ms (1-1024.5 ms in 0.5 steps)
# ts2:            inter-pulse time in ms (1.5-17 ms in 0.5 steps)



class Stimulator:

    # Constuctor
    def __init__(self, channel_stim, freq, ts1, ts2, mode, pulse_width, amplitude):
        self.channel_stim = channel_stim
        self.freq = freq
        self.ts1 = ts1
        self.ts2 = ts2
        self.mode = mode
        self.pulse_width = pulse_width
        self.amplitude = amplitude
        self.baud_rate = 460800
        self.start_byte = 0xF0
        self.stop_byte = 0x0F
        self.stuffing_byte = 0x81
        self.stuffing_key = 0x55
        
        
        print("TODO")
            
        
    # Establishes connexion acknowlege
    def init():
        
        
        print("TODO")
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
    
    