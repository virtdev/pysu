import pyb
from lib.mode import *
from dev.driver import Driver

class HCHO(Driver):
    def setup(self):
        self._adc = pyb.ADC(pyb.Pin(self.get_pin()))
        self.set(mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, rng={'PPM':[0, 4095]}, freq=0.01)
    
    def get(self):
        return {'PPM':self._adc.read()}
