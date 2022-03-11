# Crankset class
class StimulationSignal:    
    import Ergocycle as Ergocycle


    # Constuctor
    def __init__(self, frequency, amplitude, pulse_width, training_time, muscle, electrode):
        self.frequency = frequency
        self.amplitude = amplitude
        self.pulse_width = pulse_width
        self.training_time = training_time
        self.muscle = muscle
        self.electrode = electrode
        
    def set_stimulation_signal(electrode):
        frequency =[]
        amplitude = []
        pulse_width = []
        muscle = []
        for i in range(electrode):
            frequency.append(electrode[0,i]) # Vérifier comment sont envoyés les paramètres
            