# ht.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import pyb
from lib.modes import *
from lib.pulse import *
from dev.driver import Driver

class HT(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, freq=0.01, spec={'humidity':{'type':'int', 'range':[0, 100], 'unit':'%'}, 'temperature':{'type':'int', 'range':[-100, 100], 'unit':'Celsius'}})

    def get(self):
        data = [0] * 5
        pin = pyb.Pin(self.get_name(), pyb.Pin.OUT_PP)
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
            return {'humidity':data[0], 'temperature':data[2]}
