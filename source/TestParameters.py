import numpy as numpy
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:06:49 2022

@author: Nicolas Pelletier-Côté
"""

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
    def get_test_parameters(self,amp,freq,imp,muscle):
        initial_test_parameters = numpy.array([[amp],[freq],[imp],[muscle]])
        return(initial_test_parameters)
    def set_to_off(self):
        zero_parameters = numpy.array([[0],[0],[0],[0]])
        return(zero_parameters)
