import pyb
from lib.mode import *
from dev.driver import Driver

class HCHO(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, rng={'PPM':[0, 4095]}, freq=0.01)
        self._adc = pyb.ADC(pyb.Pin(name))
    
    def get(self):
        return {'PPM':self._adc.read()}
