# Crankset class
class StimulationSignal:    

    # Constuctor
    def __init__(self, frequency, amplitude, pulse_width, training_time, muscle, electrode):
        self.frequency = frequency
        self.amplitude = amplitude
        self.pulse_width = pulse_width
        self.training_time = training_time
        self.muscle = muscle
        self.electrode = electrode
        
    def set_stimulation_signal(self):
        frequency =[]
        amplitude = []
        pulse_width = []
        muscle = []
        StimulationSignal = []
        StimulationSignal.append(self.amplitude)
        StimulationSignal.append(self.frequency)
        StimulationSignal.append(self.pulse_width)
        StimulationSignal.append(self.muscle)
        
        return StimulationSignal
        
            