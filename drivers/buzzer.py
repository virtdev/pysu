import pyb
from lib import timer
from lib.mode import *
from dev.driver import Driver

class Buzzer(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_VISI | MODE_SWITCH)
        self._ti, self._ch = timer.alloc(name)
        self._pin = pyb.Pin(name)
        self._timer = None
    
    def open(self):
        if not self._timer:
            self._timer = pyb.Timer(self._ti, freq=5000)
            channel = self._timer.channel(self._ch, pyb.Timer.PWM, pin=self._pin)
            channel.pulse_width_percent(50)
    
    def close(self):
        if self._timer:
            self._timer.deinit()
            self._timer = None
