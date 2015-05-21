import pyb
from lib.mode import *
from lib.pulse import *
from dev.driver import Driver

class HT(Driver):
    def setup(self):
        self.set(mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, rng={'Humidity':[0, 100], 'Celsius':[-100, 100]}, freq=0.01)
    
    def get(self):
        data = [0] * 5
        pin = pyb.Pin(self.get_pin(), pyb.Pin.OUT_PP)
        pin.low()
        pyb.delay(25)
        pin.high()
        pyb.udelay(40)
        pin.init(pyb.Pin.IN)
        pulseIn(pin, HIGH)
        for i in range(5): 
            for j in range(8):
                val = pulseIn(pin, HIGH, width=40)
                if not val:
                    return
                elif val >= 40:
                    data[i] |= 1 << (7 - j)
        if data[4] == data[0] + data[2]:
            return {'Humidity':data[0], 'Celsius':data[2]}
