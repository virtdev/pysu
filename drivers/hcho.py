# hcho.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import pyb
from lib.modes import *
from dev.driver import Driver

class HCHO(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, freq=0.01, spec={'hcho':{'type':'int', 'range':[0, 4095], 'unit':'PPM'}})
        self._adc = pyb.ADC(pyb.Pin(name))
    
    def get(self):
        return {'hcho':self._adc.read()}
