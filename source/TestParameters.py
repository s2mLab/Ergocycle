import numpy as numpy

MAX_AMPLITUDE = 130
MIN_AMPLITUDE = 0
MAX_FREQ = 50
MIN_FREQ = 0
MAX_IMP = 500
MIN_IMP = 0


class TestParameters():
    def __init__(self):
        super(TestParameters, self).__init__()
        
        self.amplitude = 0
        self.frequency = 30
        self.imp = 200
        self.muscle = 1

    ## Recoit les nouvelles valeurs entrées par l'utilisateur et le transforme en matrice facilement exécutable par le module de communication.
    def get_test_parameters(self,amp,freq,imp,muscle):
        initial_test_parameters = numpy.empty([4,8], dtype=int)
        for i in range(4):
            if i==0:
               initial_test_parameters[i,:]=[amp, 0, 0, 0, 0, 0, 0, 0]
            if i==1:
                initial_test_parameters[i,:]=[freq, 0, 0, 0, 0, 0, 0, 0]
            if i==2:
                initial_test_parameters[i,:]=[imp, 0, 0, 0, 0, 0, 0, 0]
            if i==3:
                initial_test_parameters[i,:]=[muscle, 0, 0, 0, 0, 0, 0, 0]
        return initial_test_parameters

    def set_to_off(self):
        zero_parameters = []
        return(zero_parameters)

