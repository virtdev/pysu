import pyb
from lib.mode import *
from dev.driver import Driver
from lib.interrupt import irq_rising

class IRD(Driver):
    def setup(self):
        self.set(mode=MODE_TRIG | MODE_VISI, rng={'Enable':[True, False]})
        irq_rising(self.get_pin(), self.callback)
    
    def get(self):
        if self.event.is_set():
            self.event.clear()
            return {'Enable':True}
