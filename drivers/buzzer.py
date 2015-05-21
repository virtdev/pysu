import pyb
from lib import timer
from lib.mode import *
from dev.driver import Driver

class Buzzer(Driver):
    def setup(self):
        self._timer = None
        self._ti, self._ch = timer.alloc(self.get_pin())
        self.set(mode=MODE_VISI | MODE_SWITCH)
    
    def open(self):
        if not self._timer:
            pin = pyb.Pin(self.get_pin())
            self._timer = pyb.Timer(self._ti, freq=5000)
            channel = self._timer.channel(self._ch, pyb.Timer.PWM, pin=pin)
            channel.pulse_width_percent(50)
    
    def close(self):
        if self._timer:
            self._timer.deinit()
            self._timer = None
