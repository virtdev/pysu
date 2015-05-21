import pyb
from lib.mode import *
from dev.driver import Driver

class Relay(Driver):
    def setup(self):
        self._enable = False
        self._relay = pyb.Pin(self.get_pin(), pyb.Pin.OUT_PP)
        self.set(mode=MODE_SWITCH | MODE_VISI)
    
    def open(self):
        if not self._enable:
            self._relay.high()
            self._enable = True
    
    def close(self):
        if self._enable:
            self._relay.low()
            self._enable = False
