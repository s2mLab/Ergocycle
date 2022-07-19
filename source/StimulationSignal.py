# Crankset class
class StimulationSignal:
    def __init__(self, frequency, amplitude, pulse_width, training_time, muscle, electrode):
        self.frequency = frequency
        self.amplitude = amplitude
        self.pulse_width = pulse_width
        self.training_time = training_time
        self.muscle = muscle
        self.electrode = electrode

    def set_stimulation_signal(self):
        stimulation_signal = [self.amplitude, self.frequency, self.pulse_width, self.muscle]
        return stimulation_signal
