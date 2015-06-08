import pyb
from lib.mode import *
from dev.driver import Driver

class Relay(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_SWITCH | MODE_VISI)
        self._relay = pyb.Pin(name, pyb.Pin.OUT_PP)
        self._enable = False
    
    def open(self):
        if not self._enable:
            self._relay.high()
            self._enable = True
    
    def close(self):
        if self._enable:
            self._relay.low()
            self._enable = False
